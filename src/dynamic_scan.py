import os
import subprocess

# Ensure sandbox log directory exists
os.makedirs("sandbox_logs", exist_ok=True)

def perform_dynamic_analysis(file_path):
    trace_log = os.path.join("sandbox_logs", os.path.basename(file_path) + "_strace.log")
    command = ["firejail", "--noprofile", "--quiet", "strace", "-o", trace_log, "cat", file_path]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        return {
            "status": "success",
            "trace_log": trace_log,
            "output": result.stdout,
            "errors": result.stderr
        }
    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "trace_log": trace_log,
            "output": "",
            "errors": "Execution timed out"
        }
    except FileNotFoundError:
        return {
            "status": "error",
            "trace_log": None,
            "output": "",
            "errors": "Error: firejail or strace not found"
        }
    except PermissionError:
        return {
            "status": "error",
            "trace_log": None,
            "output": "",
            "errors": "Error: execute permission denied for /usr/bin/strace"
        }
    except Exception as e:
        return {
            "status": "error",
            "trace_log": None,
            "output": "",
            "errors": f"Unexpected error: {e}"
        }


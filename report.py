import os
import subprocess

def generate_report(file_path, static_results, dynamic_results):
    report_file = os.path.join("sandbox_logs", os.path.basename(file_path) + "_report.txt")

    with open(report_file, "w") as f:
        f.write("=== Static Analysis ===\n")
        
        # Handle if static_results is a list (it seems to be a list)
        if isinstance(static_results, list):
            for line in static_results:
                f.write(line + "\n")
        else:
            # Handle if static_results is a dictionary
            for key, value in static_results.items():
                if isinstance(value, int) and value > 0:
                    f.write(f"{key:<22} {value}\n")
                elif key == "PDF Header":
                    f.write(f"{key}: {value}\n")

        f.write("\n=== Dynamic Analysis ===\n")
        if isinstance(dynamic_results, list):
            for line in dynamic_results:
                f.write(line + "\n")
        else:
            f.write("No dynamic analysis results available.\n")

    print("[✓] Scan Complete. Report saved in sandbox_logs/")


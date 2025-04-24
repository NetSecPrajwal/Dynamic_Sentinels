from static_scan import perform_static_analysis
from dynamic_scan import perform_dynamic_analysis
from report import generate_report

def main():
    file_path = '/home/kali/Downloads/suspicious_test.pdf'  # Replace with dynamic input if needed

    # Static Analysis
    print("[1/2] Static Analysis...")
    static_results = perform_static_analysis(file_path)

    # Dynamic Analysis
    print("[2/2] Dynamic Analysis...")
    dynamic_results = perform_dynamic_analysis(file_path)

    # Generate Report
    print("[+] Generating Report...")
    generate_report(file_path, static_results, dynamic_results)

if __name__ == "__main__":
    main()


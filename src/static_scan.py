import os
import re

def perform_static_analysis(file_path):
    results = []

    try:
        with open(file_path, 'rb') as f:
            content = f.read()

        # Add PDF header
        header_match = re.search(b'%PDF-[0-9]\.[0-9]', content)
        header = header_match.group().decode() if header_match else "Unknown"
        results.append(f"PDF Header: {header}")

        # Define keywords to search in the PDF
        keywords = [
            "obj", "endobj", "stream", "endstream", "xref", "trailer",
            "startxref", "/Page", "/Encrypt", "/ObjStm", "/JS", "/JavaScript",
            "/AA", "/OpenAction", "/AcroForm", "/JBIG2Decode", "/RichMedia",
            "/Launch", "/EmbeddedFile"
        ]

        # Count each keyword
        for keyword in keywords:
            pattern = rb'(?i)' + keyword.encode()
            count = len(re.findall(pattern, content))
            results.append(f"{keyword.ljust(22)} {count}")

        # Example heuristic: color count > 2^24 check
        color_threshold_detected = b"/ColorSpace /DeviceRGB" in content
        results.append(f"/Colors > 2^24       {1 if color_threshold_detected else 0}")

    except Exception as e:
        results.append(f"[!] Error during static analysis: {e}")

    return results


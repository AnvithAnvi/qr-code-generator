import qrcode
import sys
import os

def generate_qr(url):
    # Create output directory if it doesn't exist
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)

    # Create QR code
    img = qrcode.make(url)

    # File name based on the URL
    safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")
    file_path = os.path.join(output_dir, f"{safe_name}.png")

    # Save the QR code
    img.save(file_path)

    print(f"✅ QR code generated successfully for: {url}")
    print(f"📁 Saved as: {file_path}")

if __name__ == "__main__":
    # Default URL if none provided
    url = "http://github.com/kaw393939"

    # If user passes a custom URL argument
    if len(sys.argv) > 1 and sys.argv[1] == "--url" and len(sys.argv) > 2:
        url = sys.argv[2]

    generate_qr(url)


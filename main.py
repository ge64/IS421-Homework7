import os
import qrcode

# Environment Variables
QR_CODE_IMAGE_DIRECTORY = os.getenv('QR_CODE_IMAGE_DIRECTORY', 'static')
QR_CODE_DEFAULT_URL = os.getenv('QR_CODE_DEFAULT_URL', 'https://www.njit.edu')
QR_CODE_DEFAULT_FILE_NAME = os.getenv('QR_CODE_DEFAULT_FILE_NAME', 'default.png')

def create_qr_code_image(data: str):
    """Generate QR Code"""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill='black', back_color='white')

def main():
    full_path = os.getcwd()
    directory_path_and_file_name = os.path.join(full_path, QR_CODE_IMAGE_DIRECTORY, QR_CODE_DEFAULT_FILE_NAME)
    qr_image = create_qr_code_image(QR_CODE_DEFAULT_URL)

    try:
        qr_image.save(directory_path_and_file_name)
    except FileNotFoundError:
        os.makedirs(os.path.join(full_path, QR_CODE_IMAGE_DIRECTORY), exist_ok=True)
        qr_image.save(directory_path_and_file_name)

if __name__ == "__main__":
    main()

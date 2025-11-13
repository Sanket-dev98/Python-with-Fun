import qrcode

url = input("Enter the URL you wish to download the QR code: ").strip()
# strip() --> For unnecessary white space
file_path = "C:\\Users\\Sanket\\Desktop\\qrcode.png"
# To store the qr code image

# To create a object
# Access the library
# Constructor

qr = qrcode.QRCode()

# To add our data , our URL to this QR code object

qr.add_data(url)     # Data method

# To generate the QR code image , we will assign an image object
img = qr.make_image()

# To save the image
img.save(file_path)

print("QR Code generated")
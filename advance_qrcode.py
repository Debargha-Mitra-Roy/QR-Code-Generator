import qrcode
from PIL import Image
import string
import random

# initializing size of string
N = 7

# using random.choices() generating random strings
res = ''.join(random.choices(string.ascii_letters, k=N))

# Convert the string to a .png extention
res = res + ".png"

# Customize the QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

#Fetch all data form the link
qr.add_data(input("Enter the link : "))

# Make the QR Code if all data of the link is fetched
qr.make(fit=True)

# Customize the image of QR Code in different format
img = qr.make_image(
    fill_color="red",
    back_color="yellow"
)

# Save the file name with randomly generated string
img.save(res)


print("Thanks for using our service. Your file is ready to use.")

# Open the file in reading mode
file = Image.open(res, 'r')
file.show()

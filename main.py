import qrcode as qr
from PIL import Image
import string
import random

# initializing size of string
N = 7

# using random.choices() generating random strings
res = ''.join(random.choices(string.ascii_letters, k=N))

# Convert the string to a .png extention
res = res + ".png"

# User input
img = qr.make(input("Enter the link : "))

# Save the file name with randomly generated string
img.save(res)

print("Thanks for using our service. Your file is ready to use.")

# Open the file in reading mode
file = Image.open(res, 'r')
file.show()

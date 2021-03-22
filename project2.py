import qrcode

##### img = qrcode.make("Hello World! This is NeuralNine!")
####### img.save("mycode.png")

qr = qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=50,
                     border=10)

qr.add_data("https://www.uzbooks.com")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")




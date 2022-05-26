import qrcode


a = 300


for f in range(a):
    bnr = bin(f).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]

    img = qrcode.make(f"{bnr}")
    type(img)
    img.save(f"test/test_{f}.png")
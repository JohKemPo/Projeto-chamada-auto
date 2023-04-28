import qrcode

dado = 'https://johkempo.github.io/Projeto-chamada-auto/'

PG_BLUE = (27, 54, 87)
PG_GREEN = (0, 174, 150)

if __name__ == '__main__':
    cores = [(PG_BLUE, 'white'), ('white', PG_GREEN)]
    
    qr = qrcode.QRCode(None, qrcode.ERROR_CORRECT_H)
    qr.add_data(dado)
    img = qr.make_image()
    img.save(f'img.png')
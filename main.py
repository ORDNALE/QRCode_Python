import pyqrcode
import png
from pyqrcode import QRCode

# link desejado para QRCode
QRlink = input('Entre com o link desejado: ')

# Gera o QRCODE
url = pyqrcode.create(QRlink)

# salva o QRCODE no local desejado
# imagem QR salva no diretorio do projeto
url.png(r'qr.png', scale=8)

#!/usr/bin/python3

import qrcode
from qrcode.image.svg import SvgPathImage

# Função para gerar o QR Code e salvar em formato SVG
def gerar_qr_code_svg(dados, nome_arquivo_svg):
    # Cria o QR Code com as configurações desejadas
    qr = qrcode.QRCode(
        version=1,  # Define o tamanho da grade do QR (1 é o menor)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=10,  # Tamanho de cada quadrado do QR Code
        border=4,  # Largura da borda ao redor do código
    )
    
    # Adiciona os dados ao QR Code
    qr.add_data(dados)
    qr.make(fit=True)  # Ajusta automaticamente o tamanho do QR Code
    
    # Gera a imagem SVG do QR Code
    img = qr.make_image(image_factory=SvgPathImage)
    
    # Salva o QR Code em um arquivo SVG
    with open(nome_arquivo_svg, "wb") as f:
        img.save(f)
    
    print(f"QR Code salvo em {nome_arquivo_svg}")


dados = "https://trucomanx.github.io/notebook"
nome_arquivo_svg = "qrcode_exemplo.svg"
gerar_qr_code_svg(dados, nome_arquivo_svg)


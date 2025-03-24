import os
import pytesseract
from PIL import Image, ExifTags
import xml.etree.ElementTree as ET

# Função para verificar e rotacionar a imagem se necessário
def rotate_image(image):
    # Verifica se a imagem possui dados EXIF para detectar orientação
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(image._getexif().items())
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # Se não houver dados EXIF ou não for possível rotacionar, ignoramos
        pass
    return image

# Função para extrair o texto da imagem
def extract_text_from_image(image_path):
    try:
        # Abre a imagem
        img = Image.open(image_path)
        
        # Rotaciona a imagem se necessário
        img = rotate_image(img)
        
        # Usa o pytesseract para extrair o texto da imagem
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Erro ao processar a imagem {image_path}: {e}")
        return ""

# Função para salvar o texto extraído em um arquivo XML
def save_text_to_xml(text, output_path):
    # Cria o elemento raiz do XML
    root = ET.Element("document")
    # Cria um elemento de texto
    text_element = ET.SubElement(root, "text")
    text_element.text = text
    
    # Cria a árvore XML e grava no arquivo
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

# Função para processar todas as imagens nas pastas de Resultado
def process_images_in_result_folder(result_folder):
    # Itera por todas as pastas dentro de Resultado
    for folder_name in os.listdir(result_folder):
        folder_path = os.path.join(result_folder, folder_name)
        
        # Verifica se é uma pasta
        if os.path.isdir(folder_path):
            # Cria o arquivo XML de saída baseado no nome da pasta
            xml_output_folder = os.path.join(folder_path, f"XML_{folder_name}")
            if not os.path.exists(xml_output_folder):
                os.makedirs(xml_output_folder)
            
            # Itera por todas as imagens dentro da pasta
            for image_file in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_file)
                
                # Verifica se o arquivo é uma imagem (assumindo que a extensão seja .png)
                if image_file.lower().endswith(".png"):
                    print(f"Processando imagem {image_file}...")
                    
                    # Extrai o texto da imagem
                    text = extract_text_from_image(image_path)
                    
                    if text:  # Se houver texto extraído
                        # Cria o caminho do arquivo XML
                        xml_output_path = os.path.join(xml_output_folder, f"{os.path.splitext(image_file)[0]}.xml")
                        # Salva o texto extraído no XML
                        save_text_to_xml(text, xml_output_path)
                        print(f"Texto extraído e salvo em {xml_output_path}")
                    else:
                        print(f"Nenhum texto encontrado na imagem {image_file}")

# Caminho da pasta Resultado
result_folder = 'C:\\Users\\coloque\\sua\\pasta\\Resultado'

# Processa as imagens e salva o texto extraído em XML
process_images_in_result_folder(result_folder)

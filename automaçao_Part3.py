import pytesseract
from PIL import Image
import xml.etree.ElementTree as ET
import os

# Função para extrair texto com as coordenadas de cada palavra
def extract_text_with_position(image_path):
    try:
        # Abre a imagem
        img = Image.open(image_path)
        
        # Usando pytesseract para obter o texto com as coordenadas
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        
        # Organiza as palavras e suas posições em uma lista
        words_with_position = []
        for i, word in enumerate(data["text"]):
            if word.strip():  # Ignora palavras vazias
                x = data["left"][i]
                y = data["top"][i]
                text = word
                words_with_position.append({"word": text, "x": x, "y": y})
        
        if not words_with_position:
            print(f"Nenhum texto encontrado na imagem: {image_path}")
        
        return words_with_position
    except Exception as e:
        print(f"Erro ao processar a imagem {image_path}: {e}")
        return []

# Função para criar XML organizado com base nas coordenadas das palavras
def create_organized_xml(words_with_position, output_xml_path):
    try:
        # Organiza as palavras em linhas baseadas na posição Y
        lines = []
        current_line = []
        last_y = None
        
        for word in words_with_position:
            # Se a coordenada Y mudar, significa que é uma nova linha
            if last_y is None or abs(word["y"] - last_y) > 10:  # Tolerância para variação de Y
                if current_line:
                    lines.append(" ".join(current_line))
                    current_line = []
            current_line.append(word["word"])
            last_y = word["y"]
        
        if current_line:
            lines.append(" ".join(current_line))
        
        if not lines:
            print(f"Nenhuma linha de texto organizada para o XML")
        
        # Cria o XML com as linhas organizadas
        root = ET.Element("document")
        for line in lines:
            line_element = ET.SubElement(root, "line")
            line_element.text = line
        
        # Cria a árvore XML e grava no arquivo de saída
        tree = ET.ElementTree(root)
        tree.write(output_xml_path, encoding="utf-8", xml_declaration=True)
        print(f"XML organizado salvo em {output_xml_path}")
    except Exception as e:
        print(f"Erro ao criar o XML: {e}")

# Função para processar todas as imagens em uma pasta e gerar XMLs organizados
def process_all_images_in_folder(input_folder):
    # Itera por todas as pastas dentro da pasta de entrada
    for root_folder_name in os.listdir(input_folder):
        root_folder_path = os.path.join(input_folder, root_folder_name)
        
        # Verifica se é uma pasta
        if os.path.isdir(root_folder_path):
            print(f"Processando a pasta: {root_folder_name}")
            
            # Cria a pasta XML_Organizado dentro da pasta atual (root_folder_name)
            organized_xml_folder = os.path.join(root_folder_path, "XML_Organizado")
            if not os.path.exists(organized_xml_folder):
                os.makedirs(organized_xml_folder)
                print(f"Pasta XML_Organizado criada em: {organized_xml_folder}")
            
            # Itera por todas as imagens na subpasta
            for image_file in os.listdir(root_folder_path):
                image_path = os.path.join(root_folder_path, image_file)
                
                # Verifica se o arquivo é uma imagem (assumindo que a extensão seja .png)
                if image_file.lower().endswith(".png"):
                    print(f"Processando a imagem {image_file}...")
                    
                    # Extrai o texto com a posição das palavras
                    words_with_position = extract_text_with_position(image_path)
                    
                    if words_with_position:
                        # Cria o arquivo XML de saída dentro da pasta XML_Organizado
                        output_xml_path = os.path.join(organized_xml_folder, f"Organized_{os.path.splitext(image_file)[0]}.xml")
                        create_organized_xml(words_with_position, output_xml_path)
                    else:
                        print(f"Nenhum texto extraído da imagem {image_file}")

# Caminho da pasta contendo as imagens
input_folder = 'C:\\Users\\Coloque\\sua\\pasta\\Resultado'

# Processa todas as imagens e salva os XMLs organizados
process_all_images_in_folder(input_folder)
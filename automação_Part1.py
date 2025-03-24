import fitz  # PyMuPDF
from PIL import Image
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Verifica se a pasta de saída existe, caso contrário cria a pasta
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Abre o PDF
    doc = fitz.open(pdf_path)
    image_count = 0
    
    # Itera por todas as páginas do PDF
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        
        # Itera por todas as imagens na página
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            
            # Salva a imagem temporariamente para ser processada
            temp_image_path = f"temp_image_{page_num + 1}_{img_index + 1}.png"
            with open(temp_image_path, "wb") as img_file:
                img_file.write(image_data)

            # Usa PIL para abrir a imagem e verificar sua orientação
            with Image.open(temp_image_path) as img:
                # Verifica se a imagem está na vertical
                if img.width < img.height:
                    # Rotaciona a imagem 90 graus no sentido horário
                    img = img.rotate(-90, expand=True)

                # Define o caminho do arquivo de saída
                image_filename = f"image_{page_num + 1}_{img_index + 1}.png"
                image_path = os.path.join(output_folder, image_filename)
                
                # Salva a imagem na pasta de saída
                img.save(image_path)
            
            # Deleta a imagem temporária
            os.remove(temp_image_path)
            
            image_count += 1

    return image_count

def process_all_pdfs_in_folder(folder_path, output_base_folder):
    # Verifica todos os arquivos na pasta
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    # Processa cada PDF encontrado
    total_images = 0
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        
        # Cria uma pasta para o PDF atual dentro da pasta 'Resultado'
        pdf_name = os.path.splitext(pdf_file)[0]  # Pega o nome do arquivo sem a extensão
        output_folder = os.path.join(output_base_folder, pdf_name)
        
        # Extraí as imagens e salva na pasta correspondente
        image_count = extract_images_from_pdf(pdf_path, output_folder)
        total_images += image_count
        print(f"Processado {pdf_file}: {image_count} imagens extraídas.")
    
    print(f"Total de {total_images} imagens extraídas de todos os PDFs.")

# Caminho da pasta contendo os PDFs e da pasta onde as imagens serão salvas
folder_path = 'C:\\Users\\coloque\\seu\\repositorio'
output_base_folder = 'C:\\Users\\coloque\\sua\\pasta\\Resultado'

# Processa todos os PDFs na pasta
process_all_pdfs_in_folder(folder_path, output_base_folder)

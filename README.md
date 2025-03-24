PDF Image Extraction and OCR Processing System

Este sistema fornece uma solução completa para extração de imagens de documentos PDF e subsequente reconhecimento óptico de caracteres (OCR). O processo é dividido em duas etapas principais, facilitando a extração e análise de conteúdo textual de imagens contidas em PDFs.
Requisitos
Antes de iniciar, certifique-se de que você tem os seguintes componentes instalados:

Python 3.6 ou superior
PyMuPDF (fitz)
Pillow (PIL)
pytesseract
Tesseract OCR (precisa estar instalado no sistema)

Você pode instalar as dependências Python usando pip:
pip install PyMuPDF Pillow pytesseract
Para o Tesseract OCR, siga as instruções de instalação para seu sistema operacional em: https://github.com/tesseract-ocr/tesseract
Estrutura do Sistema
O sistema opera em duas etapas sequenciais:
Etapa 1: Extração de Imagens de PDFs
O primeiro script extrai todas as imagens de arquivos PDF, com a capacidade de processar automaticamente múltiplos PDFs em uma pasta.
Funcionalidades principais:

Extração de todas as imagens contidas em PDFs
Correção automática da orientação de imagens (rotação para horizontal)
Organização das imagens em pastas separadas por PDF de origem

Etapa 2: Reconhecimento Óptico de Caracteres (OCR)
O segundo script realiza OCR nas imagens extraídas, convertendo o conteúdo visual em texto.
Funcionalidades principais:

Processamento de todas as imagens nas pastas de resultado
Detecção automática da orientação da imagem através de dados EXIF
Extração de texto usando Tesseract OCR
Salvamento do texto extraído em arquivos XML organizados

Como Usar
Configuração
Antes de executar os scripts, atualize os caminhos das pastas para corresponder ao seu ambiente:
Para o script de extração de imagens
folder_path = 'C:\Caminho\Para\Pasta\Com\PDFs'
output_base_folder = 'C:\Caminho\Para\Pasta\Resultado'
Para o script de OCR
result_folder = 'C:\Caminho\Para\Pasta\Resultado'
Execução da Etapa 1: Extração de Imagens
Execute o primeiro script para extrair imagens de todos os PDFs na pasta especificada:
python extract_images.py
Cada PDF será processado e suas imagens serão salvas em uma pasta separada dentro do diretório de resultados. O script também corrige automaticamente a orientação das imagens, garantindo que estejam na horizontal.
Execução da Etapa 2: OCR
Após a extração das imagens, execute o segundo script para realizar OCR:
python process_ocr.py
O script processará todas as imagens extraídas, identificará o texto e salvará o resultado em arquivos XML. Para cada pasta de imagens, será criada uma subpasta "XML_[nome_do_pdf]" contendo os arquivos XML correspondentes.
Detalhes das Funções
Script de Extração de Imagens

extract_images_from_pdf(pdf_path, output_folder): Extrai imagens de um único PDF
process_all_pdfs_in_folder(folder_path, output_base_folder): Processa todos os PDFs em uma pasta

Script de OCR

rotate_image(image): Ajusta a orientação da imagem baseado em dados EXIF
extract_text_from_image(image_path): Extrai texto de uma imagem usando OCR
save_text_to_xml(text, output_path): Salva o texto extraído em formato XML
process_images_in_result_folder(result_folder): Processa todas as imagens nas pastas de resultado

Estrutura de Arquivos
Após a execução completa, você terá a seguinte estrutura de arquivos:
Pasta_PDFs/
├── arquivo1.pdf
├── arquivo2.pdf
└── ...
Pasta_Resultado/
├── arquivo1/
│   ├── image_1_1.png
│   ├── image_1_2.png
│   └── XML_arquivo1/
│       ├── image_1_1.xml
│       └── image_1_2.xml
├── arquivo2/
│   ├── image_1_1.png
│   └── XML_arquivo2/
│       └── image_1_1.xml
└── ...
Solução de Problemas

Se o Tesseract OCR não estiver sendo encontrado, verifique se ele está instalado corretamente e se o caminho está configurado nas variáveis de ambiente.
Para melhorar a qualidade do OCR, considere pré-processar as imagens ajustando o contraste ou aplicando filtros antes de executar o OCR.
Em caso de erros com a rotação da imagem, verifique se a biblioteca Pillow está atualizada para a versão mais recente.

Considerações de Desempenho

O processamento de PDFs grandes ou com muitas imagens pode levar tempo considerável.
Para melhorar o desempenho, considere implementar processamento paralelo para lidar com múltiplos PDFs ou imagens simultaneamente.

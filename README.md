
# Extração de Imagens e Texto de PDFs

Este projeto tem como objetivo extrair imagens de arquivos PDF e processar essas imagens para extrair textos, salvando-os em formato XML.

## Funcionalidades

1. **Extração de imagens de PDFs**:
   - Percorre todas as páginas de arquivos PDF dentro de uma pasta.
   - Salva as imagens extraídas em subpastas dentro da pasta "Resultado".
   - Corrige a orientação das imagens, caso necessário.

2. **Processamento de imagens para extração de texto**:
   - Percorre todas as imagens extraídas e verifica sua orientação.
   - Utiliza OCR (Tesseract) para extrair textos das imagens.
   - Salva os textos extraídos em arquivos XML correspondentes.

3. **Processamento de coordenadas e identificação da linha mais próxima**:
   - A partir dos dados extraídos, processa as coordenadas de início e fim de uma linha.
   - Identifica a linha mais próxima de um ponto de referência, usando as coordenadas convertidas para UTM.
   - Exibe os dados no formato correto, incluindo as coordenadas, conversões e o valor do campo `DISPOSITIVO_ONR` da linha mais próxima.
   - O resultado é salvo em um formato específico, com as informações organizadas para análise posterior.

## Dependências

Antes de executar o projeto, instale as bibliotecas necessárias:

```bash
pip install pymupdf pillow pytesseract
```

## Como Usar

1. **Extração de imagens dos PDFs**

   - Defina o caminho da pasta onde estão os PDFs e onde deseja salvar os resultados.
   - Execute o script de extração de imagens:

   ```python
   process_all_pdfs_in_folder(folder_path, output_base_folder)
   ```

2. **Extração de texto das imagens**

   - Defina o caminho da pasta "Resultado".
   - Execute o script de extração de texto:

   ```python
   process_images_in_result_folder(result_folder)
   ```

3. **Processamento de coordenadas e identificação da linha mais próxima**

   - Defina o caminho para os arquivos CSV e o arquivo de coordenadas.
   - Execute o script de processamento de coordenadas para encontrar a linha mais próxima:

   ```python
   process_coordinates_and_identify_closest_line(csv_folder, result_folder)
   ```

## Estrutura de Pastas
```
Projeto/
│── extração_imagens.py  # Script para extrair imagens dos PDFs
│── extracao_texto.py     # Script para extrair texto das imagens
│── processamento_coordenadas.py  # Script para processar coordenadas e identificar linhas mais próximas
│── Resultado/            # Pasta onde as imagens extraídas serão salvas
│   ├── PDF_1/
│   │   ├── image1.png
│   │   ├── image2.png
│   ├── PDF_2/
│── XML_/                # Pasta onde os textos extraídos serão salvos
│   ├── image1.xml
│   ├── image2.xml
│── XML_Organizado/          # Pasta onde os dados organizados por coordenadas serão salvos
│   ├── Organized_image_1.xml
│   ├── Organized_image_2.xml
```

## Possíveis Problemas

- **Erro ao abrir PDFs**: Verifique se os arquivos estão no formato correto.
- **Imagens não extraídas corretamente**: Certifique-se de que o PDF contém imagens embutidas.
- **OCR não reconhece texto**: As imagens podem estar em baixa qualidade ou não conter texto legível.
- **Coordenadas não encontradas ou erro na conversão**: Verifique se os arquivos de coordenadas estão no formato esperado.

## Contribuição

Caso tenha sugestões ou melhorias, fique à vontade para abrir um Pull Request ou reportar problemas na aba "Issues".

## Licença

Este projeto está sob a licença MIT.

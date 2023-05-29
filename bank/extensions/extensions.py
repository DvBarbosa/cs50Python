import os

# Define a dictionary to map file extensions to media types
media_types = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip',
}
#pega o nome do arquivo pelo usuario"
file_name = input('Enter the file name: ')

#pega a extensao de arquivo
file_extension = os.path.splitext(file_name)[-1].lower()

#mapeia a extensao de arquivo correspondente ao tipo de media, ou padrao para aplicacao/octet-stream
media_type = media_types.get(file_extension, 'application/octet-stream')

# Saida do tipo de media
print(f'{media_type}')

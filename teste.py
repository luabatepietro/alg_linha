import os

base_image_path = os.path.join(os.path.dirname(__file__), 'assets')

# Verifica se o arquivo existe no local esperado
print(os.path.exists(os.path.join(base_image_path, 'coracao.gif')))  # Deve retornar True

# Carregando a imagem

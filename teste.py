import os

# Obtenha o caminho absoluto para o diretório de instalação do pacote
base_image_path = os.path.join(os.path.dirname(__file__), 'assets')

# Verifique se o caminho está correto
print(f"Acessando assets no caminho: {base_image_path}")
print(os.path.exists(os.path.join(base_image_path, 'coracao.gif')))  # Isso deve retornar True
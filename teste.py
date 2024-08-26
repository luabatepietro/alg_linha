import os

base_image_path = os.path.join(os.path.dirname(__file__), 'assets')

# Verifica se o caminho é válido
print(f"Acessando arquivos de assets no caminho: {base_image_path}")

# Verifica se o arquivo existe
if not os.path.exists(os.path.join(base_image_path, 'coracao.gif')):
    raise FileNotFoundError(f"Arquivo não encontrado: {os.path.join(base_image_path, 'coracao.gif')}")


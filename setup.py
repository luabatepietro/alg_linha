from setuptools import setup, find_packages

setup(
    name="alg_linha",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        # Liste aqui outras bibliotecas que seu pacote precisa
    ],
    package_data={
        '': ['img/.png','alg_linha/assets/.png',]  # Inclui todos os arquivos .png dentro do diretório 'img' de todos os pacotes
    },
    entry_points={
        "console_scripts": [
            "alg_linha=alg_linha.main:main",  # Se quiser criar um comando de terminal
        ],
    },
    author="Lucas Abatepietro",  # Seu nome
    author_email="luabatepietro@hotmail.com",  # Seu email
    description="jogo legal e maneiro",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/luabatepietro/alg_linha.git",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)
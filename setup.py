from setuptools import setup, find_packages

setup(
    name="alg_linha",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        'pygame',
        'numpy',
    ],
    package_data={
        '': ['assets/*.png', 'assets/*.gif', 'assets/*.webp'],  # Inclui todos os arquivos .png, .gif, .webp dentro do diretório 'assets'
    },
    entry_points={
        "console_scripts": [
            "alg_linha=alg_linha.main:main",  # Se quiser criar um comando de terminal
        ],
    },
    author="Lucas Abatepietro",  # Seu nome
    author_email="luabatepietro@hotmail.com",  # Seu email
    description="Jogo legal e maneiro",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/luabatepietro/alg_linha.git",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)

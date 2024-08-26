import os
from setuptools import setup, find_packages

def find_package_data(package, directory):
    paths = []
    for root, _, files in os.walk(os.path.join(package, directory)):
        for filename in files:
            paths.append(os.path.relpath(os.path.join(root, filename), package))
    return {package: paths}

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="alg_linha",
    version="0.1",
    packages=find_packages(),
    py_modules=['main', 'game', 'player', 'mola', 'inimigo', 'item', 'star', 'startscreen', 'telafinal'],  # Inclua 'main' como um módulo
    include_package_data=True,
    install_requires=[
        'numpy',
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'alg_linha = main:main',  # Aponta para a função 'main' dentro do arquivo 'main.py'
        ],
    },
    author="Lucas",
    author_email="luabatepietro@hotmail.com",
    description="Uma breve descrição do seu pacote",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/luabatepietro/alg_linha",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data=find_package_data('alg_linha', 'assets'),  # Coleta todos os arquivos dentro da pasta 'assets'
)

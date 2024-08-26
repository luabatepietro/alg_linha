from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="alg_linha",
    version="0.1",
    py_modules=['main', 'game', 'player', 'mola', 'inimigo', 'item', 'star', 'startscreen', 'telafinal', 'constantes'],  # Adicione os módulos que estão na raiz
    include_package_data=True,
    install_requires=[
        'numpy',
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'alg_linha = main:main',  # Aponta diretamente para o main.py
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
    package_data={
        '': ['assets/*.gif', 'assets/*.png', 'assets/*.webp'],
    },
)

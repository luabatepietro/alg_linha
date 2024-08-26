from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_assets_files():
    asset_files = []
    for dirpath, _, filenames in os.walk('assets'):
        for filename in filenames:
            asset_files.append(os.path.relpath(os.path.join(dirpath, filename), start=os.path.dirname(__file__)))
    return asset_files

setup(
    name="alg_linha",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'alg_linha = main:main',
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
        '': find_assets_files(),  # Inclui todos os arquivos encontrados dentro de 'assets'
    },
    data_files=[('assets', find_assets_files())]
)

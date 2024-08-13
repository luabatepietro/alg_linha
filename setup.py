from setuptools import setup, find_packages

setup(
    name="alg_linha",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pygame'
    ],
    entry_points={
        'console_scripts': [
            'my_package = my_package.main:main',
        ],
    },
    author="Lucas",
    author_email="luabatepietro@hotmail.com",
    description="Uma breve descrição do seu pacote",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/luabatepietro/alg_linha",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

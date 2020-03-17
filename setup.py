from setuptools import setup, find_packages

setup(
    name='proyecto_ciencia_datos',
    version='0.1',
    description='Un proyecto de ciencia de datos',
    author='Tu Nombre',
    author_email='tucorreo@gmail.com',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias requeridas
        'numpy',
        'pandas',
        'scikit-learn',
        # Agrega más dependencias según sea necesario
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

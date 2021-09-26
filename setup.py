from setuptools import setup, find_packages

setup(
    name='Depression_Detection',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
    
)
from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='rsa_pasaforte',
    version='1.0.0',
    description='RSA (Rivest-Shamir-Adleman) public-key cryptosystem algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jamespatrickryan/rsa-pasaforte',
    author='James Patrick Ryan A. Pasaforte',
    author_email='jamespatrick.pasaforte@g.msuiit.edu.ph',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7, <4',
    extras_require={
        'test': [
            'flake8==5.0.4',
            'tox==3.25.1',
            'pytest==7.1.2',
            'pytest-cov==3.0.0',
            'mypy==0.971',
        ],
    },
    package_data={
        'rsa_pasaforte': ['py.typed'],
    },
    project_urls={
        'Source': 'https://github.com/jamespatrickryan/rsa-pasaforte/',
    },
)

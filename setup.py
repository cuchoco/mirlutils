import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name = 'mirlutils',
    version = '0.0.2',
    description = 'Utils for medical image analysis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Jihwan Kim <kuchoco97@gmail.com>',
    packages = setuptools.find_packages(),
    keyword = ['utils', 'medical_image'],
    py_modules=['mirlutils'],
    python_requires = '>=3',
    zip_safe = False,
    license="MIT",
    url = 'https://github.com/cuchoco/mirlutils',
    
    classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Visualization',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.8',

    'Operating System :: OS Independent',
    ],
)
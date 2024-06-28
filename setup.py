from setuptools import setup, find_packages

setup(
    name='pythonalgosort',
    version='0.1.0',
    description='A Python library for sorting algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aarush Kute',
    author_email='aarushkute8@gmail.com',
    url='https://github.com/aarushk09/PythonSortingLibrary',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

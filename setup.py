from distutils.core import setup
import os

LOCAL = os.path.dirname(os.path.realpath(__file__))
README = open(LOCAL+'/README.md')

setup(
    name='ResponsiveTkinter',
    packages=['ResponsiveTkinter'],
    version='1.0.0',
    license='MIT',
    description='This is a simple library that allows you to create responsive widgets in your tkinter window.',
    long_description=README.read(),
    long_description_content_type="text/markdown",
    author='Legopitstop',
    author_email='officiallegopitstop@gmail.com',
    url='https://legopitstop.weebly.com/media.html',
    download_url='https://github.com/legopitstop/ResponsiveTkinter/archive/v1.0.0.tar.gz',
    keywords=['responsive', 'tkinter', 'resizeable'],
    classifiers=[
        'Development Status :: 5 - Production/Stable', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.9',
    ]
)
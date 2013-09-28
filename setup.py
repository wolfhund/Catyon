from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.0b'

install_requires = [    
    'twython==3.0.0',
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies    
]


setup(name='catyon',
    version=version,
    description="Multi-platform command-line based twitter client. Its opensource and made with Python.",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='python twitter cmd opensource linux windows mac catyon',
    author='Wolfhund',
    author_email='redocmalloc@hotmail.com',
    url='https://github.com/wolfhund/Catyon',
    license='GPL V2.0',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['catyon=catyon:main']
    }
)

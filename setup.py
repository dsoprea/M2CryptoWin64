import setuptools
import os

long_description = ""
install_requires = []

setuptools.setup(
      name='M2CryptoWin64',
      version='0.21.1',
      description="M2Crypto for Windows",
      long_description=long_description,
      classifiers=[],
      keywords='openssl ssl m2crypto',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=[]),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      package_data={
            'M2Crypto': [
                  'ssleay32.dll',
                  'libeay32.dll',
                  '__m2crypto.pyd',
                  '__m2crypto.pyc',
                  '__m2crypto.py',
            ],
      },
      scripts=[
      ],
)

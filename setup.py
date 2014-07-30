import setuptools
import os

import M2Crypto

app_path = os.path.dirname(M2Crypto.__file__)

with open(os.path.join(app_path, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = list(map(lambda s: s.strip(), f.readlines()))

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

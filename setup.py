import setuptools
import os
import sys
import distutils.command.install

def _pre_install():
      print("Verifying architecture.")

      if sys.platform != 'win32':
            raise SystemError("This package can only be installed on Windows systems.")

      is_64bits = sys.maxsize > 2**32

      if is_64bits is False:
            raise SystemError("This package can only be installed on 64-bit Windows systems.")

class _CustomInstall(distutils.command.install.install):
    def run(self):
        _pre_install()
        distutils.command.install.install.run(self)

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
      url='https://github.com/dsoprea/M2CryptoWin64',
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
      cmdclass={ 'install': _CustomInstall }
)

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

# We have to include the long-description here rather than reading it, because 
# we would need to read the package, and the root module-initializer tries to 
# load the binary. This will fail if we're assembling this package on a 
# platform that's not binary-compatiable with Windows.

long_description = """\
This is an installable version of the 64-bit Windows M2Crypto binaries for Python made 
available by `grr <https://code.google.com/p/grr/wiki/BuildingWindowsClient#M2Crypto>`_.

This package is available on PyPI as `M2CryptoWin64 <https://pypi.python.org/pypi/M2CryptoWin64>`_.

See `M2CryptoWindows <https://github.com/dsoprea/M2CryptoWindows>`_ for more 
information.


---------------
Troubleshooting
---------------

If you see an error like the following during install, then you [allegedly] 
have an old version of setuptools::

    error: option --single-version-externally-managed not recognized

This seems to happen consistently for me, under Windows, even though it
*pip* seems to download the latest version of *setuptools* when you install it.

To get around this, use the `--egg` option::

    C:\>pip install --egg M2CryptoWin64
"""

install_requires = []

setuptools.setup(
      name='M2CryptoWin64',
      version='0.21.1-3',
      description="M2Crypto for Windows (64-bit)",
      long_description=long_description,
      classifiers=[],
      keywords='openssl ssl m2crypto',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/M2CryptoWin64',
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

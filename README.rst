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

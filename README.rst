==============
CRC Calculator
==============

|PyPI version|

Usage with Installation
-----------------------

1. Install ``crc-calculator`` using pip.

.. code:: bash

   $ pip install crc-calculator

2. Run ``crc`` command with arguments.

.. code:: bash

   $ crc -h
    usage: crc -p [POLYNOMIAL] -d [DATA]

   $ crc --polynomial 100101 --data 101101001
    checksum: 00010
    validation: 00000

Usage of Windows Executable
---------------------------

1. Download ``crc-calculator-{version}-windows.zip`` from the release.
2. Unzip file and run the powershell on that path.
3. Run ``.\crc`` command with arguments

.. code:: bash

   $ .\crc -h
    usage: crc -p [POLYNOMIAL] -d [DATA]

   $ .\crc --polynomial 100101 --data 101101001
    checksum: 00010
    validation: 00000

.. |PyPI version| image:: https://img.shields.io/pypi/v/crc-calculator
   :target: https://pypi.org/project/crc-calculator/

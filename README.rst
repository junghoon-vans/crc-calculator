==============
CRC Calculator
==============

|PyPI version|

Installation
------------

.. code:: bash

   $ pip install crc-calculator

How to use
----------

.. code:: bash

   $ crc -h
    usage: crc -p [POLYNOMIAL] -d [DATA]

   $ crc --polynomial 100101 --data 101101001
    checksum: 00010
    validation: 00000

.. |PyPI version| image:: https://img.shields.io/pypi/v/crc-calculator
   :target: https://pypi.org/project/crc-calculator/

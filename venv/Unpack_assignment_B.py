
"""
* Assignment: Unpack Assignment Split
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Split input data
    2. Separate ip address and host name
    3. Run doctests - all must succeed

Polish:
    1. Podziel dane wejściowe
    2. Odseparuj adres ip i nazwę hosta
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.split()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ip is not Ellipsis, \
    'Assign your result to variable `ip`'
    >>> assert host is not Ellipsis, \
    'Assign your result to variable `host`'
    >>> assert type(ip) is str, \
    'Variable `ip` has invalid type, should be str'
    >>> assert type(host) is str, \
    'Variable `hosts` has invalid type, should be str'

    >>> ip
    '10.13.37.1'

    >>> host
    'nasa.gov'
"""
def _test():
    import doctest
    doctest.testmod()


DATA = '10.13.37.1 nasa.gov'

# String with IP address: 10.13.37.1
# type: str

result = DATA.split(" ", 1)
ip = result[0]

# String with host name: nasa.gov
# type: str
host = result[1]

_test()

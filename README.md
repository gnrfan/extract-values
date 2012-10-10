Extract Values
==============

A Python module for extracting values out of a string using a simple pattern instead of a regular expression by defining groups of named characters using a pair of opening and closing delimiters.

Examples:

```python
    from extract_values import extract_values

    >>> extract_values('/2012/08/12/test.html', '/{year}/{month}/{day}/{title}.html')
    { 'year': '2012', 'month': '08', 'day': '12', 'title': 'test' }

    >>> extract_values('John Doe <john@example.com> (http://example.com)', '{name} <{email}> ({url})')
    {'name': 'John Doe', 'email': 'john@example.com', 'url': 'http://example.com' }

    >>> extract_values('from 4th October  to 10th  October', 'from `from` to `to`', strip_values=True, whitespace=1, delimiters=['`', '`'])
    {'from': '4th October', 'to': '10th October' }

    >>> extract_values('Convert 1500 Grams to Kilograms', 'convert {quantity} {from_unit} to {to_unit}', lowercase=True)
    {'quantity': '1500', 'from_unit': 'grams', 'to_unit': 'kilograms' }]

    >>> extract_values('The time is 4:35pm here at Lima, Peru', 'The time is :time here at :city', delimiters=[':', ''])
    {'time': '4:35pm', 'city': 'Lima, Peru'}
```

Optional parameters:

* **lowercase** - When True is passed the string is lowercased first              
* **whitespace** - Minimal number of extra whitespace to remove                   
* **strip_values** - When True calls strip() for each value removing whitespace   
* **delimiters** - A sequence with only the opening and closing delimiters

In order to install this package from [PyPi](http://pypi.python.org) you can run any of these commands:

    easy_install extract-values

or

    pip install extract-values

This library can also be installed directly from Github with the following command:

    pip install git+ssh://git@github.com/gnrfan/extract-values.git

This little project was inspired by a similar [Node.js](http://nodejs.org/) module created by sri-lankan developer [Lakshan Perera](http://laktek.com/) available [here](https://github.com/laktek/extract-values).

(c) 2012 - Antonio Ognio <antonio@ognio.com> - Distributed under the BSD license - Made in Peru.

Extract Values
==============

A Python module for extracting values out of a string using a simple pattern of named group of characters delimited by a pair of opening and closing delimiters as a simpler alternative to using regular expressions.

Examples:

    from extract_values import extract_values

    >>> extract_values('/2012/08/12/test.html', '/{year}/{month}/{day}/{title}.html')
    { 'year': '2012', 'month': '08', 'day': '12', 'title': 'test' }

    >>> extract_values('John Doe <john@example.com> (http://example.com)', '{name} <{email}> ({url})')
    {'name': 'John Doe', 'email': 'john@example.com', 'url': 'http://example.com' }

    >>> extract_values('from 4th October  to 10th  October', 'from `from` to `to`', strip_values=True, whitespace=1, delimiters=['`', '`'])
    {'from': '4th October', 'to': '10th October' }

    >>> extract_values('Convert 1500 Grams to Kilograms', 'convert {quantity} {from_unit} to {to_unit}', lowercase=True)
    {'quantity': '1500', 'from_unit': 'grams', 'to_unit': 'kilograms' }]

Optional parameters:

* **lowercase** - When True is passed the string is lowercased first              
* **whitespace** - Minimal number of extra whitespace to remove                   
* **strip_values** - When True calls strip() for each value removing whitespace   
* **delimiters** - A sequence with only the opening and closing delimiters

This module can be installed directly from Github using pip with the following command:

    pip install git+ssh://git@github.com/gnrfan/extract-values.git

This little project was inspired by a similar [Node.js](http://nodejs.org/) module created by sri-lankan developer [Lakshan Perera](http://laktek.com/) available [here](https://github.com/laktek/extract-values).

(c) 2012 - Antonio Ognio <antonio@ognio.com> - Distributed under the BSD license - Made in Peru.

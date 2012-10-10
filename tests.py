"""Tests for extract_values.py"""

import unittest
from extract_values import extract_values

class Test(unittest.TestCase):
    """General test case for extract_values.py"""

    entries = [
        {
            "string" : "a:b,c:d", 
            "pattern" : "a:{a},c:{c}",
            "values" : {
                "a": "b", 
                "c": "d" 
            }
        },
        {
            "string" : "/2012/08/12/test.html", 
            "pattern" : "/{year}/{month}/{day}/{title}.html", 
            "values" : { 
                "year": "2012", 
                "month": "08", 
                "day": "12", 
                "title": "test" 
            }
        },
        {
            "string" : "Content-Type: text/html; charset=utf-8", 
            "pattern" : "Content-Type: {mime}; charset={charset}", 
            "values" : {
                "mime": "text/html", 
                "charset": "utf-8"
            }
        },
        {
            "string" : "/assets/images/logo.jpg", 
            "pattern" : "{dirpath}/{basename}.{extension}", 
            "values" : {
                "dirpath": "/assets/images", 
                "basename": "logo",
                "extension": "jpg"
            }
        },
        {
            "string" : "some long file name.html.mustache", 
            "pattern" : "{name}.{output_extension}.{template_extension}", 
            "values" : {
                "name": "some long file name", 
                "output_extension": "html", 
                "template_extension": "mustache"
            }
        },
        {
            "string" : "Antonio Ognio <gnrfan@gnrfan.org> (http://gnrfan.org)", 
            "pattern" : "{name} <{email}> ({url})", 
            "values" : {
                "name": "Antonio Ognio", 
                "email": "gnrfan@gnrfan.org", 
                "url": "http://gnrfan.org"
            }
        },
        {
            "string" : "a:b,c:d", 
            "pattern" : "a:{{a}},c:{{c}}", 
            "values" : {
                "a": "b", 
                "c": "d"
            },
            "extra_params" : { 
                "delimiters": ["{{", "}}"] 
            } 
        },
        {
            "string" : "red  blue   green",
            "pattern" : "{first} {second} {third}", 
            "values" : {
                "first": "red", 
                "second": "blue",
                "third": "green"
            },
            "extra_params" : {
                "whitespace": 1 
            }
        },
        {
            "string" : "red\n blue\n\ngreen", 
            "pattern" : "{first}\n{second}\n{third}",
            "values" : {
                "first": "red",
                "second": "blue",
                "third": "green"
            },
            "extra_params" : { 
                "whitespace": 1
            } 
        },
        {
            "string" : "from 4th October  to 10th  October", 
            "pattern" : "from `from` to `to`",
            "values" : {
                "from": "4th October",
                "to": "10th October"
            },
            "extra_params" : {
                "whitespace" : 1, 
                "delimiters" : ["`", "`"]
            }
        }, 
        {
            "string" : "4th October  to 10th  October", 
            "pattern" : "from `from` to `to`", 
            "values" : {},
            "extra_params" : {
                "whitespace" : 1, 
                "delimiters": ["`", "`"] 
            }
        },
        {
            "string" : "Convert 1500 Grams to Kilograms",
            "pattern" : "convert {quantity} {from_unit} to {to_unit}", 
            "values" : {
                "quantity": "1500", 
                "from_unit": "grams", 
                "to_unit": "kilograms"
            },
            "extra_params" : {
                "lowercase": True
            } 
        }
    ]

    def test_expected_values(self):
        for entry in self.entries:
            params = {}
            params['string'] = entry['string']
            params['pattern'] = entry['pattern']
            if 'extra_params' in entry:
                params.update(entry['extra_params'])
            self.assertEqual(extract_values(**params), entry['values'])


if __name__ == "__main__":
        unittest.main()

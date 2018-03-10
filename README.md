# configuration-options
Translate HJSON, YAML to JSON. For configuration.

## Get started

1. Install [`pipenv`](https://pipenv.readthedocs.io/en/latest/basics/#example-pipenv-workflow).
2. `pipenv install`
3. `pipenv shell` to get started hacking!

## Example

```
$ cat example/complicated.yml
invoice: 34843
date   : 2001-01-23
given  : Chris
family : Dumars
address:
  lines: |
    458 Walkman Dr.
    Suite #292
  city    : Royal Oak
  state   : MI
  postal  : 48046
  product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
    - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
      tax  : 251.42
      total: 4443.52
      comments: >
        Late afternoon is best.
        Backup contact is Nancy
        Billsmer @ 338-4338.
$ python main.py translate example/complicated.yml --sniff
{"invoice": "34843", "date": "2001-01-23", "given": "Chris", "family": "Dumars", "address": {"lines": "458 Walkman Dr.\nSuite #292\n", "city": "Royal Oak", "state": "MI", "postal": "48046", "product": [{"sku": "BL394D", "quantity": "4", "description": "Basketball", "price": "450.00"}, {"sku": "BL4438H", "quantity": "1", "description": "Super Hoop", "price": "2392.00", "tax": "251.42", "total": "4443.52", "comments": "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338.\n"}]}}
```

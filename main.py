"""configuration-options.

Usage:
    co --version
    co translate <file> [(--type=<filetype> | --sniff )]

Options:
    --version   Show version

"""

import os
import json

from docopt import docopt
from schema import Schema, Optional, Use, And, Or, SchemaError

from strictyaml import load, Map, Str, Int, Seq, YAMLError
from hjson import loads as hjsonLoads
from enum import Enum

def loadYaml(possiblyYaml):
    return load(possiblyYaml).data

class Filetype(Enum):
    UNKNOWN = 1
    YAML = 2
    HJSON = 3

loaders = {
        Filetype.HJSON: { 
            'loader': hjsonLoads,
            'ext': ['.hjson'] 
            },
        Filetype.YAML: {
            'loader': loadYaml,
            'ext': [ '.yml', '.yaml' ],
            },
        Filetype.UNKNOWN: {
            'loader': lambda: "unknown filetype",
            'ext': [ '.*' ],
        },
    }

def peek(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

def sniff(f):
    line = peek(f)

    if '{' in line:
        return Filetype.HJSON
    elif ':' in line:
        return Filetype.YAML
    else:
        return Filetype.UNKNOWN


if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.0.1')

    schema = Schema({
        '<file>': And(Use(str), Use(open, error='file should be readable')),
        Optional('--sniff'): Or(None, True),
        Optional('--type'): Or(None, Use(str)),
        Optional('translate'): Use(bool),
        '--version': Or(None, Use(str)),
        })

    try:
        arguments = schema.validate(arguments)
    except SchemaError as e:
        exit(e)

    if arguments['--type'] is not None:
        for ft, info in loaders.items():
            if arguments['--type'] in ft.ext:
                ext = ft
    else:
        ext = sniff(arguments['<file>'])

    if ext is Filetype.UNKNOWN:
        print(loaders.get(ext)['loader']())
        exit(1)

    f = arguments['<file>']
    l = loaders.get(ext, lambda: "missing loader")

    try:
        v = l['loader']((f.read()))
        print(json.dumps(v))
    except Exception as e:
        print(e)

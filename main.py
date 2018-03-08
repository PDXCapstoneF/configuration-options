"""configuration-options.

Usage:
    co --version
    co translate <file> [(--type=<filetype> | --sniff )]

Options:
    --version   Show version

"""

from docopt import docopt

from strictyaml import load, Map, Str, Int, Seq, YAMLError
from hjson import loads as hjsonLoads

schema = Map({
        "name": Str(),
        "age": Int(),
})

def loadYaml(possiblyYaml):
    return load(possiblyYaml, schema).data


loaders = {
    '.hjson': hjsonLoads,
    '.yml': loadYaml,
    '.yaml': loadYaml,
}

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.0.1')
    print(arguments)
    with open(arguments['<file>']) as f:
        l = loaders.get(arguments['--type'], lambda x: "blah")
        try:
            print(l(f.read()))
        except Exception as e:
            print(e)

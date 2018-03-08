"""configuration-options.

Usage:
    main.py --version

Options:
    --version   Show version

"""
from strictyaml import load, Map, Str, Int, Seq, YAMLError
from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.0.1')
    print(arguments)

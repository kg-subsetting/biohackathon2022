

from argparse import ArgumentParser
import gzip
import random
import sys
import io
from typing import Optional, Union, List
from pathlib import Path

def genargs(prog: Optional[str] = None) -> ArgumentParser:
    parser = ArgumentParser(prog)
    parser.add_argument("--input", help="Input JSON dump", required=True)
    parser.add_argument("--output", help="Output random dump", required=True)
    parser.add_argument("--num", help="Number of items", required=True)
    return parser


def extract_random_lines(file_path: str, num_lines: int, output_file: str):
    with gzip.open(file_path, 'rt') as in_file:
        print('Reading input file...')
        lines = in_file.readlines()
        print('Random sampling, following lines will be selected:')
        random_lines = random.sample(range(1,len(lines)-1), num_lines)
        print(random_lines)
        with gzip.open(output_file, 'wt') as out_file:
            print('Writing output...')
            out_file.write('[\n')
            for i in random_lines:
                out_file.write(lines[i])    
            out_file.write(']\n')
        print('DONE')

def Random_Dump_Generator(argv: Optional[Union[str, List[str]]] = None, prog: Optional[str] = None) -> int:
    if isinstance(argv, str):
        argv = argv.split()
    opts = genargs(prog).parse_args(argv if argv is not None else sys.argv[1:])

    opts.input = Path(opts.input)
    if not opts.input.exists():
        print('There is no input file on: '.format(opts.input))
        return 1
    opts.output = Path(opts.output)
    opts.num = int(opts.num)

    extract_random_lines(opts.input, opts.num, opts.output)    

if __name__ == '__main__':
    Random_Dump_Generator(sys.argv[1:])
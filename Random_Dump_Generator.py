

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
    in_file = gzip.open(file_path, 'rt')
    out_file = gzip.open(output_file, 'wt')
    print('Getting input file line numbers...')
    lines = sum([1 for line in in_file])
    in_file.close()
    print('Number of lines: ', lines)
    print('Random sampling, following lines will be selected:')
    random_lines = random.sample(range(1, lines-1), num_lines)
    random_lines = sorted(random_lines)
    print(random_lines)
    print('Writing output...')
    out_file.write('[\n')
    ctr = 1
    in_file = gzip.open(file_path, 'rt')
    for line in in_file:
        if ctr in random_lines:
            out_file.write(line)
            random_lines.remove(ctr)    
        ctr += 1
    out_file.write(']\n')
    in_file.close()
    out_file.close()
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

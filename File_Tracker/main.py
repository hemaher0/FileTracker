import argparse
from my_package import my_function

def main():
    parser = argparse.ArgumentParser(description='My command-line tool')
    parser.add_argument('input_file', help='The input file to process')
    parser.add_argument('--output-file', help='The output file to write to')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file or input_file + '.out'

    my_function(input_file, output_file)

if __name__ == '__main__':
    main()
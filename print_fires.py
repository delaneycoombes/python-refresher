import my_utils
import argparse

# create parser to store information
parser = argparse.ArgumentParser(
    description='Print fires from desired country.')

# get inputs from command line
parser.add_argument('country', help='What country to search for')
parser.add_argument('country_column', type=int,
                    help='What column for the country')
parser.add_argument('fires_column', type=int, help='What column for the fires')
parser.add_argument('file_name', help='What CSV file to search')

# optional argument that specifies operation
parser.add_argument('--operation',
                    '-o',
                    choices=['mean', 'median', 'std'],
                    default=None,
                    help='Optional operation perfomred on returned values')

# read arguments when program is called
args = parser.parse_args()

# get fire values for desired country
fires = my_utils.get_column(args.file_name, args.country_column,
                            args.country, result_column=args.fires_column)

# apply specified operation or print fires list
if args.operation is None:
    print(fires)
elif not fires:
    print([])
elif args.operation == 'mean':
    print(my_utils.mean(fires))
elif args.operation == 'median':
    print(my_utils.median(fires))
elif args.operation == 'std':
    print(my_utils.standard_deviation(fires))

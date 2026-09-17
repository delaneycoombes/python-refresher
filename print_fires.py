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

# read arguments when program is called
args = parser.parse_args()

# get fire values for desired country
fires = my_utils.get_column(args.file_name, args.country_column,
                            args.country, result_column=args.fires_column)

print(fires)

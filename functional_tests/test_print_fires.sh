test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Exit code tests
run test_exit_success_no_operation python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv
assert_exit_code 0

run test_exit_success_mean python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv --operation mean
assert_exit_code 0

run test_exit_success_median python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv -o median
assert_exit_code 0

run test_exit_success_std python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv --operation std
assert_exit_code 0

run test_exit_missing_args python3 ../print_fires.py
assert_exit_code 2

run test_exit_bad_operation python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv --operation foo
assert_exit_code 2

# Raw list output tests
run test_raw_brazil python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv
assert_exit_code 0
assert_in_stdout 100
assert_in_stdout 150
assert_in_stdout 200

run test_raw_usa python3 ../print_fires.py USA 0 2 ../data/test_fires.csv
assert_exit_code 0
assert_in_stdout 20
assert_in_stdout 25

run test_raw_unknown_country python3 ../print_fires.py Nowhere 0 2 ../data/test_fires.csv
assert_exit_code 0
assert_in_stdout []

# Operation tests
run test_mean_brazil python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv --operation mean
assert_exit_code 0
assert_in_stdout 150.0

run test_median_brazil python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv -o median
assert_exit_code 0
assert_in_stdout 150.0

run test_std_brazil python3 ../print_fires.py Brazil 0 2 ../data/test_fires.csv --operation std
assert_exit_code 0
assert_stdout

run test_mean_usa python3 ../print_fires.py USA 0 2 ../data/test_fires.csv --operation mean
assert_exit_code 0
assert_in_stdout 22.5

run test_mean_unknown python3 ../print_fires.py Nowhere 0 2 ../data/test_fires.csv --operation mean
assert_exit_code 0
assert_in_stdout []
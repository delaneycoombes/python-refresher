# python-refresher
This project contains the python function, 'get_column()' which reads data from a CSV file, specifically 'Agrofood_co2_emissions.csv', to locate desired columns for two values and display their results. The function first locates the desired country in the country column, then it displays the results from a specified fire column for that country. The program uses command-line arguments to obtain the desired country, columns, and file from the user. Additionally, the fire values are outputted as integer values.

# File Descriptions
'my_utils.py' has the 'get_column()' function
'print_fires.py' calls the 'get_column()' function to display the fire emissions for a specific country
'run.sh' runs the 'print_fires.py' program
'environment.yml' contains the dependencies for the Mamba enviornment

# Assignment 3 Changes
Added mean, median, and standard deviation functions to 'my_utils.py'. Added command-line operation options to 'print_fires.py' and created unit and functional tests to test normal and error-producing behavior.

# Assignment 4 Changes 
Added a GitHub Actions continuous integration workflow that automatically runs style checks, unit tests, and functional tests. The workflow runs when changes are pushed to any branch and when a pull request is made to the master branch. Added a .gitignore file to exclude Jupyter notebook checkpoints and Python cache files. 
def get_column(file_name, query_column, query_value, result_column=1):

    # create an empty array to store results
    results = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                values = line.split(',')

                # check if the column contains desired country
                if values[query_column] == query_value:
                    try:
                        results.append(int(round(
                            float(values[result_column]))))
                    except ValueError:
                        pass
    except OSError:
        print('Error: file could not be opened.')

    return results

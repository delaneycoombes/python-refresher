def get_column(file_name, query_column, query_value, result_column):
   
    # create an empty array to store results
    results = []

    with open(file_name, "r") as file:
        for line in file:
            values = line.split(',')

            # check if the column contains desired country
            if values[query_column] == query_value:
                results.append(values[result_column])
                
    return None

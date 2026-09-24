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


def mean(arr):
    # display error message for empty arrays
    if not arr:
        raise ValueError("The mean of an empty array cannot be computed")

    # calculate the mean of an array of integers
    return sum(arr) / len(arr)

def median(arr):
    # display error message for empty arrays
    if not arr:
        raise ValueError("The median of an empty array cannot be computed")

    # sort and count the array elements
    sort = sorted(arr)
    n = len(sort)
    
    # divide by two and round down
    mid = n // 2

    # calculate the median of an array of integers
    if n % 2 == 0:
        return(sort[mid - 1] + sort[mid]) / 2
    return float(sort[mid])

def standard_deviation(arr):
    # display error message for empty arrays
    if not arr:
        raise ValueError("The standard deviation of an empty array cannot be computed")

    # calculate the mean and variance
    m = mean(arr)
    variance = sum((x - m) ** 2 for x in arr) / len(arr)

    # calculate standard devication which is the square root of the variance
    return variance ** 0.5

    
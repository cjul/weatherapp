
series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def mean(in_series):
    total = 0
    count = 0

    for value in in_series:
        if value is not None:   # skip missing values
            total += value
            count += 1

    if count == 0:
        return None

    return total / count

def variance(in_series):
   pass

def standard_deviation(in_series):
   return variance(in_series) ** 0.5

def interquartile_range(in_series):
    # Remove None values
    data = [x for x in in_series if x is not None]

    if len(data) == 0:
        return None

    # Sort the data
    data.sort()

    # Median helper
    def median(values):
        n = len(values)
        mid = n // 2

        if n % 2 == 0:
            return (values[mid - 1] + values[mid]) / 2
        else:
            return values[mid]

    n = len(data)
    mid = n // 2

    # Split into halves
    if n % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid + 1:]

    # Quartiles
    Q1 = median(lower_half)
    Q3 = median(upper_half)

    return Q3 - Q1

def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    pass

def series_range(in_series):    
    data = [x for x in in_series if x is not None]

    if len(data) == 0:
        return None

    minimum = min(data)
    maximum = max(data)

    return maximum - minimum

def read_csv(file,default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(len(lines[0])):
        data_table[lines[0][i]] = [default_value if (len(line[i]) == 0) else float(line[i]) for line in lines[1:]]
    return data_table

def get_user_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Enter the number of your choice: ")
    if choice.lower() == 'exit':
        return None
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        print("Invalid choice. Please try again.")
        return get_user_choice(options)
    choice = int(choice) - 1
    return options[choice]

def menu(data_table):
    print("Select a data series:")
    choice = get_user_choice(series_titles)

    series = data_table[choice]

    print(f"Range: {series_range(series)}")
    print(f"Mean: {mean(series)}")
    print(f"IQR: {interquartile_range(series)}")

if __name__ == "__main__":
    data = read_csv('weather.csv')
    menu(data)
    
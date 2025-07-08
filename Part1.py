def get_years():
    user_input = 0
    while True:
        try:
            user_input = int(input('How many years? '))

            if user_input <= 0:
                raise ValueError
            break
        except ValueError:
            print('Please enter a value greater than zero.')

    return user_input

def gather_rainfall(years):
    rainfall_data = []
    for i in range(years):
        for j in range(12):
            while True:
                try:
                    temp = int(input('How much rain (in inches) occured for year {}, month {}: '.format(i + 1, j + 1)))

                    if temp < 0:
                        raise ValueError

                    rainfall_data.append(temp)
                    break
                except ValueError:
                    print('Please enter a number 0 or greater')
    return rainfall_data

def main():
    years_requested = get_years()
    monthly_rainfall = gather_rainfall(years_requested)

    print('-Rainfall Report-')
    print('  Number of Months: {}'.format(years_requested * 12))
    print('  Total Inches of rainfall: {}'.format(sum(monthly_rainfall)))
    print('  Average Rainfall per Month: {}'.format(sum(monthly_rainfall) / len(monthly_rainfall)))

if __name__ == '__main__':main()

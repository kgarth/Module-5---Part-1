# Method used to collect the amount of years from the user
# Holds the user in a loop until input is valid.
def get_years():
    user_input = 0
    while True:
        try:
            user_input = int(input('How many years? '))

            if user_input <= 0:
                raise ValueError
            break
        except ValueError: # Exception raised if inputted data is invalid
            print('Please enter a value greater than zero.')

    return user_input # Returns integer

# Method that takes an integer (number of years) and collects monthly
# rainfall data using nested loops and stores it in a list and returns that list
def gather_rainfall(years):
    rainfall_data = [] # Temporary collection
    # Collection of month names for use in inner loop
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(years): # Outer loop
        for j in range(12): # Inner loop
            while True:
                try:
                    temp = int(input('How much rain (in inches) occured for year {} in {}: '.format(i + 1, months[j])))

                    if temp < 0:
                        raise ValueError

                    rainfall_data.append(temp)
                    break
                except ValueError: # Exception raised if input is invalid
                    print('Please enter a number 0 or greater')
    return rainfall_data # Returns list

def main():
    years_requested = get_years() # Calls method to collect number of years from user
    
    # Calls method inserting the number of years to receive list of collected rainfall
    monthly_rainfall = gather_rainfall(years_requested) 

    # Outputs report to screen
    print('-Rainfall Report-')
    print('  Number of Months: {}'.format(years_requested * 12))
    print('  Total Inches of rainfall: {}'.format(sum(monthly_rainfall)))
    print('  Average Rainfall per Month: {:.2f}'.format(sum(monthly_rainfall) / len(monthly_rainfall)))

if __name__ == '__main__':main()

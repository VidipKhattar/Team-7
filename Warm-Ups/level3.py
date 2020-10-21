""" Hackathon - Level 3 """

def oddish_evenish(number):
    """ Function to determine if the sum of a number's digits are odd or even.
    If odd, the number is oddish, and if even the number is evenish. """
    
    string_form = str(number)   # Converting number to a string
    list_digits = list(string_form) # Splitting string into a list
    
    count = 0   # Declaring the total count. This will become the sum of all digits.
    
    for digit in list_digits:   # Loop to go through every digit and add it to the count.
        digit_integer = int(digit)  # Converting the digit string into an integer
        count = count + digit_integer   # Adding the digit to the total count
    
    if count % 2 == 0:  # Finds if the count is even or not.
        type = "Evenish"    # If the count is even
    else:
        type = "Oddish" # If the count is odd
    return type # Return type (evenish or oddish)

if __name__ == '__main__':  # Testing it
    print(oddish_evenish(1190)) # Prints out "Oddish"
    print(oddish_evenish(523))  # Prints out "Evenish"

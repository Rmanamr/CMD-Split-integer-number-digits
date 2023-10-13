"""Python CMD program for splitting the digits of integer numbers.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
     """
     main function for interacting with the user
     """
     while(True):
     # while loop to keep the program running

        print("Please enter your integer number :")
        input_Number = int(input())
        result = integer_To_Digits_Splitter(input_Number)
        # passing the input_Number to the integer_To_Digits_Splitter function and storing the result in result variable

        print("Your digits from the most right digit to the most left digit :")
        array_Printer(result)
        # passing the result to the array_Printer to print each array element in a line

        print("***********************************")


def integer_To_Digits_Splitter(number):
    """
    function for splitting the digits of integer numbers.
    @param number: a number
    @type number: integer
    @return: array_Of_Digits
    @rtype: array of integers
    @examples: 
     >>> integer_To_Digits_Splitter(0)
         [0]
     >>> integer_To_Digits_Splitter(123)
         [3, 2, 1]   
    """
    string_Number = (str(number))
    # converting number to string to be able to use len() function

    number_Of_Digits = len(string_Number)
    # usung len() function to calculate number of digits

    array_Of_Digits = []
    # initializing an empty array to store digits in

    for i in range(number_Of_Digits):
        a = number//10
        reminder = number - a*10
        number = a
        array_Of_Digits.append(reminder)
        # appending the last digit to array_Of_Digits

    return array_Of_Digits

def array_Printer(array):
    """
    function for printing each array element in a line.
    @param array: an array of elements.
    @type array: anything like integer, double and string.
    @examples: 
         array_1 = []
         array_2 = [1, 2, 3]
     >>> array_Printer(array_1)
          
     >>> array_Printer(array_2)
         1
         2
         3
    """
    for element in array:
        print(element)


if __name__ == '__main__':
    main()
    # run the main function after executing this file
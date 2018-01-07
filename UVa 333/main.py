# Reza, TUM Informatics
# UVa_333

# Critical Input : "     THIS IS NOT A VALID DATA    "
# The correct output should truncate the leading and trailing spaces while printing the String.
# i.e., "THIS IS NOT A VALID DATA" is correct/incorrect.
# Another Info : If X appears in any spot other than the 10th digit, it's incorrect.

import sys

class CheckISBN:
    def __init__(self):
        #self.file = open("output.txt", "w")
        self.get_input()

    def reset_data(self):
        self.alpha_numeric_string = ""
        self.sum1 = 0
        self.sum2 = 0
        self.isValid = True
        self.num_digit = 0

    def calculation(self, isbn_str):
        isbn_str = isbn_str.lstrip() #deleting the leading spaces .... It can cause PE
        
        for ch in isbn_str:
            if(ch == 'X'):
                self.sum1 += 10
                self.sum2 += self.sum1
                self.num_digit += 1 
                if(self.num_digit != 10): #If X appears in any spot other than the 10th digit, it's incorrect.
                    self.isValid = False

            elif(ch.isdigit()):
                self.sum1 += ord(ch)-48
                self.sum2 += self.sum1
                self.num_digit += 1 
                
            elif(ch != '-' and ch != ' '):
                self.isValid = False

            self.alpha_numeric_string += ch

        #print "S1 : ", self.sum1
        #print "S2 : ", self.sum2
        #print "num digit  :", self.num_digit
        #print "String : ", self.alpha_numeric_string
        #print "Validity : " , self.isValid
        
        self.alpha_numeric_string = self.alpha_numeric_string.rstrip() #deleting the trailing spaces .... It can cause PE

        if(self.num_digit == 10 and self.sum2 % 11 == 0 and self.isValid == True):
            #self.file.write("%s is correct.\n" % self.alpha_numeric_string)
            print(self.alpha_numeric_string, "is correct.")
        else:
            #self.file.write("%s is incorrect.\n" % self.alpha_numeric_string)
            print(self.alpha_numeric_string, "is incorrect.")


    def get_input(self):
        for raw_str_input in sys.stdin.read().splitlines():
            self.reset_data()
            self.calculation(raw_str_input)

     
if __name__ == '__main__':
    obj = CheckISBN()

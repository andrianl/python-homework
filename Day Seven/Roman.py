class RomanNumerals(int):

    values=[1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    symbols = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    def __init__(self, number, bit=10):
        self.number=number
        self.bit=bit



    # def ArabicToRoman(self, number):
    #     ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    #     tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    #     hundredth=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    #     thousands=["","M","MM","MMM","MMMM"]
        

    #     one=ones[self.number%10]
    #     ten=tens[self.number//10%10]
    #     hundred=hundredth[self.number//100%10]
    #     thousand=thousands[self.number//1000]

    #     return  thousand+hundred+ten+one




    def arabic_to_roman(self, number):
        values=[1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        symbols = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman=''
        i = 0
        while  number > 0:
            for _ in range(number // values[i]):
                roman+= symbols[i]
                number -= values[i]
            i += 1
        return roman

    



    def __sub__(self,other):
        self.number-=other
        return self.arabic_to_roman(self.number)


    def __add__(self,other):
        self.number+=other
        return self.arabic_to_roman(self.number)

    def __mul__(self, other):
        self.number*=other
        return self.arabic_to_roman(self.number)

    def __truediv__(self, other):
        self.number/=other
        return self.arabic_to_roman(self.number)

    def __mod__(self,other):
        self.number%=other
        return self.arabic_to_roman(self.number)

    def __neg__(self):
        return - self.number

    def __lt__(self,other):
        if(self.number < other):
            return f'{self.number} is less than {other}'
        else:
            return f'{self.number} is not less than {other}'

    def __gt__(self,other):
        if(self.number > other:
            return True
        else:
            return False

    def __eq__(self, other):
        if (self.number == other:
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.number != other):
            return True
        else:
            return False

    def __le__(self, other):
        if (self.number <= other):
            return True
        else:
            return False

    def __ge__(self, other):
        if (self.number >=other):
            return True
        else:
            return False

        


















x=(int(input('x:')))
y=(int(input('y:')))
        
roman = RomanNumerals(x)
roman2 = RomanNumerals(y)
print(roman+4)

print(roman.arabic_to_roman(x))
print(roman.arabic_to_roman(y))

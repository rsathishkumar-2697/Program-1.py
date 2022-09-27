class Calacultor:
    def values(self,value1 = 0 ,value2 = 0,operator = ""):
        result= 0
        if operator == '+':
            result = value1 + value2
        elif operator == '-':
            result = value1 - value2
        elif operator == '*':
            result = value1 * value2
        elif operator == '/':
            try:
                result = value1 / value2
            except ZeroDivisionError:
                result = "Denominator Must not be Zero"
        return result

cal = Calacultor()
print(cal.values(5,2,'*'))

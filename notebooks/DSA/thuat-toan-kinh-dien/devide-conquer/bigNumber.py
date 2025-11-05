def makeEqualLength(a, b):
    len1 = len(a)
    len2 = len(b)
    if len1 < len2:
        for i in range(len2 - len1):
            a = '0' + a
        return a, b, len2
    elif len2 < len1:
        for i in range(len1 - len2):
            b = '0' + b
        return a, b, len1
    return a, b, len1

class bigNumber:
    
    @staticmethod
    def addingString(a, b):
        #* check if numbers are negative
        a_negative = a[0] == '-'
        b_negative = b[0] == '-'
        
        if a_negative:
            a = a[1:]
        if b_negative:
            b = b[1:]
        
        #* if negative, adding "-" after adding        
        if a_negative and b_negative:
            result = bigNumber.addingString(a, b)
            return "-" + result if result != '0' else '0'
        
        #* if one is negative, use subtraction
        # if a_negative:
        #     return bigNumber.subtractingString(b, a)
        # if b_negative:
        #     return bigNumber.subtractingString(a, b)
        
        #* normal case
        a, b, length = makeEqualLength(a, b)
        carry = 0
        result = []
        
        for i in range(length-1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            carry = digit_sum // 10
            result.append(str(digit_sum % 10))
            
        if carry: 
            result.append(str(carry))
            
        #* revert and join result
        result_str = ''.join(result[::-1])

        #* remove 0s
        result_str = result_str.lstrip('0')
        return result_str if result_str else '0'
    
a = input()
b = input()

print("a" + "b: ", bigNumber.addingString(str(a), str(b)))
#
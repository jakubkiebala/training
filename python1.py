def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    
    if n == 0:
        return "zero"
    
    result = ""
    
    if n >= 1000:
        thousand = n // 1000
        if thousand == 1:
            result += "one thousand "
        else:
            result += number_to_words(thousand) + " thousand "
        n %= 1000
    
    if n >= 100:
        result += hundreds[n // 100] + " "
        n %= 100
    
    if n >= 10 and n < 20:
        result += teens[n - 10] + " "
        return result.strip()
    
    if n >= 20:
        result += tens[n // 10] + " "
        n %= 10
    
    if n > 0:
        result += ones[n] + " "
    
    return result.strip()

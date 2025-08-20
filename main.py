start_cur_type = str(input("What currency are you trying to convert? "))

USD_conversion_rates = {
        #equivalencies of 1 US dollar
        "EUR" : 0.85926,
        "INR" : 87.08036,
        "GBP" : 0.74174,
        "CNY" : 7.1834,
        "JPY" : 147.7615,
        "KRW" : 1392.84784,
        "CAD" : 1.38704,
        "MYR" : 4.226,
        "MXN" : 18.8403,
        "JMD" : 160.13865,
        "VND" : 26312.32778,
    }

while not(USD_conversion_rates.__contains__(start_cur_type) or start_cur_type == "USD"):
    print("Sorry! This currency is not included.")
    start_cur_type = str(input("What currency are you trying to convert? "))

end_cur_type = str(input("What currency are you trying to convert to? "))

while not(USD_conversion_rates.__contains__(start_cur_type) or end_cur_type == "USD"):
    print("Sorry! This currency is not included.")
    end_cur_type = str(input("What currency are you trying to convert to? "))

start_cur_amount = float(input("How much {} are you trying to convert? ".format(start_cur_type)))
if (start_cur_type == "USD"):
    end_cur_amount == start_cur_amount * USD_conversion_rates[end_cur_type]
    print("Your {} USD is the equivalent of {} {}".format())

#write a program to convert temperature from celsius to fahrenheit.
#taking temperature in celsius as input
celsius_temp = float(input("Enter tempreture in celsius: "))

#converting it to f
fah_temp = (celsius_temp * 9/5) + 32

#printing temperature in fahrenheit
print("Temperature in fahrenheit :", fah_temp)
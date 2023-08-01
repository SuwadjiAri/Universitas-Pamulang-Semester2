# input 4 variable
variable_one = input("masukkan variable 1=")
variable_two = input("masukkan variable 2=")
variable_three = input("masukkan variable 3=")
variable_four = input("masukkan variable 4=")

variable_one = int(variable_one)
variable_two= int(variable_two)
variable_three = int(variable_three)
variable_four = int (variable_four)

print("variable 1=", variable_one)
print("variable 2=", variable_two)
print("variable 3=", variable_three)
print("variable 4=", variable_four)

result_maks_one = int(0)
if variable_one > variable_two:
    result_maks_one = variable_one
else:    
    result_maks_one = variable_two 
    
result_maks_two = int(0)
if variable_three > variable_four:
    result_maks_two = variable_three
else:
    result_maks_two = variable_four

last_maks = int (0)
if result_maks_one > result_maks_two:
    last_maks = result_maks_one
else:
    last_maks = result_maks_two
    
print("nilai terbesar dari 4 nilai adalah", last_maks)
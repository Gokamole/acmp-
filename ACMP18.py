input_data = open('input.txt', 'r')
data = input_data.read ()
output_data = open ('output.txt', 'w')
a = int(data)
factorial = 1
while a > 1:
    factorial *= a
    a -= 1
output_data.write(str(factorial))
input_data.close()
output_data.close()
input_data = open('input.txt', 'r')
data = input_data.read ()
output_data = open ('output.txt', 'w')
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if a*b == c:
     output_data.write('YES')
else:
    output_data.write('NO')
input_data.close()
output_data.close()

input_data = open('input.txt', 'r')
output_data = open ('output.txt', 'w')
data = input_data.read ()
data = data.split()
a = int(data[0])
b = int(data[1])
while a!=0 or b!=0:
    if a>b:
        a=a%b
        if a==0:
            break
    else:
        b=b%a 
        if b==0:
            break
if a==0:
    c=(int(data[0])*int(data[1]))/b
    output_data.write(str(c))
else:
     c=(int(data[0])*int(data[1]))/a
     output_data.write(str(c))
input_data.close()
output_data.close()
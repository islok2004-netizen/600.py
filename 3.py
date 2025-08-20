
input_number=12345
output=0
while input_number:
    output += input_number %10
    input_number //= 10
print(output)
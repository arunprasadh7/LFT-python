# 2 Exception handling

# division by zero

try:
    num = int(input('Enter numerator: '))
    den = int(input('Enter denominator: '))
    result = num/den
    # print(result)

except ZeroDivisionError as z:	
   	print(z,': Denominator cannot be zero.')

except ValueError as v:
    print(v,': Enter numeric values.')

except Exception:
	print('Some error occured')

else:
	print(result)

finally:
	print('Finally block always executes.')

print('Bye')

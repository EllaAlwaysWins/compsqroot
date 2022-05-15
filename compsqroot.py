#import complex math module
import cmath

#request input from user
num = complex(input('Enter complex number:'))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.2f} + {2:0.2f}j'.format(num,num_sqrt.real,num_sqrt.imag))

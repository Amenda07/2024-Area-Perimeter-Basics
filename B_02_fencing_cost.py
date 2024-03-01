
def num_check(question):
    error = 'Please enter a number that is more than zero'
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

keep_going='yes'
while keep_going == 'yes':

   width=num_check('width: ')
   height=num_check('Height: ')
   cost=num_check('cost per meter: ')

   perimeter = (int(width) + int(height)) * 2
   price=int(perimeter)*int(cost)

   print(f'perimeter is {perimeter}')
   print(f'cost per meter is {cost}')
   print(f'Total cost is ${price:.2f}')
   print()
   keep_going=input("Do you want to continue? ")

print("Thank you for using our program")


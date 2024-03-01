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

        area=int(width)*int(height)
        perimeter= (int(width)+ int(height)) * 2
        print()

        print(f'perimeter is {perimeter}')
        print(f'area is {area}')

        keep_going= input("Do you want to keep going? ")
        print()

print('Thank you for using our program')


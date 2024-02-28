def num_check(question) :

    error=('Please enter a number that is more than zero\n')
    while True:

        try:
            response = float(input(question))

            if response > 0 :
                return response
            else:
                print(error)
        except ValueError :
            print(error)

#main routine goes here
for item in range (0, 2):
    width = int(num_check ('width: '))
    print(width)

print()

for item in range (0, 2):
    height = int(num_check ('Height: '))
    print(height)

print()

area=width*height
perimeter=2 * (width+height)
print(f" The area is {area}")
print(f" The perimeter is {perimeter}")

import csv

#unit 5-8

#unit 5 introduced reading from text files and handing exceptions

def starts_with(filename, letter):
    #this function parses through a file and finds every word that starts with the letter specified 
    #in the parameter
    with open(filename) as file:
        count = 0
        word_set = set()
        for line in file:
            words = line.lower().split()
            for word in words:
                if word[0] == letter:
                    count += 1
                    word_set.add(word)
        # print(word_set)
        return count

def zip_lookup(filename, zip_code):
    with open(filename) as zip_database:
        csv_reader = csv.reader(zip_database) #(turns the file from the with-as statement into a csv object)
        next(csv_reader) #skips the header row (only use if there is a header row in the file)
        for record in csv_reader: #iterates over each line
            if record[0] == zip_code: #
                return record[1]
        
        #raises a value error if the entered zip code isn't in the file
        raise ValueError("Unknown zip code: " + zip_code)

#this function finds out if number 'a' is equal to the number 'b' raised to any power (x)
#for example, if a=64 and b=2, is_power() will return True, since 64 is 2 raised to some power (x)
def is_power(a, b):
    if a == 1 or a == b:
        return True
    elif a % b == 0:
        return is_power(a/b , b)
    else: 
        return ValueError(str(a) + " is not a power of " + str(b))

print(is_power(1, 2)) #returns True since a = 1
print(is_power(34, 34)) #returns True since a = b
print(is_power(8, 2)) #returns True since 2^3 = 8
print(is_power(34, 5)) #returns a ValueError saying that '34 is not a power of 5'

def what_power(a, b, x=0):
    if a == 1:
        return 0
    elif a % b == 0:
        return 1 + what_power(a/b , b)
    else:
        raise ValueError(a + ' is not a power of ' + b)

print(what_power(8 , 2)) #returns 3 because 8 = 2^3
print(what_power(625, 5)) #returns 4 because 5*5*5*5 = 625

#unit 7 focused on sorting and time complexity
#sorting refers to arranging elements in a data structure in some kind of order

#in place sort - a sort that's destructive (meaning a copy of the original data structure will not exist)

#unit 8: lists and tuples

my_list = [2 * x for x in range(50)] #you can create lists like this
print(my_list)

#takes input for 3 fields (first, middle, and last names) and creates a tuple out of them
def tuplify():
    first = input('Enter your first name: ')
    middle = input('Enter your middle name: ')
    last = input('Enter your last name: ')
    if middle != '':
        return (first, middle, last)
    else:
        return (first, last)

sample = [x for x in range(11)] #a list from the range 0 <= x <= 10
sample2 = [x for x in range(11)] #a list from the range 0 <= x <= 10
sample3 = [x for x in range(11)] #a list from the range 0 <= x <= 10


def cubed_while_loop(a_list):
    z = 0
    while z < len(a_list):
        a_list[z] = a_list[z] ** 3
        z += 1
    return a_list

def cubed_for_loop(a_list):
    for index in range(len(a_list)):
        a_list[index] = a_list[index] ** 3
    return a_list

print(cubed_while_loop(sample)) #two functions that use different kinds of loops to do the same thing
print(cubed_for_loop(sample2))

def reversal(a_list):
    new_list = []
    length = len(a_list)-1
    z = 0
    while z < length:
        new_list.append(a_list[length-z])
        z += 1
        if z == length:
            new_list.append(a_list[0])
            return new_list

print(reversal(sample2))

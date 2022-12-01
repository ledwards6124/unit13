#lce1868
#Section 01
#Luke Edwards

def div_by_3_or_5(a_list, n, k=1):
    if k % 3 == 0 or k % 5 == 0:
        a_list.append(k)
    elif k == n:
        return a_list
    return div_by_3_or_5(a_list, n, k+1)

a_list = []      
#print(div_by_3_or_5(a_list, 20, 1))

def find_words(filename, letter):
    word_list = []
    with open(filename) as file:
        for line in file:
            for word in line:
                splitted = word.split(' ')
                if splitted[0] == letter:
                    word_list.append(splitted[word])
    return word_list

def fill_week():
    week = []
    z = 1
    while z < 8: 
        week.append(z)
        z += 1
    return week

def calendar_month(weekday, day_count):
    week_dict = {
        'sunday': 0,
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6
    }
    month = []
    week1 = fill_week()
    week2 = fill_week()
    week3 = fill_week()
    week4 = fill_week()





    


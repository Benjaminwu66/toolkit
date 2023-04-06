lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')


wh = 35
rate = 51.45
if wh > 35
    rate = 88.9

input


letters_lst = ["a", "b", "c", "d"]

for letter in letters_lst:
    print(letter)



# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.


f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}

nf_suburbs = []

for suburb in nf_suburbs:
    f_suburbs.pop(suburb)

f_suburbs.update({
    "Fairfield": 18081,
    "Fairfield East": 5273,
    "Fairfield Height": 7517,
    "Fairfield West": 11575,
    "Fairlight": 5840,
    "Fiddletown": 233,
    "Five Dock": 9356,
    "Flemington": None,
    "Forest Glen": None,
    "Forest Lodge": 4583,
    "Forestville": 8329,
    "Freemans Reach": 1973,
    "Frenchs Forest": 13473,
    "Freshwater": 8866
})

print(f_suburbs)



numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest = number[0]
print('Before', temp_largest)

for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print(number, temp_largest)

print(f'The largest value is {temp_largest}')


numbers = [3,9,1,5,7,2,11,0,3,12,3,15]

largest = max(numbers)

print(f'The largest value is (largest)')




for i in range(1,4):
    for j in range(1,4):
        if i <= j:
            print(i,j)









import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code

female_max=[]
male_max=[]
femaletimes=0
maletimes=0
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename) as file:
        femalesum=0
        malesum=0
        femaletimes=0
        maletimes=0
        for line in file:
            line1 =line.rstrip('\n')
            name = line1.split(',')[0]
            gender = line1.split(',')[1]
            fre=line1.split(',')[2]
            if gender == 'F':
                femalesum += int(fre)
            else:
                malesum += int(fre)
            if name== first_name:
                if gender=='F':
                    femaletimes=int(fre)
                else:
                    maletimes=int(fre)
        female_freq= femaletimes /femalesum*100
        male_freq= maletimes /malesum*100
        if min_male_frequency < male_freq:
            min_male_frequency = male_freq
            male_first_year = int(year)
        if min_male_frequency == male_freq:
            if male_first_year != None:
                if male_first_year > int(year):
                    male_first_year = int(year)
        if min_female_frequency < female_freq:
            min_female_frequency = female_freq
            female_first_year = int(year)
        if min_female_frequency == female_freq:
            if female_first_year != None:
                if female_first_year > int(year):
                    female_first_year = int(year)
            


	
if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

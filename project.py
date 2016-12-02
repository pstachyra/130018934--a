# -*- coding: utf-8 -*
"""
Created on Mon Nov 21 15:18:26 2016

@author: Vanessza And Emily some lil help fromm Pavs
"""

from J6305 import Spectrometer
import time
x = 1
info = ('This program runs the spectrophotometer readings and saves the results in a file named absorbance(x).txt. Where x is the number of different experiments the user runs. The data is saved in a tabulated format, with the headers of wl (wavelength in nm), and rd (reading). The data is ready for statistical analysis in R studio. Use constant time increments and wavelength ranges for more reliable results.\n')
input('Insert cuvette! Then press enter.')
a = input('Are you ready? (yes/no/help) ')
if a == 'help':
    print(info)
    a = input('Are you ready? (yes/no): ')
if a == 'yes':
    name = input('Please enter a filename to save your results: ')
    filename = '{}.txt'.format(name)
    myfile= open(filename, 'w')
    b = int(input('Enter minimum wavelength (nm): '))
    d = int(input('Please enter maximum wavelength: '))
    i = int(input('What incerements would you like to use?: '))
    spec = Spectrometer()
    myfile.write('#Min wavelength:{:5} Max wavelength:{:5} Increments:{:5}\n'.format(b,d,i))
    myfile.write('wl\trd')
    spec.set_wavelength(b)
    spec.calibrate()
    time.sleep(2)
    for c in range(b,d + i,i):
        spec.set_wavelength(c)
        time.sleep(2)
        reading = spec.absorbance()
        myfile.write('\n{}\t{}'.format(c,reading[0]))
        print('The absorbance at {} is {}'.format(reading[1],reading[0]))
    myfile.close()
    e = input('Do you wish to use a different sample/filter? (yes or no): ')
    while e =='yes':
        name = input('Please enter a filename to save your new results (this will overwrite the previous results under the same filename): ')
        filename = '{}.txt'.format(name)
        myfile = open(filename, 'w')
        time.sleep(5)
        f = int(input('Enter minimum wavelength (nm): '))
        g = int(input('Enter maximum wavelength (nm): '))
        j = input('Would you like to use the same increment? (yes/no)')
        myfile.write('#Min wavelength:{:5} Max wavelength:{:5} Increments:{:5}\n'.format(b,d,i)) 
        myfile.write('wl\trd')
        spec = Spectrometer()
        spec.set_wavelength(f)
        spec.calibrate()
        if j =='yes':
            for h in range(f,g + i, i):
                spec.set_wavelength(h)
                time.sleep(2)
                reading = spec.absorbance()
                myfile.write('\n{}\t{}'.format(h,reading[0]))
                print('The absorbance at {} is {}'.format(reading[1], reading[0]))
            e = input('Do you wish to use another sample/filter? (yes/no): ')
        else:
            j = int(input('What increments would you like to use instead?: '))
            for h in range(f, g + j, j):
                spec.set_wavelength(h)
                time.sleep(2)
                reading =  spec.absorbance()
                myfile.write('\n{}\t{}'.format(h,reading[0]))
                print('The absorbance at {} is {}'.format(reading[1], reading[0]))
            e = input('Do you wish to use another smaple/filter? (yes/no): ')
    else:
        print('Fine…')
else:
    print("K bye :’(")
    

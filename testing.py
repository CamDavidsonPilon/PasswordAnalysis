#This implements a simple password creator: creating passwords that a really aweful. This should not be used to create passwords


#lets make this easy and make everything lowercase
import string
import numpy as np
from numpy import genfromtxt
import csv
 
from multinomialMM import MultinomialMM
from encoding import EncodingScheme



     

file = open('password.txt', 'r')
data = map( string.strip, file.readlines() )
file.close()


bins = ['[0-9]', '[A-Za-z]', '\s']
es = EncodingScheme( bins, to_append_to_end=" ", garbage_bin=True)


npdata = es.encode( data )


mmm = MultinomialMM()

mmm.fit(npdata)




        
        
        
        

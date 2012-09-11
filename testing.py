#This implements a simple password creator: creating passwords that a really aweful. This should not be used to create passwords


import string
import numpy as np
import time
 
from multinomialMM import MultinomialMM
from encoding import EncodingScheme



     

file = open('linkedin_passwords.txt', 'r')
start = time.clock()
data = map( string.strip, file.readlines() )
print time.clock() - start
file.close()


#bins = ['[0-9]', '[A-Za-z]', '\s']
bins = []
es = EncodingScheme( bins, to_append_to_end=" ", garbage_bin=True)


start = time.clock()
npdata = es.encode( data )
print time.clock()-start


mmm = MultinomialMM()

start = time.clock()
mmm.fit(npdata)
print time.clock()-start


#generate some fake passwords.
inv_map = {v:k for k, v in es.unique_bins.items()}

print "".join([ inv_map[s] for s in mmm.sample()[0] ])
print "".join([ inv_map[s] for s in mmm.sample()[0] ])
print "".join([ inv_map[s] for s in mmm.sample()[0] ])

        
        
        
        

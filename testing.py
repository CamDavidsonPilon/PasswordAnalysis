#This implements a simple password creator: creating passwords that a really aweful. This should not be used to create passwords


import string
import numpy as np
import time
 
from multinomialMM import MultinomialMM
from encoding import EncodingScheme

#pretty printing
np.set_printoptions(precision=3, suppress=True)



def n_gram_even( s, n=1):
    #create a (n+1)-gram list of string s
    return [ s[i-n:i+1] for i in range(n,len(s),n+1)]
def n_gram_odd( s, n=1):
    #create a (n+1)-gram list of string s
    return [ s[i:i+1+n] for i in range(1,len(s),n+1) ]

       

     

file = open('linkedin_passwords.txt', 'r')
data = map( string.strip, file.readlines() )
data = map( string.lower, data )
file.close()


twogramdataEven = map( n_gram_even, data)
twogramdataOdd = map( n_gram_odd, data)


data = twogramdataOdd + twogramdataEven
#bins = ['[0-9]', '[A-Z]','[a-z]', '\s']
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





        

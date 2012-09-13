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

       
"""The most important single contribution to cracking knowledge came in late 2009, when an SQL injection attack 
against online games service RockYou.com exposed 32 million plaintext passwords used by its members to log in to 
their accounts. The passcodes, which came to 14.3 million once duplicates were removed, were posted online; 
almost overnight, the unprecedented corpus of real-world credentials changed the way whitehat and blackhat 
hackers alike cracked passwords.


"""
     

file = open('linkedin_passwords.txt', 'r')
data = map( string.strip, file.readlines() )
data = map( string.lower, data )
file.close()


#twogramdataEven = map( n_gram_even, data)
#twogramdataOdd = map( n_gram_odd, data)
#data = twogramdataOdd + twogramdataEven


#bins = ['[0-9]', '[A-Z]','[a-z]', '\s']
bins = []
es = EncodingScheme( bins, to_append_to_end=" ", garbage_bin=True)

start = time.clock()
npdata = es.encode( data )
print time.clock()-start


mmm = MultinomialMM(encoding=es)

start = time.clock()
mmm.fit(npdata)
print time.clock()-start


#generate some fake passwords.
print "Sample learned passwords:"
for sample in  mmm.decoded_sample( 3 ):
    print sample





        

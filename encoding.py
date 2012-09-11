import re
import numpy as np


class EncodingScheme(object):
        """
        Encoding_scheme is a class to make Markov model data out of raw data. 
        Input:
            list_of_regex_bins: a list of regular expressions, as strings, representing how to "bin"
                the raw data. eg: [ '[0-9]', '[a-z]', '[A-Z]' ]
                A -1 is inserted if the item cannot be binned correctly. 
                Notes: -Try not to overlap bins. 
                       -To specify all unique bins, leave the list empty.
                       -An exception is thrown if a item is not able to be binned.
            to_append_to_end:
                if the series data is not the same length ( eg: password data), this specifies what to append
                to end before performing analysis. If not needed, leave as None. This is still buggy.
                
            garbage_bin: a boolean to include a garbage bin, ie a bin that collects everything not collected.
                Notes: having garbage_bin to True is pretty much useless if all unique bins is set, ie. 
                       having list_of_regex_bins = []
                       
        attributes:
            self.unique_bins: a dictionary of the bins used to encode the data and the encode mapping.
            self.realized_bins: a dictionary of the bins used to encode the realized data values that
                                satisfy the bins. Useful for debugging and seeing what garbage is collected
                                with realized_bins['garbage']
         
        Methods:
            encode(raw_data): returns the encoded data
            
        """


        def __init__(self, list_of_regex_bins=[], to_append_to_end = None, garbage_bin=False ):
            self.list_of_regex_bins = list_of_regex_bins
            self.to_append_to_end = to_append_to_end
            self.unique_bins = dict()
            self.number_of_bins = -1
            self.garbage_bin = garbage_bin
            self.realized_bins = dict( zip ( self.list_of_regex_bins, [ set() for i in range(len(list_of_regex_bins) )  ] ) )
            
        def encode(self, data):
            """
            This function creates a representation of the data.
            Input:
                data: a list of iterables (eg: strings, lists, arrays, np.arrays), all of the same type.
            output:
                a 2d numpy array of computer-readable time series
                
            ex:
                eScheme = Encoding_scheme( [] )
                input = ['data', 'atad', 'dta']
                eScheme.encode( data)
                >> array( [ [0,1,2,1], [1,2,1,0], [0,2,1] ] )
            """
            max_length = self.max_length(data)
            data = self.append_ends( data, max_length )
            encoded_data = np.zeros( (len(data), max_length ), dtype="int" )
            
            #iterate through the time series
            for row_i,series in enumerate(data):
                for col_i, item in enumerate(series):
                    encoded_data[row_i, col_i] = self._encode( item )
            
            return encoded_data
        
        
        
        def max_length(self,data):
            return max( map( len, data ) )
            
        def append_ends( self, data, length):
            #this entire functions needs to be redone
            new_data = []
            if self.to_append_to_end:
                for series in data:
                    if len(series)<length:
                        series+= self.to_append_to_end*(length-len(series) ) #this is too specific
                        new_data.append(series)
                return new_data
            else:
                return data
            
        def _encode(self, item):
            
            if not self.list_of_regex_bins:
                if str(item) not in self.unique_bins.keys():
                    #This won't distinguish 1.0 from 1 etc.
                    self.number_of_bins +=1
                    self.unique_bins[str(item)] = self.number_of_bins 
                #self.realized_bins[str(item)].add( item) #this is probably redudant to have if the all unique bins is on
                return self.unique_bins[str(item)]
            
            else:
                for regex in self.list_of_regex_bins:
                    if re.match( regex, str(item) ):
                        if regex not in self.unique_bins.keys():
                            self.number_of_bins +=1
                            self.unique_bins[regex] = self.number_of_bins 
                        self.realized_bins[regex].add( item)
                        return self.unique_bins[regex]
                            
                #we didnt collect it. See if garbage bin is enabled.
                if self.garbage_bin:
                    if 'garbage' not in self.unique_bins.keys():
                        self.number_of_bins +=1
                        self.unique_bins['garbage'] = self.number_of_bins
                        self.realized_bins['garbage'] = set()
                        
                    self.realized_bins['garbage'].add( item)           
                    return self.unique_bins['garbage']
                    
                else:
                    raise BinningError(item)
                
                
class BinningError( Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "Could not find a bin for value %s."%repr(self.value)
            
            
            
            
            
                    
            
            
        
            
            
            
        
            
        
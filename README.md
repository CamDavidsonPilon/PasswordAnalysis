PasswordAnalysis
================

This is a description of human-created passwords using markov models. See camdp.com/blogs for a detailed blog post on the subject.

encoding.py and EncodingScheme()
--------------------------------
This module contains the *EncodingScheme* class to create computer readable data from a multinomial time series (that means it has finite support). From the 
docs:

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


mulitnomialMM.py and MultinomialMM()
------------------------------------
From the docs:

    Create and learn a multinomial Markov model.
    
    Attributes:
        self.data: the data used to fit the model
        self.unique_elements: the found unique elements of the data
        self.init_probs_esimate: the probability vector of inital emissions
        self.trans_probs_estimate: the trasmission probability matrix of going from 
            emission [row] to emission [col].
    
    Methods:
        self.fit(data, encoded=True)
        self.sample( n=1)
        


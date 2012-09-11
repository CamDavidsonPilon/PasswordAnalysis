
import numpy as np


class MultinomialMM(object):
    def __init__(self, min_length=None):
        self.min_length = min_length
        
        
    def _fit_init(self,data):
        self.data = data
        self.unique_elements = np.arange( np.unique(data).shape[0] )[None, :]
        self.n_trials, self.len_trials = data.shape
        self.init_probs_estimate = np.zeros( self.unique_elements.shape[1] )
        self.trans_probs_estimate = np.zeros( (self.unique_elements.shape[1], self.unique_elements.shape[1]) )

       
    def fit(self, data):
        self._fit_init(data)
        
        #set intial probabilities estimate
        initial_values = self.data[:,1]
        for i in range(self.unique_elements.shape[1]):
            ele = self.unique_elements[:,i]
            self.init_probs_estimate[i] = sum( initial_values == ele )
        self.init_probs_estimate /= self.n_trials
        
        #set transition probabilities estimate
        for i in range(1, self.len_trials):
            _from = self.data[:,i-1]
            _to = self.data[ :,i]
            self.trans_probs_estimate[_from, _to]+=1
        
        self.trans_probs_estimate = self._normalize( self.trans_probs_estimate )
        
    def sample(self, n=1):
        samples = np.empty( (n, self.len_trials) )
        for i in range(n):
            samples[i,:] = self._sample()
        return samples
        
    def _sample(self):
        sample = np.empty( (1,self.len_trials) )
        sample[0,0] = np.argmax(np.random.multinomial(1, self.init_probs_estimate )) # argmax. something like this.
        for i in range( 1, self.len_trials):
            sample[0, i] = np.argmax(np.random.multinomial( 1, self.trans_probs_estimate[ sample[0,i-1],: ] ) )
        return sample
    
    
        
    def _normalize(self, array ):
        return array/array.sum(1)[:,None]
            


            
            
                    
            
            
        
            
            
            
        
            
        
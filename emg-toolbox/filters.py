import numpy as np

class PlifEegSubtractFilter:
    def __init__(self, sf, pwlf):
        # Perform some sanity checks
        if sf < 100:
            raise ValueError("Sample frequency (sf) must be >= 100Hz")
        
        if pwlf not in [50, 60]:
            raise ValueError("Powerline frequency (pwlf) must be either 50Hz or 60Hz")
        
        if sf % pwlf != 0:
            raise ValueError("Ratio between sample frequency (sf) and powerline frequency (pwlf) must be an integer multiple")
        
        self.sf = sf
        self.pwrcycles = pwlf // 2
        self.pwrcyclesmpls = sf // pwlf
        self.sz = sf // 2
        self.buf = np.zeros(self.sz)
        self.idx = 0
    
    def run_subtract_filter(self, new_input):
        self.buf[self.idx] = new_input
        
        avg = np.mean(self.buf)
        val = np.mean([self.buf[(self.idx + (i * self.pwrcyclesmpls)) % self.sz] for i in range(self.pwrcycles)])
        
        self.idx = (self.idx + 1) % self.sz
        
        return new_input - (val - avg)
    
    def reset_subtract_filter(self):
        self.idx = 0
        self.buf = np.zeros(self.sz)

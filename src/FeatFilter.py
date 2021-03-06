from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd



class FeatFilter(BaseEstimator, TransformerMixin):
    
    def __init__(self, ixCols = None):
        self.ixCols = ixCols
        
    def fit(self, X, y = None):    
        return self

    def transform(self, X):         
        if self.ixCols is None:
            return X
        else:
            return X[:,self.ixCols==1]

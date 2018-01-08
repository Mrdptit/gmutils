""" dataset.py

Code and objects to manage datasets for training models

"""
import os, sys, re
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from .utils import *
from .objects import Object

################################################################################
# DEFAULTS

default = {
    'default_file'        : 'dataset',
}
    
################################################################################
# OBJECTS

class Dataset(Object):
    """
    A dataset object to simplify the training and use of a model

    Attributes
    ----------
    x_train : numpy ndarray
    y_train : numpy ndarray

    x_test : numpy ndarray
    y_test : numpy ndarray

    x_validation : numpy ndarray
    y_validation : numpy ndarray

    """
    def __init__(self, options=None):
        """
        Instantiate the object and set options

        """
        self.set_options(options, default)        # For more on 'self.set_options()' see object.Object

        
    def load(self, input=None, read_data=None):
        """
        Using a prescribed reading function, 'read_data', this function loads data into the object's attributes.

        Parameters
        ----------
        input : text file, CSV, panda DataFrame, directory, or other, depending on the read_data function

        read_data : a function which can read the specified input

        """
        if read_data is not None:
            self.read_data = read_data
            
        self.read_data(input)       # Use provided read function
        self.print_set_sizes()

            
    def print_set_sizes(self):
        """
        Print info about the training and test sets
        """
        n_train = len(self.y_train)         # Lines of input text for training
        n_test  = len(self.y_test)          # Lines of input text for testing
        sys.stderr.write('Training set:  %s\n'% str(n_train))
        sys.stderr.write('Test set:      %s\n'% str(n_test))

    
    def get_class_counts(self, Y):
        """
        To know how many of each class is in the training samples

        Parameters
        ----------
        Y : pandas.Series

        Returns
        -------
        counts : a dict having each class name and number of occurrences
        """
        counts = {}
        for y in Y:
            y = int(y)
            if y in counts:
                counts[y] += 1
            else:
                counts[y] = 1
                
        return counts
            
            
################################################################################
##   MAIN   ##

if __name__ == '__main__':
    try:
        parser = argparser({'desc': "Tools to manage a training set: dataset.py"})
        #  --  Tool-specific command-line args may be added here
        args = parser.parse_args()   # Get inputs and options

        print(__doc__)

    except Exception as e:
        print(__doc__)
        err([], {'exception':e, 'exit':True})

        
################################################################################
################################################################################
    
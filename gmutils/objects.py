""" objects.py

    Using these Objects as superclasses will help produce cleaner, simpler code.

"""
import sys, os, re
import argparse
import types

from .utils import *


################################################################################
# OBJECTS

class Object(object):
    """
    A custom subclass of object to assist in the handling of options within code and
    to result in cleaner code overall

    """
    def set_options(self, options=None, default=None):
        """
        The purpose of this and related functions is to enable getting and setting of options without having to check first if a dict key exists-- results in cleaner code.

        Parameters
        ----------
        options : dict
            In this case each key in this dict will be converted to an attribute. The name of each key must be only lower case with underscores

            or  : None
            In this case an empty object is created

            or  : argparse.Namespace
            In this case it iterates over non internal attributes accruing them to this object
        """
        try:   # Confirm that self._value_ exists
            if not hasattr(self, '_value_'):
                self._value_ = {}
        except AttributeError:
            self._value_ = {}
        except:
            self._value_ = {}

        self.options = options
        
        if options is not None:

            if isinstance(options, dict):
                for key in options.keys():
                    if not key == 'input':
                        self.set(key, options[key])

            elif isinstance(options, Options):
                for key,val in options._value_.items():

                    # Skip some keys that shouldn't be absorbed into the next object
                    if re.search('^_', key):
                        continue
                    if key == 'input'  or  key == 'options':
                        continue
                    if isinstance(val, types.MethodType):
                        continue
                    
                    self.set(key, val)

            elif isinstance(options, argparse.Namespace):
                for key in dir(options):

                    # Skip some keys that shouldn't be absorbed into the next object
                    if re.search('^_', key):
                        continue
                    if key == 'input'  or  key == 'options':
                        continue
                    val = getattr(options, key)
                    if isinstance(val, types.MethodType):
                        continue
                    
                    self.set(key, val)

            else:
                print('ERROR: options object is of type:', type(options))
                exit()

        self.set_defaults(default)
        self.mkdirs()  # Some settings require that a given directory exists
                    

    def set_defaults(self, default=None):
        """
        Set some missing options using a dict of defaults.
        Some options may have been missing because they either weren't serializable or simply weren't specified.

        """
        if default is not None:
            for param in default.keys():
                if not self.get(param):
                    self.set(param, default[param])

        
    def set(self, key, val):
        """
        Set key/val pair (for options)

        Parameters
        ----------
        key : str

        val : anything
        """
        self._value_[key] = val

        
    def get(self, key):
        try:
            return self._value_[key]
        except KeyError:
            # raise AttributeError(key)
            return False
        except:
            self._value_ = {}
            return False


    def __repr__(self):
        out = {}
        for k,v in self._value_.items():
            out[k] = str(v)
        return out

        
    def __str__(self):
        return str( self.__repr__() )


    def isTrue(self, key):
        """
        To enable shorter code for determining if an option is set
        """
        try:
            out = self.get(key)
            if out:
                return out
            return False
        except:
            pass

        return False


    def isVerbose(self):
        """
        To enable shorter code for determining if an option is set
        """
        return self.isTrue(options, 'verbose')


    def mkdirs(self):
        """
        For some options, a directory is called for.  Ensure that each of these exist.

        """
        mkdir(self.get('output_dir'))
        mkdir(self.get('model_dir'))
        
    
    def get_config(self, options=None):
        """
        Generate a dict of the option settings.

        Returns
        -------
        dict

        """
        config = {}
        for param, val in self._value_.items():

            if isTrue(options, 'serializable'):
                if is_jsonable(val):
                    config[param] = val
            else:
                config[param] = val
            
        return config

    
    def done(self):
        """
        Used to make sure that a given function is only called once or a limited number of times.

        Returns
        -------
        int : the number of times 'caller' has been called for this object

        """
        caller = sys._getframe(1).f_code.co_name   # name of the function in which 'done()' was called
        tracker = '_DONE_' + caller                # name of stored key to track how many times 'caller' has been called for this object
        so_far = self.get(tracker)                 # number of times 'caller' has been called so far
        self.set(tracker, so_far + 1)              # increment the number of times

        return so_far
        

class Options(Object):
    """
    A custom subclass of object>Object to assist in the handling of options outside of object code

    """
    def __init__(self, options):
        self.set_options(options)


        
################################################################################
################################################################################

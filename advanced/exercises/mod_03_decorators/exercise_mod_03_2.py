#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: Implement a function that returns the n-th element of the 
             fibonacci sequence, it should print a message with the ellapsed total time
             Test it with 40
'''
import unittest
import time

import simcache 

@cached_func
def fibonacci(n):
    ''' get the n-th element in the fibonacci sequence
        >>> value = fibonacci(40)
        ellapsed_time: 2 ms
        >>> value
        102334155
    '''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def cached_func(f):               
    def wrapper(n):    
        item =  simcache.get_key(n)    
        if item:                                                                              
            return item                                                                       
        simcache.set_key(n, f(n))                                                             
        return simcache.get_key(n)                                                            
    return wrapper    
    
#fibonacci = cached_func(fibonacci)
                                                                                                  
print fibonacci(40)
                                                                                                  

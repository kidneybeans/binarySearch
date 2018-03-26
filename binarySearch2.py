# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:09:32 2017

@author: kidneybeans

Solve the bug when the value lasts for a period
"""

class Solution:
    def __init__(self, value=2):
        self.nums = None
        self.len_nums = 0
        self.key = 0
        self.value = value
        self.keys = []
    
    def bs(self, start, end):
        if end == start:
            if self.value == self.nums[end]:
                for i in range(start,end+1):
                    if self.value == self.nums[i]:
                        self.keys.append(i)
                if len(self.keys) > 0:
                    return self.keys
                else:
                    self.key = end
            else:
                print ('cant find the correct number!')
            return
            
        mid = int ((end + start) / 2)
        if self.value <= self.nums[mid]:
            if self.value == self.nums[mid]:
                for i in range(start,end+1):
                    if self.value == self.nums[i]:
                        self.keys.append(i)
                if len(self.keys) > 0:
                    return self.keys
            else:
                self.bs(start, mid)
        else:
            self.bs(mid+1, end)
        
    def bsWrappder(self, candidates):
        self.nums = candidates
        self.nums.sort()
        self.len_nums = len(self.nums)
        if 0 == self.len_nums:
            return [ ]
        self.bs(0, self.len_nums-1)
        if len(self.keys) > 0:
            return self.keys
        return self.key
        
        
s = Solution(1)
print('self value is', s.value )
print('binary search: the key of value', s.value, 'is', s.bsWrappder([10, 1, 2, 7, 6, 1, 5]))    
print('sorted data is', s.nums )   
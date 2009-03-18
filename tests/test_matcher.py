#!/usr/bin/env python
# encoding: utf-8
"""
test_matcher.py

Tests PyMethodMatcher

Created by Ryan Wilcox on 2009-03-18.
Copyright (c) 2009 Wilcox Development Solutions. All rights reserved.
"""

import unittest
from method_matcher import Matcher


class TestMatcher(unittest.TestCase):
    
    def match_one(self, match):
        self.functionCalled = True
    
    def setUp(self):
        self.newMatcher = Matcher()
        self.functionCalled = False
        
    def test_register_and_registry_count_does_increase(self):
        self.newMatcher.register("method1", self.match_one)
        self.assertEquals( 1, self.newMatcher.registry_length() )
        
    def test_register_and_can_find_via_matching_method(self):
        self.newMatcher.register("method1", self.match_one)
        self.assertEquals( True, self.newMatcher.has_matching_method("method1") )
        
    def test_register_and_returns_false_when_not_found_via_matching_method(self):
        self.newMatcher.register("method1", self.match_one)
        self.assertEquals( False, self.newMatcher.has_matching_method("method2") )
        
    def test_register_and_calls(self):
        self.newMatcher.register("method1", self.match_one)
        self.assertEquals( True, self.newMatcher.has_matching_method("method1") )
        self.newMatcher.execute_method_for("method1")
        self.assertEquals( True, self.functionCalled)
        
    def test_calls_bad_name(self):
        self.assertRaises(NameError, self.newMatcher.execute_method_for, "blowUp" )
    
if __name__ == '__main__':
    unittest.main()



import re
from types import *

class Matcher(object):
    """Is responsible for registering methods we can call, and calling them when user wants"""
    def __init__(self):
        super(Matcher, self).__init__()
        self.registery = []
    
    def register(self, regex, method_object):
        """Call register when you have a method that you want called when your end user inputs a phrase that matches a certain regular expression.
        
        The signature of these method objects should be one parameter: this parameter will be the MatchObject that tells you about the matches.
        From this you can extract groups etc if you want (or just ignore).
        
        If you pass a string for the regex parameter it will be re.compile-d for you. If you pass a compiled re object, then great!
        """
        
        compiled = None
        if( isinstance(regex, str) ):
            compiled = re.compile(regex)
        else:
            compiled = regex
        
        self.registery.append( (compiled, method_object) )
        
    def __matching_method(self, string):
        for regex, method in self.registery:
            matchObj = regex.match(string)
            if matchObj:
                return matchObj, method
        return None, None
    
    def has_matching_method(self, string):
        """Returns True if this Matcher object has a method that matches (the string passed in)"""
        
        matchObj, junk = self.__matching_method(string)
        return not(matchObj == None)
        
    def execute_method_for(self, string):
        """If there is a method that matches that passed in string, call that method. Else throw NoMethodError"""
        
        matchObj, method = self.__matching_method(string)
        if matchObj:
            return method(matchObj)
        else:
            raise NameError("no definition for %s" % string)
    
    def registry_length(self):
        """Returns the length of the current registry """
        return len(self.registery)
class NoMethodError(RuntimeException):
    pass        

class Matcher(object):
    """Is responsible for registering methods we can call, and calling them when user wants"""
    def __init__(self):
        super(ClassName, self).__init__()
        registery = []
    
    def register(self, regex, method_object):
        """Call register when you have a method that you want called when your end user inputs a phrase that matches a certain regular expression.
        
        The signature of these method objects should be one parameter: this parameter will be the MatchObject that tells you about the matches.
        From this you can extract groups etc if you want (or just ignore)
        """
        pass
        
    def has_matching_method(self, string):
        """Returns True if this Matcher object has a method that matches (the string passed in)"""
        pass
        
    def excute_method_for(self, string):
        """If there is a method that matches that passed in string, call that method. Else throw NoMethodError"""
        throw NoMethodError
    
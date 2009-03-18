from method_matcher import Matcher

def i_am_given_n_fish(match):
    return "I have been given %d fish" % int(match.group(1))
    
mat = Matcher()

mat.register("When I am given (\d+) fish", i_am_given_n_fish)


print mat.execute_method_for("When I am given 12 fish")
print "You should have been given 12 fish..."
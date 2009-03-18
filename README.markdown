To the Readme for PyMethodMatch
============================================
This software was written by Ryan Wilcox, of [Wilcox Development Solutions](http://www.wilcoxd.com). This document is formatted with [Markdown](http://daringfireball.net/projects/markdown/) syntax, a markup syntax that's easy to read, even if you just open the text file in an editor.


PyMethodMatch's Purpose In Life
=============================================

PyMethodMatch is a library for parsing very high level (and ideally very Human Language like) commands.

There's two ways to look at PyMethodMatch:

  1. From the end user's perspective: your app takes very simple phrases that will run things
  2. From the programmer's perspective: you set up regex keys and values. If the phrase coming in matches one of the regex,
    that function will be executed.


This is great for creating Very High Level (Non-Turing Compliant) Domain Specific Languages, or sets of instructions that must be readable by non-technical people but that, underneath, do complex things

Inspirations
==============================================

PyMethodMatch is inspired by the language in Ruby On Rails' [Cucumber tool](http://wiki.github.com/aslakhellesoy/cucumber/ruby-on-rails).

An example of that is:

`Given a logged in, registered user
And I have a blog post that I can edit
Then I should see "Edit"`

In Cucumber these phrases are matched to blocks of code, and these code blocks executed as the parser reads the file.

PyMatcher API
==============================================

First, create a new Matcher object:

`from PyMethodMatch.method_matcher import Matcher
matcher = Matcher()`

Define a function to be called and match it up with a regular expression with a register() call

`def call_me(matchObj):
    print "hello world"
matcher.register("I am the regular expression to match to this function", call_me)`

When you are ready to (potentially) call one of your functions, call

`matcher.execute("I am the regular expression to match to this function")`

The result of the function will be returned to you.

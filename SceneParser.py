import fileinput
import string
from pyparsing import *
from grammar import node, event, functions
#from grammar import test
#from grammar.test import test_node
import re

strip_comments_re = re.compile("//.*?$", re.MULTILINE)

def strip_comments(src):
    return re.sub(strip_comments_re, "", src)


file = fileinput.FileInput("./td.scn")
line = file.readline()
add_line_to_string = False
string_to_parse = ''

r_node = False
r_track = False
r_event = False
#test_node.


#r = test_node.test_track()
#pass

while line:
    #szukamy po slowach kluczowych

    if node.NodeTag.searchString(line).asList().__len__()>0:
        r = functions.readNode(file, line)
        pass
    elif event.EventTag:
       pass
        
    line = file.readline()
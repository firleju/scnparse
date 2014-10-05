from pyparsing import *
from grammar import node
import re

strip_comments_re = re.compile("//.*?$", re.MULTILINE)

def strip_comments(src):
    return re.sub(strip_comments_re, "", src)

def parseTrack(string_to_parse):

    result = node.Track.parseString(strip_comments(string_to_parse)).asDict()
            
    if 'rail' in result:
        result['rail'] = dict(result['rail'])
        result['ballast'] = dict(result['ballast'])
    result['point1'] = dict(result['point1'])
    result['control1'] = dict(result['control1'])
    result['control2'] = dict(result['control2'])
    result['point2'] = dict(result['point2'])

    return result

def parseSwitch(string_to_parse):
    
    result = node.Switch.parseString(strip_comments(string_to_parse)).asDict()

    if 'rail' in result:
        result['rail'] = dict(result['rail'])
        result['ballast'] = dict(result['ballast'])
    result['point1'] = dict(result['point1'])
    result['control1'] = dict(result['control1'])
    result['control2'] = dict(result['control2'])
    result['point2'] = dict(result['point2'])
    result['point3'] = dict(result['point3'])
    result['control3'] = dict(result['control3'])
    result['control4'] = dict(result['control4'])
    result['point4'] = dict(result['point4'])

    return result

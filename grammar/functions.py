from pyparsing import *
from grammar import node
import re
import os, sys
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

def readNode(file, line):

    string_to_parse = ""
    searched_node = ""

    while(line):

        string_to_parse += line

        #najpierw trzeba sprawdzic koniec
        #inaczej pyparsing zwroci ze znajduje keyword track w endtrack
        #to jest jakis blad

        if node.EndTrackTag.searchString(line).asList().__len__()>0 and searched_node=="track":
            #koniec node track, zwykly czy switch
            if node.TrackNormalTag.searchString(string_to_parse).asList().__len__()>0:
                try:
                    r = parseTrack(string_to_parse)
                except ParseException as pe:
                    #print pe.line
                    #print pe.lineno
                    pass
                finally:
                    return r
            elif node.TrackSwitchTag.searchString(string_to_parse).asList().__len__()>0:
                try:
                    r = parseSwitch(string_to_parse)
                except ParseException:
                    pass
                finally:
                    return r

        elif node.TrackTag.searchString(line).asList().__len__()>0:
            searched_node = "track"

        line = file.readline()

    return None

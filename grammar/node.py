from pyparsing import *
from grammar.common import Identifier, UIntNum, DecimalNum, Position, FileName

# common
NodeTag = CaselessKeyword('node')
Preamble = NodeTag + \
    DecimalNum('max_dist') + \
    DecimalNum('min_dist') + \
    Identifier('name')

# track
TrackTag = CaselessKeyword('track')
EndTrackTag = CaselessKeyword('endtrack')

Environment = oneOf('flat mountains canyon tunnel')
TrackPrefix = DecimalNum('length') + \
    DecimalNum('width') + \
    DecimalNum('friction') + \
    DecimalNum('sound_dist') + \
    UIntNum('quality') + \
    UIntNum('damage_flag') + \
    Environment('environment') 

TrackSuffix = Each([\
    Optional(CaselessKeyword('velocity') + DecimalNum('velocity')), \
    Optional(CaselessKeyword('event0') + Identifier('event0')), \
    Optional(CaselessKeyword('event1') + Identifier('event1')), \
    Optional(CaselessKeyword('event2') + Identifier('event2')), \
    Optional(CaselessKeyword('isolated') + Identifier('isolated')) \
])

VisTag = CaselessKeyword("vis").setParseAction(replaceWith(True))("visibile")
UnvisTag = CaselessKeyword("unvis").setParseAction(replaceWith(False))("visibile")

TrackMaterialParams = Group(
        FileName('tex') + \
        DecimalNum('scale'))('rail') + \
    Group(
        FileName('tex') + \
        DecimalNum('height') + \
        DecimalNum('width') + \
        DecimalNum('slope'))('ballast')

TrackMaterial = (VisTag + TrackMaterialParams) | UnvisTag

TrackGeometry = Position('point1') + \
    DecimalNum('roll1') + \
    Position('control1') + \
    Position('control2') + \
    Position('point2') + \
    DecimalNum('roll2') + \
    DecimalNum('radius1')

SwitchGeometry = TrackGeometry + \
    Position('point3') + \
    DecimalNum('roll3') + \
    Position('control3') + \
    Position('control4') + \
    DecimalNum('roll4') + \
    DecimalNum('radius2')

TrackNormalTag = CaselessKeyword('normal')
TrackSwitchTag = CaselessKeyword('switch')

Track = Preamble + \
    TrackTag + \
    TrackNormalTag + \
    TrackPrefix + \
    TrackMaterial + \
    TrackGeometry + \
    TrackSuffix + \
    EndTrackTag

Switch = Preamble + \
    TrackTag + \
    TrackSwitchTag + \
    TrackPrefix + \
    TrackMaterial + \
    SwitchGeometry + \
    TrackSuffix +\
    EndTrackTag

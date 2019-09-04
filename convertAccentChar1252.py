#!/usr/bin/python
# -*- coding: cp1252 -*-

import sys
from GlyphSprites import Sprites

def enc(letter):
    return letter.encode('utf-8').decode('cp1252')

dictGlyph = {
    '�': ('e', Sprites.letterEacute),
    '�': ('e', Sprites.letterEgrave),
    '�': ('e', Sprites.letterEcirc),
    '�': ('e', Sprites.letterEuml),
    '�': ('E', None),
    '�': ('E', None),
    '�': ('E', None),
    '�': ('E', None),
    '�': ('a', Sprites.letterAgrave),
    '�': ('A', None),
    '�': ('u', Sprites.letterUgrave),
    '�': ('o', Sprites.letterOcirc),
    '�': ('O', None)
}

maxCustomChar = 8

def convertMsg(message, glyphList=[], charList=[], maxChar=maxCustomChar):
    """ return message and glyph list """
    new_msg = ''
    offset_glyph_list = len(glyphList) - len(charList)

    for c in message:
        if c in dictGlyph:
            if c in charList:  # glyph has already been added to the list, so use it!
                new_msg += chr(offset_glyph_list + charList.index(c))
            else:
                glyphTuple = dictGlyph[c]
                if len(glyphList) < maxChar and glyphTuple[1] is not None:  # is there still a free place? is a glyph defined ?
                    glyphList.append(glyphTuple[1])
                    charList.append(c)
                    new_msg += chr(len(glyphList)-1)
                else:
                    new_msg += glyphTuple[0]  # use replacement char (because there is no glyph or because there is no more place for custom char)
        else:
            new_msg += c  # add normal char to the message
    return (new_msg,glyphList,charList)

if __name__ == '__main__':
    print(repr(dictGlyph))
    if len(sys.argv) > 1:
        print(repr(convertMsg(" ".join(sys.argv[1:]).decode('utf-8').encode('cp1252'))))
    else:
        print(repr(convertMsg('Accents du a : �\nAccents du e: �������\nAccents du u: �\nAccents du o : ��')))


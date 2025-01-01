#_______________________________________________________________________
#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                        / /
#  /  | | |\ |  \   |  | / | | /   |   \                        (^^)
#  \_ |_| | \| _/   |  | \ |_| \_  |  _/                        (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#  Copyright 2024, Rebecca Rashkin
#  -------------------------------
#  This code may be copied, redistributed, transformed, or built upon in
#  any format for educational, non-commercial purposes.
#
#  Please give me appropriate credit should you choose to use this
#  resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#  //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
#_______________________________________________________________________

#_______________________________________________________________________
# This program replaces a file header and copyright notice with a string
# indicated in a file.
#_______________________________________________________________________

'''
if directory
    walk through each file and replace or add

replace

- read through file

Enum
language
c
py

FILE_TYPES
    'c':    {ext: ['c', 'cpp', 'h', 'hpp'], comment_style: '//'}
    'ada':  {ext: ['ada', 'adb', 'ads'],    comment_style: '--'}
    'py':   {ext: ['py'],                   comment_style: '#'}

read delimter file, save to string


format_delimiter(lang, delimiter)
    comment_symbol = file_type[lang][comment_style]
    replace first characters of length


replace-text(delimiter, text)
    if delimiter
        - while comment and not delimiter
        - keep reading

    if no delimiter again
'''
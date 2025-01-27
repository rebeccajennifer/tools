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

import argparse
from os import path, walk

from classes.file_header_arg_parser import FileHeaderArgParser
from classes.file_header_strings import FileHeaderStrings
from classes.header_insert import HeaderInsert

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

#_______________________________________________________________________
if __name__ == '__main__':

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  FileHeaderArgParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  ext: str = args.file_ext

  # trim period from extension
  if ext and ext[0] == '.':
    ext = ext[1:len(ext)]

  #_____________________________________________________________________
  # TODO implement modification of file headers by file type
  #_____________________________________________________________________
  comment_delim = FileHeaderStrings.COMMENT_DELIMETERS[ext]
  #_____________________________________________________________________

  header_str: str = ''

  if path.isfile(args.header_path):
    with open (args.header_path, 'r') as file:

      header_str = file.read()


  if (path.isfile(args.path)):
    print('you entered a file')

  if (path.isdir(args.path)):
    print('you entered a path')

    for root, dirs, files in walk(args.path):
      for f in files:
        file_path = path.join(root, f)
        HeaderInsert.insert_full_header(header_str, file_path)

  header_str: str = ''

  if path.isfile(args.header_path):
    with open (args.header_path, 'r') as file:

      header_str = file.read()




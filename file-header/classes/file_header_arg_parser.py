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
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

import argparse

#_______________________________________________________________________
class ParserStrings:

  PROGRAM_NAME: str =\
    'File Header Insert'

  PROGRAM_DESC: str =\
    'This program inserts a comment header into all relevant files'\
    'in a given path.'

  PROGRAM_EPI:  str =\
    'This is the epilog to the help menu.'

  FILE_EXT_HELP_DESC: str =\
    'File extension of files to add header to'

  PATH_HELP_DESC: str =\
    'Path to file or directory to apply the header to'

#_______________________________________________________________________
class FileHeaderArgParser:

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """
    parser.prog = ParserStrings.PROGRAM_NAME
    parser.epilog = ParserStrings.PROGRAM_EPI
    parser.description = ParserStrings.PROGRAM_DESC

    parser.add_argument( '--file_ext'
      , help=ParserStrings.FILE_EXT_HELP_DESC
      , action='store'
      , type=str
      , required=False
    )

    parser.add_argument( '--path'
      , help=ParserStrings.PATH_HELP_DESC
      , action='store'
      , type=str
      , required=True
    )

    return


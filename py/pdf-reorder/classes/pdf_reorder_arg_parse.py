#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2024, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#   DESCRIPTION
#   Argument parser for PDF reorder.
#_______________________________________________________________________

import argparse

#_______________________________________________________________________
class ParserStrings:

  PROGRAM_NAME: str =\
    'PDF Reorderer'

  PROGRAM_DESC: str =\
    'This script rearranges the pages in a pdf such that it can be '\
    'easily printed double-sided on half sheets.'\
    '\n\n'\
    'After running the script and generating the reordered pdf, the '\
    'user will print the pdf with two pages per sheet on a printer '\
    'that supports double-sided prints. They should select the option '\
    'to "flip on short edge".'

  PROGRAM_EPI:  str =\
    'This is the epilog to the help menu.'

  FILE_PATH_DESC: str =\
    'Full path to PDF file to reorder.'

  OUT_DIR_DESC: str =\
    "Path to output directory. Will attempt to create directory if it"\
    "doesn't exist."

  START_PAGE_DESC: str =\
    'Start page of pdf to reorder. Must be greater than 0.'

  END_PAGE_DESC: str =\
    'End page of pdf to reorder. Must be greater than 0.'


#_______________________________________________________________________
class PdfReorderParser:

  #_______________________________________________________________________
  def positive_int(value):
    """
    Returns the integer representation of the value. Raises exception
    if value is less than or equal to 0.
    """
    int_val: int = int(value)

    if (int_val) <= 0:
      raise argparse.ArgumentTypeError\
      ( f'{value} is not a positive integer greater than 0.')

    return int_val

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """

    parser.prog = ParserStrings.PROGRAM_NAME
    parser.epilog = ParserStrings.PROGRAM_EPI
    parser.description = ParserStrings.PROGRAM_DESC

    parser.add_argument\
    ( '--file_path'
    , '-f'
    , help=ParserStrings.FILE_PATH_DESC
    , action='store'
    , type=str
    , required=True
    )

    parser.add_argument\
    ( '--output_dir'
    , '-o'
    , help=ParserStrings.OUT_DIR_DESC
    , action='store'
    , type=str
    , required=False
    , default='.'
    )

    parser.add_argument\
    ( '--start_pg'
    , '-s'
    , help=ParserStrings.START_PAGE_DESC
    , action='store'
    , type=PdfReorderParser.positive_int
    , required=False
    )

    parser.add_argument\
    ( '--end_pg'
    , '-e'
    , help=ParserStrings.END_PAGE_DESC
    , action='store'
    , type=PdfReorderParser.positive_int
    , required=False
    )

    return


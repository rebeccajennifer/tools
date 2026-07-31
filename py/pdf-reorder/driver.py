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
#   This script rearranges the pages in a pdf such that it can be easily
#   printed double-sided on half sheets.
#
#   After running the script and generating the reordered pdf, the user
#   will print the pdf with two pages per sheet on a printer that
#   supports double-sided prints. They should select the option to
#   "flip on short edge".
#
#   Future development for this program will allow the user to select
#   single or double sided, and will put two pages per sheet in the pdf.
#_______________________________________________________________________

import argparse

from classes.pdf_reorder import PdfReorder
from classes.pdf_reorder_arg_parse import PdfReorderParser


#_______________________________________________________________________
if __name__ == '__main__':

  print()
  print()

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PdfReorderParser.init_parser(parser)
  args: argparse.Namespace = parser.parse_args()

  # Subtract one from start and end page to turn it into the page index
  # from 0.
  pdf_reorder = PdfReorder\
  ( file_path=args.file_path
  , output_dir=args.output_dir
  , start_page=args.pdf_start_page - 1
  , end_page=args.pdf_end_page - 1
  )

  print()
  print()

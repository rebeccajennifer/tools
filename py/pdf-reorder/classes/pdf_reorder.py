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
#   Class for pdf reorder.
#_______________________________________________________________________

import os

from shutil import rmtree
from math import floor
from math import ceil
from pypdf import PdfReader
from pypdf import PdfWriter

from classes.pdf_reorder_strings import PdfReorderStrings as Strings

class PdfReorder:

  def __init__\
  ( self
  , file_path: str
  , output_dir: str
  , output_name: str = 'reordered.pdf'
  , start_page: int = 0
  , end_page: int = 0
  , has_cover: bool = False
  ):
    """
    Parameters:
      file_path:  path to pdf to reorder
      output_dir: path to output directory
      start_page: first page of reordered pdf
    """
    self.file_path:str    = file_path
    self.output_dir:str   = output_dir
    self.output_name:str  = output_name
    self.start_page: int  = start_page
    self.end_page: int    = end_page
    self.page_count: int  = end_page - start_page + 1
    self.has_cover: bool  = has_cover

    self.temp_dir: str  = Strings.TEMP_DIR

    if (self.is_pdf() and (end_page >= start_page)):
      self.input_pdf = PdfReader(open(self.file_path, 'rb'))
    else:
      exit()

    self.split_pdf_file_paths: list = self.split_pdf()
    self.page_order: list           = self.get_page_order()
    self.reorder_pdf()

  #_____________________________________________________________________
  def is_pdf(self) -> bool:
    """
    Determines if file is a pdf.

    Parameters:
      file_path: path to file

    Side Effects:
      Populates self.page_count

    Returns:
      bool indicating if file is pdf
    """

    try:
      with open(self.file_path, 'rb') as f:
        header = f.read(4)
        return header == b'%PDF'

    except Exception as e:
      print(f'Error reading file: {e}')
      return False

    return True


  #_____________________________________________________________________
  def split_pdf(self) -> None:
    """
    Splits pdf file into individual sheets.

    Paramters:
      file_path:  path to pdf
      output_dir: path to output directory

    Side Effects:
      Splits input pdf into individual pages and saves them to a
      temp directory that will be later deleted one the reordered pdf
      is created.

    Returns:
      None
    """

    if (not self.is_pdf()):
      return

    # Create output directory if it doesn't exist
    if (not os.path.isdir(self.output_dir)):
      try:
        os.makedirs(self.output_dir)
        print(f'Created directory {self.output_dir}')

      except Exception as e:
        print(f'Error creating directory {self.output_dir}: {e}')

    # Delete temp dir if it exists
    if (os.path.isdir(self.temp_dir)):
      rmtree(self.temp_dir)

    os.makedirs(self.temp_dir)

    file_list: list = []

    for i in range(self.start_page, self.end_page +1):
      output = PdfWriter()
      output.add_page(self.input_pdf.pages[i])

      file_path: str = os.path.join(self.temp_dir, f'{i}.pdf')

      with open(file_path, 'wb') as output_stream:
          output.write(output_stream)

      file_list = file_list + [file_path]

    return file_list

  #_____________________________________________________________________
  def get_page_order(self) -> list:
    """
    Determines the page order for the reordered pdf.

    Parameters:
      None

    Returns:
      List of new page order
    """

    # Pages are arranged in groups of 4, for the four pages that will
    # printed on each 8.5x11 sheet of paper

    half_page_count: int = floor(self.page_count/2)

    page_group: list =\
    [ self.start_page
    , half_page_count + self.start_page
    , half_page_count + self.start_page + 1
    , self.start_page + 1]

    page_order: list = page_group

    for i in range(ceil(self.page_count/4)):

      for page in page_group:
        if (page not in page_order and page <= self.end_page):
          page_order = page_order  + [page]

      page_group = [val + 2 for val in page_group ]

    return page_order

  #_____________________________________________________________________
  def reorder_pdf(self):
    """
    Uses page order list to recombine pdf. Writes newly ordered pdf.

    Parameters:
      None

    Side Effects:
      Creates new reordered pdf in output directory.
      Deletes temp directory.

    Returns:
      None
    """

    pdf_writer = PdfWriter()

    for page in self.page_order:

      pdf_file_name = os.path.join(self.temp_dir, f'{page}.pdf')
      with open (pdf_file_name, 'rb') as file:
        pdf_writer.append(file)

    with open\
      ( os.path.join(self.output_dir, self.output_name)
      , 'wb') as out:

      pdf_writer.write(out)

    print('Reordered pdf successfully created!')

    # Delete temp dir if it exists
    if (os.path.isdir(self.temp_dir)):
      rmtree(self.temp_dir)

    return

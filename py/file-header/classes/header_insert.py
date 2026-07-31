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

from os import path


#_______________________________________________________________________
class HeaderInsert:

  def insert_full_header(header_str: str, file_path: str):

    if not path.isfile(file_path):
      raise FileNotFoundError

    # TODO do I need an else here?
    else:

      file_text: str = ''

      with open(file_path, 'r') as file:

        # Create string with header + existing file text
        file_text = file.read()
        file_text = f'{header_str}\n{file_text}'

      # Overwrite file
      with open(file_path, 'w') as file:
        file.write(file_text)

    return




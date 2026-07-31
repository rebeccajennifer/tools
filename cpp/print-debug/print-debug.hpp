//______________________________________________________________________
//______________________________________________________________________
//       _   __   _   _ _   _   _   _         _
//  |   |_| | _  | | | V | | | | / |_/ |_| | /
//  |__ | | |__| |_| |   | |_| | \ |   | | | \_
//   _  _         _ ___  _       _ ___   _                    / /
//  /  | | |\ |  \   |  | / | | /   |   \                    (^^)
//  \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
//______________________________________________________________________
//______________________________________________________________________
//
//----------------------------------------------------------------------
//  Copyright 2024, Rebecca Rashkin
//  -------------------------------
//  This code may be copied, redistributed, transformed, or built
//  upon in any format for educational, non-commercial purposes.
//
//  Please give me appropriate credit should you choose to use this
//  resource. Thank you :)
//----------------------------------------------------------------------
//
//______________________________________________________________________
//  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
//______________________________________________________________________
//  DESCRIPTION
//  This file contains debugging print functions.
//______________________________________________________________________

/// \file print-debug.hpp
/// \brief Debugging print functions.

#ifndef PRINT_DEBUG_HPP
#define PRINT_DEBUG_HPP

#include <stdio.h>
#include <stdint.h>
#include <string.h>

/// \class PrintDebug
/// \brief Debugging print functions.
class PrintDebug
{
 public:

  /// \brief Checks if buffer needs to be flushed and flushes if needed.
  /// If adding the next line would exceed the buffer limit, prints and
  /// clears the buffer.
  /// \param char* print_ptr - Pointer to print buffer.
  /// \param uint16_t char_limit - Character limit for buffer.
  /// \param uint16_t line_length - Length of line to be added.
  static void check_and_flush_buffer
  ( char* print_ptr
  , uint16_t char_limit
  , uint16_t line_length
  )
  {
    uint16_t chars_left = char_limit - strlen(print_ptr);

    if (chars_left < line_length)
    {
      printf("%s", print_ptr);
      memset(print_ptr, 0, char_limit);
    }
    return;
  }

  /// \brief Prints memory groups of 4 bytes.
  /// \param void* ptr - Pointer to memory location.
  /// \param size_t byte_count - Number of bytes to print.
  /// \param uint16_t char_limit = 1024 - Character limit for
  ///   print buffer.
  /// \param uint8_t bytes_per_line = 4 - bytes to print per line
  /// \param const char* optional_str = "" - Optional string to print.
  static void print_mem_bytes
  ( void* ptr
  , size_t byte_count
  , uint16_t char_limit = 1024
  , uint8_t  bytes_per_line = 4
  , const char* optional_str = 0x00
  )
  {
    // Cast input pointer as uint8 pointer for printing
    uint8_t * byte_ptr = static_cast<uint8_t*>(ptr);
    char print_ptr[char_limit];

    snprintf(print_ptr, char_limit, "  Start address: %p\r\n", byte_ptr);
    check_and_flush_buffer(print_ptr, char_limit, char_limit);

    // Add optional string.
    if (optional_str != nullptr)
    {
      snprintf(print_ptr, char_limit, "%s", optional_str);
    }

    // Determine pointer print length for header formatting.
    uint16_t ptr_size = snprintf(nullptr, 0, "%p", ptr);

    // Temporary buffer for building lines.
    uint8_t temp_len = 64;
    char temp[temp_len];
    memset(temp, 0, temp_len);

    // Position "Address" label to line up with length of printed ptr
    char table_header[temp_len];
    snprintf
    ( table_header
    , temp_len
    , "\r\n  %-*s  "
    , ptr_size, "Address  "
    );

    check_and_flush_buffer(print_ptr, char_limit, char_limit);
    // Offset list - bytes per line
    // E.g. "+3  +2  +1  +0"
    memset(temp, 0, temp_len);
    for (int8_t i = bytes_per_line; i > 0; i--)
    {
      memset(temp, 0, temp_len);
      snprintf
      ( temp
      , temp_len
      , "+%d  "
      , i-1);
      strcat(table_header, temp);
    }

    //__________________________________________________________________
    // Line length used for:
    // 1. Underline length
    // 2. Determine if char limit is exceeded
    //__________________________________________________________________
    uint8_t line_length = strlen(table_header) - 1;
    //__________________________________________________________________
    strcat(print_ptr, table_header);
    strcat(print_ptr, "\r\n");

    check_and_flush_buffer(print_ptr, char_limit, char_limit);

    //__________________________________________________________________
    // Print underline under table header.

    // Reset temp
    memset(temp, 0, temp_len);

    // Create temp
    memset(temp, '_', line_length);
    strcat(temp, "\r\n");
    strcat(print_ptr, temp);


    // Calculate remaining characters left in buffer.
    check_and_flush_buffer(print_ptr, char_limit, line_length);

    // Nothing to print. Flush header and leave.
    if (byte_count == 0)
    {
      printf("%s", print_ptr);
      return;
    }

    // Print bytes in groups of bytes_per_line.
    // Print in reverse order so lower addresses are at the bottom
    // of table output. Columns outside the requested range print '--'
    // and are never dereferenced.
    uintptr_t start_addr = reinterpret_cast<uintptr_t>(byte_ptr);
    uintptr_t end_addr   = start_addr + byte_count - 1;

    // Rows are aligned to bytes_per_line boundaries.
    uintptr_t top_base    = end_addr   - (end_addr   % bytes_per_line);
    uintptr_t bottom_base = start_addr - (start_addr % bytes_per_line);

    for (uintptr_t base = top_base; ; base -= bytes_per_line)
    {
      check_and_flush_buffer(print_ptr, char_limit, line_length);

      snprintf
      ( temp
      , temp_len
      , "\r\n  %*p  "
      , ptr_size
      , reinterpret_cast<void*>(base)
      );
      strcat(print_ptr, temp);

      for (int col = bytes_per_line - 1; col >= 0; col--)
      {
        uintptr_t addr = base + col;

        if (addr < start_addr || addr > end_addr)
        {
          strcat(print_ptr, "--  ");
        }
        else
        {
          snprintf
          ( temp
          , temp_len
          , "%02X  "
          , *reinterpret_cast<uint8_t*>(addr)
          );
          strcat(print_ptr, temp);
        }
      }

      if (base == bottom_base)
      {
        break;
      }
    }

    // Ensure next console output starts at beginning of next line
    snprintf(temp, 16, "\r\n");
    strcat(print_ptr, temp);

    printf("%s", print_ptr);
    return;
  }
};

#endif
/*
  Copyright(C) 2016-2017 Brazil
  Copyright(C) 2019 Sutou Kouhei <kou@clear-code.com>

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License version 2.1 as published by the Free Software Foundation.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include "grn_str.h"

void
grn_raw_string_lstrip(grn_ctx *ctx,
                      grn_raw_string *string)
{
  const char *end;
  int space_len;

  end = string->value + string->length;
  while (string->value < end) {
    space_len = grn_isspace(string->value, ctx->encoding);
    if (space_len == 0) {
      break;
    }
    string->value += space_len;
    string->length -= space_len;
  }
}

bool
grn_raw_string_have_sub_string(grn_ctx *ctx,
                               grn_raw_string *string,
                               grn_raw_string *sub_string)
{
  if (sub_string->length == 0) {
    return false;
  }

  if (sub_string->length > string->length) {
    return false;
  }

  const char *string_current = string->value;
  const char *string_end = string->value + string->length;
  const char *sub_string_current = sub_string->value;
  const char *sub_string_end = sub_string->value + sub_string->length;
  int sub_string_start_char_len;
  int sub_string_char_len;

  sub_string_start_char_len =
    grn_charlen(ctx, sub_string_current, sub_string_end);
  if (sub_string_start_char_len == 0) {
    return false;
  }
  sub_string_char_len = sub_string_start_char_len;

  while (string_current < string_end) {
    int string_char_len;

    string_char_len = grn_charlen(ctx, string_current, string_end);
    if (string_char_len == 0) {
      return false;
    }

    if (string_char_len == sub_string_char_len &&
        memcmp(string_current, sub_string_current, string_char_len) == 0) {
      sub_string_current += sub_string_char_len;
      if (sub_string_current == sub_string_end) {
        return true;
      }

      sub_string_char_len = grn_charlen(ctx, sub_string_current, sub_string_end);
      if (sub_string_char_len == 0) {
        return false;
      }
    } else {
      if (sub_string_current != sub_string->value) {
        sub_string_current = sub_string->value;
        sub_string_char_len = sub_string_start_char_len;
        continue;
      }
    }

    string_current += string_char_len;
  }

  return false;
}

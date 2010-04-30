/* -*- c-basic-offset: 2 -*- */
/* Copyright(C) 2010 Brazil

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License version 2.1 as published by the Free Software Foundation.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/
#ifndef GRN_MODULE_H
#define GRN_MODULE_H

#ifndef GROONGA_IN_H
#include "groonga_in.h"
#endif /* GROONGA_IN_H */

#ifndef GRN_CTX_H
#include "ctx.h"
#endif /* GRN_CTX_H */

#ifndef GRN_STORE_H
#include "store.h"
#endif /* GRN_STORE_H */

#ifdef __cplusplus
extern "C" {
#endif

#ifdef WIN32
typedef MODULE grn_dl;
typedef FARPROC grn_dl_symbol;

#else
typedef void * grn_dl;
typedef void * grn_dl_symbol;
#endif

typedef struct _grn_module grn_module;

struct _grn_module {
  grn_dl dl;
  char *path;
  char *base_name;
  grn_module_func init_func;
  grn_module_func register_func;
  grn_module_func unregister_func;
  grn_module_func fin_func;
};

grn_rc grn_modules_init(void);
grn_rc grn_modules_fin(void);
grn_id grn_module_open(grn_ctx *ctx, const char *filename);
grn_rc grn_module_close(grn_ctx *ctx, grn_id id);
grn_rc grn_module_init(grn_ctx *ctx, grn_id id);
grn_rc grn_module_register(grn_ctx *ctx, grn_id id);
grn_rc grn_module_fin(grn_ctx *ctx, grn_id id);
grn_id grn_module_get(grn_ctx *ctx, const char *filename);
const char *grn_module_path(grn_ctx *ctx, grn_id id);

#ifdef __cplusplus
}
#endif

#endif /* GRN_MODULE_H */

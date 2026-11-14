---
title: "ncl_tdseti(3)"
name: "ncl_tdseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdseti/"
---

TDSETI - Provides a new integer value for a Tdpack parameter.

<h2>Synopsis</h2>

CALL TDSETI (PNAM,IVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdseti (char *pnam, int ival)

<h2>Description</h2>

The arguments of TDSETI are as follows:
<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) - The name of the parameter that you want to set. The character string can be of any length, but only the first three characters of it will be examined.
<dt>IVAL
<dd>(an input expression of type INTEGER) - The integer value you select for the parameter. If the parameter is of type INTEGER, it will be given the value IVAL; if is is of type REAL, it will be given the value REAL(IVAL).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Tdpack parameters. For a complete list of parameters available in this utility, see the &quot;tdpack_params&quot; man page.

<h2>Access</h2>

To use TDSETI or c_tdseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the &quot;tdpack&quot; man page for a description of all Tdpack error messages and/or informational messages.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

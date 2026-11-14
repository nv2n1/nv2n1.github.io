---
title: "ncl_tdsetr(3)"
name: "ncl_tdsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdsetr/"
---

TDSETR - Provides a new real value for a Tdpack parameter.

<h2>Synopsis</h2>

CALL TDSETR (PNAM,RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdsetr (char *pnam, float rval)

<h2>Description</h2>

The arguments of TDSETR are as follows:
<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) - The name of the parameter that you want to set. The character string can be of any length, but only the first three characters of it will be examined.
<dt>RVAL
<dd>(an input expression of type REAL) - The real value you select for the parameter. If the parameter is of type REAL, it will be given the value RVAL; if is is of type INTEGER, it will be given the value INT(RVAL).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Tdpack parameters. For a complete list of parameters available in this utility, see the &quot;tdpack_params&quot; man page.

<h2>Access</h2>

To use TDSETR or c_tdsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the &quot;tdpack&quot; man page for a description of all Tdpack error messages and/or informational messages.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

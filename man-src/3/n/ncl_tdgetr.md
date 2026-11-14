---
title: "ncl_tdgetr(3)"
name: "ncl_tdgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdgetr/"
---

TDGETR - Retrieves the real value of a Tdpack parameter.

<h2>Synopsis</h2>

CALL TDGETR (PNAM,RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdgetr (char *pnam, float *rval)

<h2>Description</h2>

The arguments of TDGETR are as follows:
<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) - The name of the parameter that you want to retrieve. The character string can be of any length, but only the first three characters of it will be examined.
<dt>RVAL
<dd>(an output variable of type REAL) - A real variable to receive the desired parameter value. If the internal parameter is of type REAL and has the value &quot;r&quot;, RVAL will be given the value &quot;r&quot;; if the internal parameter is of type INTEGER and has the value &quot;i&quot;, RVAL will be given the value &quot;REAL(i)&quot;.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current value of Tdpack parameters. For a complete list of parameters available in this utility, see the &quot;tdpack_params&quot; man page.

<h2>Access</h2>

To use TDGETR or c_tdgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the &quot;tdpack&quot; man page for a description of all Tdpack error messages and/or informational messages.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

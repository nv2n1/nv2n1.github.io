---
title: "ncl_wmgetr(3)"
name: "ncl_wmgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmgetr/"
---

WMGETR - Retrieves the real value of an internal parameter of type REAL.

<h2>Synopsis</h2>

CALL WMGETR (PNAM,RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_wmgetr (char *pnam, float *rval)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input expression of type CHARACTER) specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>RVAL
<dd>(an output variable of type REAL) is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current value of Wmap parameters. For a complete list of parameters available in this utility, see the wmap_params man page.

<h2>Access</h2>

To use WMGETR or c_wmgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmlabs, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

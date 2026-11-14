---
title: "ncl_wmsetc(3)"
name: "ncl_wmsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmsetc/"
---

WMSETC - Sets the value of an internal parameter of type CHARACTER.

<h2>Synopsis</h2>

CALL WMSETC (PNAM,CVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_wmsetc (char *pnam, char *cval)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. The name must appear as the first three characters of the string.
<dt>CVAL
<dd>(an input expression of type CHARACTER) is the value to be assigned to the internal parameter specified by PNAM.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Wmap parameters. For a complete list of parameters available in this utility, see the wmap_params man page.

<h2>Access</h2>

To use WMSETC or c_wmsetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetr, wmseti, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

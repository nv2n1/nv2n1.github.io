---
title: "ncl_wmdflt(3)"
name: "ncl_wmdflt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmdflt/"
---

WMDFLT - returns all values of internal parameters in the Wmap package to their default values.

<h2>Synopsis</h2>

CALL WMDFLT ()

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmdflt()

<h2>Usage</h2>

All values of all internal parameters are returned to their default values. See the man page for wmap_params for default values.

<h2>Access</h2>

To use WMDFLT or c_wmdflt, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

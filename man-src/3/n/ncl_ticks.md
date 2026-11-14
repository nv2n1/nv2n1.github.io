---
title: "ncl_ticks(3)"
name: "ncl_ticks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ticks/"
---

TICKS - Allows for program control of tick mark length and direction. This routine has been superseded by TICK4, which should be used instead.

<h2>Synopsis</h2>

CALL TICKS(LMJR,LMNR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ticks (int lmjr, int lmnr)

<h2>Description</h2>

<dl><dt>LMJR and LMNR
<dd>See the description in the TICK4 man page.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

The statement
<dl><dd>CALL TICKS (LMJR,LMNR) 

</dl>
 is equivalent to
<dl><dd>CALL TICK4 (LMJR,LMNR,LMJR,LMNR)</dl>

<h2>Access</h2>

To use TICKS or c_ticks, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gridall, gridall_params, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridal, gridl, halfax, labmod, perim, periml, tick4, ncarg_cbind.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

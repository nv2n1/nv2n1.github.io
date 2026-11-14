---
title: "ncl_agbnch(3)"
name: "ncl_agbnch"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agbnch/"
---

AGBNCH - Provides an easy way to convert binary dash patterns into character dash patterns. 

<h2>Synopsis</h2>AGBNCH (IDSH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 char *c_agbnch(int idsh)
<h2>Description</h2><dl COMPACT><dt>IDSH
<dd>(an input expression of type INTEGER) is between 0 and 65535, inclusive.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Access</h2>To use AGBNCH or c_agbnch, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, agback, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

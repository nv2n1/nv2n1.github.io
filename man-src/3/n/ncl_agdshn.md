---
title: "ncl_agdshn(3)"
name: "ncl_agdshn"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agdshn/"
---

AGDSHN - Provides an easy way to generate the names of parameters in the group 'DASH/PATTERN.', for use in calls to AGSETC and AGGETC. 

<h2>Synopsis</h2>AGDSHN (IDSH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 char *c_agdshn (int idsh)
<h2>Description</h2><dl COMPACT><dt>IDSH
<dd>(an input expression of type INTEGER) is between 1 and 26, inclusive.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>This routine generates parameter names for use in calls to other routines. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Access</h2>To use AGDSHN or c_agdshn, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

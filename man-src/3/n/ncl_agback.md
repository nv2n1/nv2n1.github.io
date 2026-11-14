---
title: "ncl_agback(3)"
name: "ncl_agback"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agback/"
---

AGBACK - Draws the background specified by the current values of the control parameters - the primary parameters with default values or with values supplied by the user, and the secondary parameters with values computed by AGSTUP. 

<h2>Synopsis</h2>CALL AGBACK
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_agback()
<h2>Description</h2>None.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex13, cbex01.
<h2>Access</h2>To use AGBACK or c_agback, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

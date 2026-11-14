---
title: "ncl_agsave(3)"
name: "ncl_agsave"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agsave/"
---

AGSAVE - Saves the current state of Autograph for later restoration by AGRSTR. 

<h2>Synopsis</h2>CALL AGSAVE (IFNO)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_agsave (int ifno)
<h2>Description</h2><dl COMPACT><dt>IFNO
<dd>(an input expression of type INTEGER) is the number of a unit to which a single unformatted record is to be written. It is the user's responsibility to position this unit. AGSAVE does not rewind it, either before or after writing the record.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>This routine saves internal parameter values to a file. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Access</h2>To use AGSAVE or c_agsave, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>Messages</h2>See the autograph man page for a description of all Autograph error messages and/or informational messages.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

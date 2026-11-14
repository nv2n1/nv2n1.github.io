---
title: "ncl_agseti(3)"
name: "ncl_agseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agseti/"
---

AGSETI - Allows a user program to store the real equivalent of an integer as the value of a single parameter. 

<h2>Synopsis</h2>CALL AGSETI (TPGN,IUSR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_agseti (char *tpgn, int iusr)
<h2>Description</h2><dl COMPACT><dt>TPGN
<dd>(an input expression of type CHARACTER) is a parameter identifier, as described for AGSETP, above. If a group of more than one parameter is specified, only the first element of that group will be affected by the call.
<dt>IUSR
<dd>(an input expression of type INTEGER) is the value to be given to the parameter specified by TPGN.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Autograph parameters. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex05, agex06, agex07, agex08, agex09, agex10, agex11, agex12, agex13, bnchmk, cbex01, tagupw, tautog, fagaxlbl, fagovrvw, fspponts.
<h2>Access</h2>To use AGSETI or c_agseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

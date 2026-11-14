---
title: "ncl_agsetf(3)"
name: "ncl_agsetf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agsetf/"
---

AGSETF - Allows a user program to store a real number as the value of a single parameter. 

<h2>Synopsis</h2>CALL AGSETF (TPGN,FUSR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_agsetf (char *tpgn, float fusr)
<h2>Description</h2><dl COMPACT><dt>TPGN
<dd>(an input expression of type CHARACTER) is an parameter identifier, as described in AGSETP man page. If a group of more than one parameter is specified, only the first element of that group will be affected by the call.
<dt>FUSR
<dd>(an input expression of type REAL) is the value to be given to the parameter specified by TPGN.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Autograph parameters. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex05, agex07, agex08, agex10, agex13, fagaxmax, fagcudsh, fagovrvw.
<h2>Access</h2>To use AGSETF or c_agsetf, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetr, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

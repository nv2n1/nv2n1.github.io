---
title: "ncl_aggetc(3)"
name: "ncl_aggetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_aggetc/"
---

AGGETC - Allows a user program to retrieve (in effect) the character-string values of certain single parameters. 

<h2>Synopsis</h2>CALL AGGETC (TPGN,CUSR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_aggetc (char *tpgn, char *cusr, int len)
<h2>Description</h2><dl COMPACT><dt>TPGN
<dd>(an input expression of type CHARACTER) is a parameter identifier, as described for AGGETP, above. The specified parameter must be one of those which intrinsically have values of type character: 'LINE/END.', 'LABEL/NAME.', 'LINE/ TEXT.', or 'DASH/PATTERN/n.'
<dt>CUSR
<dd>(an output variable of type CHARACTER) receives the desired character string. If CUSR is too short, only the beginning of the string will be put in it. If CUSR is too long, it will be padded with blanks on the end.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exception:
<dl COMPACT><dt>len
<dd>The size of cusr as dimensioned in the calling program.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Autograph parameters. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Access</h2>To use AGGETC or c_aggetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>Messages</h2>See the autograph man page for a description of all Autograph error messages and/or informational messages.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

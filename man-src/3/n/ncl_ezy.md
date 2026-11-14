---
title: "ncl_ezy(3)"
name: "ncl_ezy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezy/"
---

EZY - Draws, in a manner determined by the current values of the control parameters, a complete graph of a single curve through the points (I,YDRA(I)), for I from 1 to NPTS. The argument GLAB may be used to specify a &quot;graph label&quot;, to be placed at the top of the graph. 

<h2>Synopsis</h2>CALL EZY (YDRA,NPTS,GLAB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezy (float *ydra, int npts, char *glab)
<h2>Description</h2><dl COMPACT><dt>YDRA
<dd>(an input array of type REAL, dimensioned at least NPTS) defines the Y coordinates of points on the curve. The current value of 'NULL/1.' (default value &quot;1.E36&quot;) may be used in YDRA to signal missing points; curve segments on either side of a missing point are omitted.
<dt>NPTS
<dd>(an input expression of type INTEGER) is the number of curve points defined by the array YDRA.
<dt>GLAB
<dd>(an input expression of type CHARACTER) defines a new &quot;graph label&quot;. (If the first character of this expression is &quot;CHAR(0)&quot;, no new &quot;graph label&quot; is defined; the current one will continue to be used.) A character string defining a new graph label must either be of the exact length specified by the current value of 'LINE/MAXIMUM.' (default: 40 characters), or shorter; if shorter, it must be terminated by the character defined by the current value of 'LINE/END.' (default: a '$'). The string becomes the new text of line number 100 of the label named 'T'.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex01, bnchmk, example, tagupw, tautog, fagezy.
<h2>Access</h2>To use EZY or c_ezy, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

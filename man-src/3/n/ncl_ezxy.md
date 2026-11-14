---
title: "ncl_ezxy(3)"
name: "ncl_ezxy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezxy/"
---

EZXY - Draws, in a manner determined by the current values of the control parameters, a complete graph of a single curve through the points (XDRA(I),YDRA(I)), for I from 1 to NPTS. The argument GLAB may be used to specify a &quot;graph label&quot;, to be placed at the top of the graph. 

<h2>Synopsis</h2>CALL EZXY (XDRA,YDRA,NPTS,GLAB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezxy (float *xdra, float *ydra, int npts, char *glab)
<h2>Description</h2><dl COMPACT><dt>XDRA
<dd>(an input array of type REAL, dimensioned NPTS) defines the X coordinates of points on the curve.
<dt>YDRA
<dd>(an input array of type REAL, dimensioned NPTS) defines the Y coordinates of points on the curve. 

 The points on the curve have coordinates (XDRA(I),YDRA(I)), for I from 1 to NPTS. The current value of 'NULL/1.' (default value &quot;1.E36&quot;) may be used to signal missing data in these arrays. If either coordinate of a point is missing, the point is considered to be missing; curve segments on either side of a missing point are not drawn. Note: Because all non-missing coordinates are used in figuring the minimum and maximum user values along a given axis, it is safest to mark both coordinates as &quot;missing&quot;.
<dt>NPTS
<dd>(an input expression of type INTEGER) is the number of curve points defined by the arrays XDRA and YDRA.
<dt>GLAB
<dd>(an input expression of type CHARACTER) defines a new &quot;graph label&quot;. (If the first character of this expression is &quot;CHAR(0)&quot;, no new &quot;graph label&quot; is defined; the current one will continue to be used.) A character string defining a new graph label must either be of the exact length specified by the current value of 'LINE/MAXIMUM.' (default: 40 characters), or shorter; if shorter, it must be terminated by the character defined by the current value of text of line number 100 of the label named 'T'.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex02, agex06, agex09, agex10, agex11, agex12, splogy, sprevx, tagupw, tautog, fagezxy, fspponts.
<h2>Access</h2>To use EZXY or c_ezxy, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

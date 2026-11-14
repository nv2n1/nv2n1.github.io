---
title: "ncl_ezmy(3)"
name: "ncl_ezmy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezmy/"
---

EZMY - Draws, in a manner determined by the current values of the control parameters, a complete graph of one or more curves, each defined by a set of points (I,YDRA(I,J)) (or (I,YDRA(J,I)), depending on the current value of 'ROW.'), for I from 1 to NPTS. The curve number J runs from 1 to MANY. The argument GLAB may be used to specify a &quot;graph label&quot;, to be placed at the top of the graph. 

<h2>Synopsis</h2>CALL EZMY (YDRA,IDXY,MANY,NPTS,GLAB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezmy (float *ydra, int idxy, int many, int npts, \ 
 char *glab)
<h2>Description</h2><dl COMPACT><dt>YDRA
<dd>(an input array of type REAL, dimensioned IDXY x MANY or IDXY x NPTS, depending on the current value of 'ROW.') defines curve-point Y coordinates. The current value of 'NULL/1.' (default value &quot;1.E36&quot;) may be used in YDRA to signal missing points; curve segments on either side of a missing point are omitted.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'ROW.' is positive (the default), the first subscript of YDRA is a point number and the second is a curve number.
<dt>&bull;
<dd>If 'ROW.' is negative, the order of the subscripts is reversed (&quot;row-wise&quot;, as opposed to &quot;column-wise&quot;, storage); the first subscript is a curve number and the second is a point number.</dl></dl><dt>IDXY
<dd>(an input expression of type INTEGER) defines the first dimension of the array YDRA, which is required by EZMY in order to index the array properly.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'ROW.' is positive (the default), IDXY must be greater than or equal to NPTS.
<dt>&bull;
<dd>If 'ROW.' is negative, IDXY must be greater than or equal to MANY.</dl></dl><dt>MANY
<dd>(an input expression of type INTEGER) is the number of curves to be drawn by EZMY.
<dt>NPTS
<dd>(an input expression of type INTEGER) is the number of points defining each curve to be drawn by EZMY.
<dt>GLAB
<dd>(an input expression of type CHARACTER) defines a new &quot;graph label&quot;. (If the first character of this expression is &quot;CHAR(0)&quot;, no new &quot;graph label&quot; is defined; the current one will continue to be used.) A character string defining a new graph label must either be of the exact length specified by the current value of 'LINE/MAXIMUM.' (default: 40 characters), or shorter; if shorter, it must be terminated by the character defined by the current value of 'LINE/END.' (default: a '$'). The string becomes the new text of line number 100 of the label named 'T'.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex03, tagupw, tautog, fagezmy.
<h2>Access</h2>To use EZMY or c_ezmy, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

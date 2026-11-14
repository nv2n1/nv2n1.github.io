---
title: "ncl_ezmxy(3)"
name: "ncl_ezmxy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezmxy/"
---

EZMXY - Draws, in a manner determined by the current values of the control parameters, a complete graph of one or more curves, each defined by a set of points (XDRA(I),YDRA(I,J)) (or (XDRA(I),YDRA(J,I)) or (XDRA(I,J),YDRA(I,J)) or (XDRA(J,I),YDRA(J,I)), depending on the current value of 'ROW.'), for I from 1 to NPTS. The curve number J runs from 1 to MANY. The argument GLAB may be used to specify a &quot;graph label&quot;, to be placed at the top of the graph. 

<h2>Synopsis</h2>CALL EZMXY (XDRA,YDRA,IDXY,MANY,NPTS,GLAB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezmxy(float *xdra, float *ydra, int idxy, int many, \ 
 int npts, char *glab)
<h2>Description</h2><dl COMPACT><dt>XDRA
<dd>(an input array of type REAL, dimensioned NPTS or IDXY x MANY or IDXY x NPTS, depending on the current value of 'ROW.') contains curve-point X coordinates. The current value of 'NULL/1.' (default value &quot;1.E36&quot;) may be used in XDRA to signal missing points; curve segments on either side of a missing point are not drawn. Note: Because all non-missing coordinates are used in figuring the minimum and maximum user values along a given axis, it is safest to mark both coordinates as &quot;missing&quot;.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'ROW.' has the absolute value &quot;1.&quot; (the default), XDRA is singly-dimensioned. It is subscripted by point number.
<dt>&bull;
<dd>If 'ROW.' has the absolute value &quot;2.&quot; or greater, XDRA is doubly-dimensioned. It is subscripted by point number and curve number, in that order if 'ROW.' is positive (the default), and in the reverse order if 'ROW.' is negative.</dl></dl><dt>YDRA
<dd>(an input array of type REAL, dimensioned IDXY x MANY or IDXY x NPTS, depending on the current value of 'ROW.') contains curve-point Y coordinates. The current value of 'NULL/1.' (default value &quot;1.E36&quot;) may be used in YDRA to signal missing points; curve segments on either side of a missing point are not drawn. Note: Because all non-missing coordinates are used in figuring the minimum and maximum user values along a given axis, it is safest to mark both coordinates as &quot;missing&quot;.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'ROW.' is positive (the default), YDRA is subscripted by point number and curve number, in that order.
<dt>&bull;
<dd>If 'ROW.' is negative, YDRA is subscripted by curve number and point number, in that order.</dl></dl><dt>IDXY
<dd>(an input expression of type INTEGER) is the first dimension of the arrays XDRA (if it is doubly-dimensioned) and YDRA (unconditionally), required by EZMXY in order to index these arrays properly.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'ROW.' is positive (the default), IDXY must be greater than or equal to NPTS.
<dt>&bull;
<dd>If 'ROW.' is negative, IDXY must be greater than or equal to MANY.</dl></dl><dt>MANY
<dd>(an input expression of type INTEGER) is the number of curves to be drawn by EZMXY.
<dt>NPTS
<dd>(an input expression of type INTEGER) is the number of points defining each curve to be drawn by EZMXY.
<dt>GLAB
<dd>(an input expression of type CHARACTER) defines a new &quot;graph label&quot;. (If the first character of this expression is &quot;CHAR(0)&quot;, no new &quot;graph label&quot; is defined; the current one will continue to be used.) A character string defining a new graph label must either be of the exact length specified by the current value of 'LINE/MAXIMUM.' (default: 40 characters), or shorter; if shorter, it must be terminated by the character defined by the current value of 'LINE/END.' (default: a '$'). The string becomes the new text of line number 100 of the label named 'T'.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex04, agex05, agex07, agex08, tagupw, tautog, fagaxclr, fagaxlbl, fagaxmax, fagcuclr, fagcudsh, fagezmxy, fagilclr, fagovrvw.
<h2>Access</h2>To use EZMXY or c_ezmxy, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_pcseti(3)"
name: "ncl_pcseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcseti/"
---

PCSETI - Sets the value of an internal parameter of type INTEGER or REAL.

<h2>Synopsis</h2>

CALL PCSETI (PNAM,IVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pcseti (char *pnam, int ival)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. The name must appear as the first two characters of the string. If the internal parameter is one of the two ('BC' and 'CC') that are arrays, the index of the desired array element may appear, enclosed in parentheses, in columns 3 and following. Other characters may be used to document the use of the parameter being retrieved; for example, instead of just 'MA', one can use 'MA - MAPPING FLAG' and, instead of 'CC(10)', one can use 'CC(10) - SPECIAL COLOR 10'.
<dt>IVAL
<dd>(an input expression of type INTEGER) is the value to be assigned to the internal parameter specified by PNAM. If the internal parameter is of type INTEGER, the value given to it is IVAL. If the internal parameter is of type REAL, the value given to it is REAL(IVAL).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Plotchar parameters. For a complete list of parameters available in this utility, see the plotchar_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: cpex01, cpex09, cpexcc, epltch, srex01, vvexcc. fcell0, fcoord1, fcoord2, fgkgpm, fgpm01, fngwsym, fpcfonts, fpchiqu.

<h2>Access</h2>

To use PCSETI or c_pcseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: plotchar, plotchar_params, pcdlsc, pcgetc, pcgeti, pcgetr, pchiqu, pcloqu, pcmequ, pcmpxy, pcpnwi, pcrset, pcsetc, pcsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

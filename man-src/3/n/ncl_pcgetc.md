---
title: "ncl_pcgetc(3)"
name: "ncl_pcgetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcgetc/"
---

PCGETC - Retrieves the current character value of an internal parameter.

<h2>Synopsis</h2>

CALL PCGETC (PNAM,CVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pcgetc (char *pnam, char *cval, int len)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to get. The name must appear as the first two characters of the string. If the internal parameter is one of the two ('BC' and 'CC') that are arrays, the index of the desired array element may appear, enclosed in parentheses, in columns 3 and following. Other characters may be used to document the use of the parameter being retrieved; for example, instead of just 'MA', one can use 'MA - MAPPING FLAG' and, instead of 'CC(10)', one can use 'CC(10) - SPECIAL COLOR 10'.
<dt>CVAL
<dd>(an output variable of type CHARACTER) is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exception:
<dl><dt>len
<dd>The size of cval as dimensioned in the calling program.</dl>

<h2>Usage</h2>

This routine allows you to retrieve the current value of Plotchar parameters. For a complete list of parameters available in this utility, see the plotchar_params man page.

<h2>Access</h2>

To use PCGETC or c_pcgetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the plotchar man page for a description of all Plotchar error messages and/or informational messages.

<h2>See Also</h2>

Online: plotchar, plotchar_params, pcdlsc, pcgeti, pcgetr, pchiqu, pcloqu, pcmequ, pcmpxy, pcpnwi, pcrset, pcsetc, pcseti, pcsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

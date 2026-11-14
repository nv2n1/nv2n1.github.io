---
title: "ncl_pcgetr(3)"
name: "ncl_pcgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcgetr/"
---

PCGETR - Retrieves the real value of an internal parameter of type REAL or INTEGER.

<h2>Synopsis</h2>

CALL PCGETR (PNAM,RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pcgetr (char *pnam, float *rval)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input expression of type CHARACTER) specifies the name of the parameter to get. The name must appear as the first two characters of the string. If the internal parameter is one of the two ('BC' and 'CC') that are arrays, the index of the desired array element may appear, enclosed in parentheses, in columns 3 and following. Other characters may be used to document the use of the parameter being retrieved; for example, instead of just 'MA', one can use 'MA - MAPPING FLAG' and, instead of 'CC(10)', one can use 'CC(10) - SPECIAL COLOR 10'.
<dt>RVAL
<dd>(an output variable of type REAL) is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved. If the internal parameter is a value &quot;r&quot; of type REAL, the value returned is &quot;r&quot;. If the internal parameter is a value &quot;i&quot; of type INTEGER, the value returned is &quot;REAL(i)&quot;.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current value of Plotchar parameters. For a complete list of parameters available in this utility, see the plotchar_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: cpexcc, epltch, vvexcc, fpchiqu.

<h2>Access</h2>

To use PCGETR or c_pcgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the plotchar man page for a description of all Plotchar error messages and/or informational messages.

<h2>See Also</h2>

Online: plotchar, plotchar_params, pcdlsc, pcgetc, pcgeti, pchiqu, pcloqu, pcmequ, pcmpxy, pcpnwi, pcrset, pcsetc, pcseti, pcsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

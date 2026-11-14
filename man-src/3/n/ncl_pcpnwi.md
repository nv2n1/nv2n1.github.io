---
title: "ncl_pcpnwi(3)"
name: "ncl_pcpnwi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcpnwi/"
---

PCPNWI - A function of type CHARACTER*16.

<h2>Synopsis</h2>

<pre>CHARACTER*16 PCPNWI,ENAM
ENAM = PCPNWI (PNAM,IPAI)</pre>

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pcpnwi (char *pnam, int *ipai)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) is a character string, the first two characters of which are the name of an internal parameter array of Plotchar (currently, 'BC' or 'CC').
<dt>IPAI
<dd>(an input expression of type INTEGER) is an integer expression specifying the index of that element of the internal parameter array of which one wants the name.</dl>
 

 Given the above two arguments, the value of PCPNWI(PNAM,IPAI) is that character string which serves as the name of element IPAI of the internal parameter array identified by PNAM. 

 For example, if IPAI has the value 3, then the value of &quot;PCPNWI('CC',IPAI)&quot; is the character string '<a HREF="/docs/linux/man/3-cc/">CC</a>(3)' (padded with blanks to the right) and the call &quot;CALL PCSETI (PCPNWI('CC',IPAI),62)&quot; would give the value 62 to the third element of the parameter array 'CC'.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine generates parameter names for use in calls to other routines. For a complete list of parameters available in this utility, see the plotchar_params man page.

<h2>Access</h2>

To use PCPNWI or c_pcpnwi, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the plotchar page for a description of all Plotchar error messages and/or informational messages.

<h2>See Also</h2>

Online: plotchar, plotchar_params, pcdlsc, pcgetc, pcgeti, pcgetr, pchiqu, pcloqu, pcmequ, pcmpxy, pcrset, pcsetc, pcseti, pcsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

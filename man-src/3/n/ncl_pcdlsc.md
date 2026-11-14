---
title: "ncl_pcdlsc(3)"
name: "ncl_pcdlsc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcdlsc/"
---

PCDLSC - Defines the default list of &quot;special colors&quot; used by PCHIQU in drawing certain characters from the filled fonts. Calling PCDLSC with the argument IFCI will define color indices IFCI, IFCI+1, IFCI+2, ..., IFCI+15 and it will set all elements of the internal parameter array 'CC' corresponding to indices 1 through 16. At the moment, although such a call does define a set of sixteen colors (ranging from blue to red) and set the elements of 'CC', it's a bit pointless, since there are no characters for which the special colors are used. In the future, there will be a few such (like the state highway symbol, which is normally drawn in a particular pair of colors); at that time, the routine will be of more use.

<h2>Synopsis</h2>

CALL PCDLSC (IFCI)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pcdlsc (int ifci)

<h2>Description</h2>

<dl><dt>IFCI
<dd>(an input expression of type INTEGER) specifies the first of a set of sixteen color indices that may be defined by PCDLSC. Make sure that these color indices are not already used.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Plotchar parameters. For a complete list of parameters available in this utility, see the plotchar_params man page.

<h2>Access</h2>

To use PCDLSC or c_pcdlsc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the plotchar man page for a description of all Plotchar error messages and/or informational messages.

<h2>See Also</h2>

Online: plotchar, plotchar_params, pcgetc, pcgeti, pcgetr, pchiqu, pcloqu, pcmequ, pcmpxy, pcpnwi, pcrset, pcsetc, pcseti, pcsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

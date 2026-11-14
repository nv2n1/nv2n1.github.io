---
title: "ncl_icloem(3)"
name: "ncl_icloem"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_icloem/"
---

ICLOEM - Called to get the length of the non-blank portion of an error message. 

<h2>Synopsis</h2>LNGTH = ICLOEM(MESSG)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_icloem(char *messg)
<h2>Description</h2>The value of the expression &quot;ICLOEM(MESSG)&quot; is the actual length of the non-blank portion of the input character variable MESSG. Thus, &quot;MESSG(1:ICLOEM(MESSG))&quot; is the non-blank part of MESSG. (It is assumed that the non-blank part of MESSG is left-justified in the character string, with blank fill to the right, as is the case for all NCAR Graphics error messages in calls to SETER.) 

 The argument of ICLOEM is as follows: 

<dl COMPACT><dt>MESSG
<dd>(an input variable or constant of type CHARACTER) - Most likely an error message returned by a reference to the function SEMESS.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tseter, arex02.
<h2>Access</h2>To use ICLOEM or c_icloem, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: entsr, eprin, errof, error_handling, fdum, icfell, nerro, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

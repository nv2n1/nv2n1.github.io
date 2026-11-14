---
title: "ncl_errof(3)"
name: "ncl_errof"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_errof/"
---

ERROF - Turns off the internal error flag of SETER. 

<h2>Synopsis</h2>CALL ERROF
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_errof()
<h2>Description</h2>The FORTRAN statement &quot;CALL ERROF&quot; turns off (zeroes) SETER's internal error flag. 

 ERROF has no arguments.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tseter, arex02.
<h2>Access</h2>To use ERROF or c_errof, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: entsr, eprin, error_handling, fdum, icfell, icloem, nerro, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

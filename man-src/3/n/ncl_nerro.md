---
title: "ncl_nerro(3)"
name: "ncl_nerro"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nerro/"
---

NERRO - Referenced by a user to obtain the current value of the internal error flag of SETER. 

<h2>Synopsis</h2>NERR=NERRO(NERRF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_nerro(int *nerrf)
<h2>Description</h2>The FORTRAN expression &quot;NERRO(NERRF)&quot; has the value of the internal error flag of SETER. If its value is non-zero, this indicates that a prior recoverable error occurred and has not yet been cleared. The argument NERRF is given the same value as the function reference; this is useful in some situations. 

 The argument of NERRO is as follows: 

<dl COMPACT><dt>NERRF
<dd>(an output variable of type INTEGER) - Receives the same value that is returned as the value of the function itself.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tseter, arex02.
<h2>Access</h2>To use nerro or c_nerro, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: entsr, eprin, errof, error_handling, fdum, icfell, icloem, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

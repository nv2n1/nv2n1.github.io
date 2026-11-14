---
title: "ncl_retsr(3)"
name: "ncl_retsr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_retsr/"
---

RETSR - Called by a user to return to a saved state of the recovery mode in NCAR Graphics.

<h2>Synopsis</h2>

CALL RETSR(IROLD)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_entsr(int irold)

<h2>Description</h2>

The FORTRAN statement &quot;CALL RETSR(IROLD)&quot; is normally used to return the internal error flag of SETER that says whether or not recovery mode is in effect to the state that it was in before some past call to ENTSR. 

 If recovery mode is turned off by a call to RETSR at a time when the internal error flag is non-zero, this is treated as a fatal error; the error message is printed, the dump routine FDUM is called, and a STOP is executed. 

 The argument of RETSR is as follows: 

<dl><dt>IROLD
<dd>(an input expression of type INTEGER) - Specifies a desired value for the internal flag that indicates whether recovery mode is in effect or not. The value 1 turns recovery mode on and the value 2 turns it off. Normally, one uses a value of IROLD that was previously returned by a call to ENTSR.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tseter, arex02.

<h2>Access</h2>

To use RETSR or c_retsr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: entsr, eprin, errof, error_handling, fdum, icfell, icloem, nerro, semess, seter, ncarg_cbind

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

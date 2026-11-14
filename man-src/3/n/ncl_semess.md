---
title: "ncl_semess(3)"
name: "ncl_semess"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_semess/"
---

SEMESS - Called by a user to get a specified portion of the current error message.

<h2>Synopsis</h2>

MESSG = SEMESS(ITRIM)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 char *c_semess(int itrim)

<h2>Description</h2>

In any routine that references SEMESS, it must be declared to be of type CHARACTER*113. 

 If the internal error flag of SETER is non-zero, the value of the character expression &quot;SEMESS(ITRIM)&quot; is the remembered error message associated with that error flag, trimmed as indicated by the value of the input quantity ITRIM. Otherwise, it is a string of blanks. 

 When ITRIM = 0 or less, no trimming is done; the whole error message is returned. When ITRIM = 1, prepended routine names and the associated slashes are trimmed off. When ITRIM = 2 or greater, all leading routine names are trimmed off; just the error description is returned. 

 Example: Assume that the current error message is the string &quot;CPCLAM/AREDAM - AREA-MAP ARRAY OVERFLOW&quot;; then, SEMESS(0) is that entire string, while <a HREF="/docs/linux/man/1-semess/">SEMESS</a>(1) = &quot;AREDAM - AREA-MAP ARRAY OVERFLOW&quot;, and <a HREF="/docs/linux/man/2-semess/">SEMESS</a>(2) = &quot;AREA-MAP ARRAY OVERFLOW&quot;. 

 The argument of SEMESS is as follows: 

<dl><dt>ITRIM
<dd>(an input expression of type INTEGER) - Says what part of the error message is to be returned, as detailed above.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tseter, arex02.

<h2>Access</h2>

To use SEMESS or c_semess, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: entsr, eprin, errof, error_handling, fdum, icfell, icloem, nerro, retsr, seter, ncarg_cbind

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_sfsetr(3)"
name: "ncl_sfsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfsetr/"
---

SFSETR - Used to set the current real value of a specified internal parameter.

<h2>Synopsis</h2>

CALL SFSETR (CNP, RVP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfsetr (char *cnp, float rvp)

<h2>Description</h2>

<dl><dt>CNP
<dd>(an input expression of type CHARACTER) is one of the character strings 'AN', 'CH', 'DO', 'SP', or 'TY' (or a longer string beginning with one of these strings), meaning &quot;ANgle&quot;, &quot;CHaracter&quot;, &quot;DOts&quot;, &quot;SPacing&quot;, and &quot;TYpe&quot;, respectively.
<dt>RVP
<dd>(an input expression of type REAL) is the desired new value of the parameter specified by CNP. This value will be used until the next call resetting it. If the internal parameter is inherently of type INTEGER, the value &quot;INT(RVP)&quot; will be given to it.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Softfill parameters. For a complete list of parameters available in this utility, see the softfill_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ccpscam, cmptit, agex12, cpex01, cpex02, cpex03, cpex04, cpex05, sfex01, vvex01, tsoftf, fsfwrld.

<h2>Access</h2>

To use SFSETR or c_sfsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the softfill man page for a description of all Softfill error messages and/or informational messages.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgetc, sfgeti, sfgetp, sfgetr, sfsetc, sfseti, sfsetp, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

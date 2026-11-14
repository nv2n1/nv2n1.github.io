---
title: "ncl_sfseti(3)"
name: "ncl_sfseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfseti/"
---

SFSETI - Used to set the current integer value of a specified internal parameter.

<h2>Synopsis</h2>

CALL SFSETI (CNP, IVP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfseti (char *cnp, int ivp)

<h2>Description</h2>

<dl><dt>CNP
<dd>(an input expression of type CHARACTER) is one of the character strings 'AN', 'CH', 'DO', 'SP', or 'TY' (or a longer string beginning with one of these strings), meaning &quot;ANgle&quot;, &quot;CHaracter&quot;, &quot;DOts&quot;, &quot;SPacing&quot;, and &quot;TYpe&quot;, respectively.
<dt>IVP
<dd>(an input expression of type INTEGER) is the desired new value of the parameter specified by CNP. This value will be used until the next call resetting it. If the internal parameter is inherently of type REAL, the value &quot;REAL(IVP)&quot; will be given to it.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Softfill parameters. For a complete list of parameters available in this utility, see the softfill_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: agex12, cpex01, cpex02, cpex03, cpex04, cpex05, elblba, sfex01, sfex02, vvex01, tlblba, tsoftf, fsfsgfa.

<h2>Access</h2>

To use SFSETI or c_sfseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the softfill man page for a description of all Softfill error messages and/or informational messages.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgetc, sfgeti, sfgetp, sfgetr, sfsetc, sfseti, sfsetp, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

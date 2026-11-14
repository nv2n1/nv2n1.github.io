---
title: "ncl_sfgeti(3)"
name: "ncl_sfgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfgeti/"
---

SFGETI - Used to retrieve the current integer value of a specified parameter.

<h2>Synopsis</h2>

CALL SFGETI (CNP, IVP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfgeti (char *cnp, int *ivp)

<h2>Description</h2>

<dl><dt>CNP
<dd>(an input expression of type CHARACTER) is one of the character strings 'AN', 'CH', 'DO', 'SP', or 'TY' (or a longer string beginning with one of these strings), meaning &quot;ANgle&quot;, &quot;CHaracter&quot;, &quot;DOts&quot;, &quot;SPacing&quot;, and &quot;TYpe&quot;, respectively.
<dt>IVP
<dd>(an output variable of type INTEGER) is the name of a variable into which the value of the parameter specified by CNP is to be retrieved. If the internal parameter is inherently a real value &quot;r&quot;, &quot;INT(r)&quot; will be returned as the value of IVP.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current integer value of Softfill parameters. For a complete list of parameters available in this utility, see the softfill_params man page.

<h2>Access</h2>

To use SFGETI or c_sfgeti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the softfill man page for a description of all Softfill error messages and/or informational messages.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgetc, sfgetp, sfgetr, sfsetc, sfseti, sfsetp, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

---
title: "ncl_isseti(3)"
name: "ncl_isseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_isseti/"
---

ISSETI - Resets the current values of internal parameters of type INTEGER. 

<h2>Synopsis</h2>CALL ISSETI (CNP,IVP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_isseti (char *cnp, int ivp)
<h2>Description</h2><dl COMPACT><dt>CNP
<dd>(an input expression of type CHARACTER) is the name of an internal parameter. Only the first two characters of the name are meaningful, but a longer character string may be used to more clearly document what internal parameter is being set.
<dt>IVP
<dd>(an input expression of type INTEGER) is the desired new value of the parameter specified by CNP. This value will be used until the next call resetting it. If the internal parameter is inherently of type REAL, the value &quot;REAL(IVP)&quot; will be given to it.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Isosurface parameters. For a complete list of parameters available in this utility, see the isosurface_params man page.
<h2>Access</h2>To use ISSETI or c_isseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the isosurface man page for a description of all Isosurface error messages and/or informational messages.
<h2>See Also</h2>Online: isosurface, isosurface_params, ezisos, isgeti, isgetr, isosrf, issetr, pwrzi, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

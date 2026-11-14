---
title: "ncl_isgeti(3)"
name: "ncl_isgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_isgeti/"
---

ISGETI - Gets the current values of internal parameters of type INTEGER. 

<h2>Synopsis</h2>CALL ISGETI (CNP,IVP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_isgeti (char *cnp, int *ivp)
<h2>Description</h2><dl COMPACT><dt>CNP
<dd>(an input expression of type CHARACTER) is the name of an internal parameter. Only the first two characters of the name are meaningful, but a longer character string may be used to more clearly document what internal parameter is being retrieved.
<dt>IVP
<dd>(an output variable of type INTEGER) is the name of a variable into which the value of the parameter specified by CNP is to be retrieved. If the internal parameter is inherently a real value &quot;r&quot;, &quot;INT(r)&quot; will be returned as the value of IVP.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to retrieve the current value of Isosurface parameters. For a complete list of parameters available in this utility, see the isosurface_params man page.
<h2>Access</h2>To use ISGETI or c_isgeti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the isosurface man page for a description of all Isosurface error messages and/or informational messages.
<h2>See Also</h2>Online: isosurface, isosurface_params, ezisos, isgetr, isosrf, isseti, issetr, pwrzi, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

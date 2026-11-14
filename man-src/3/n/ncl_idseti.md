---
title: "ncl_idseti(3)"
name: "ncl_idseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_idseti/"
---

IDSETI - Provides a new integer value for a Bivar parameter. 

<h2>Synopsis</h2>CALL IDSETI (PNAM,IVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_idseti (char *pnam, int ival)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) - The name of the parameter that you want to set. The character string can be of any length, but only the first two characters of it will be examined.
<dt>IVAL
<dd>(an input expression of type INTEGER) - The integer value you select for the parameter. If the parameter is of type INTEGER, it will be given the value IVAL; if is is of type REAL, it will be given the value REAL(IVAL).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Bivar parameters. For a complete list of parameters available in this utility, see the bivar_params man page.
<h2>Access</h2>To use IDSETI or c_idseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the bivar man page for a description of all Bivar error messages and/or informational messages.
<h2>See Also</h2>Online: bivar, bivar_params, idbvip, idsfft, idpltr, idgeti, idgetr, idsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

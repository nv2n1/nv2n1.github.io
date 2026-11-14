---
title: "ncl_argeti(3)"
name: "ncl_argeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_argeti/"
---

ARGETI - Retrieves the integer value of an Areas parameter. 

<h2>Synopsis</h2>CALL ARGETI (PNAM,IVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_argeti (char *pnam, int *ival)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) - The name of the parameter that you want to retrieve. The character string can be of any length, but only the first two characters of it will be examined.
<dt>IVAL
<dd>(an output variable of type INTEGER) - An integer variable to receive the desired parameter value. If the internal parameter is of type INTEGER and has the value &quot;i&quot;, IVAL will be given the value &quot;i&quot;; if the internal parameter is of type REAL and has the value &quot;r&quot;, IVAL will be given the value &quot;INT(r)&quot;.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to retrieve the current value of Areas parameters. For a complete list of parameters available in this utility, see the areas_params man page.
<h2>Access</h2>To use ARGETI or c_argeti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, aredam, argetr, argtai, arinam, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

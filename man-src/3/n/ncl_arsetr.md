---
title: "ncl_arsetr(3)"
name: "ncl_arsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_arsetr/"
---

ARSETR - Provides a new real value for an Areas parameter. 

<h2>Synopsis</h2>CALL ARSETR (PNAM,RVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_arsetr (char *pnam, float rval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) - The name of the parameter that you want to set. The character string can be of any length, but only the first two characters of it will be examined.
<dt>RVAL
<dd>(an input expression of type REAL) - The real value you select for the parameter. If the parameter is of type REAL, it will be given the value RVAL; if is is of type INTEGER, it will be given the value INT(RVAL).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Areas parameters. For a complete list of parameters available in this utility, see the areas_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cardb1, arex01.
<h2>Access</h2>To use ARSETR or c_arsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, aredam, argeti, argetr, argtai, arinam, armvam, arpram, arscam, arseti, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

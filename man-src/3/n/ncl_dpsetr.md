---
title: "ncl_dpsetr(3)"
name: "ncl_dpsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpsetr/"
---

DPSETR - Sets the value of an internal parameter of type REAL or INTEGER. 

<h2>Synopsis</h2>CALL DPSETR (PNAM,RVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpsetr (char *pnam, float rval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. The name must appear as the first three characters of the string. Other characters may be used to document the use of the parameter being set; for example, instead of just 'LS1', one can use 'LS1 - LABEL SPACING PARAMETER 1'.
<dt>RVAL
<dd>(an input expression of type REAL) is the value to be assigned to the internal parameter specified by PNAM. If the internal parameter is of type REAL, the value given to it is RVAL. If the internal parameter is of type INTEGER, the value given to it is INT(RVAL).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Dashpack parameters. For a complete list of parameters available in this utility, see the dashpack_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPSETR or c_dpsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the dashpack man page for a description of all Dashpack error messages and/or informational messages.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpline, dpsetc, dpseti, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

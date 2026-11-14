---
title: "ncl_dpseti(3)"
name: "ncl_dpseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpseti/"
---

DPSETI - Sets the value of an internal parameter of type INTEGER or REAL. 

<h2>Synopsis</h2>CALL DPSETI (PNAM,IVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpseti (char *pnam, int ival)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. The name must appear as the first three characters of the string. Other characters may be used to document the use of the parameter being set; for example, instead of just 'DPL', one can use 'DPL - DASH PATTERN LENGTH'.
<dt>IVAL
<dd>(an input expression of type INTEGER) is the value to be assigned to the internal parameter specified by PNAM. If the internal parameter is of type INTEGER, the value given to it is IVAL. If the internal parameter is of type REAL, the value given to it is REAL(IVAL).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Dashpack parameters. For a complete list of parameters available in this utility, see the dashpack_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPSETI or c_dpseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpline, dpsetc, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

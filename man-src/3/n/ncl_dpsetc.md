---
title: "ncl_dpsetc(3)"
name: "ncl_dpsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpsetc/"
---

DPSETC - Gives a new character value to a specified internal parameter. 

<h2>Synopsis</h2>CALL DPSETC (PNAM,CVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpsetc (char *pnam, char *cval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. The name must appear as the first three characters of the string. Other characters may be used to document the use of the parameter being set; for example, instead of just 'CRB', one can use 'CRB - CHARACTER REPRESENTING BREAK'.
<dt>CVAL
<dd>(an input constant or variable of type CHARACTER) is the value to be assigned to the internal parameter specified by PNAM.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Dashpack parameters. For a complete list of parameters available in this utility, see the dashpack_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPSETC or c_dpsetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the dashpack man page for a description of all Dashpack error messages and/or informational messages.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpline, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

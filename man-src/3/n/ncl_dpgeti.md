---
title: "ncl_dpgeti(3)"
name: "ncl_dpgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpgeti/"
---

DPGETI - Retrieves the integral value of an internal parameter of type INTEGER or REAL. 

<h2>Synopsis</h2>CALL DPGETI (PNAM,IVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpgeti (char *pnam, int *ival)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to get. The name must appear as the first three characters of the string. Other characters may be used to document the use of the parameter being retrieved; for example, instead of just 'DPL', one can use 'DPL - DASH PATTERN LENGTH'.
<dt>IVAL
<dd>(an output variable of type INTEGER) is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved. If the internal parameter is a value &quot;i&quot; of type INTEGER, the value returned is &quot;i&quot;. If the internal parameter is a value &quot;r&quot; of type REAL, the value returned is &quot;INT(r)&quot;.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to retrieve the current value of Dashpack parameters. For a complete list of parameters available in this utility, see the dashpack_params man page.
<h2>Access</h2>To use DPGETI or c_dpgeti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgetr, dplast, dpline, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

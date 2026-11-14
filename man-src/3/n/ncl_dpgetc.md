---
title: "ncl_dpgetc(3)"
name: "ncl_dpgetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpgetc/"
---

DPGETC - Retrieves the current character value of an internal parameter. 

<h2>Synopsis</h2>CALL DPGETC (PNAM,CVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpgetc (char *pnam, char *cval, int len)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to get. The name must appear as the first three characters of the string. Other characters may be used to document the use of the parameter being retrieved; for example, instead of just 'CRB', one can use 'CRB - CHARACTER REPRESENTING BREAK'.
<dt>CVAL
<dd>(an output variable of type CHARACTER) is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exception:
<dl COMPACT><dt>len
<dd>The size of cval as dimensioned in the calling program.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Dashpack parameters. For a complete list of parameters available in this utility, see the dashpack_params man page.
<h2>Access</h2>To use DPGETC or c_dpgetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the dashpack man page for a description of all Dashpack error messages and/or informational messages.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgeti, dpgetr, dplast, dpline, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

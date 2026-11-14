---
title: "ncl_ngsetr(3)"
name: "ncl_ngsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngsetr/"
---

NGSETR - Provides a new real value for an internal parameter of Ngmisc of type REAL. See the ngmisc_params man page for a complete list of all the Ngmisc internal parameters.

<h2>Synopsis</h2>

CALL NGSETR (PNAM, RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngsetr (char *pnam, float rval)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. Only the first two characters of the string are examined.
<dt>RVAL
<dd>(an input expression of type REAL) is the desired value of the internal parameter.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Ngmisc parameters. For a complete list of parameters available in this utility, see the ngmisc_params man page.

<h2>Access</h2>

To use NGSETR or c_ngsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: ngmisc_params, nggetr, ngsetc, nggetc, ngseti, nggeti, ncarg_cbind. 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version;

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

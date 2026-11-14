---
title: "ncl_ngsetc(3)"
name: "ncl_ngsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngsetc/"
---

NGSETC - Used to set the character value of a specified internal parameter.

<h2>Synopsis</h2>

CALL NGSETC (CNP, CVP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngsetc (char *cnp, char *cvp)

<h2>Description</h2>

<dl><dt>CNP
<dd>(an input expression of type CHARACTER) is the name of an internal parameter of Ngmisc. Only the first two characters will be examined.
<dt>CVP
<dd>(an input expression of type CHARACTER) is the desired new value of the parameter specified by CNP. This value will be used until the next call resetting it.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Ngmisc parameters. For a complete list of parameters available in this utility, see the ngmisc_params man page.

<h2>Access</h2>

To use NGSETC or c_ngsetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: ngmisc_params, nggetc, ngseti, nggeti, ngsetr, nggetr, ncarg_cbind. 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version;

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

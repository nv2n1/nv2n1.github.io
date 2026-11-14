---
title: "ncl_nggetc(3)"
name: "ncl_nggetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nggetc/"
---

NGGETC - Used to retrieve the current value of a specified internal parameter. 

<h2>Synopsis</h2>CALL NGGETC (CNP,CVP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_nggetc (char *cnp, char *cvp, int len)
<h2>Description</h2><dl COMPACT><dt>CNP
<dd>(an input expression of type CHARACTER) is the name of an internal parameter of Ngmisc. Only the first two characters of the string are examined.
<dt>CVP
<dd>(an output variable of type CHARACTER) is the name of a variable into which the value of the parameter specified by CNP is to be retrieved.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exception:
<dl COMPACT><dt>len
<dd>The size of cvp as dimensioned in the calling program.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Ngmisc parameters. For a complete list of parameters available in this utility, see the ngmisc_params man page.
<h2>Access</h2>To use NGGETC or c_nggetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ngmisc_params, ngsetc, ngseti, nggeti, ngsetr, nggetr, ncarg_cbind. 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

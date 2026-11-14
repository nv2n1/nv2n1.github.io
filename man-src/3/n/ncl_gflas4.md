---
title: "ncl_gflas4(3)"
name: "ncl_gflas4"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gflas4/"
---

GFLAS4 - Allows you to access a disk file of plotting instructions, generated with a GFLAS1 and GFLAS2 sequence in a previous job, for use in a GFLAS3 call. 

<h2>Synopsis</h2>CALL GFLAS4 (IB, FNAME)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gflas4 (int ib, char *fname)
<h2>Description</h2><dl COMPACT><dt>IB
<dd>(INTEGER, input) Specifies the identifier to be used for subsequent GFLAS3 calls. This needs to be between 0 and 99 inclusive, just as with the argument IB to GFLAS1.
<dt>FNAME
<dd>(CHARACTER, input) Specifies the name of the file in which the plotting instructions are stored; FNAME is a FORTRAN character variable specifying the file name of the disk file.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Access</h2>To use GFLAS4 or c_gflas4, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gflash, gflas1, gflas2, gflas3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

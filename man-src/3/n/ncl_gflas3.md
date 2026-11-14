---
title: "ncl_gflas3(3)"
name: "ncl_gflas3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gflas3/"
---

GFLAS3 - Inserts the instructions saved on disk with a previous GFLAS1 identifier IB into the output stream. GFLAS3 can be called only after a previous GFLAS1 and GFLAS2 sequence or after a call to GFLAS4. GFLAS3 uses FORTRAN logical unit IC as specified in the GOPWK call for WISS. 

<h2>Synopsis</h2>CALL GFLAS3 (IB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gflas3 (int ib)
<h2>Description</h2><dl COMPACT><dt>IB
<dd>(INTEGER, input) The same identifying integer used for an (IB) argument in GFLAS1.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpmovi, tgflas, fgke02.
<h2>Access</h2>To use GFLAS3 or c_gflas3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gflash, gflas1, gflas2, gflas4, ncarg_cbind. 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_gflas1(3)"
name: "ncl_gflas1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gflas1/"
---

GFLAS1 - Initiates storage of plotting instructions into a disk file. Instructions subsequent to GFLAS1, but prior to a GFLAS2 call, will be stored on disk rather than inserted into the output metafile. 

<h2>Synopsis</h2>CALL GFLAS1 (IB) 

<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gflas1 (int ib)
<h2>Description</h2><dl COMPACT><dt>IB
<dd>(INTEGER, input) Can be any integer between 0 and 99 inclusive, thus making it possible to define 100 different storage buffers in a single job step.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>GFLAS1 automatically assigns the name GNFBxx (GKS New Flash Buffer) to the file that will receive subsequent plotting instructions, where xx is the integer value of IB. For example, if GFLAS1 is called with an argument of 9, then subsequent plotting instructions will be stored in file GNFB09. You may need to know the name of the disk file where the plotting instructions are stored if and when you use GFLAS4. The GNFBxx files are all created using FORTRAN logical unit IC as specified in the GOPWK call for WISS.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpmovi, tgflas, fgke02.
<h2>Access</h2>To use GFLAS1 or c_gflas1, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gflash, gflas2, gflas3, gflas4, ncarg_cbind. 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

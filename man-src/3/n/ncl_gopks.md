---
title: "ncl_gopks(3)"
name: "ncl_gopks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gopks/"
---

GOPKS (Open GKS) - opens the GKS package
<h2>Synopsis</h2>CALL GOPKS (ERRFIL, BUFA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gopen_gks(const char *err_file, size_t mem_unit);
<h2>Description</h2><dl COMPACT><dt>ERRFIL
<dd>(Input, Integer) - The Fortran unit number to which error messages are to be written. Typically this should be unit 6.
<dt>BUFA
<dd>(Input, Integer) - The dimension of an internal buffer. Currently in NCAR GKS-0A, BUFA is ignored.</dl><h2>Usage</h2>To get output to any workstation, GOPKS, GOPWK and GACWK must be called in that order. For jobs producing only CGM output, the three calls to GOPKS, GOPWK and GACWK can be replaced with a call to the SPPS function OPNGKS.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopwk, gacwk, gdawk, gclwk, gclks, guwk, opngks, clsgks, gopen_gks 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

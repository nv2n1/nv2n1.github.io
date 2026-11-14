---
title: "ncl_gclks(3)"
name: "ncl_gclks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclks/"
---

GCLKS (Close GSK) - closes the GKS package.
<h2>Synopsis</h2>CALL GCLKS
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gclose_gks( void );
<h2>Usage</h2>A call to GCLKS insures that the graphics package is properly terminated. No graphics calls depending on GKS should be made during the time that GKS is closed. If output to a CGM has been the exclusive requirement of the graphics job, and the SPPS entry OPNGKS has been used to open GKS and to open and activate a CGM workstation, then CLSGKS can be used to deactivate and close the CGM workstation, and to close GKS, making a direct call to GCLKS unnecessary in that case.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gopwk, gacwk, gdawk, gclwk, gupwk, opngks, clsgks, gclose_gks 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

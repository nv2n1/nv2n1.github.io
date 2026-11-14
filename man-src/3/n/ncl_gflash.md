---
title: "ncl_gflash(3)"
name: "ncl_gflash"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gflash/"
---

Gflash - Allows for storing segments of a picture for insertion into any subsequent picture. 

<h2>Synopsis</h2>GFLAS1 - Starts storage of plotting instructions. 

 GFLAS2 - Stops storage of plotting instructions. 

 GFLAS3 - Inserts saved plotting instructions into the output stream. 

 GFLAS4 - Associates the filename of a previously generated picture segment with an id suitable for use with GFLAS3.
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_gflas1 
 c_gflas2 
 c_gflas3 
 c_gflas4
<h2>Access</h2>To use Gflash C or Fortran routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>When error conditions are detected, the support routine SETER is called in such a way that it writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. The possible error messages are as follows:
<dl COMPACT><dt>GFLAS1 CALLED CONSECUTIVELY WITHOUT AN INTERVENING GFLAS2 CALL
<dd>You must terminate the usage of one FLASH buffer before reusing it.
<dt>THE NON-NCAR GKS PACKAGE IS NOT LEVEL 2
<dd>Gflash requires GKS level 2A or higher in order to function in a non-NCAR GKS environment.
<dt>WISS MUST BE OPEN BEFORE CALL TO GFLAS1
<dd>Gflash entries must have access to the appropriate GKS segmentation functions in order to work. This is accomplished by making a call to the GKS entry GOPWK to open WISS.
<dt>MAXIMUM NUMBER OF OPEN WORKSTATIONS ALLOWED IS 100
<dd>You have called GFLAS1 with more than 100 different identifiers.
<dt>BUFFER IDENTIFIER .LT. 0, OR .GT. 99
<dd>The argument to Gflash is out of the described range.
<dt>GKS MUST BE OPEN BEFORE A CALL TO GFLAS1
<dd>You have tried calling GFLAS1 without opening GKS. A call to the GKS entry GOPWK is required before calling any Gflash entry.
<dt>GFLAS2 CALLED WITHOUT CALLING GFLAS1
<dd>GFLAS2 terminates the GFLAS1 job of writing plotting instructions to disk. GFLAS2 has no functionality if not called in the legal sequence.
<dt>WISS NOT OPEN AT GFLAS2 TIME
<dd>Gflash entries must have access to the appropriate GKS segmentation functions in order to work. This is accomplished by making a call to the GKS entry GOPWK to open WISS.
<dt>GFLAS3 CALLED WITHOUT CALLING GFLAS2 OR GFLAS4
<dd>GFLAS3 has no access to the plotting instructions that it is to insert into the output metafile unless a call to either GFLAS2 or GFLAS4 is made first.
<dt>THE NON-NCAR GKS PACKAGE IS NOT LEVEL 2
<dd>Gflash requires GKS level 2A or higher in order to function in a non-NCAR GKS environment.
<dt>WISS MUST BE OPEN BEFORE A CALL TO GFLAS4
<dd>Gflash entries must have access to the appropriate GKS segmentation functions in order to work. This is accomplished by making a call to the GKS entry GOPWK to open WISS.
<dt>MAXIMUM NUMBER OF WORKSTATIONS ALLOWED IS 100
<dd>You have called GFLAS1 with more than 100 different identifiers.
<dt>GKS MUST BE OPEN BEFORE A CALL TO GFLAS4
<dd>You have tried calling GFLAS4 without opening the NCAR GKS package. (The GFLAS4 subroutine is an option only if you are using the NCAR GKS package.)
<dt>CANNOT BE CALLED WHILE GFLAS1 IS STILL OPEN
<dd>Call GFLAS2 to complete the GFLAS1/GFLAS2 sequence before attempting to call GFLAS4.</dl><h2>See Also</h2>Online: gflas1, gflas2, gflas3, gflas4, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

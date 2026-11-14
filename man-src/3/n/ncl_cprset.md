---
title: "ncl_cprset(3)"
name: "ncl_cprset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cprset/"
---

CPRSET - Resets all parameters to their initial default values. 

<h2>Synopsis</h2>CALL CPRSET
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cprset()
<h2>Description</h2>CPRSET has no arguments.
<h2>Usage</h2>Calling this routine restores all Conpack parameters to their initial default values. For a complete list of parameters available in this utility, see the conpack_params man page.
<h2>Access</h2>To use CPRSET or c_cprset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: conpack, conpack_params, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

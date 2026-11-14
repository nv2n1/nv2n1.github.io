---
title: "ncl_gqops(3)"
name: "ncl_gqops"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqops/"
---

GQOPS (Inquire operating state value) - returns the operating state of GKS.
<h2>Synopsis</h2>CALL GQOPS (OPSTA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_op_st(Gop_st *op_st);
<h2>Description</h2><dl COMPACT><dt>OPSTA
<dd>(Integer, Output) - Returns the GKS operating state:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>GKS is closed
<dt>1
<dd>GKS is open
<dt>2
<dd>Additionally, a workstation is open
<dt>3
<dd>Additionally, a workstation is active
<dt>4
<dd>Additionally, a segment is open</dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gopwk, gacwk, gdawk, gclwk, gclks, opngks, clsgks, ginq_op_st 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

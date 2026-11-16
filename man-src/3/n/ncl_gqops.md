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
</dt><dd>(Integer, Output) - Returns the GKS operating state:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>GKS is closed
</dd><dt>1
</dt><dd>GKS is open
</dd><dt>2
</dt><dd>Additionally, a workstation is open
</dd><dt>3
</dt><dd>Additionally, a workstation is active
</dd><dt>4
</dt><dd>Additionally, a segment is open</dd></dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gopwk, gacwk, gdawk, gclwk, gclks, opngks, clsgks, ginq_op_st 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

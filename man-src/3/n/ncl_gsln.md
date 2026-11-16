---
title: "ncl_gsln(3)"
name: "ncl_gsln"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsln/"
---

GSLN (Set line type) - sets the line type to solid or various dashed patterns.
<h2>Synopsis</h2>CALL GSLN (LTYPE)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_linetype(Gint linetype);
<h2>Description</h2><dl COMPACT><dt>LTYPE
</dt><dd>(Integer, Input) - The type of polyline to be drawn. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>&lt; 0
</dt><dd>Implementation dependent (not used in NCAR GKS-0A)
</dd><dt>1
</dt><dd>Solid line (default)
</dd><dt>2
</dt><dd>Dashed line
</dd><dt>3
</dt><dd>Dotted line
</dd><dt>4
</dt><dd>Dashed dotted line
</dd><dt>&ge; 5
</dt><dd>Reserved for registration or future standardization (not used in NCAR GKS-0A)</dd></dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpl, gslwsc, gscr, gsplci, gqln, gqlwsc, gqplci, dashline, gset_linetype 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_gsfasi(3)"
name: "ncl_gsfasi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsfasi/"
---

GSFASI (Set fill are style index) - sets the fill area style index.
<h2>Synopsis</h2>CALL GSFASI (STYLI)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_fill_style_ind(Gint fill_style_ind);
<h2>Description</h2><dl COMPACT><dt>STYLI
</dt><dd>(Integer, Input) - Specifies workstation-dependent options for hatch or pattern fills. Pattern fill options are not supported in NCAR Graphics. Hatch fill options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>1
</dt><dd>Horizontal lines (default)
</dd><dt>2
</dt><dd>Vertical lines
</dd><dt>3
</dt><dd>Lines of positive slope
</dd><dt>4
</dt><dd>Lines of negative slope
</dd><dt>5
</dt><dd>Horizontal and vertical lines
</dd><dt>6
</dt><dd>Lines of positive and negative slope
</dd><dl COMPACT><dd></dd></dl></dl>
</dl></dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gfa, gsfais, gscr, gsfaci, gqfais, gqfasi, areas, gset_fill_style_ind 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

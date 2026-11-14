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
<dd>(Integer, Input) - Specifies workstation-dependent options for hatch or pattern fills. Pattern fill options are not supported in NCAR Graphics. Hatch fill options are:
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>Horizontal lines (default)
<dt>2
<dd>Vertical lines
<dt>3
<dd>Lines of positive slope
<dt>4
<dd>Lines of negative slope
<dt>5
<dd>Horizontal and vertical lines
<dt>6
<dd>Lines of positive and negative slope
<dl COMPACT><dd></dl></dl>
</dl></dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gfa, gsfais, gscr, gsfaci, gqfais, gqfasi, areas, gset_fill_style_ind 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

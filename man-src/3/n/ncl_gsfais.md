---
title: "ncl_gsfais(3)"
name: "ncl_gsfais"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsfais/"
---

GSFAIS (Set fill area interior style) - sets the fill style of polygons drawn with GFA.
<h2>Synopsis</h2>CALL GSFAIS (INTS)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_fill_int_style(Gfill_int_style fill_int_style);
<h2>Description</h2><dl COMPACT><dt>INTS
</dt><dd>(Integer, Input) - Gives the style of fill to be used in subsequent calls to the GFA output primitive. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>Hollow fill (the default)
</dd><dt>1
</dt><dd>Solid fill
</dd><dt>2
</dt><dd>Pattern fill (not implemented in NCAR GKS).
</dd><dt>3
</dt><dd>Hatch fill</dd></dl></dl>
</dl><h2>Usage</h2>For fill style &quot;Hatch&quot;, GSFASI should be used to specify the type of hatch pattern used (horizontal lines, vertical lines, etc.) 

 Note: If you call GFA and generate an output graphic only to find that you have a closed curve with no fill, you probably have allowed the fill choice to default to hollow fill (no fill).
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gfa, gsfasi, gscr, gsfaci, gqfais, gqfasi, areas, gset_fill_int_style 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_gqfasi(3)"
name: "ncl_gqfasi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqfasi/"
---

GQFASI (Inquire fill area style index) - retrieves the current value of the fill area style index.
<h2>Synopsis</h2>CALL GQFASI (ERRIND, STYLI)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_fill_style_ind(Gint *err_ind, Gint *fill_style_ind);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>STYLI
<dd>(Integer, Output) - Returns the fill area style index as set by default or by a call to GSFASI.
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
<dd>Lines of positive and negative slope</dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gfa, gsfais, gscr, gsfaci, gqfais, gqfasi, areas, ginq_fill_style_ind 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

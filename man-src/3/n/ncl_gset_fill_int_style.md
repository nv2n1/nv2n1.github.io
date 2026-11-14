---
title: "ncl_gset_fill_int_style(3)"
name: "ncl_gset_fill_int_style"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_fill_int_style/"
description: "gset_fill_int_style (Set fill area interior style) – sets the fill style of polygons drawn with gfill_area."
---

<p>gset_fill_int_style (Set fill area interior style) &#8211; sets the fill style of polygons drawn with gfill_area.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_fill_int_style(Gfill_int_style fill_int_style);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>fill_int_style</p>
<dd>(Input) &#8211; Gives the style of fill to be used in subsequent calls to the gfill_area output primitive. Options are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GSTYLE_HOLLOW</p>
<dd>Hollow fill (the default)</p>
<dt>GSTYLE_SOLID</p>
<dd>Solid fill</p>
<dt>GSTYLE_PAT</p>
<dd>Pattern fill (not implemented in NCAR GKS).</p>
<dt>GSTYLE_HATCH</p>
<dd>Hatch fill</dl>
</dl>
</dl>
<h2>Usage</h2>
<p>For fill style &quot;Hatch&quot;, gset_fill_style_ind should be used to specify the type of hatch pattern used (horizontal lines, vertical lines, etc.) </p>
<p> Note: If you call gfill_area and generate an output graphic only to find that you have a closed curve with no fill, you probably have allowed the fill choice to default to hollow fill (no fill).</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gfill_area(3NCARG),</code> <code>gset_fill_style_ind(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>areas(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

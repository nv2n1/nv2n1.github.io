---
title: "ncl_gset_linetype(3)"
name: "ncl_gset_linetype"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_linetype/"
description: "gset_linetype (Set line type) – sets the line type to solid or various dashed patterns."
---

<p>gset_linetype (Set line type) &#8211; sets the line type to solid or various dashed patterns.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_linetype(Gint linetype);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>linetype</p>
<dd>(Input) &#8211; The type of polyline to be drawn. Options are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&lt; 0</p>
<dd>Implementation dependent (not used in NCAR GKS-0A)</p>
<dt>1</p>
<dd>Solid line (default)</p>
<dt>2</p>
<dd>Dashed line</p>
<dt>3</p>
<dd>Dotted line</p>
<dt>4</p>
<dd>Dashed dotted line</p>
<dt>&ge; 5</p>
<dd>Reserved for registration or future standardization (not used in NCAR GKS-0A)</dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gpolyline(3NCARG),</code> <code>gset_linewidth(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>ginq_linetype(3NCARG),</code> <code>ginq_linewidth(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>dashline(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

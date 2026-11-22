---
title: "ncl_gset_fill_style_ind(3)"
name: "ncl_gset_fill_style_ind"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_fill_style_ind/"
description: "gset_fill_style_ind (Set fill are style index) – sets the fill area style index."
---

<p>gset_fill_style_ind (Set fill are style index) &#8211; sets the fill area style index.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_fill_style_ind(Gint fill_style_ind);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>fill_style_ind</dt>
<dd>(Input) &#8211; Specifies workstation-dependent options for hatch or pattern fills. Pattern fill options are not supported in NCAR Graphics. Hatch fill options are:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>1</dt>
<dd>Horizontal lines (default)</dd>
<dt>2</dt>
<dd>Vertical lines</dd>
<dt>3</dt>
<dd>Lines of positive slope</dd>
<dt>4</dt>
<dd>Lines of negative slope</dd>
<dt>5</dt>
<dd>Horizontal and vertical lines</dd>
<dt>6</dt>
<dd>Lines of positive and negative slope</dd>
<dl COMPACT>
<dd></dd></dl>
</dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gfill_area(3NCARG),</code> <code>gset_fill_int_style(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>areas(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br/>
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement.</p>

---
title: "ncl_ginq_fill_style_ind(3)"
name: "ncl_ginq_fill_style_ind"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_fill_style_ind/"
description: "ginq_fill_style_ind (Inquire fill area style index) – retrieves the current value of the fill area style index."
---

<p>ginq_fill_style_ind (Inquire fill area style index) &#8211; retrieves the current value of the fill area style index.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_fill_style_ind(Gint *err_ind, Gint *fill_style_ind);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</dt>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</dd>
<dt>fill_style_ind</dt>
<dd>(Output) &#8211; Returns the fill area style index as set by default or by a call to gset_fill_style_ind.</dd>
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
<dd>Lines of positive and negative slope</dd></dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gfill_area(3NCARG),</code> <code>gset_fill_int_style(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>areas(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

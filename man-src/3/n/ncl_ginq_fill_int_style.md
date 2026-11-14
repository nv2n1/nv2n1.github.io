---
title: "ncl_ginq_fill_int_style(3)"
name: "ncl_ginq_fill_int_style"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_fill_int_style/"
description: "ginq_fill_int_style (Inquire fill area interior style) – retrieves the current value for fill area interior style."
---

<p>ginq_fill_int_style (Inquire fill area interior style) &#8211; retrieves the current value for fill area interior style.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_fill_int_style(Gint *err_ind, Gfill_int_style *fill_int_style);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>fill_int_style</p>
<dd>(Output) &#8211; Returns the current value for fill style as set by default or by a call to gset_fill_int_style. Possible return values include:</p>
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
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gfill_area(3NCARG),</code> <code>gset_fill_int_style(3NCARG),</code> <code>gset_fill_style_ind(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>areas(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

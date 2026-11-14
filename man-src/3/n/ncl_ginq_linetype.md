---
title: "ncl_ginq_linetype(3)"
name: "ncl_ginq_linetype"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_linetype/"
description: "ginq_linetype (Inquire line type) – retrieves the current setting for linetype."
---

<p>ginq_linetype (Inquire line type) &#8211; retrieves the current setting for linetype.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_linetype(Gint *err_ind, Gint *linetype);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>linetype</p>
<dd>(Output) &#8211; Returns the current value for the line type as set by default or by a call to gset_linetype.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1</p>
<dd>Solid</p>
<dt>2</p>
<dd>Dashed</p>
<dt>3</p>
<dd>Dotted</p>
<dt>4</p>
<dd>Dot-dash</dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gpolyline(3NCARG),</code> <code>gset_linetype(3NCARG),</code> <code>gset_linewidth(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>ginq_linewidth(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>dashline(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

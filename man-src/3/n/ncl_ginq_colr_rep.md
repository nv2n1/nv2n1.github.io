---
title: "ncl_ginq_colr_rep(3)"
name: "ncl_ginq_colr_rep"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_colr_rep/"
description: "ginq_colr_rep (Inquire color representation) – retrieves the color value associated with a color index on a particular workstation."
---

<p>ginq_colr_rep (Inquire color representation) &#8211; retrieves the color value associated with a color index on a particular workstation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_colr_rep(Gint ws_id, Gint colr_ind, Ginq_type type, Gint *err_ind, Gcolr_rep *colr_rep);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) &#8211; Gives a workstation identifier as was set in a previous call to gopen_ws.</p>
<dt>colr_ind</p>
<dd>(Input) &#8211; A color index.</p>
<dt>type</p>
<dd>(Input) &#8211; Specifies whether the returned color values are the ones that were specified by a call to gset_colr_rep or whether they are the color values that are actually being used on the specified workstation (frequently a workstation will not be able to represent a requested color value precisely).</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GINQ_SET</p>
<dd>Returns the color value set for index colr_ind either by default or by a call to gset_colr_rep.</p>
<dt>GINQ_REALIZED</p>
<dd>Returns the color value actually used by the workstation to represent the requested color.</dl>
</dl>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired values cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>colr_rep.rgb.red</p>
<dd>(Gfloat, Output) &#8211; Returns an intensity value for red in the range 0. to 1. inclusive.</p>
<dt>colr_rep.rgb.green</p>
<dd>(Gfloat, Output) &#8211; Returns an intensity value for green in the range 0. to 1. inclusive.</p>
<dt>colr_rep.rgb.blue</p>
<dd>(Gfloat, Output) &#8211; Returns an intensity value for blue in the range 0. to 1. inclusive.</dl>
<h2>Usage</h2>
<p>For details on setting and using color indices see the man page for gset_colr_rep.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_colr_rep(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>gset_marker_size(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

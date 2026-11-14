---
title: "ncl_gset_colr_rep(3)"
name: "ncl_gset_colr_rep"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_colr_rep/"
description: "gset_colr_rep (Set color representation) – associates a color value with a color index."
---

<p>gset_colr_rep (Set color representation) &#8211; associates a color value with a color index.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_colr_rep(Gint ws_id, Gint colr_ind, const Gcolr_rep *colr_rep);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) &#8211; A workstation identifier. ws_id must be the same as that used in some previous gopen_ws call.</p>
<dt>colr_ind</p>
<dd>(Input) &#8211; A color index.</p>
<dt>colr_rep.rgb.red</p>
<dd>(Gfloat, Input) &#8211; An intensity value for red between 0. and 1. inclusive.</p>
<dt>colr_rep.rgb.green</p>
<dd>(Gfloat, Input) &#8211; An intensity value for green between 0. and 1. inclusive.</p>
<dt>colr_rep.rgb.blue</p>
<dd>(Gfloat, Input) &#8211; An intensity value for blue between 0. and 1. inclusive.</dl>
<h2>Usage</h2>
<p>Color in GKS is &quot;indexed&quot;, i.e. color attributes are assigned to primitives by using a color index. The GKS function gset_colr_rep is used to associate a color value with color indices. </p>
<p> It is recommended that all color indices used in a given job be defined prior to calling any output primitive. Since the result of a dynamic color change can be ambiguous, it is also recommended that gset_colr_rep not be called to change a color value after the original definitions. </p>
<p> gset_colr_rep may be called after opening the workstation for which the color indices are to be defined, and not before that workstation is opened. Different color tables can be maintained for different workstations. For example, color index 2 for a CGM file may be associated with &quot;red&quot; while at the same time it may be associated with &quot;green&quot; for some X workstation. </p>
<p> It is important to stress that color index 0 defines the background color. If any color indices are defined, then you should define the background color index 0. Otherwise you run the risk of having a user-defined color match the default background color. </p>
<p> For all GKS output primitives, color is assigned by an indexing scheme. The indices run from 0 to 255, where 0 is the background color index and 1 is the foreground color index.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>ginq_colr_rep(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>gset_marker_colr_ind(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>ginq_marker_colr_ind(3NCARG),</code> <code>ginq_fill_colr_ind(3NCARG),</code> <code>ginq_text_colr_ind(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

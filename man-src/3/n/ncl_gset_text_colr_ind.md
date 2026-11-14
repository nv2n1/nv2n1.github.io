---
title: "ncl_gset_text_colr_ind(3)"
name: "ncl_gset_text_colr_ind"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_text_colr_ind/"
description: "gset_text_colr_ind (Set text color index) – sets the text color index."
---

<p>gset_text_colr_ind (Set text color index) &#8211; sets the text color index.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_text_colr_ind(Gint text_colr_ind);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>text_colr_ind</p>
<dd>(Input) A color index.</dl>
<h2>Usage</h2>
<p>All text strings drawn with calls to the gtext output primitive will be drawn with the color associated with index text_colr_ind until gset_text_colr_ind is called again and a new index is assigned. </p>
<p> For all GKS output primitives, color is assigned using a color index. The color indices run from 0 to 255, where 0 is the background color index and 1 is the foreground color index. Color values are associated with indices by calls to the GKS routine gset_colr_rep. If a color index is used that has no user-assigned color value set in a gset_colr_rep call, then a device-dependent color value will be assigned to that index.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

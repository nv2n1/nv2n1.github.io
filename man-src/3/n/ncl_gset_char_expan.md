---
title: "ncl_gset_char_expan(3)"
name: "ncl_gset_char_expan"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_char_expan/"
description: "gset_char_expan (Set character expansion factor) – sets the width to height ratio of text."
---

<p>gset_char_expan (Set character expansion factor) &#8211; sets the width to height ratio of text.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_char_expan(Gdouble char_expan);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>char_expan</p>
<dd>(Input) &#8211; Specifies a deviation of the width to height ratio for characters drawn using the GTX output primitive. char_expan of 10.0 would specify a character that is 10 times as wide as normal. char_expan of 0.1 would request characters that are 1/10th as wide as normal. The character height remains unchanged. char_expan &gt; 0. By default char_expan = 1.0</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

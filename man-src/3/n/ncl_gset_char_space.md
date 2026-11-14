---
title: "ncl_gset_char_space(3)"
name: "ncl_gset_char_space"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_char_space/"
description: "gset_char_space (Set character spacing) – sets the character spacing for text."
---

<p>gset_char_space (Set character spacing) &#8211; sets the character spacing for text.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_char_space(Gdouble char_space);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>char_space</p>
<dd>(Input) &#8211; Specifies how much additional white space should be inserted between characters drawn using the gtext output primitive. char_space is specified as a fraction of the character height. </p>
<p> A character spacing of zero positions the character body of each successive character contiguously with enough white space between them to produce pleasing normal spacing. A positive value inserts extra space between successive characters. A negative value causes successive characters to overlap. By default char_space = 0.0.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

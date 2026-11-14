---
title: "ncl_gtext(3)"
name: "ncl_gtext"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gtext/"
description: "gtext (Text) – The basic output primitive for drawing text. A number of attribute setting routines are available for selecting the size, font, precision, orientation, color, character spacing, etc."
---

<p>gtext (Text) &#8211; The basic output primitive for drawing text. A number of attribute setting routines are available for selecting the size, font, precision, orientation, color, character spacing, etc.</p>
<h2>Synopsis</h2>
<p>void gtext(const Gpoint *text_pos, const char *char_string);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>text_pos.x</p>
<dd>(Gfloat, Input) The x world coordinate of the text alignment of the first character in char_string.</p>
<dt>text_pos.y</p>
<dd>(Gfloat, Input) The y world coordinate of the text alignment of the first character in char_string.</p>
<dt>char_string</p>
<dd>(Input) The characters to be drawn.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

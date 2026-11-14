---
title: "ncl_gset_char_up_vec(3)"
name: "ncl_gset_char_up_vec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_char_up_vec/"
description: "gset_char_up_vec (Set character up vector) – specifies the angle at which subsequent text is to be drawn with gtext."
---

<p>gset_char_up_vec (Set character up vector) &#8211; specifies the angle at which subsequent text is to be drawn with gtext.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_char_up_vec(const Gvec *char_up_vec);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>char_up_vec.delta_x</p>
<dd>(Gfloat, Input) &#8211; Gives the X (horizontal) world coordinate of a vector.</p>
<dt>char_up_vec.delta_y</p>
<dd>(Gfloat, Input) &#8211; Gives the Y (vertical) world coordinate of a vector.</dl>
<h2>Usage</h2>
<p>The coordinates (char_up_vec.delta_x, char_up_vec.delta_y) relative to the point (0.,0.) establish a vector direction. This direction specifies the up direction of individual characters. This direction also specifies the orientation of a text string in that the characters in a string are placed along a line perpendicular to the character up vector. By default the character up vector is (0.,1.) so that characters are drawn in their normal horizontal orientation. The magnitude of the up vector is not used so that (0.,23.) is the same as (0.,1.).</p>
<h2>Examples</h2>
<pre> char_up_vec.delta_x = -1.
 char_up_vec.delta_y = 0.
 gset_char_up_vec(&amp;char_up_vec);</pre>
<p>would specify the character up vector as (-1.,0.) and subsequent text written with gtext would be rotated 90 degrees from normal and would be appropriate for a Y-axis label. </p>
<pre> char_up_vec.delta_x = 1.
 char_up_vec.delta_y = 1..
 gset_char_up_vec(&amp;char_up_vec);</pre>
<p>would specify the character up vector as (1.,1.) and subsequent text written with gtext would be rotated -45 degress from normal.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

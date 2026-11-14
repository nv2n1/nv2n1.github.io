---
title: "ncl_ginq_char_up_vec(3)"
name: "ncl_ginq_char_up_vec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_char_up_vec/"
description: "ginq_char_up_vec (Inquire character up vector) – retrieves the current value of the character up vector."
---

<p>ginq_char_up_vec (Inquire character up vector) &#8211; retrieves the current value of the character up vector.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_char_up_vec(Gint *err_ind, Gvec *char_up_vec);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired values cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>char_up_vec.delta_x</p>
<dd>(Gfloat, Output) &#8211; Gives the X world coordinate of a the up vector.</p>
<dt>char_up_vec.delta_y</p>
<dd>(Gfloat, Output) &#8211; Gives the Y world coordinate of a the up vector.</dl>
<h2>Usage</h2>
<p>The up vector is that vector formed by the two coordinate points (0.,0.) and (char_up_vec.delta_x,char_up_vec.delta_y). See gset_char_up_vec for more details on the meaning of the character up vector.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

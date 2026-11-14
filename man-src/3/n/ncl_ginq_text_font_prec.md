---
title: "ncl_ginq_text_font_prec(3)"
name: "ncl_ginq_text_font_prec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_text_font_prec/"
description: "ginq_text_font_prec (Inquire text font and precision) – retrieves the current setting of the text font and precision values."
---

<p>ginq_text_font_prec (Inquire text font and precision) &#8211; retrieves the current setting of the text font and precision values.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_text_font_prec(Gint *err_ind, Gtext_font_prec *text_font_prec);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired values cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>text_font_prec.font</p>
<dd>(Output) &#8211; Gives the font number as set by default or by a call to gset_text_font_prec. Font number one is a simple default ASCII font. Values for font between -2 and -20 (inclusive) are Hershey fonts.</p>
<dt>text_font_prec.prec</p>
<dd>(Output) &#8211; Gives the text precision as set by default or by a call to gset_text_font_prec. Possible values include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GPREC_STRING</p>
<dd>String precision (good)</p>
<dt>GPREC_CHAR</p>
<dd>Character precision (better)</p>
<dt>GPREC_STROK</p>
<dd>Stroke precision (best)</dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

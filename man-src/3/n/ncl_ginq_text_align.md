---
title: "ncl_ginq_text_align(3)"
name: "ncl_ginq_text_align"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_text_align/"
description: "ginq_text_align (Inquire text alignment) – retrieves the horizontal and vertical text alignments."
---

<p>ginq_text_align (Inquire text alignment) &#8211; retrieves the horizontal and vertical text alignments.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_text_align(Gint *err_ind, Gtext_align *text_align);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired values cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>text_align.hor</p>
<dd>(Output) &#8211; Returns the current horizontal text alignment:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GHOR_NORM</p>
<dd>Normal (default)</p>
<dt>GHOR_LEFT</p>
<dd>Left</p>
<dt>GHOR_CTR</p>
<dd>Center</p>
<dt>GHOR_RIGHT</p>
<dd>Right</dl>
</dl>
<dt>text_align.vert</p>
<dd>(Output) &#8211; Returns the current vertical text alignment:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GVERT_NORM</p>
<dd>Normal (default)</p>
<dt>GVERT_TOP</p>
<dd>Top</p>
<dt>GVERT_CAP</p>
<dd>Cap</p>
<dt>GVERT_HALF</p>
<dd>Half</p>
<dt>GVERT_BASE</p>
<dd>Base</p>
<dt>GVERT_BOTTOM</p>
<dd>Bottom</dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>ngdots(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

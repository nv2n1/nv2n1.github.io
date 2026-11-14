---
title: "ncl_ginq_text_path(3)"
name: "ncl_ginq_text_path"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_text_path/"
description: "ginq_text_path (Inquire text path) – retrieves the current text path."
---

<p>ginq_text_path (Inquire text path) &#8211; retrieves the current text path.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_text_path(Gint *err_ind, Gtext_path *text_path);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>text_path</p>
<dd>(Output) &#8211; Returns the current text path as set by default or by a call to gset_text_path. Legal values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GPATH_RIGHT</p>
<dd>Draw successive characters in the string such that character n+l appears to the right of character n. This is text path &quot;right&quot; and is the default.</p>
<dt>GPATH_LEFT</p>
<dd>Draw character n+1 to the left of character n. This is text path &quot;left&quot;.</p>
<dt>GPATH_UP</p>
<dd>Draw character n+1 above character n. This is text path &quot;up&quot;.</p>
<dt>GPATH_DOWN</p>
<dd>Draw character n+1 below character n. This is text path &quot;down&quot;.</dl>
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

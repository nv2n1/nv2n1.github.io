---
title: "ncl_gset_text_path(3)"
name: "ncl_gset_text_path"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_text_path/"
description: "gset_text_path (Set text path) – sets the text paths or directions in which text is to be drawn."
---

<p>gset_text_path (Set text path) &#8211; sets the text paths or directions in which text is to be drawn.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_text_path(Gtext_path text_path);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>text_path</p>
<dd>(Input) Gives the direction in which a character string is to be drawn. Options are:</p>
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
<p> The right, left, up, and down directions are relative to the character up vector. The right text path direction is perpendicular to the up vector direction. Thus, to draw a text string at a 45 degree angle the character up vector would be (-1,1), and the text path would be right .</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG)</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

---
title: "ncl_ginq_asfs(3)"
name: "ncl_ginq_asfs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_asfs/"
description: "ginq_asfs – (Inquire aspect source flags) – Inquires the values for the aspect source flags that determine whether primitive attributes are to be selected from individual settings or from \"bundle t..."
---

<p>ginq_asfs &#8211; (Inquire aspect source flags) &#8211; Inquires the values for the aspect source flags that determine whether primitive attributes are to be selected from individual settings or from &quot;bundle tables&quot;.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_asfs(Gint *err_ind, Gasfs *list_asf);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</dt>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</dd>
<dt>list_asf</dt>
<dd>(Output) &#8211; A structure of settings for the thirteen attributes:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>list_asfs.linetype</dt>
<dd>Linetype</dd>
<dt>list_asfs.linewidth</dt>
<dd>Linewidth scale factor</dd>
<dt>list_asfs.line_colr_ind</dt>
<dd>Polyline color index</dd>
<dt>list_asfs.marker_type</dt>
<dd>Marker type</dd>
<dt>list_asfs.marker_size</dt>
<dd>Marker size scale factor</dd>
<dt>list_asfs.marker_colr_ind</dt>
<dd>Polymarker color index</dd>
<dt>list_asfs.text_font_prec</dt>
<dd>Text font and precision</dd>
<dt>list_asfs.char_expan</dt>
<dd>Character expansion factor</dd>
<dt>list_asfs.char_space</dt>
<dd>Character spacing</dd>
<dt>list_asfs.text_colr_ind</dt>
<dd>Text color index</dd>
<dt>list_asfs.fill_int_style</dt>
<dd>Fill area interior style</dd>
<dt>list_asfs.fill_style_ind</dt>
<dd>Fill area style index</dd>
<dt>list_asfs.fill_colr_ind</dt>
<dd>Fill area color index</dd></dl>
</dl>
<p> Each value of list_asf is either GASF_BUNDLED(for &quot;bundled&quot;) or GASF_INDIV (for &quot;individual&quot;).</dl>
<h2>Usage</h2>
<p>In NCAR Graphics all attribute aspect source flags are defaulted to &quot;individual&quot; (all values for list_asf are GASF_INDIV). It is advised that for dependable results when using NCAR Graphics these values remain in their default settings. Some GKS packages default these values to &quot;bundled&quot;. ginq_asfs can be called to determine the values of all aspect source flags.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_asfs(3NCARG),</code> <code>gset_linetype(3NCARG),</code> <code>gset_linewidth(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>gset_marker_type(3NCARG),</code> <code>gset_marker_size(3NCARG),</code> <code>gset_marker_colr_ind(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>gset_fill_int_style(3NCARG),</code> <code>gset_fill_style_ind(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_linetype(3NCARG),</code> <code>ginq_linewidth(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>ginq_marker_type(3NCARG),</code> <code>ginq_marker_size(3NCARG),</code> <code>ginq_marker_colr_ind(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_text_colr_ind(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>ginq_fill_colr_ind(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br/>
 University Corporation for Atmospheric Research<br/>
 The use of this Software is governed by a License Agreement.</p>
</p>
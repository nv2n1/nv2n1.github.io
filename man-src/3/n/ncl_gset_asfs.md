---
title: "ncl_gset_asfs(3)"
name: "ncl_gset_asfs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_asfs/"
description: "gset_asfs – (Set aspect source flags) – Sets the aspect source flags that determine whether primitive attributes are to be selected from individual settings or from \"bundle tables\"."
---

<p>gset_asfs &#8211; (Set aspect source flags) &#8211; Sets the aspect source flags that determine whether primitive attributes are to be selected from individual settings or from &quot;bundle tables&quot;.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_asfs(const Gasfs *list_asf);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>list_asf</p>
<dd>(input) &#8211; A structure of settings for the thirteen attributes:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>list_asfs.linetype</p>
<dd>Linetype</p>
<dt>list_asfs.linewidth</p>
<dd>Linewidth scale factor</p>
<dt>list_asfs.line_colr_ind</p>
<dd>Polyline color index</p>
<dt>list_asfs.marker_type</p>
<dd>Marker type</p>
<dt>list_asfs.marker_size</p>
<dd>Marker size scale factor</p>
<dt>list_asfs.marker_colr_ind</p>
<dd>Polymarker color index</p>
<dt>list_asfs.text_font_prec</p>
<dd>Text font and precision</p>
<dt>list_asfs.char_expan</p>
<dd>Character expansion factor</p>
<dt>list_asfs.char_space</p>
<dd>Character spacing</p>
<dt>list_asfs.text_colr_ind</p>
<dd>Text color index</p>
<dt>list_asfs.fill_int_style</p>
<dd>Fill area interior style</p>
<dt>list_asfs.fill_style_ind</p>
<dd>Fill area style index</p>
<dt>list_asfs.fill_colr_ind</p>
<dd>Fill area color index</dl>
</dl>
<p> Each value of list_asf is of either GASF_BUNDLED (for &quot;bundled&quot;) or GASF_INDIV (for &quot;individual&quot;).</dl>
<h2>Usage</h2>
<p>In NCAR Graphics all attribute aspect source flags are defaulted to GASF_INDIV (all values for list_asf are &quot;1&quot;). It is advised that for dependable results when using NCAR Graphics these values remain in their default settings. Some GKS packages default these values to GASF_BUNDLED, so, if one expects to use such a package, it would be precautionary to call gset_asfs to set all aspect source flags to GASF_INDIV before calling other GKS functions.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>ginq_asfs(3NCARG),</code> <code>gset_linetype(3NCARG),</code> <code>gset_linewidth(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>gset_marker_type(3NCARG),</code> <code>gset_marker_size(3NCARG),</code> <code>gset_marker_colr_ind(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_text_font_prec(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>gset_fill_int_style(3NCARG),</code> <code>gset_fill_style_ind(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_linetype(3NCARG),</code> <code>ginq_linewidth(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>ginq_marker_type(3NCARG),</code> <code>ginq_marker_size(3NCARG),</code> <code>ginq_marker_colr_ind(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_text_colr_ind(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>ginq_fill_colr_ind(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

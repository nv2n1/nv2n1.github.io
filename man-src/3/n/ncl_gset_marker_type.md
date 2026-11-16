---
title: "ncl_gset_marker_type(3)"
name: "ncl_gset_marker_type"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_marker_type/"
description: "gset_marker_type (Set marker type) – sets the type of polymarker to be used in subsequent GPM calls."
---

<p>gset_marker_type (Set marker type) &#8211; sets the type of polymarker to be used in subsequent GPM calls.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_marker_type(Gint marker_type);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>marker_type</dt>
<dd>(Input) &#8211; Selects the type of marker to be drawn. Options are:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>&lt; 0</dt>
<dd>implementation dependent (not used in NCAR GKS-0A)</dd>
<dt> 1</dt>
<dd>&nbsp;<wbr>.&nbsp;<wbr>(dot)</dd>
<dt> 2</dt>
<dd>&nbsp;<wbr>+&nbsp;<wbr>(plus)</dd>
<dt> 3</dt>
<dd>&nbsp;<wbr>*&nbsp;<wbr>(asterisk)&nbsp;<wbr>This is the default</dd>
<dt> 4</dt>
<dd>&nbsp;<wbr>o&nbsp;<wbr>(circle)</dd>
<dt> 5</dt>
<dd>&nbsp;<wbr>X&nbsp;<wbr>(cross)</dd>
<dt>&ge; 6</dt>
<dd>&nbsp;<wbr>reserved for registration or future standardization</dd></dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gpolymarker(3NCARG),</code> <code>gset_marker_size(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_marker_colr_ind(3NCARG),</code> <code>ginq_marker_type(3NCARG),</code> <code>ginq_marker_size(3NCARG),</code> <code>ginq_marker_colr_ind(3NCARG),</code> <code>point(3NCARG),</code> <code>points(3NCARG),</code> <code>ngdots(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

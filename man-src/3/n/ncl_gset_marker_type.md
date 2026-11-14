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
<dt>marker_type</p>
<dd>(Input) &#8211; Selects the type of marker to be drawn. Options are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&lt; 0</p>
<dd>implementation dependent (not used in NCAR GKS-0A)</p>
<dt> 1</p>
<dd>&nbsp;<wbr>.&nbsp;<wbr>(dot)</p>
<dt> 2</p>
<dd>&nbsp;<wbr>+&nbsp;<wbr>(plus)</p>
<dt> 3</p>
<dd>&nbsp;<wbr>*&nbsp;<wbr>(asterisk)&nbsp;<wbr>This is the default</p>
<dt> 4</p>
<dd>&nbsp;<wbr>o&nbsp;<wbr>(circle)</p>
<dt> 5</p>
<dd>&nbsp;<wbr>X&nbsp;<wbr>(cross)</p>
<dt>&ge; 6</p>
<dd>&nbsp;<wbr>reserved for registration or future standardization</dl>
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

---
title: "ncl_gset_clip_ind(3)"
name: "ncl_gset_clip_ind"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_clip_ind/"
description: "gset_clip_ind (Set clipping indicator) – controls whether data are displayed outside the boundaries of the world coordinate window of the current normalization transformation."
---

<p>gset_clip_ind (Set clipping indicator) &#8211; controls whether data are displayed outside the boundaries of the world coordinate window of the current normalization transformation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_clip_ind(Gclip_ind clip_ind);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>clip_ind</p>
<dd>(Input) &#8211; A flag to turn clipping on or off.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GIND_NO_CLIP</p>
<dd>Clipping is off. Data outside of the window will be plotted.</p>
<dt>GIND_CLIP</p>
<dd>Clipping is on. Data outside of the window will not be plotted. This is the default.</dl>
</dl>
</dl>
<h2>Usage</h2>
<p>If the clipping indicator is off, and you make GKS output calls to plot world coordinate data outside your defined world coordinate window (and your viewport is smaller than the full plotting surface), those data will appear with your plot. If the clipping indicator is on, the data will be clipped to fit your window.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>set(3NCARG),</code> <code>gsup(3NCARG),</code> <code>gset_win(3NCARG),</code> <code>gsel_norm_tran(3NCARG),</code> <code>ginq_clip(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

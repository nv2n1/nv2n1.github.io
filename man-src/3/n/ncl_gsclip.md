---
title: "ncl_gsclip(3)"
name: "ncl_gsclip"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsclip/"
---

GSCLIP (Set clipping indicator) - controls whether data are displayed outside the boundaries of the world coordinate window of the current normalization transformation.
<h2>Synopsis</h2>CALL GSCLIP (ICLIP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_clip_ind(Gclip_ind clip_ind);
<h2>Description</h2><dl COMPACT><dt>ICLIP
<dd>(Integer, Input) - A flag to turn clipping on or off.
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Clipping is off. Data outside of the window will be plotted.
<dt>1
<dd>Clipping is on. Data outside of the window will not be plotted. This is the default.</dl></dl>
</dl><h2>Usage</h2>If the clipping indicator is off, and you make GKS output calls to plot world coordinate data outside your defined world coordinate window (and your viewport is smaller than the full plotting surface), those data will appear with your plot. If the clipping indicator is on, the data will be clipped to fit your window.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: set, gsup, gswn, gselnt, gqclip, gset_clip_ind 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "xtaddexposuretoregion(3)"
name: "xtaddexposuretoregion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaddexposuretoregion/"
description: "XtAddExposureToRegion – merge exposure events into a region"
---

<p>XtAddExposureToRegion &#8211; merge exposure events into a region </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAddExposureToRegion(XEvent *<i>event</i>, Region <i>region</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>event</i></p>
<dd>Specifies a pointer to the <code>Expose</code> or <code>GraphicsExpose</code> event.</p>
<dt><i>region</i></p>
<dd>Specifies the region object (as defined in <code>&lt;X11/Xutil.h&gt;</code>).</dl>
<h2>Description</h2>
<p>The <code>XtAddExposureToRegion</code> function computes the union of the rectangle defined by the exposure event and the specified region. Then, it stores the results back in region. If the event argument is not an <code>Expose</code> or <code>GraphicsExpose</code> event, <code>XtAddExposureToRegion</code> returns without an error and without modifying region. </p>
<p> This function is used by the exposure compression mechanism (see Section 7.9.3).</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

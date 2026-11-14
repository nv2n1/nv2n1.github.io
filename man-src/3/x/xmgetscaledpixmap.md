---
title: "xmgetscaledpixmap(3)"
name: "xmgetscaledpixmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetscaledpixmap/"
description: "XmGetScaledPixmap — read a pixmap file and scale it according to pixmap and print resolution"
---

<p><code>XmGetScaledPixmap</code> &#8212; read a pixmap file and scale it according to pixmap and print resolution</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XtEnum XmGetScaledPixmap</code>(
<code>Widget widget</code>,
<code>String image_name</code>,
<code>Pixel foreground</code>,
<code>Pixel background</code>,
<code>int depth</code>,
<code>Double scaling_ratio</code>);</pre>
<h2>Description</h2>
<p><code>XmGetScaledPixmap</code> uses its <code>Widget</code> argument to look up for a Print Shell ancestor to get the pixmap resolution and the default printer resolution information to be used if <code>scaling_ratio</code> <code>==0</code>. </p>
<p> If scaling is 0, and a valid PrintShell is present <code>XmGetScaledPixmap</code> applies a ratio equals to (printer resolution / default pixmap resolution) before creating the Pixmap on the widget&#8217;s Screen. Otherwise, the <code>scaling_ratio</code> is used in scaling both dimensions of the image being converted as a Pixmap. </p>
<p> <code>XmGetScaledPixmap</code> completes the <code>XmGetPixmapByDepth</code> existing API by making use of the <code>XmNdefaultPixmapResolution</code> of the rooting <code>XmPrintShell</code>. Refer to the <code>XmGetPixmapByDepth</code> documentation for details.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Widget used to determine the default pixmap resolution (of the print shell ancestor).</p>
<dt><i>image_name</i></p>
<dd>See XmGetPixmapByDepth for description.</p>
<dt><i>foreground</i></p>
<dd>See XmGetPixmapByDepth for description.</p>
<dt><i>background</i></p>
<dd>See XmGetPixmapByDepth for description.</p>
<dt><i>depth</i></p>
<dd>See XmGetPixmapByDepth for description.</p>
<dt><i>scaling_ratio</i></p>
<dd>Indicate the scaling ratio to be applied, or 0.</dl>
<h2>Return Value</h2>
<p>Returns Pixmap or NULL if failed.</p>
<h2>Errors/Warnings</h2>
<p>Same as for <code>XmGetPixmapByDepth</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmprintsetup/">XmPrintSetup</a></code>(3), <code><a href="/docs/linux/man/3-xmprintshell/">XmPrintShell</a></code>(3), <code><a href="/docs/linux/man/3-xmredisplaywidget/">XmRedisplayWidget</a></code>(3)</p>

---
title: "tk_getpixmap(3)"
name: "tk_getpixmap"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getpixmap/"
description: "Tk_GetPixmap, Tk_FreePixmap – allocate and free pixmaps"
---

<p>Tk_GetPixmap, Tk_FreePixmap &#8211; allocate and free pixmaps </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Pixmap
<code>Tk_GetPixmap(</code><i>display, d, width, height, depth</i><code>)</code>
<code>Tk_FreePixmap(</code><i>display, pixmap</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Display <i>*display</i> (in) X display for the pixmap.</p>
<dd>Drawable <i>d</i> (in) Pixmap or window where the new pixmap will be used for drawing.</p>
<dd>int <i>width</i> (in) Width of pixmap.</p>
<dd>int <i>height</i> (in) Height of pixmap.</p>
<dd>int <i>depth</i> (in) Number of bits per pixel in pixmap.</p>
<dd>Pixmap <i>pixmap</i> (in) Pixmap to destroy. </p>
</dl>
<h2>Description</h2>
<p>These procedures are identical to the Xlib procedures <code>XCreatePixmap</code> and <code>XFreePixmap</code>, except that they have extra code to manage X resource identifiers so that identifiers for deleted pixmaps can be reused in the future. It is important for Tk applications to use these procedures rather than <code>XCreatePixmap</code> and <code>XFreePixmap</code>; otherwise long-running applications may run out of resource identifiers. </p>
<p> <code>Tk_GetPixmap</code> creates a pixmap suitable for drawing in <i>d</i>, with dimensions given by <i>width</i>, <i>height</i>, and <i>depth</i>, and returns its identifier. <code>Tk_FreePixmap</code> destroys the pixmap given by <i>pixmap</i> and makes its resource identifier available for reuse. </p>
<h2>Keywords</h2>
<p>pixmap, resource identifier</p>

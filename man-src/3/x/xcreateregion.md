---
title: "xcreateregion(3)"
name: "xcreateregion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcreateregion/"
description: "XCreateRegion, XSetRegion, XDestroyRegion – create or destroy regions"
---

<p>XCreateRegion, XSetRegion, XDestroyRegion &#8211; create or destroy regions </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Region XCreateRegion(void);</p>
<dd>int XSetRegion(Display *<i>display</i>, GC <i>gc</i>, Region <i>r</i>);</p>
<dd>int XDestroyRegion(Region <i>r</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>r</i></p>
<dd>Specifies the region.</dl>
<h2>Description</h2>
<p>The <code>XCreateRegion</code> function creates a new empty region. </p>
<p> The <code>XSetRegion</code> function sets the clip-mask in the GC to the specified region. The region is specified relative to the drawable&#8217;s origin. The resulting GC clip origin is implementation-dependent. Once it is set in the GC, the region can be destroyed. </p>
<p> The <code>XDestroyRegion</code> function deallocates the storage associated with a specified region.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xemptyregion/">XEmptyRegion</a>(3), <a href="/docs/linux/man/3-xintersectregion/">XIntersectRegion</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

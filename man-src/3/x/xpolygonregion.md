---
title: "xpolygonregion(3)"
name: "xpolygonregion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xpolygonregion/"
description: "XPolygonRegion, XClipBox – generate regions"
---

<p>XPolygonRegion, XClipBox &#8211; generate regions </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Region XPolygonRegion(XPoint <i>points</i>[], int <i>n</i>, int <i>fill_rule</i>);</p>
<dd>int XClipBox(Region <i>r</i>, XRectangle *<i>rect_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>fill_rule</i></p>
<dd>Specifies the fill-rule you want to set for the specified GC. You can pass <code>EvenOddRule</code> or <code>WindingRule</code>.</p>
<dt><i>n</i></p>
<dd>Specifies the number of points in the polygon.</p>
<dt><i>points</i></p>
<dd>Specifies an array of points.</p>
<dt><i>r</i></p>
<dd>Specifies the region.</p>
<dt><i>rect_return</i></p>
<dd>Returns the smallest enclosing rectangle.</dl>
<h2>Description</h2>
<p>The <code>XPolygonRegion</code> function returns a region for the polygon defined by the points array. For an explanation of fill_rule, see <code>XCreateGC</code>. </p>
<p> The <code>XClipBox</code> function returns the smallest rectangle enclosing the specified region.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xdrawpoint/">XDrawPoint</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

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
<dd>Region XPolygonRegion(XPoint <i>points</i>[], int <i>n</i>, int <i>fill_rule</i>);</dd>
<dd>int XClipBox(Region <i>r</i>, XRectangle *<i>rect_return</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>fill_rule</i></dt>
<dd>Specifies the fill-rule you want to set for the specified GC. You can pass <code>EvenOddRule</code> or <code>WindingRule</code>.</dd>
<dt><i>n</i></dt>
<dd>Specifies the number of points in the polygon.</dd>
<dt><i>points</i></dt>
<dd>Specifies an array of points.</dd>
<dt><i>r</i></dt>
<dd>Specifies the region.</dd>
<dt><i>rect_return</i></dt>
<dd>Returns the smallest enclosing rectangle.</dd></dl>
<h2>Description</h2>
<p>The <code>XPolygonRegion</code> function returns a region for the polygon defined by the points array. For an explanation of fill_rule, see <code>XCreateGC</code>. </p>
<p> The <code>XClipBox</code> function returns the smallest rectangle enclosing the specified region.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xdrawpoint/">XDrawPoint</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3)<br/>
 <i>Xlib &#8211; C Language X Interface</i></p>

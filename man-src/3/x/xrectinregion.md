---
title: "xrectinregion(3)"
name: "xrectinregion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrectinregion/"
description: "XEmptyRegion, XEqualRegion, XPointInRegion, XRectInRegion – determine if regions are empty or equal"
---

<p>XEmptyRegion, XEqualRegion, XPointInRegion, XRectInRegion &#8211; determine if regions are empty or equal </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Bool XEmptyRegion(Region <i>r</i>);</p>
<dd>Bool XEqualRegion(Region <i>r1</i>, Region <i>r2</i>);</p>
<dd>Bool XPointInRegion(Region <i>r</i>, int <i>x</i>, int <i>y</i>);</p>
<dd>int XRectInRegion(Region <i>r</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>r</i></p>
<dd>Specifies the region.</p>
<dt><i>r1</i></p>
<dd>
<dt><i>r2</i></p>
<dd>Specify the two regions.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which define the rectangle.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which define the point or the coordinates of the upper-left corner of the rectangle.</dl>
<h2>Description</h2>
<p>The <code>XEmptyRegion</code> function returns <code>True</code> if the region is empty. </p>
<p> The <code>XEqualRegion</code> function returns <code>True</code> if the two regions have the same offset, size, and shape. </p>
<p> The <code>XPointInRegion</code> function returns <code>True</code> if the point (x, y) is contained in the region r. </p>
<p> The <code>XRectInRegion</code> function returns <code>RectangleIn</code> if the rectangle is entirely in the specified region, <code>RectangleOut</code> if the rectangle is entirely out of the specified region, and <code>RectanglePart</code> if the rectangle is partially in the specified region.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateregion/">XCreateRegion</a>(3), <a href="/docs/linux/man/3-xintersectregion/">XIntersectRegion</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

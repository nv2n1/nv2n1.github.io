---
title: "xintersectregion(3)"
name: "xintersectregion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xintersectregion/"
description: "XIntersectRegion, XUnionRegion, XUnionRectWithRegion, XSubtractRegion, XXorRegion, XOffsetRegion, XShrinkRegion – region arithmetic"
---

<p>XIntersectRegion, XUnionRegion, XUnionRectWithRegion, XSubtractRegion, XXorRegion, XOffsetRegion, XShrinkRegion &#8211; region arithmetic </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XIntersectRegion(Region <i>sra</i>, Region <i>srb</i>, Region <i>dr_return</i>);</p>
<dd>int XUnionRegion(Region <i>sra</i>, Region <i>srb</i>, Region <i>dr_return</i>);</p>
<dd>int XUnionRectWithRegion(XRectangle *<i>rectangle</i>, Region <i>src_region</i>, Region <i>dest_region_return</i>);</p>
<dd>int XSubtractRegion(Region <i>sra</i>, Region <i>srb</i>, Region <i>dr_return</i>);</p>
<dd>int XXorRegion(Region <i>sra</i>, Region <i>srb</i>, Region <i>dr_return</i>);</p>
<dd>int XOffsetRegion(Region <i>r</i>, int <i>dx</i>, int <i>dy</i>);</p>
<dd>int XShrinkRegion(Region <i>r</i>, int <i>dx</i>, int <i>dy</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dest_region_return</i></p>
<dd>Returns the destination region.</p>
<dt><i>dr_return</i></p>
<dd>Returns the result of the computation.</p>
<dt><i>dx</i></p>
<dd>
<dt><i>dy</i></p>
<dd>Specify the x and y coordinates, which define the amount you want to move or shrink the specified region.</p>
<dt><i>r</i></p>
<dd>Specifies the region.</p>
<dt><i>rectangle</i></p>
<dd>Specifies the rectangle.</p>
<dt><i>sra</i></p>
<dd>
<dt><i>srb</i></p>
<dd>Specify the two regions with which you want to perform the computation.</p>
<dt><i>src_region</i></p>
<dd>Specifies the source region to be used.</dl>
<h2>Description</h2>
<p>The <code>XIntersectRegion</code> function computes the intersection of two regions. </p>
<p> The <code>XUnionRegion</code> function computes the union of two regions. </p>
<p> The <code>XUnionRectWithRegion</code> function updates the destination region from a union of the specified rectangle and the specified source region. </p>
<p> The <code>XSubtractRegion</code> function subtracts srb from sra and stores the results in dr_return. </p>
<p> The <code>XXorRegion</code> function calculates the difference between the union and intersection of two regions. </p>
<p> The <code>XOffsetRegion</code> function moves the specified region by a specified amount. </p>
<p> The <code>XShrinkRegion</code> function reduces the specified region by a specified amount. Positive values shrink the size of the region, and negative values expand the region.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateregion/">XCreateRegion</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3), <a href="/docs/linux/man/3-xemptyregion/">XEmptyRegion</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

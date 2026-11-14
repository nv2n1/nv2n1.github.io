---
title: "xkbcomputeshapetop(3)"
name: "xkbcomputeshapetop"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbcomputeshapetop/"
description: "XkbComputeShapeTop – Determines the bounding box of the top surface of a shape"
---

<p>XkbComputeShapeTop &#8211; Determines the bounding box of the top surface of a shape </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbComputeShapeTop</code> <code>(XkbShapePtr </code><i>shape</i><code>,</code> <code>XkbBoundsPtr </code><i>bounds_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; shape</i></p>
<dd>
<dd>shape to be examined</p>
<dt><i>&#8211; bounds_rtrn</i></p>
<dd>backfilled with the bounding box for the shape</dl>
<h2>Description</h2>
<p>Xkb provides a number of convenience functions to help use a keyboard geometry. These include functions to return the bounding box of a shape&#8217;s top surface and to update the bounding box of a shape row or section. </p>
<p> A shape is made up of a number of outlines. Each outline is a polygon made up of a number of points. The bounding box of a shape is a rectangle that contains all the outlines of that shape. </p>
<p> <i>XkbComputeShapeTop </i> returns a BoundsRec that contains two x and y coordinates. These coordinates describe the corners of a rectangle that contains the outline that describes the top surface of the shape. The top surface is defined to be the approximating outline if the <i>approx </i> field of <i>shape </i> is not NULL. If <i>approx </i> is NULL, the top surface is defined as the last outline in the <i>shape&#8217;s </i> array of outlines. <i>XkbComputeShapeTop </i> returns False if <i>shape </i> is NULL or if there are no outlines for the shape; otherwise, it returns True.</p>
<h2>Structures</h2>
<pre>typedef struct _XkbBounds {
 short x1,y1; /* upper left corner of the bounds, in mm/10 */
 short x2,y2; /* lower right corner of the bounds, in mm/10 */
} XkbBoundsRec, *XkbBoundsPtr;</pre>

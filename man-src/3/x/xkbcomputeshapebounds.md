---
title: "xkbcomputeshapebounds(3)"
name: "xkbcomputeshapebounds"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbcomputeshapebounds/"
description: "XkbComputeShapeBounds – Updates the bounding box of a shape"
---

<p>XkbComputeShapeBounds &#8211; Updates the bounding box of a shape </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbComputeShapeBounds</code> <code>(XkbShapePtr </code><i>shape</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; shape</i></p>
<dd>
<dd>shape to be examined</dl>
<h2>Description</h2>
<p>Xkb provides a number of convenience functions to help use a keyboard geometry. These include functions to return the bounding box of a shape&#8217;s top surface and to update the bounding box of a shape row or section. </p>
<p> A shape is made up of a number of outlines. Each outline is a polygon made up of a number of points. The bounding box of a shape is a rectangle that contains all the outlines of that shape. </p>
<p> A ShapeRec contains a BoundsRec that describes the bounds of the shape. If you add or delete an outline to or from a shape, the bounding box must be updated. </p>
<p> <i>XkbComputeShapeBounds </i> updates the BoundsRec contained in the <i>shape </i> by examining all the outlines of the shape and setting the BoundsRec to the minimum x and minimum y, and maximum x and maximum y values found in those outlines. <i>XkbComputeShapeBounds </i> returns False if <i>shape </i> is NULL or if there are no outlines for the shape; otherwise, it returns True. </p>
<p> If you add or delete a key to or from a row, or if you update the shape of one of the keys in that row, you may need to update the bounding box of that row. To update the bounding box of a row, use <i>XkbComputeRowBounds.</i></p>
<h2>Structures</h2>
<pre>typedef struct _XkbShape {
 Atom name; /* shape's name */
 unsigned short num_outlines; /* number of outlines for the shape */
 unsigned short sz_outlines; /* size of the outlines array */
 XkbOutlinePtr outlines; /* array of outlines for the shape */
 XkbOutlinePtr approx; /* pointer into the array to the approximating outline */
 XkbOutlinePtr primary; /* pointer into the array to the primary outline */
 XkbBoundsRec bounds; /* bounding box for the shape; encompasses all outlines */
} XkbShapeRec, *XkbShapePtr;
typedef struct _XkbBounds {
 short x1,y1; /* upper left corner of the bounds, in mm/10 */
 short x2,y2; /* lower right corner of the bounds, in mm/10 */
} XkbBoundsRec, *XkbBoundsPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbcomputerowbounds/">XkbComputeRowBounds</a></code>(3)</p>

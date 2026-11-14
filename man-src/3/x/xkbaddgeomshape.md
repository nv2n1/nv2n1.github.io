---
title: "xkbaddgeomshape(3)"
name: "xkbaddgeomshape"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomshape/"
description: "XkbAddGeomShape – Add a shape to a keyboard geometry"
---

<p>XkbAddGeomShape &#8211; Add a shape to a keyboard geometry </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbShapePtr XkbAddGeomShape</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>int </code><i>sz_outlines</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry to be updated</p>
<dt><i>&#8211; name</i></p>
<dd>name of the new shape</p>
<dt><i>&#8211; sz_outlines</i></p>
<dd>number of outlines to be reserved</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> A geometry contains an arbitrary number of shapes, each of which is made up of an arbitrary number of outlines. <i>XkbAddGeomShape </i> adds a shape to a geometry <i>geom </i> by allocating space for <i>sz_outlines </i> outlines for it and giving it the name specified by <i>name. </i> If a shape with name <i>name </i> already exists in the geometry, a pointer to the existing shape is returned. <i>XkbAddGeomShape </i> returns NULL if any of the parameters is empty or if it was not able to allocate space. To allocate space for an arbitrary number of geometry shapes, use <i>XkbAllocGeomShapes.</i></p>
<h2>Structures</h2>
<pre> typedef struct _XkbShape {
 Atom name; /* shape's name */
 unsigned short num_outlines; /* number of outlines for the shape */
 unsigned short sz_outlines; /* size of the outlines array */
 XkbOutlinePtr outlines; /* array of outlines for the shape */
 XkbOutlinePtr approx; /* pointer into the array to the approximating outline */
 XkbOutlinePtr primary; /* pointer into the array to the primary outline */
 XkbBoundsRec bounds; /* bounding box for the shape; encompasses all outlines */
 } XkbShapeRec, *XkbShapePtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomshapes/">XkbAllocGeomShapes</a></code>(3)</p>

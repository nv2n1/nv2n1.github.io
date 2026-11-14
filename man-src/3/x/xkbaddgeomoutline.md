---
title: "xkbaddgeomoutline(3)"
name: "xkbaddgeomoutline"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomoutline/"
description: "XkbAddGeomOutline – Add one outline to an existing shape"
---

<p>XkbAddGeomOutline &#8211; Add one outline to an existing shape </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbOutlinePtr XkbAddGeomOutline</code> <code>(XkbShapePtr </code><i>shape</i><code>,</code> <code>int </code><i>sz_points</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; shape</i></p>
<dd>
<dd>shape to be updated</p>
<dt><i>&#8211; sz_points</i></p>
<dd>number of points to be reserved</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> An outline consists of an arbitrary number of points. <i>XkbAddGeomOutline </i> adds an outline to the specified <i>shape </i> by reserving <i>sz_points </i> points for it. The new outline is allocated and zeroed. <i>XkbAddGeomOutline </i> returns NULL if any of the parameters is empty or if it was not able to allocate space. To allocate space for an arbitrary number of outlines to a shape, use <i>XkbAllocGeomOutlines.</i></p>
<h2>Structures</h2>
<pre> typedef struct _XkbOutline {
 unsigned short num_points; /* number of points in the outline */
 unsigned short sz_points; /* size of the points array */
 unsigned short corner_radius; /* draw corners as circles with this radius */
 XkbPointPtr points; /* array of points defining the outline */
 } XkbOutlineRec, *XkbOutlinePtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomoutlines/">XkbAllocGeomOutlines</a></code>(3)</p>

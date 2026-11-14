---
title: "xkballocgeomshapes(3)"
name: "xkballocgeomshapes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeomshapes/"
description: "XkbAllocGeomShapes – Allocate space for an arbitrary number of geometry shapes"
---

<p>XkbAllocGeomShapes &#8211; Allocate space for an arbitrary number of geometry shapes </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeomShapes</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry for which shapes should be allocated</p>
<dt><i>&#8211; num_needed</i></p>
<dd>number of new shapes required</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeomShapes </i> allocates space for <i>num_needed </i> shapes in the specified geometry <i>geom. </i> The shapes are not initialized. </p>
<p> To free geometry shapes, use <i>XkbFreeGeomShapes.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreegeomshapes/">XkbFreeGeomShapes</a></code>(3)</p>

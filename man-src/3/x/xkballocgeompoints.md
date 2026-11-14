---
title: "xkballocgeompoints(3)"
name: "xkballocgeompoints"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeompoints/"
description: "XkbAllocGeomPoints – Allocate points in an outline"
---

<p>XkbAllocGeomPoints &#8211; Allocate points in an outline </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeomPoints</code> <code>(XkbOutlinePtr </code><i>outline</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; outline</i></p>
<dd>
<dd>outline for which points should be allocated</p>
<dt><i>&#8211; num_needed</i></p>
<dd>number of new points required</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeomPoints </i> allocates space for <i>num_needed </i> points in the specified <i>outline. </i> The points are not initialized.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>

---
title: "xkballocgeomoutlines(3)"
name: "xkballocgeomoutlines"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeomoutlines/"
description: "XkbAllocGeomOutlines – Allocate space for an arbitrary number of outlines to a shape"
---

<p>XkbAllocGeomOutlines &#8211; Allocate space for an arbitrary number of outlines to a shape </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeomOutlines</code> <code>(XkbShapePtr </code><i>shape</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; shape</i></p>
<dd>
<dd>shape for which outlines should be allocated</p>
<dt><i>&#8211; num_needed</i></p>
<dd>number of new outlines required</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeomOutlines </i> allocates space for <i>num_needed </i> outlines in the specified <i>shape. </i> The outlines are not initialized. </p>
<p> To free geometry outlines, use <i>XkbFreeGeomOutlines.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreegeomoutlines/">XkbFreeGeomOutlines</a></code>(3)</p>

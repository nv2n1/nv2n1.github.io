---
title: "xkballocgeomprops(3)"
name: "xkballocgeomprops"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeomprops/"
description: "XkbAllocGeomProps – Allocate geometry properties"
---

<p>XkbAllocGeomProps &#8211; Allocate geometry properties </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeomProps</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>_summary_</p>
<dt><i>&#8211; num_needed</i></p>
<dd>_summary_</dl>
<h2>Description</h2>
<dd>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeomProps </i> allocates space for <i>num_needed </i> properties and adds them to the specified geometry <i>geom. </i> No initialization of the properties is done. A geometry property associates an arbitrary string with an equally arbitrary name. Geometry properties can be used to provide hints to programs that display images of keyboards, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>

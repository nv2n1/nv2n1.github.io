---
title: "xkballocgeomsections(3)"
name: "xkballocgeomsections"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeomsections/"
description: "XkbAllocGeomSections – Allocate geometry sections"
---

<p>XkbAllocGeomSections &#8211; Allocate geometry sections </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeomSections</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry for which sections should be allocated</p>
<dt><i>&#8211; num_needed</i></p>
<dd>number of new sections required</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeomSections </i> allocates <i>num_needed </i> sections and adds them to the geometry <i>geom. </i> No initialization of the sections is done. </p>
<p> To free geometry sections, use <i>XkbFreeGeomSections.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreegeomsections/">XkbFreeGeomSections</a></code>(3)</p>

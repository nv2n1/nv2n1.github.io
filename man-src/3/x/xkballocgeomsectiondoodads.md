---
title: "xkballocgeomsectiondoodads(3)"
name: "xkballocgeomsectiondoodads"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeomsectiondoodads/"
description: "XkbAllocGeomSectionDoodads – Allocate doodads that are specific to a section"
---

<p>XkbAllocGeomSectionDoodads &#8211; Allocate doodads that are specific to a section </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeomSectionDoodads</code> <code>(XkbSectionPtr </code><i>section</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; section</i></p>
<dd>
<dd>section for which doodads should be allocated</p>
<dt><i>&#8211; num_needed</i></p>
<dd>number of new doodads required</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeomSectionDoodads </i> allocates <i>num_needed </i> doodads and adds them to the specified <i>section. </i> No initialization of the doodads is done. </p>
<p> To free geometry doodads, use <i>XkbFreeGeomDoodads.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreegeomdoodads/">XkbFreeGeomDoodads</a></code>(3)</p>

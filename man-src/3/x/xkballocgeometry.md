---
title: "xkballocgeometry(3)"
name: "xkballocgeometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocgeometry/"
description: "XkbAllocGeometry – Allocate an entire geometry"
---

<p>XkbAllocGeometry &#8211; Allocate an entire geometry </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocGeometry</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbGeometrySizesPtr </code><i>sizes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description for which geometry is to be allocated</p>
<dt><i>&#8211; sizes</i></p>
<dd>initial sizes for all geometry components</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> <i>XkbAllocGeometry </i> allocates a keyboard geometry and adds it to the keyboard description specified by <i>xkb. </i> The keyboard description should be obtained via the <i>XkbGetKeyboard </i> or <i>XkbAllocKeyboard </i> functions. The <i>sizes </i> parameter specifies the number of elements to be reserved for the subcomponents of the keyboard geometry and can be zero or more. These subcomponents include the <i>properties, colors, shapes, sections, and doodads. </i> </p>
<p> To free an entire geometry, use <i>XkbFreeGeometry.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballockeyboard/">XkbAllocKeyboard</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreegeometry/">XkbFreeGeometry</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyboard/">XkbGetKeyboard</a></code>(3)</p>

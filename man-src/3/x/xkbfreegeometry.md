---
title: "xkbfreegeometry(3)"
name: "xkbfreegeometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreegeometry/"
description: "XkbFreeGeometry – Free an entire geometry"
---

<p>XkbFreeGeometry &#8211; Free an entire geometry </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeGeometry</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br/>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></dt>
<dd>
</dd><dd>geometry to be freed</dd>
<dt><i>&#8211; which</i></dt>
<dd>mask of geometry components to be freed</dd>
<dt><i>&#8211; free_all</i></dt>
<dd>True =&gt; the entire geometry is freed</dd></dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> The values of <i>which </i> and <i>free_all </i> determine how much of the specified geometry is freed. The valid values for <i>which </i> are: </p>
<pre> #define XkbGeomPropertiesMask (1&lt;&lt;0)
 #define XkbGeomColorsMask (1&lt;&lt;1)
 #define XkbGeomShapesMask (1&lt;&lt;2)
 #define XkbGeomSectionsMask (1&lt;&lt;3)
 #define XkbGeomDoodadsMask (1&lt;&lt;4)
 #define XkbGeomKeyAliasesMask (1&lt;&lt;5)
 #define XkbGeomAllMask (0x3f)</pre>
<p>If <i>free_all </i> is True, the entire geometry is freed regardless of the value of <i>which. </i> Otherwise, the portions of the geometry specified by <i>which </i> are freed.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>Unable to allocate storage</dd>
<dt><code>BadValue</code></dt>
<dd>An argument is out of range </dd>
</dl>

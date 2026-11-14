---
title: "xkbcomputerowbounds(3)"
name: "xkbcomputerowbounds"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbcomputerowbounds/"
description: "XkbComputeRowBounds – Update the bounding box of a row"
---

<p>XkbComputeRowBounds &#8211; Update the bounding box of a row </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbComputeRowBounds</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>XkbSectionPtr </code><i>section</i><code>,</code> <code>XkbRowPtr </code><i>row</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry that contains the section</p>
<dt><i>&#8211; section</i></p>
<dd>section that contains the row</p>
<dt><i>&#8211; row</i></p>
<dd>row to be examined and updated</dl>
<h2>Description</h2>
<p><i>XkbComputeRowBounds </i> checks the bounds of all keys in the <i>row </i> and updates the bounding box of the row if necessary. <i>XkbComputeRowBounds </i> returns False if any of the arguments is NULL; otherwise, it returns True.</p>

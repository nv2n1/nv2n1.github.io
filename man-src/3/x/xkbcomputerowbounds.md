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
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></dt>
<dd>
</dd><dd>geometry that contains the section</dd>
<dt><i>&#8211; section</i></dt>
<dd>section that contains the row</dd>
<dt><i>&#8211; row</i></dt>
<dd>row to be examined and updated</dd></dl>
<h2>Description</h2>
<p><i>XkbComputeRowBounds </i> checks the bounds of all keys in the <i>row </i> and updates the bounding box of the row if necessary. <i>XkbComputeRowBounds </i> returns False if any of the arguments is NULL; otherwise, it returns True.</p>

---
title: "xkbcomputesectionbounds(3)"
name: "xkbcomputesectionbounds"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbcomputesectionbounds/"
description: "XkbComputeSectionBounds – Update the bounding box of a section"
---

<p>XkbComputeSectionBounds &#8211; Update the bounding box of a section </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbComputeSectionBounds</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>XkbSectionPtr </code><i>section</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry that contains the section</p>
<dt><i>&#8211; section</i></p>
<dd>section to be examined and updated</dl>
<h2>Description</h2>
<p>&nbsp;If you add or delete a row to or from a section, or if you change the geometry&nbsp; of any of the rows in that section, you may need to update the bounding box for that section.<br />
&nbsp; <i>XkbComputeSectionBounds </i> examines all the rows of the <i>section </i> and updates the bounding box of that section so that it contains all rows. <i>XkbComputeSectionBounds </i> returns False if any of the arguments is NULL; otherwise, it returns True.</p>

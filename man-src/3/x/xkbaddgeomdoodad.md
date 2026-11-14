---
title: "xkbaddgeomdoodad(3)"
name: "xkbaddgeomdoodad"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomdoodad/"
description: "XkbAddGeomDoodad – Add one doodad to a section of a keyboard geometry or to the top-level geometry"
---

<p>XkbAddGeomDoodad &#8211; Add one doodad to a section of a keyboard geometry or to the top-level geometry </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDoodadPtr XkbAddGeomDoodad</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>XkbSectionPtr </code><i>section</i><code>,</code> <code>Atom </code><i>name</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry to which the doodad is added</p>
<dt><i>&#8211; section</i></p>
<dd>section, if any, to which the doodad is added</p>
<dt><i>&#8211; name</i></p>
<dd>name of the new doodad</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> A <i>doodad </i> describes some visible aspect of the keyboard that is not a key and is not a section. <i>XkbAddGeomDoodad </i> adds a doodad with name specified by <i>name </i> to the geometry <i>geom </i> if <i>section </i> is NULL or to the section of the geometry specified by <i>section </i> if <i>section </i> is not NULL. <i>XkbAddGeomDoodad </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the doodad. If there is already a doodad with the name <i>name </i> in the doodad array for the geometry (if <i>section </i> is NULL) or the section (if <i>section </i> is non-NULL), a pointer to that doodad is returned. To allocate space for an arbitrary number of doodads to a section, use the <i>XkbAllocGeomSectionDoodads </i> function. To allocate space for an arbitrary number of doodads to a keyboard geometry, use the <i>XkbAllocGeomDoodads </i> function.</p>
<h2>Structures</h2>
<pre> typedef union _XkbDoodad {
 XkbAnyDoodadRec any;
 XkbShapeDoodadRec shape;
 XkbTextDoodadRec text;
 XkbIndicatorDoodadRec indicator;
 XkbLogoDoodadRec logo;
 } XkbDoodadRec, *XkbDoodadPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomdoodads/">XkbAllocGeomDoodads</a></code>(3), <code><a href="/docs/linux/man/3-xkballocgeomsectiondoodads/">XkbAllocGeomSectionDoodads</a></code>(3)</p>

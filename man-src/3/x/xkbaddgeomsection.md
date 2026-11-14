---
title: "xkbaddgeomsection(3)"
name: "xkbaddgeomsection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomsection/"
description: "XkbAddGeomSection – Add one section to an existing keyboard geometry"
---

<p>XkbAddGeomSection &#8211; Add one section to an existing keyboard geometry </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbSectionPtr XkbAddGeomSection</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>int </code><i>sz_rows</i><code>,</code> <code>int </code><i>sz_doodads</i><code>,</code> <code>int </code><i>sz_overlays</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry to be updated</p>
<dt><i>&#8211; name</i></p>
<dd>name of the new section</p>
<dt><i>&#8211; sz_rows</i></p>
<dd>number of rows to reserve in the section</p>
<dt><i>&#8211; sz_doodads</i></p>
<dd>number of doodads to reserve in the section</p>
<dt><i>&#8211; sz_overlays</i></p>
<dd>number of overlays to reserve in the section</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> A keyboard geometry contains an arbitrary number of sections. <i>XkbAddGeomSection </i> adds one section to an existing keyboard geometry <i>geom. </i> The new section contains space for the number of rows, doodads, and overlays specified by <i>sz_rows, sz_doodads, </i> and <i>sz_overlays. </i> The new section is allocated and zeroed and given the name specified by <i>name. </i> If a section with name <i>name </i> already exists in the geometry, a pointer to the existing section is returned. <i>XkbAddGeomSection </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the section. To allocate space for an arbitrary number of sections to a geometry, use <i>XkbAllocGeomSections.</i></p>
<h2>Structures</h2>
<pre>typedef struct _XkbSection {
 Atom name; /* section name */
 unsigned char priority; /* drawing priority, 0=&gt;highest, 255=&gt;lowest */
 short top; /* top coordinate of section origin */
 short left; /* left coordinate of row origin */
 unsigned short width; /* section width, in mm/10 */
 unsigned short height; /* section height, in mm/10 */
 short angle; /* angle of section rotation, counterclockwise */
 unsigned short num_rows; /* number of rows in the rows array */
 unsigned short num_doodads; /* number of doodads in the doodads array */
 unsigned short num_overlays; /* number of overlays in the overlays array */
 unsigned short sz_rows; /* size of the rows array */
 unsigned short sz_doodads; /* size of the doodads array */
 unsigned short sz_overlays; /* size of the overlays array */
 XkbRowPtr rows; /* section rows array */
 XkbDoodadPtr doodads; /* section doodads array */
 XkbBoundsRec bounds; /* bounding box for the section, before rotation*/
 XkbOverlayPtr overlays; /* section overlays array */
} XkbSectionRec, *XkbSectionPtr;</pre>
<p><i>top </i> and <i>left </i> are the origin of the section, relative to the origin of the keyboard, in mm/10. angle is in 1/10 degrees.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomsections/">XkbAllocGeomSections</a></code>(3)</p>

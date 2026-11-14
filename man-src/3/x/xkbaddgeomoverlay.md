---
title: "xkbaddgeomoverlay(3)"
name: "xkbaddgeomoverlay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomoverlay/"
description: "XkbAddGeomOverlay – Add one overlay to a section"
---

<p>XkbAddGeomOverlay &#8211; Add one overlay to a section </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbOverlayPtr XkbAddGeomOverlay</code> <code>(XkbSectionPtr </code><i>section</i><code>,</code> <code>Atom </code><i>name</i><code>,</code> <code>int </code><i>sz_rows</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; section</i></p>
<dd>
<dd>section to which an overlay will be added</p>
<dt><i>&#8211; name</i></p>
<dd>name of the overlay</p>
<dt><i>&#8211; sz_rows</i></p>
<dd>number of rows to reserve in the overlay</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> <i>XkbAddGeomOverlay </i> adds an overlay with the specified name to the specified <i>section. </i> The new overlay is created with space allocated for <i>sz_rows </i> rows. If an overlay with name <i>name </i> already exists in the section, a pointer to the existing overlay is returned. <i>XkbAddGeomOverlay </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the overlay. To allocate space for an arbitrary number of overlays to a section, use the <i>XkbAllocGeomOverlay </i> function.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbOverlayRec {
 Atom name; /* overlay name */
 XkbSectionPtr section_under; /* the section under this overlay */
 unsigned short num_rows; /* number of rows in the rows array */
 unsigned short sz_rows; /* size of the rows array */
 XkbOverlayRowPtr rows; /* array of rows in the overlay */
 XkbBoundsPtr bounds; /* bounding box for the overlay */
 } XkbOverlayRec,*XkbOverlayPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomoverlay/">XkbAllocGeomOverlay</a></code>(3)</p>

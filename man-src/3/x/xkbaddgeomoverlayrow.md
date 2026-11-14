---
title: "xkbaddgeomoverlayrow(3)"
name: "xkbaddgeomoverlayrow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomoverlayrow/"
description: "XkbAddGeomOverlayRow – Add a row to an existing overlay"
---

<p>XkbAddGeomOverlayRow &#8211; Add a row to an existing overlay </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbOverlayRowPtr XkbAddGeomOverlayRow</code> <code>(XkbOverlayPtr </code><i>overlay</i><code>,</code> <code>XkbRowPtr </code><i>row_under</i><code>,</code> <code>int </code><i>sz_keys</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; overlay</i></p>
<dd>
<dd>overlay to be updated</p>
<dt><i>&#8211; row_under</i></p>
<dd>row to be overlayed in the section overlay overlays</p>
<dt><i>&#8211; sz_keys</i></p>
<dd>number of keys to reserve in the row</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> <i>XkbAddGeomOverlayRow </i> adds one row to the <i>overlay. </i> The new row contains space for <i>sz_keys </i> keys. If <i>row_under </i> specifies a row that doesn&#8217;t exist on the underlying section, <i>XkbAddGeomOverlayRow </i> returns NULL and doesn&#8217;t change the overlay. <i>XkbAddGeomOverlayRow </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the overlay.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbOverlayRow {
 unsigned short row_under; /* index into the row under this overlay row */
 unsigned short num_keys; /* number of keys in the keys array */
 unsigned short sz_keys; /* size of the keys array */
 XkbOverlayKeyPtr keys; /* array of keys in the overlay row */
 } XkbOverlayRowRec,*XkbOverlayRowPtr;</pre>

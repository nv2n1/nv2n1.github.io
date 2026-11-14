---
title: "xkbaddgeomoverlaykey(3)"
name: "xkbaddgeomoverlaykey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomoverlaykey/"
description: "XkbAddGeomOverlayKey – Add a key to an existing overlay row"
---

<p>XkbAddGeomOverlayKey &#8211; Add a key to an existing overlay row </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbOverlayKeyPtr XkbAddGeomOverlayKey</code> <code>(XkbOverlayPtr </code><i>overlay</i><code>,</code> <code>XkbRowPtr </code><i>row</i><code>,</code> <code>char *</code><i>under</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; overlay</i></p>
<dd>
<dd>overlay to be updated</p>
<dt><i>&#8211; row</i></p>
<dd>row in overlay to be updated</p>
<dt><i>&#8211; under</i></p>
<dd>primary name of the key to be considered</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> <i>XkbAddGeomOverlayKey </i> adds one key to the <i>row </i> in the <i>overlay. </i> If there is no key named <i>under </i> in the row of the underlying section, <i>XkbAddGeomOverlayKey </i> returns NULL.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbOverlayKey {
 XkbKeyNameRec over; /* name of this overlay key */
 XkbKeyNameRec under; /* name of the key under this overlay key */
 } XkbOverlayKeyRec,*XkbOverlayKeyPtr;</pre>

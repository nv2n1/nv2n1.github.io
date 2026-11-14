---
title: "xkbaddgeomkey(3)"
name: "xkbaddgeomkey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomkey/"
description: "XkbAddGeomKey – Add one key at the end of an existing row of keys"
---

<p>XkbAddGeomKey &#8211; Add one key at the end of an existing row of keys </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbKeyPtr XkbAddGeomKey</code> <code>(XkbRowPtr </code><i>row</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; row</i></p>
<dd>
<dd>row to be updated</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> Keys are grouped into rows. <i>XkbAddGeomKey </i> adds one key to the end of the specified <i>row. </i> The key is allocated and zeroed. <i>XkbAddGeomKey </i> returns NULL if <i>row </i> is empty or if it was not able to allocate space for the key. To allocate space for an arbitrary number of keys to a row, use <i>XkbAllocGeomKeys.</i></p>
<h2>Structures</h2>
<pre> typedef struct _XkbKey { /* key in a row */
 XkbKeyNameRec name; /* key name */
 short gap; /* gap in mm/10 from previous key in row */
 unsigned char shape_ndx; /* index of shape for key */
 unsigned char color_ndx; /* index of color for key body */
 } XkbKeyRec, *XkbKeyPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomkeys/">XkbAllocGeomKeys</a></code>(3)</p>

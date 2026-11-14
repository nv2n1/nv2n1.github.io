---
title: "xkbaddgeomrow(3)"
name: "xkbaddgeomrow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomrow/"
description: "XkbAddGeomRow – Add a row to a section"
---

<p>XkbAddGeomRow &#8211; Add a row to a section </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbRowPtr XkbAddGeomRow</code> <code>(XkbSectionPtr </code><i>section</i><code>,</code> <code>int </code><i>sz_keys</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; section</i></p>
<dd>
<dd>section to be updated</p>
<dt><i>&#8211; sz_keys</i></p>
<dd>number of keys to be reserved</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> One of the components of a keyboard geometry section is one or more rows of keys. <i>XkbAddGeomRow </i> adds one row to the specified <i>section. </i> The newly created row contains space for the number of keys specified in <i>sz_keys. </i> They are allocated and zeroed, but otherwise uninitialized. <i>XkbAddGeomRow </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the row. To allocate space for an arbitrary number of rows to a section, use the <i>XkbAllocGeomRows </i> function.</p>
<h2>Structures</h2>
<pre>typedef struct _XkbRow {
 short top;
 short left;
 unsigned short num_keys;
 unsigned short sz_keys;
 int vertical;
 XkbKeyPtr keys;
 XkbBoundsRec bounds;
} XkbRowRec, *XkbRowPtr; </pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomrows/">XkbAllocGeomRows</a></code>(3)</p>

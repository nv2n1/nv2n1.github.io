---
title: "xkbaddgeomproperty(3)"
name: "xkbaddgeomproperty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomproperty/"
description: "XkbAddGeomProperty – Add one property to an existing keyboard geometry description"
---

<p>XkbAddGeomProperty &#8211; Add one property to an existing keyboard geometry description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbPropertyPtr XkbAddGeomProperty</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>char *</code><i>name</i><code>,</code> <code>char *</code><i>value</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry to be updated</p>
<dt><i>&#8211; name</i></p>
<dd>name of the new property</p>
<dt><i>&#8211; value</i></p>
<dd>value for the new property</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> <i>XkbAddGeomProperty </i> adds one property with the specified <i>name </i> and <i>value </i> to the keyboard geometry specified by <i>geom. XkbAddGeomProperty </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the property. To allocate space for an arbitrary number of properties, use the <i>XkbAllocGeomProps </i> function.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbProperty {
 char * name; /* property name */
 char * value; /* property value */
 } XkbPropertyRec,*XkbPropertyPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomprops/">XkbAllocGeomProps</a></code>(3)</p>

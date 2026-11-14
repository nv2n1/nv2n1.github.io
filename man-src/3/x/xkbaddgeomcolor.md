---
title: "xkbaddgeomcolor(3)"
name: "xkbaddgeomcolor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomcolor/"
description: "XkbAddGeomColor – Add one color name to an existing keyboard geometry description"
---

<p>XkbAddGeomColor &#8211; Add one color name to an existing keyboard geometry description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbColorPtr XkbAddGeomColor</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>char *</code><i>spec</i><code>,</code> <code>unsigned int </code><i>pixel</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry to be updated</p>
<dt><i>&#8211; spec</i></p>
<dd>color to be added</p>
<dt><i>&#8211; pixel</i></p>
<dd>color to be added</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> <i>XkbAddGeomColor </i> adds the specified color <i>name </i> and <i>pixel </i> to the specified geometry <i>geom. </i> The top-level geometry description includes a list of up to MaxColors (32) <i>color names. </i> A color <i>name </i> is a string whose interpretation is not specified by Xkb and neither is the <i>pixel </i> value&#8217;s interpretation. All other geometry data structures refer to colors using their indices in this global list or pointers to colors in this list. <i>XkbAddGeomColor </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the color. To allocate space for an arbitrary number of colors to a geometry, use the <i>XkbAllocGeomColors </i> function.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbColor {
 unsigned int pixel; /* color */
 char * spec; /* color name */
 } XkbColorRec,*XkbColorPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomcolors/">XkbAllocGeomColors</a></code>(3)</p>

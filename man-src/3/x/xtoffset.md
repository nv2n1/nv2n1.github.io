---
title: "xtoffset(3)"
name: "xtoffset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtoffset/"
description: "XtOffset, XtOffsetOf, XtNumber – determine the byte offset or number of array elements"
---

<p>XtOffset, XtOffsetOf, XtNumber &#8211; determine the byte offset or number of array elements </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Cardinal XtOffset(Type <i>pointer_type</i>, Field <i>field_name</i>);</p>
<dd>Cardinal XtOffsetOf(Type <i>structure_type</i>, Field <i>field_name</i>);</p>
<dd>Cardinal XtNumber(ArrayVariable <i>array</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>array</i></p>
<dd>Specifies a fixed-size array.</p>
<dt><i>field_name</i></p>
<dd>Specifies the name of the field for which to calculate the byte offset.</p>
<dt><i>pointer_type</i></p>
<dd>Specifies a type that is declared as a pointer to the structure.</p>
<dt><i>structure_type</i></p>
<dd>Specifies a type that is declared as a structure.</dl>
<h2>Description</h2>
<p>The <code>XtOffset</code> macro is usually used to determine the offset of various resource fields from the beginning of a widget and can be used at compile time in static initializations. </p>
<p> The <code>XtOffsetOf</code> macro expands to a constant expression that gives the offset in bytes to the specified structure member from the beginning of the structure. It is normally used to statically initialize resource lists and is more portable than <code>XtOffset</code>, which serves the same function. </p>
<p> The <code>XtNumber</code> macro returns the number of elements in the specified argument lists, resources lists, and other counted arrays.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtgetresourcelist/">XtGetResourceList</a>(3), <a href="/docs/linux/man/3-xtsetarg/">XtSetArg</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

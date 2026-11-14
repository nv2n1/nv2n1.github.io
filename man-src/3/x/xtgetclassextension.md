---
title: "xtgetclassextension(3)"
name: "xtgetclassextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetclassextension/"
description: "XtGetClassExtension – locate a class extension record"
---

<p>XtGetClassExtension &#8211; locate a class extension record </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtPointer XtGetClassExtension(WidgetClass <i>object_class</i>, Cardinal <i>byte_offset</i>, XrmQuark <i>type</i>, long <i>version</i>, Cardinal <i>record_size</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>object_class</i></p>
<dd>Specifies the widget class containing the extension list to be searched.</p>
<dt><i>byte_offset</i></p>
<dd>Specifies the offset in bytes form the base of the widget class of the extension field to be searched.</p>
<dt><i>type</i></p>
<dd>Specifies the name of the class extension to be located.</p>
<dt><i>version</i></p>
<dd>Specifies the minimum acceptable version of the class extension required for a match.</p>
<dt><i>record_size</i></p>
<dd>Specifies the minimum acceptable length of the class extension record required for match, or 0.</dl>
<h2>Description</h2>
<p>The list of extension records at the specified offset in the specified <i>widget_class</i> will be searched for a match on the specified <i>type</i>, a version greater than or equal to the specified <i>version</i>, and a record size greater than or equal the specified <i>record_size</i> if it is nonzero. <code>XtGetClassExtension</code> returns a pointer to a matching extension record or NULL if no match is found. The returned extension record is owned by the widget class and must not be modified or freed by the caller, except possibly to be modified by the widget class owner.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

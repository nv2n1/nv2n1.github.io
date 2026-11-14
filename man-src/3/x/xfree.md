---
title: "xfree(3)"
name: "xfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfree/"
description: "XFree – free client data"
---

<p>XFree &#8211; free client data </p>
<h2>Syntax</h2>
<p>int XFree(void *<i>data</i>);</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>data</i></p>
<dd>Specifies the data that are to be freed.</dl>
<h2>Description</h2>
<p>The <code>XFree</code> function is a general-purpose Xlib routine that frees the specified data. You must use it to free any objects that were allocated by Xlib, unless an alternate function is explicitly specified for the object. </p>
<p> If data is NULL, no operation is performed.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>

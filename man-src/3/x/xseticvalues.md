---
title: "xseticvalues(3)"
name: "xseticvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xseticvalues/"
description: "XSetICValues, XGetICValues – set and obtain XIC values"
---

<p>XSetICValues, XGetICValues &#8211; set and obtain XIC values </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>char * XSetICValues(XIC <i>ic</i>, &#8230;);</p>
<dd>char * XGetICValues(XIC <i>ic</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ic</i></p>
<dd>Specifies the input context.</p>
<dt>&#8230;</p>
<dd>Specifies the variable length argument list to set or get XIC values.</dl>
<h2>Description</h2>
<p>The <code>XSetICValues</code> function returns NULL if no error occurred; otherwise, it returns the name of the first argument that could not be set. An argument might not be set for any of the following reasons:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The argument is read-only (for example, <code>XNFilterEvents</code>).</p>
<dt>&bull;</p>
<dd>The argument name is not recognized.</p>
<dt>&bull;</p>
<dd>An implementation-dependent error occurs.</dl>
<p> Each value to be set must be an appropriate datum, matching the data type imposed by the semantics of the argument. </p>
<p> The <code>XSetICValues</code> can generate <code>BadAtom</code>, <code>BadColor</code>, <code>BadCursor</code>, <code>BadPixmap</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XGetICValues</code> function returns NULL if no error occurred; otherwise, it returns the name of the first argument that could not be obtained. An argument could not be obtained for any of the following reasons:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The argument name is not recognized.</p>
<dt>&bull;</p>
<dd>The input method encountered an implementation-dependent error.</dl>
<p> Each IC attribute value argument (following a name) must point to a location where the IC value is to be stored. That is, if the IC value is of type T, the argument must be of type T*. If T itself is a pointer type, then <code>XGetICValues</code> allocates memory to store the actual data, and the client is responsible for freeing this data by calling <code>XFree</code> with the returned pointer. The exception to this rule is for an IC value of type <code>XNVaNestedList</code> (for preedit and status attributes). In this case, the argument must also be of type <code>XVaNestedList</code>. Then, the rule of changing type T to T* and freeing the allocated data applies to each element of the nested list.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateic/">XCreateIC</a>(3), <a href="/docs/linux/man/3-xopenim/">XOpenIM</a>(3), <a href="/docs/linux/man/3-xseticfocus/">XSetICFocus</a>(3), <a href="/docs/linux/man/3-xmbresetic/">XmbResetIC</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

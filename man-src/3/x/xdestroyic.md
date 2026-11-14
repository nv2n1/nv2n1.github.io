---
title: "xdestroyic(3)"
name: "xdestroyic"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdestroyic/"
description: "XCreateIC, XDestroyIC, XIMOfIC – create, destroy, and obtain the input method of an input context"
---

<p>XCreateIC, XDestroyIC, XIMOfIC &#8211; create, destroy, and obtain the input method of an input context </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XIC XCreateIC(XIM <i>im</i>, &#8230;);</p>
<dd>void XDestroyIC(XIC <i>ic</i>);</p>
<dd>XIM XIMOfIC(XIC <i>ic</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ic</i></p>
<dd>Specifies the input context.</p>
<dt><i>im</i></p>
<dd>Specifies the input method.</p>
<dt>&#8230;</p>
<dd>Specifies the variable length argument list to set XIC values.</dl>
<h2>Description</h2>
<p>The <code>XCreateIC</code> function creates a context within the specified input method. </p>
<p> Some of the arguments are mandatory at creation time, and the input context will not be created if those arguments are not provided. The mandatory arguments are the input style and the set of text callbacks (if the input style selected requires callbacks). All other input context values can be set later. </p>
<p> <code>XCreateIC</code> returns a NULL value if no input context could be created. A NULL value could be returned for any of the following reasons:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>A required argument was not set.</p>
<dt>&bull;</p>
<dd>A read-only argument was set (for example, <code>XNFilterEvents</code>).</p>
<dt>&bull;</p>
<dd>The argument name is not recognized.</p>
<dt>&bull;</p>
<dd>The input method encountered an input method implementation-dependent error.</dl>
<p> The <code>XCreateIC</code> can generate <code>BadAtom</code>, <code>BadColor</code>, <code>BadPixmap</code>, and <code>BadWindow</code> errors. </p>
<p> <code>XDestroyIC</code> destroys the specified input context. </p>
<p> The <code>XIMOfIC</code> function returns the input method associated with the specified input context.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xopenim/">XOpenIM</a>(3), <a href="/docs/linux/man/3-xseticfocus/">XSetICFocus</a>(3), <a href="/docs/linux/man/3-xseticvalues/">XSetICValues</a>(3), <a href="/docs/linux/man/3-xmbresetic/">XmbResetIC</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

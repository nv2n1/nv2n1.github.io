---
title: "xtgetapplicationnameandclass(3)"
name: "xtgetapplicationnameandclass"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetapplicationnameandclass/"
description: "XtGetApplicationNameAndClass – retrieve application name and class"
---

<p>XtGetApplicationNameAndClass &#8211; retrieve application name and class </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetApplicationNameAndClass(Display* <i>display</i>, String* <i>name_return</i>, String* <i>class_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies an open display connection that has been initialized with <code>XtDisplayInitialize</code>.</p>
<dt><i>name_return</i></p>
<dd>Returns the application name.</p>
<dt><i>class_return</i></p>
<dd>Returns the application class.</dl>
<h2>Description</h2>
<p><code>XtGetApplicationNameAndClass</code> returns the application name and class passed to <code>XtDisplayInitialize</code> for the specified display. If the display was never initialized or has been closed, the result is undefined. The returned strings are owned by the Intrinsics and must not be modified or freed by the caller.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtdisplayinitialize/">XtDisplayInitialize</a></code>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

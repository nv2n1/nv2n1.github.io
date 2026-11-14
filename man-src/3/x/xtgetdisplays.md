---
title: "xtgetdisplays(3)"
name: "xtgetdisplays"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetdisplays/"
description: "XtGetDisplays – retrieve a list of displays associated with an application context"
---

<p>XtGetDisplays &#8211; retrieve a list of displays associated with an application context </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetDisplays(XtAppContext <i>app_context</i>, Display ***<i>dpy_return</i>, Cardinal* <i>num_dpy_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>dpy_return</i></p>
<dd>Returns a list of open X display connections in the specified application context.</p>
<dt><i>num_dpy_return</i></p>
<dd>Returns the count of open X display connections in <i>dpy_return</i>.</dl>
<h2>Description</h2>
<p>To free the list of displays, use <code>XtFree</code>.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

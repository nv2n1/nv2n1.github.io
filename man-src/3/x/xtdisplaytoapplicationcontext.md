---
title: "xtdisplaytoapplicationcontext(3)"
name: "xtdisplaytoapplicationcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtdisplaytoapplicationcontext/"
description: "XtDisplayToApplicationContext – obtain an application context"
---

<p>XtDisplayToApplicationContext &#8211; obtain an application context </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtAppContext XtDisplayToApplicationContext(Display* <i>dpy</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the display that you want the application context for.</dl>
<h2>Description</h2>
<p>The <code>XtDisplayToApplicationContext</code> function returns the application context for the specified display.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

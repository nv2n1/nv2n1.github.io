---
title: "xttoolkitthreadinitialize(3)"
name: "xttoolkitthreadinitialize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xttoolkitthreadinitialize/"
description: "XtToolkitThreadInitialize – initialize the toolkit for multiple threads"
---

<p>XtToolkitThreadInitialize &#8211; initialize the toolkit for multiple threads </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Boolean XtToolkitThreadInitialize(void);</dl>
<h2>Description</h2>
<p>If <code>XtToolkitThreadInitialize</code> was previously called, it returns. The application programmer must ensure that two or more threads do not simultaneously attempt to call <code>XtToolkitThreadInitialize</code>; the effect of this is undefined. <code>XtToolkitThreadInitialize</code> returns <code>True</code> if the host operating system has threads and the Intrinsics are thread safe.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

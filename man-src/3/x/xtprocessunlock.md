---
title: "xtprocessunlock(3)"
name: "xtprocessunlock"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtprocessunlock/"
description: "XtProcessLock, XtProcessUnlock – lock and unlock process"
---

<p>XtProcessLock, XtProcessUnlock &#8211; lock and unlock process </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtProcessLock(void);</p>
<dd>void XtProcessUnlock(void);</dl>
<h2>Description</h2>
<p><code>XtProcessLock</code> is used to lock all process global data. </p>
<p> <code>XtProcessUnlock</code> unlocks the process.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

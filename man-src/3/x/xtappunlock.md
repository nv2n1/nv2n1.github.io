---
title: "xtappunlock(3)"
name: "xtappunlock"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappunlock/"
description: "XtAppLock, XtAppUnlock – lock and unlock application context"
---

<p>XtAppLock, XtAppUnlock &#8211; lock and unlock application context </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppLock(XtAppContext <i>app_context</i>);</p>
<dd>void XtAppUnlock(XtAppContext <i>app_context</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</dl>
<h2>Description</h2>
<p><code>XtAppLock</code> locks the application context including all its related displays and widgets. </p>
<p> <code>XtAppUnlock</code> unlocks the application context.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

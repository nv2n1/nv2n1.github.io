---
title: "xdestroywindow(3)"
name: "xdestroywindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdestroywindow/"
description: "XDestroyWindow, XDestroySubwindows – destroy windows"
---

<p>XDestroyWindow, XDestroySubwindows &#8211; destroy windows </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDestroyWindow(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XDestroySubwindows(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XDestroyWindow</code> function destroys the specified window as well as all of its subwindows and causes the X server to generate a <code>DestroyNotify</code> event for each window. The window should never be referenced again. If the window specified by the w argument is mapped, it is unmapped automatically. The ordering of the <code>DestroyNotify</code> events is such that for any given window being destroyed, <code>DestroyNotify</code> is generated on any inferiors of the window before being generated on the window itself. The ordering among siblings and across subhierarchies is not otherwise constrained. If the window you specified is a root window, no windows are destroyed. Destroying a mapped window will generate <code>Expose</code> events on other windows that were obscured by the window being destroyed. </p>
<p> <code>XDestroyWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XDestroySubwindows</code> function destroys all inferior windows of the specified window, in bottom-to-top stacking order. It causes the X server to generate a <code>DestroyNotify</code> event for each window. If any mapped subwindows were actually destroyed, <code>XDestroySubwindows</code> causes the X server to generate <code>Expose</code> events on the specified window. This is much more efficient than deleting many windows one at a time because much of the work need be performed only once for all of the windows, rather than for each window. The subwindows should never be referenced again. </p>
<p> <code>XDestroySubwindows</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3), <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

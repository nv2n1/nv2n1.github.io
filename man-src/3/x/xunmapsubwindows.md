---
title: "xunmapsubwindows(3)"
name: "xunmapsubwindows"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xunmapsubwindows/"
description: "XUnmapWindow, XUnmapSubwindows – unmap windows"
---

<p>XUnmapWindow, XUnmapSubwindows &#8211; unmap windows </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XUnmapWindow(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XUnmapSubwindows(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XUnmapWindow</code> function unmaps the specified window and causes the X server to generate an <code>UnmapNotify</code> event. If the specified window is already unmapped, <code>XUnmapWindow</code> has no effect. Normal exposure processing on formerly obscured windows is performed. Any child window will no longer be visible until another map call is made on the parent. In other words, the subwindows are still mapped but are not visible until the parent is mapped. Unmapping a window will generate <code>Expose</code> events on windows that were formerly obscured by it. </p>
<p> <code>XUnmapWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XUnmapSubwindows</code> function unmaps all subwindows for the specified window in bottom-to-top stacking order. It causes the X server to generate an <code>UnmapNotify</code> event on each subwindow and <code>Expose</code> events on formerly obscured windows. Using this function is much more efficient than unmapping multiple windows one at a time because the server needs to perform much of the work only once, for all of the windows, rather than for each window. </p>
<p> <code>XUnmapSubwindows</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3) <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

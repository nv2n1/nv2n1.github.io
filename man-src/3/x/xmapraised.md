---
title: "xmapraised(3)"
name: "xmapraised"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmapraised/"
description: "XMapWindow, XMapRaised, XMapSubwindows – map windows"
---

<p>XMapWindow, XMapRaised, XMapSubwindows &#8211; map windows </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XMapWindow(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XMapRaised(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XMapSubwindows(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XMapWindow</code> function maps the window and all of its subwindows that have had map requests. Mapping a window that has an unmapped ancestor does not display the window but marks it as eligible for display when the ancestor becomes mapped. Such a window is called unviewable. When all its ancestors are mapped, the window becomes viewable and will be visible on the screen if it is not obscured by another window. This function has no effect if the window is already mapped. </p>
<p> If the override-redirect of the window is <code>False</code> and if some other client has selected <code>SubstructureRedirectMask</code> on the parent window, then the X server generates a <code>MapRequest</code> event, and the <code>XMapWindow</code> function does not map the window. Otherwise, the window is mapped, and the X server generates a <code>MapNotify</code> event. </p>
<p> If the window becomes viewable and no earlier contents for it are remembered, the X server tiles the window with its background. If the window&#8217;s background is undefined, the existing screen contents are not altered, and the X server generates zero or more <code>Expose</code> events. If backing-store was maintained while the window was unmapped, no <code>Expose</code> events are generated. If backing-store will now be maintained, a full-window exposure is always generated. Otherwise, only visible regions may be reported. Similar tiling and exposure take place for any newly viewable inferiors. </p>
<p> If the window is an <code>InputOutput</code> window, <code>XMapWindow</code> generates <code>Expose</code> events on each <code>InputOutput</code> window that it causes to be displayed. If the client maps and paints the window and if the client begins processing events, the window is painted twice. To avoid this, first ask for <code>Expose</code> events and then map the window, so the client processes input events as usual. The event list will include <code>Expose</code> for each window that has appeared on the screen. The client&#8217;s normal response to an <code>Expose</code> event should be to repaint the window. This method usually leads to simpler programs and to proper interaction with window managers. </p>
<p> <code>XMapWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XMapRaised</code> function essentially is similar to <code>XMapWindow</code> in that it maps the window and all of its subwindows that have had map requests. However, it also raises the specified window to the top of the stack. </p>
<p> <code>XMapRaised</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XMapSubwindows</code> function maps all subwindows for a specified window in top-to-bottom stacking order. The X server generates <code>Expose</code> events on each newly displayed window. This may be much more efficient than mapping many windows one at a time because the server needs to perform much of the work only once, for all of the windows, rather than for each window. </p>
<p> <code>XMapSubwindows</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

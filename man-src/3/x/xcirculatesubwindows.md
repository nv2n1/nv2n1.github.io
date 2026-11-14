---
title: "xcirculatesubwindows(3)"
name: "xcirculatesubwindows"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcirculatesubwindows/"
description: "XRaiseWindow, XLowerWindow, XCirculateSubwindows, XCirculateSubwindowsUp, XCirculateSubwindowsDown, XRestackWindows – change window stacking order"
---

<p>XRaiseWindow, XLowerWindow, XCirculateSubwindows, XCirculateSubwindowsUp, XCirculateSubwindowsDown, XRestackWindows &#8211; change window stacking order </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XRaiseWindow(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XLowerWindow(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XCirculateSubwindows(Display *<i>display</i>, Window <i>w</i>, int <i>direction</i>);</p>
<dd>int XCirculateSubwindowsUp(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XCirculateSubwindowsDown(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XRestackWindows(Display *<i>display</i>, Window <i>windows</i>[], int <i>nwindows</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>direction</i></p>
<dd>Specifies the direction (up or down) that you want to circulate the window. You can pass <code>RaiseLowest</code> or <code>LowerHighest</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>nwindows</i></p>
<dd>Specifies the number of windows to be restacked.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>windows</i></p>
<dd>Specifies an array containing the windows to be restacked.</dl>
<h2>Description</h2>
<p>The <code>XRaiseWindow</code> function raises the specified window to the top of the stack so that no sibling window obscures it. If the windows are regarded as overlapping sheets of paper stacked on a desk, then raising a window is analogous to moving the sheet to the top of the stack but leaving its x and y location on the desk constant. Raising a mapped window may generate <code>Expose</code> events for the window and any mapped subwindows that were formerly obscured. </p>
<p> If the override-redirect attribute of the window is <code>False</code> and some other client has selected <code>SubstructureRedirectMask</code> on the parent, the X server generates a <code>ConfigureRequest</code> event, and no processing is performed. Otherwise, the window is raised. </p>
<p> <code>XRaiseWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XLowerWindow</code> function lowers the specified window to the bottom of the stack so that it does not obscure any sibling windows. If the windows are regarded as overlapping sheets of paper stacked on a desk, then lowering a window is analogous to moving the sheet to the bottom of the stack but leaving its x and y location on the desk constant. Lowering a mapped window will generate <code>Expose</code> events on any windows it formerly obscured. </p>
<p> If the override-redirect attribute of the window is <code>False</code> and some other client has selected <code>SubstructureRedirectMask</code> on the parent, the X server generates a <code>ConfigureRequest</code> event, and no processing is performed. Otherwise, the window is lowered to the bottom of the stack. </p>
<p> <code>XLowerWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XCirculateSubwindows</code> function circulates children of the specified window in the specified direction. If you specify <code>RaiseLowest</code>, <code>XCirculateSubwindows</code> raises the lowest mapped child (if any) that is occluded by another child to the top of the stack. If you specify <code>LowerHighest</code>, <code>XCirculateSubwindows</code> lowers the highest mapped child (if any) that occludes another child to the bottom of the stack. Exposure processing is then performed on formerly obscured windows. If some other client has selected <code>SubstructureRedirectMask</code> on the window, the X server generates a <code>CirculateRequest</code> event, and no further processing is performed. If a child is actually restacked, the X server generates a <code>CirculateNotify</code> event. </p>
<p> <code>XCirculateSubwindows</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XCirculateSubwindowsUp</code> function raises the lowest mapped child of the specified window that is partially or completely occluded by another child. Completely unobscured children are not affected. This is a convenience function equivalent to <code>XCirculateSubwindows</code> with <code>RaiseLowest</code> specified. </p>
<p> <code>XCirculateSubwindowsUp</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XCirculateSubwindowsDown</code> function lowers the highest mapped child of the specified window that partially or completely occludes another child. Completely unobscured children are not affected. This is a convenience function equivalent to <code>XCirculateSubwindows</code> with <code>LowerHighest</code> specified. </p>
<p> <code>XCirculateSubwindowsDown</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XRestackWindows</code> function restacks the windows in the order specified, from top to bottom. The stacking order of the first window in the windows array is unaffected, but the other windows in the array are stacked underneath the first window, in the order of the array. The stacking order of the other windows is not affected. For each window in the window array that is not a sibling of the first window, a <code>BadMatch</code> error results. </p>
<p> If the override-redirect attribute of a window is <code>False</code> and some other client has selected <code>SubstructureRedirectMask</code> on the parent, the X server generates <code>ConfigureRequest</code> events for each window whose override-redirect flag is not set, and no further processing is performed. Otherwise, the windows will be restacked in top-to-bottom order. </p>
<p> <code>XRestackWindows</code> can generate <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

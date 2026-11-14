---
title: "xiconifywindow(3)"
name: "xiconifywindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xiconifywindow/"
description: "XIconifyWindow, XWithdrawWindow, XReconfigureWMWindow – manipulate top-level windows"
---

<p>XIconifyWindow, XWithdrawWindow, XReconfigureWMWindow &#8211; manipulate top-level windows </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XIconifyWindow(Display *<i>display</i>, Window <i>w</i>, int <i>screen_number</i>);</p>
<dd>Status XWithdrawWindow(Display *<i>display</i>, Window <i>w</i>, int <i>screen_number</i>);</p>
<dd>Status XReconfigureWMWindow(Display *<i>display</i>, Window <i>w</i>, int <i>screen_number</i>, unsigned int <i>value_mask</i>, XWindowChanges *<i>values</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen_number</i></p>
<dd>Specifies the appropriate screen number on the host server.</p>
<dt><i>value_mask</i></p>
<dd>Specifies which values are to be set using information in the values structure. This mask is the bitwise inclusive OR of the valid configure window values bits.</p>
<dt><i>values</i></p>
<dd>Specifies the <code>XWindowChanges</code> structure.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>The <code>XIconifyWindow</code> function sends a WM_CHANGE_STATE <code>ClientMessage</code> event with a format of 32 and a first data element of <code>IconicState</code> (as described in section 4.1.4 of the <i>Inter-Client Communication Conventions Manual</i>) and a window of w to the root window of the specified screen with an event mask set to <code>SubstructureNotifyMask</code>| <code>SubstructureRedirectMask</code>. Window managers may elect to receive this message and if the window is in its normal state, may treat it as a request to change the window&#8217;s state from normal to iconic. If the WM_CHANGE_STATE property cannot be interned, <code>XIconifyWindow</code> does not send a message and returns a zero status. It returns a nonzero status if the client message is sent successfully; otherwise, it returns a zero status. </p>
<p> The <code>XWithdrawWindow</code> function unmaps the specified window and sends a synthetic <code>UnmapNotify</code> event to the root window of the specified screen. Window managers may elect to receive this message and may treat it as a request to change the window&#8217;s state to withdrawn. When a window is in the withdrawn state, neither its normal nor its iconic representations is visible. It returns a nonzero status if the <code>UnmapNotify</code> event is successfully sent; otherwise, it returns a zero status. </p>
<p> <code>XWithdrawWindow</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XReconfigureWMWindow</code> function issues a <code>ConfigureWindow</code> request on the specified top-level window. If the stacking mode is changed and the request fails with a <code>BadMatch</code> error, the error is trapped by Xlib and a synthetic <code>ConfigureRequestEvent</code> containing the same configuration parameters is sent to the root of the specified window. Window managers may elect to receive this event and treat it as a request to reconfigure the indicated window. It returns a nonzero status if the request or event is successfully sent; otherwise, it returns a zero status. </p>
<p> <code>XReconfigureWMWindow</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xconfigurewindow/">XConfigureWindow</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xdestroywindow/">XDestroyWindow</a>(3), <a href="/docs/linux/man/3-xraisewindow/">XRaiseWindow</a>(3), <a href="/docs/linux/man/3-xmapwindow/">XMapWindow</a>(3), <a href="/docs/linux/man/3-xunmapwindow/">XUnmapWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

---
title: "xselectinput(3)"
name: "xselectinput"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xselectinput/"
description: "XSelectInput – select input events"
---

<p>XSelectInput &#8211; select input events </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSelectInput(Display *<i>display</i>, Window <i>w</i>, long <i>event_mask</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mask</i></p>
<dd>Specifies the event mask.</p>
<dt><i>w</i></p>
<dd>Specifies the window whose events you are interested in.</dl>
<h2>Description</h2>
<p>The <code>XSelectInput</code> function requests that the X server report the events associated with the specified event mask. Initially, X will not report any of these events. Events are reported relative to a window. If a window is not interested in a device event, it usually propagates to the closest ancestor that is interested, unless the do_not_propagate mask prohibits it. </p>
<p> Setting the event-mask attribute of a window overrides any previous call for the same window but not for other clients. Multiple clients can select for the same events on the same window with the following restrictions:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Multiple clients can select events on the same window because their event masks are disjoint. When the X server generates an event, it reports it to all interested clients.</p>
<dt>&bull;</p>
<dd>Only one client at a time can select <code>CirculateRequest</code>, <code>ConfigureRequest</code>, or <code>MapRequest</code> events, which are associated with the event mask <code>SubstructureRedirectMask</code>.</p>
<dt>&bull;</p>
<dd>Only one client at a time can select a <code>ResizeRequest</code> event, which is associated with the event mask <code>ResizeRedirectMask</code>.</p>
<dt>&bull;</p>
<dd>Only one client at a time can select a <code>ButtonPress</code> event, which is associated with the event mask <code>ButtonPressMask</code>.</dl>
<p> The server reports the event to all interested clients. </p>
<p> <code>XSelectInput</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>

---
title: "xkillclient(3)"
name: "xkillclient"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkillclient/"
description: "XSetCloseDownMode, XKillClient – control clients"
---

<p>XSetCloseDownMode, XKillClient &#8211; control clients </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetCloseDownMode(Display *<i>display</i>, int <i>close_mode</i>);</p>
<dd>int XKillClient(Display *<i>display</i>, XID <i>resource</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>close_mode</i></p>
<dd>Specifies the client close-down mode. You can pass <code>DestroyAll</code>, <code>RetainPermanent</code>, or <code>RetainTemporary</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>resource</i></p>
<dd>Specifies any resource associated with the client that you want to destroy or <code>AllTemporary</code>.</dl>
<h2>Description</h2>
<p>The <code>XSetCloseDownMode</code> defines what will happen to the client&#8217;s resources at connection close. A connection starts in <code>DestroyAll</code> mode. For information on what happens to the client&#8217;s resources when the close_mode argument is <code>RetainPermanent</code> or <code>RetainTemporary</code>, see section 2.6. </p>
<p> <code>XSetCloseDownMode</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XKillClient</code> function forces a close down of the client that created the resource if a valid resource is specified. If the client has already terminated in either <code>RetainPermanent</code> or <code>RetainTemporary</code> mode, all of the client&#8217;s resources are destroyed. If <code>AllTemporary</code> is specified, the resources of all clients that have terminated in <code>RetainTemporary</code> are destroyed (see section 2.5). This permits implementation of window manager facilities that aid debugging. A client can set its close-down mode to <code>RetainTemporary</code>. If the client then crashes, its windows would not be destroyed. The programmer can then inspect the application&#8217;s window tree and use the window manager to destroy the zombie windows. </p>
<p> <code>XKillClient</code> can generate a <code>BadValue</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>

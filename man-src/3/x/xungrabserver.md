---
title: "xungrabserver(3)"
name: "xungrabserver"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xungrabserver/"
description: "XGrabServer, XUngrabServer – grab the server"
---

<p>XGrabServer, XUngrabServer &#8211; grab the server </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XGrabServer(Display *<i>display</i>);</p>
<dd>int XUngrabServer(Display *<i>display</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</dl>
<h2>Description</h2>
<p>The <code>XGrabServer</code> function disables processing of requests and close downs on all other connections than the one this request arrived on. You should not grab the X server any more than is absolutely necessary. </p>
<p> The <code>XUngrabServer</code> function restarts processing of requests and close downs on other connections. You should avoid grabbing the X server as much as possible.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xgrabbutton/">XGrabButton</a>(3), <a href="/docs/linux/man/3-xgrabkey/">XGrabKey</a>(3), <a href="/docs/linux/man/3-xgrabkeyboard/">XGrabKeyboard</a>(3), <a href="/docs/linux/man/3-xgrabpointer/">XGrabPointer</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

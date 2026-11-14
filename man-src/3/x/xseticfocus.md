---
title: "xseticfocus(3)"
name: "xseticfocus"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xseticfocus/"
description: "XSetICFocus, XUnsetICFocus – set and unset input context focus"
---

<p>XSetICFocus, XUnsetICFocus &#8211; set and unset input context focus </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XSetICFocus(XIC <i>ic</i>);</p>
<dd>void XUnsetICFocus(XIC <i>ic</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ic</i></p>
<dd>Specifies the input context.</dl>
<h2>Description</h2>
<p>The <code>XSetICFocus</code> function allows a client to notify an input method that the focus window attached to the specified input context has received keyboard focus. The input method should take action to provide appropriate feedback. Complete feedback specification is a matter of user interface policy. </p>
<p> Calling <code>XSetICFocus</code> does not affect the focus window value. </p>
<p> The <code>XUnsetICFocus</code> function allows a client to notify an input method that the specified input context has lost the keyboard focus and that no more input is expected on the focus window attached to that input context. The input method should take action to provide appropriate feedback. Complete feedback specification is a matter of user interface policy. </p>
<p> Calling <code>XUnsetICFocus</code> does not affect the focus window value; the client may still receive events from the input method that are directed to the focus window.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateic/">XCreateIC</a>(3), <a href="/docs/linux/man/3-xopenim/">XOpenIM</a>(3), <a href="/docs/linux/man/3-xseticvalues/">XSetICValues</a>(3), <a href="/docs/linux/man/3-xmbresetic/">XmbResetIC</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

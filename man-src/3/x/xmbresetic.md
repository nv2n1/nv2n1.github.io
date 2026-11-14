---
title: "xmbresetic(3)"
name: "xmbresetic"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmbresetic/"
description: "XmbResetIC, XwcResetIC, Xutf8ResetIC – reset the state of an input context"
---

<p>XmbResetIC, XwcResetIC, Xutf8ResetIC &#8211; reset the state of an input context </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>char *XmbResetIC(XIC <i>ic</i>);</p>
<dd>wchar_t *XwcResetIC(XIC <i>ic</i>);</p>
<dd>char *Xutf8ResetIC(XIC <i>ic</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ic</i></p>
<dd>Specifies the input context.</dl>
<h2>Description</h2>
<p>When <code>XNResetState</code> is set to <code>XIMInitialState</code>, <code>XmbResetIC</code>, <code>XwcResetIC</code> and <code>Xutf8ResetIC</code> reset an input context to its initial state; when <code>XNResetState</code> is set to <code>XIMPreserveState</code>, the current input context state is preserved. In both cases, any input pending on that context is deleted. The input method is required to clear the preedit area, if any, and update the status accordingly. Calling <code>XmbResetIC</code>, <code>XwcResetIC</code> or <code>Xutf8ResetIC</code> does not change the focus. </p>
<p> The return value of <code>XmbResetIC</code> is its current preedit string as a multibyte string. The return value of <code>XwcResetIC</code> is its current preedit string as a wide character string. The return value of <code>Xutf8ResetIC</code> is its current preedit string as an UTF-8 string. If there is any preedit text drawn or visible to the user, then these procedures must return a non-NULL string. If there is no visible preedit text, then it is input method implementation-dependent whether these procedures return a non-NULL string or NULL. </p>
<p> The client should free the returned string by calling <code>XFree</code>. </p>
<p> The function <code>Xutf8ResetIC</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreateic/">XCreateIC</a>(3), <a href="/docs/linux/man/3-xopenim/">XOpenIM</a>(3), <a href="/docs/linux/man/3-xseticfocus/">XSetICFocus</a>(3), <a href="/docs/linux/man/3-xseticvalues/">XSetICValues</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

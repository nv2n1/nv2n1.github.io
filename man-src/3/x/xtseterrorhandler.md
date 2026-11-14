---
title: "xtseterrorhandler(3)"
name: "xtseterrorhandler"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtseterrorhandler/"
description: "XtError, XtSetErrorHandler, XtSetWarningHandler, XtWarning – low-level error handlers"
---

<p>XtError, XtSetErrorHandler, XtSetWarningHandler, XtWarning &#8211; low-level error handlers </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtError(const char *<i>message</i>);</p>
<dd>void XtSetErrorHandler(XtErrorHandler <i>handler</i>);</p>
<dd>void XtSetWarningHandler(XtErrorHandler <i>handler</i>);</p>
<dd>void XtWarning(const char *<i>message</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>message</i></p>
<dd>Specifies the nonfatal error message that is to be reported.</p>
<dt><i>handler</i></p>
<dd>Specifies the new fatal error procedure, which should not return, or the nonfatal error procedure, which usually returns.</p>
<dt><i>message</i></p>
<dd>Specifies the message that is to be reported.</dl>
<h2>Description</h2>
<p>The <code>XtError</code> function has been superceded by <code>XtAppError</code>. </p>
<p> The <code>XtSetErrorHandler</code> function has been superceded by <code>XtAppSetErrorHandler</code>. </p>
<p> The <code>XtSetWarningHandler</code> function has been superceded by <code>XtAppSetWarningHandler</code>. </p>
<p> The <code>XtWarning</code> function has been superceded by <code>XtAppWarning</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtapperror/">XtAppError</a></code>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

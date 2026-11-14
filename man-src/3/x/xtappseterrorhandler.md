---
title: "xtappseterrorhandler(3)"
name: "xtappseterrorhandler"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappseterrorhandler/"
description: "XtAppError, XtAppSetErrorHandler, XtAppSetWarningHandler, XtAppWarning – low-level error handlers"
---

<p>XtAppError, XtAppSetErrorHandler, XtAppSetWarningHandler, XtAppWarning &#8211; low-level error handlers </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppError(XtAppContext <i>app_context</i>, const char *<i>message</i>);</p>
<dd>XtErrorHandler XtAppSetErrorHandler(XtAppContext <i>app_context</i>, XtErrorHandler <i>handler</i>);</p>
<dd>XtErrorHandler XtAppSetWarningHandler(XtAppContext <i>app_context</i>, XtErrorHandler <i>handler</i>);</p>
<dd>void XtAppWarning(XtAppContext <i>app_context</i>, const char *<i>message</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>message</i></p>
<dd>Specifies the nonfatal error message that is to be reported.</p>
<dt><i>handler</i></p>
<dd>Specifies the new fatal error procedure, which should not return, or the nonfatal error procedure, which usually returns.</p>
<dt><i>message</i></p>
<dd>Specifies the message that is to be reported.</dl>
<h2>Description</h2>
<p>The <code>XtAppError</code> function calls the installed error procedure and passes the specified message. </p>
<p> The <code>XtAppSetErrorHandler</code> function registers the specified procedure, which is called when a fatal error condition occurs. </p>
<p> The <code>XtAppSetWarningHandler</code> registers the specified procedure, which is called when a nonfatal error condition occurs. </p>
<p> The <code>XtAppWarning</code> function calls the installed nonfatal error procedure and passes the specified message.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappgeterrordatabase/">XtAppGetErrorDatabase</a>(3), <a href="/docs/linux/man/3-xtapperrormsg/">XtAppErrorMsg</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

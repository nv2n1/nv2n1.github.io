---
title: "xtappseterrormsghandler(3)"
name: "xtappseterrormsghandler"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappseterrormsghandler/"
description: "XtAppErrorMsg, XtAppSetErrorMsgHandler, XtAppSetWarningMsgHandler, XtAppWarningMsg – high-level error handlers"
---

<p>XtAppErrorMsg, XtAppSetErrorMsgHandler, XtAppSetWarningMsgHandler, XtAppWarningMsg &#8211; high-level error handlers </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppErrorMsg(XtAppContext <i>app_context</i>, const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</p>
<dd>XtErrorMsgHandler XtAppSetErrorMsgHandler(XtAppContext <i>app_context</i>, XtErrorMsgHandler <i>msg_handler</i>);</p>
<dd>XtErrorMsgHandler XtAppSetWarningMsgHandler(XtAppContext <i>app_context</i>, XtErrorMsgHandler <i>msg_handler</i>);</p>
<dd>void XtAppWarningMsg(XtAppContext <i>app_context</i>, const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>class</i></p>
<dd>Specifies the resource class of the error message.</p>
<dt><i>defaultMsg</i></p>
<dd>Specifies the default message to use.</p>
<dt><i>name</i></p>
<dd>Specifies the general kind of error.</p>
<dt><i>type</i></p>
<dd>Specifies the detailed name of the error.</p>
<dt><i>msg_handler</i></p>
<dd>Specifies the new fatal error procedure, which should not return or the nonfatal error procedure, which usually returns.</p>
<dt><i>num_params</i></p>
<dd>Specifies the number of values in the parameter list.</p>
<dt><i>params</i></p>
<dd>Specifies a pointer to a list of values to be stored in the message.</dl>
<h2>Description</h2>
<p>The <code>XtAppErrorMsg</code> function calls the high-level error handler and passes the specified information. </p>
<p> The <code>XtAppSetErrorMsgHandler</code> function registers the specified procedure, which is called when a fatal error occurs. </p>
<p> The <code>XtAppSetWarningMsgHandler</code> function registers the specified procedure, which is called when a nonfatal error condition occurs. </p>
<p> The <code>XtAppWarningMsg</code> function calls the high-level error handler and passes the specified information.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappgeterrordatabase/">XtAppGetErrorDatabase</a>(3), <a href="/docs/linux/man/3-xtapperror/">XtAppError</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

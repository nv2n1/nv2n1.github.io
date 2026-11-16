---
title: "xtappsetwarningmsghandler(3)"
name: "xtappsetwarningmsghandler"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappsetwarningmsghandler/"
description: "XtAppErrorMsg, XtAppSetErrorMsgHandler, XtAppSetWarningMsgHandler, XtAppWarningMsg – high-level error handlers"
---

<p>XtAppErrorMsg, XtAppSetErrorMsgHandler, XtAppSetWarningMsgHandler, XtAppWarningMsg &#8211; high-level error handlers </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppErrorMsg(XtAppContext <i>app_context</i>, const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</dd>
<dd>XtErrorMsgHandler XtAppSetErrorMsgHandler(XtAppContext <i>app_context</i>, XtErrorMsgHandler <i>msg_handler</i>);</dd>
<dd>XtErrorMsgHandler XtAppSetWarningMsgHandler(XtAppContext <i>app_context</i>, XtErrorMsgHandler <i>msg_handler</i>);</dd>
<dd>void XtAppWarningMsg(XtAppContext <i>app_context</i>, const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></dt>
<dd>Specifies the application context.</dd>
<dt><i>class</i></dt>
<dd>Specifies the resource class of the error message.</dd>
<dt><i>defaultMsg</i></dt>
<dd>Specifies the default message to use.</dd>
<dt><i>name</i></dt>
<dd>Specifies the general kind of error.</dd>
<dt><i>type</i></dt>
<dd>Specifies the detailed name of the error.</dd>
<dt><i>msg_handler</i></dt>
<dd>Specifies the new fatal error procedure, which should not return or the nonfatal error procedure, which usually returns.</dd>
<dt><i>num_params</i></dt>
<dd>Specifies the number of values in the parameter list.</dd>
<dt><i>params</i></dt>
<dd>Specifies a pointer to a list of values to be stored in the message.</dd></dl>
<h2>Description</h2>
<p>The <code>XtAppErrorMsg</code> function calls the high-level error handler and passes the specified information. </p>
<p> The <code>XtAppSetErrorMsgHandler</code> function registers the specified procedure, which is called when a fatal error occurs. </p>
<p> The <code>XtAppSetWarningMsgHandler</code> function registers the specified procedure, which is called when a nonfatal error condition occurs. </p>
<p> The <code>XtAppWarningMsg</code> function calls the high-level error handler and passes the specified information.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappgeterrordatabase/">XtAppGetErrorDatabase</a>(3), <a href="/docs/linux/man/3-xtapperror/">XtAppError</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

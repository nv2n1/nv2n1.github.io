---
title: "xtwarningmsg(3)"
name: "xtwarningmsg"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtwarningmsg/"
description: "XtErrorMsg, XtSetErrorMsgHandler, XtWarningMsg, XtSetWarningMsgHandler – high-level error handlers"
---

<p>XtErrorMsg, XtSetErrorMsgHandler, XtWarningMsg, XtSetWarningMsgHandler &#8211; high-level error handlers </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtErrorMsg(const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</dd>
<dd>void XtSetErrorMsgHandler(XtErrorMsgHandler <i>msg_handler</i>);</dd>
<dd>void XtSetWarningMsgHandler(XtErrorMsgHandler <i>msg_handler</i>);</dd>
<dd>void XtWarningMsg(const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>class</i></dt>
<dd>Specifies the resource class of the error message.</dd>
<dt><i>default</i></dt>
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
<p>The <code>XtErrorMsg</code> function has been superceded by <code>XtAppErrorMsg</code>. </p>
<p> The <code>XtSetErrorMsgHandler</code> function has been superceded by <code>XtAppSetErrorMsgHandler</code>. </p>
<p> The <code>XtSetWarningMsgHandler</code> function has been superceded by <code>XtAppSetWarningMsgHandler</code>. </p>
<p> The <code>XtWarningMsg</code> function has been superceded by <code>XtAppWarningMsg</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtapperrormsg/">XtAppErrorMsg</a></code>(3)<br/>
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>

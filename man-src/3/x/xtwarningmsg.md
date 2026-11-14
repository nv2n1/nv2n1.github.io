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
<dd>void XtErrorMsg(const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</p>
<dd>void XtSetErrorMsgHandler(XtErrorMsgHandler <i>msg_handler</i>);</p>
<dd>void XtSetWarningMsgHandler(XtErrorMsgHandler <i>msg_handler</i>);</p>
<dd>void XtWarningMsg(const char *<i>name</i>, const char *<i>type</i>, const char *<i>class</i>, const char *<i>defaultMsg</i>, String *<i>params</i>, Cardinal *<i>num_params</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>class</i></p>
<dd>Specifies the resource class of the error message.</p>
<dt><i>default</i></p>
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
<p>The <code>XtErrorMsg</code> function has been superceded by <code>XtAppErrorMsg</code>. </p>
<p> The <code>XtSetErrorMsgHandler</code> function has been superceded by <code>XtAppSetErrorMsgHandler</code>. </p>
<p> The <code>XtSetWarningMsgHandler</code> function has been superceded by <code>XtAppSetWarningMsgHandler</code>. </p>
<p> The <code>XtWarningMsg</code> function has been superceded by <code>XtAppWarningMsg</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtapperrormsg/">XtAppErrorMsg</a></code>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

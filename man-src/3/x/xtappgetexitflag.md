---
title: "xtappgetexitflag(3)"
name: "xtappgetexitflag"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappgetexitflag/"
description: "XtAppSetExitFlag, XtAppGetExitFlag – thread support functions"
---

<p>XtAppSetExitFlag, XtAppGetExitFlag &#8211; thread support functions </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppSetExitFlag(XtAppContext <i>app_context</i>);</p>
<dd>Boolean XtAppGetExitFlag(XtAppContext <i>app_context</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</dl>
<h2>Description</h2>
<p>To indicate that an application context should exit, use <code>XtAppSetExitFlag</code>. </p>
<p> To test the exit status of an application context, use <code>XtAppGetExitFlag</code>.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

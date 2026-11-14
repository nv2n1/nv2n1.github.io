---
title: "xtappgetselectiontimeout(3)"
name: "xtappgetselectiontimeout"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappgetselectiontimeout/"
description: "XtAppGetSelectionTimeout, XtAppSetSelectionTimeout – set and obtain selection timeout values"
---

<p>XtAppGetSelectionTimeout, XtAppSetSelectionTimeout &#8211; set and obtain selection timeout values </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>unsigned long XtAppGetSelectionTimeout(XtAppContext <i>app_context</i>);</p>
<dd>void XtAppSetSelectionTimeout(XtAppContext <i>app_context</i>, unsigned long <i>timeout</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>timeout</i></p>
<dd>Specifies the selection timeout in milliseconds.</dl>
<h2>Description</h2>
<p>The <code>XtAppGetSelectionTimeout</code> function returns the current selection timeout value, in milliseconds. The selection timeout is the time within which the two communicating applications must respond to one another. The initial timeout value is set by the <code>selectionTimeout</code> application resource, or, if <code>selectionTimeout</code> is not specified, it defaults to five seconds. </p>
<p> The <code>XtAppSetSelectionTimeout</code> function sets the Intrinsics&#8217;s selection timeout mechanism. Note that most applications should not set the selection timeout.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtownselection/">XtOwnSelection</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

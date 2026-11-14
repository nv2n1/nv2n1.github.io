---
title: "xtgetselectiontimeout(3)"
name: "xtgetselectiontimeout"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetselectiontimeout/"
description: "XtGetSelectionTimeout, XtSetSelectionTimeout – set and obtain selection timeout values"
---

<p>XtGetSelectionTimeout, XtSetSelectionTimeout &#8211; set and obtain selection timeout values </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>unsigned long XtGetSelectionTimeout(void);</p>
<dd>void XtSetSelectionTimeout(unsigned long <i>timeout</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>timeout</i></p>
<dd>Specifies the selection timeout in milliseconds.</dl>
<h2>Description</h2>
<p>The <code>XtGetSelectionTimeout</code> function has been superceded by <code>XtAppGetSelectionTimeout</code>. </p>
<p> The <code>XtSetSelectionTimeout</code> function has been superceded by <code>XtAppSetSelectionTimeout</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xtappgetselectiontimeout/">XtAppGetSelectionTimeout</a></code>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

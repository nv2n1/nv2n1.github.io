---
title: "xtaddactions(3)"
name: "xtaddactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaddactions/"
description: "XtAddActions – register an action table"
---

<p>XtAddActions &#8211; register an action table </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAddActions(XtActionList <i>actions</i>, Cardinal <i>num_actions</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>actions</i></dt>
<dd>Specifies the action table to register.</dd>
<dt><i>num_args</i></dt>
<dd>Specifies the number of entries in this action table.</dd></dl>
<h2>Description</h2>
<p><code>XtAddActions</code> has been replaced by <code>XtAppAddActions</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddactions/">XtAppAddActions</a>(3)<br/>
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>

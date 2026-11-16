---
title: "xtsessionreturntoken(3)"
name: "xtsessionreturntoken"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsessionreturntoken/"
description: "XtSessionGetToken, XtSessionReturnToken – token management for checkpointing"
---

<p>XtSessionGetToken, XtSessionReturnToken &#8211; token management for checkpointing </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtCheckpointToken XtSessionGetToken(Widget <i>w</i>);</dd>
<dd>void XtSessionReturnToken(XtCheckpointToken <i>token</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></dt>
<dd>Specifies the session widget.</dd>
<dt><i>token</i></dt>
<dd>Specifies the token to be returned.</dd></dl>
<h2>Description</h2>
<p>The <code>XtSessionGetToken</code> function will return NULL if the checkpoint operation instigated by the session manager is not currently under way. </p>
<p> To indicate the completion of a deferred save operation and to return the checkpoint token use <code>XtSessionReturnToken</code>.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

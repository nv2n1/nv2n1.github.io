---
title: "xtremoveworkproc(3)"
name: "xtremoveworkproc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtremoveworkproc/"
description: "XtAppAddWorkProc, XtRemoveWorkProc – Add and remove background processing procedures"
---

<p>XtAppAddWorkProc, XtRemoveWorkProc &#8211; Add and remove background processing procedures </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtWorkProcId XtAppAddWorkProc(XtAppContext <i>app_context</i>, XtWorkProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveWorkProc(XtWorkProcId <i>id</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context that identifies the application.</p>
<dt><i>client_data</i></p>
<dd>Specifies the argument that is to be passed to the specified procedure when it is called.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be called.</p>
<dt><i>id</i></p>
<dd>Specifies which work procedure to remove.</dl>
<h2>Description</h2>
<p>The <code>XtAppAddWorkProc</code> function adds the specified work procedure for the application identified by app_context. </p>
<p> The <code>XtRemoveWorkProc</code> function explicitly removes the specified background work procedure.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappnextevent/">XtAppNextEvent</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

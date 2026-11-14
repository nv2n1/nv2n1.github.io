---
title: "xtappaddsignal(3)"
name: "xtappaddsignal"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappaddsignal/"
description: "XtAppAddSignal, XtRemoveSignal, XtNoticeSignal – register and remove a signal source"
---

<p>XtAppAddSignal, XtRemoveSignal, XtNoticeSignal &#8211; register and remove a signal source </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtSignalId XtAppAddSignal(XtAppContext <i>app_context</i>, XtSignalCallbackProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveSignal(XtSignalId <i>id</i>);</p>
<dd>void XtNoticeSignal(XtSignalId <i>id</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>client_data</i></p>
<dd>Specifies the argument that is to be passed to the specified procedure when a signal has been raised.</p>
<dt><i>id</i></p>
<dd>Specifies the ID returned from the corresponding <code>XtAppAddSignal</code> call.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be called when the signal has been raised.</dl>
<h2>Description</h2>
<p>The <code>XtAppAddSignal</code> function initiates a mechanism for handling signals within the context of the Intrinsics. Prior to establishing an operating system dependent signal handler the application may call <code>XtAppAddSignal</code> and store the returned <i>id</i> in a place accessible to the signal handler. </p>
<p> Upon receipt of a signal from the operating system, the application may call <code>XtNoticeSignal</code> passing the <i>id</i> returned by the call to <code>XtAppAddSignal</code>. </p>
<p> <code>XtNoticeSignal</code> is the only Intrinsics function that can safely be called from a signal handler. If <code>XtNoticeSignal</code> is called multiple times before the Intrinsics are able to invoke the registered callback, the callback is only called once. Logically the Intrinsics maintain &#8220;pending&#8221; for each registered callback. This flag is initially <code>False</code> and is set to <code>True</code> by <code>XtNoticeSignal</code>; the Intrinsics invoke the callback whenever the flag is <code>True</code>, and the flag is set to <code>False</code> just before the callback is invoked. </p>
<p> The <code>XtRemoveSignal</code> function is called to remove the specified Intrinsics signal handler. The client should disable the source of the signal before calling <code>XtRemoveSignal</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddtimeout/">XtAppAddTimeOut</a>(3),<a href="/docs/linux/man/3-xtappaddinput/">XtAppAddInput</a>(3),<a href="/docs/linux/man/3-xtappaddworkproc/">XtAppAddWorkProc</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

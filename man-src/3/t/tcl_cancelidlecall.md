---
title: "tcl_cancelidlecall(3)"
name: "tcl_cancelidlecall"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_cancelidlecall/"
description: "Tcl_DoWhenIdle, Tcl_CancelIdleCall – invoke a procedure when there are no pending events"
---

<p>Tcl_DoWhenIdle, Tcl_CancelIdleCall &#8211; invoke a procedure when there are no pending events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_DoWhenIdle</code>(<i>proc, clientData</i>)
<code>Tcl_CancelIdleCall</code>(<i>proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_IdleProc <i>*proc</i> (in) Procedure to invoke.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_DoWhenIdle</code> arranges for <i>proc</i> to be invoked when the application becomes idle. The application is considered to be idle when <code>Tcl_DoOneEvent</code> has been called, could not find any events to handle, and is about to go to sleep waiting for an event to occur. At this point all pending <code>Tcl_DoWhenIdle</code> handlers are invoked. For each call to <code>Tcl_DoWhenIdle</code> there will be a single call to <i>proc</i>; after <i>proc</i> is invoked the handler is automatically removed. <code>Tcl_DoWhenIdle</code> is only usable in programs that use <code>Tcl_DoOneEvent</code> to dispatch events. </p>
<p> <i>Proc</i> should have arguments and result that match the type <code>Tcl_IdleProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_IdleProc(ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tcl_DoWhenIdle</code>. Typically, <i>clientData</i> points to a data structure containing application-specific information about what <i>proc</i> should do. </p>
<p> <code>Tcl_CancelIdleCall</code> may be used to cancel one or more previous calls to <code>Tcl_DoWhenIdle</code>: if there is a <code>Tcl_DoWhenIdle</code> handler registered for <i>proc</i> and <i>clientData</i>, then it is removed without invoking it. If there is more than one handler on the idle list that refers to <i>proc</i> and <i>clientData</i>, all of the handlers are removed. If no existing handlers match <i>proc</i> and <i>clientData</i> then nothing happens. </p>
<p> <code>Tcl_DoWhenIdle</code> is most useful in situations where (a) a piece of work will have to be done but (b) it is possible that something will happen in the near future that will change what has to be done or require something different to be done. <code>Tcl_DoWhenIdle</code> allows the actual work to be deferred until all pending events have been processed. At this point the exact work to be done will presumably be known and it can be done exactly once. </p>
<p> For example, <code>Tcl_DoWhenIdle</code> might be used by an editor to defer display updates until all pending commands have been processed. Without this feature, redundant redisplays might occur in some situations, such as the processing of a command file.</p>
<h2>Bugs</h2>
<p>At present it is not safe for an idle callback to reschedule itself continuously. This will interact badly with certain features of Tk that attempt to wait for all idle callbacks to complete. If you would like for an idle callback to reschedule itself continuously, it is better to use a timer handler with a zero timeout period. </p>
<h2>Keywords</h2>
<p>callback, defer, idle callback</p>

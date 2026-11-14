---
title: "tcl_createtimerhandler(3)"
name: "tcl_createtimerhandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createtimerhandler/"
description: "Tcl_CreateTimerHandler, Tcl_DeleteTimerHandler – call a procedure at a given time"
---

<p>Tcl_CreateTimerHandler, Tcl_DeleteTimerHandler &#8211; call a procedure at a given time </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_TimerToken
<code>Tcl_CreateTimerHandler</code>(<i>milliseconds, proc, clientData</i>)
<code>Tcl_DeleteTimerHandler</code>(<i>token</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>milliseconds</i> (in) How many milliseconds to wait before invoking <i>proc</i>.</p>
<dd>Tcl_TimerProc <i>*proc</i> (in) Procedure to invoke after <i>milliseconds</i> have elapsed.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>.</p>
<dd>Tcl_TimerToken <i>token</i> (in) Token for previously created timer handler (the return value from some previous call to <code>Tcl_CreateTimerHandler</code>). </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateTimerHandler</code> arranges for <i>proc</i> to be invoked at a time <i>milliseconds</i> milliseconds in the future. The callback to <i>proc</i> will be made by <code>Tcl_DoOneEvent</code>, so <code>Tcl_CreateTimerHandler</code> is only useful in programs that dispatch events through <code>Tcl_DoOneEvent</code> or through Tcl commands such as <code>vwait</code>. The call to <i>proc</i> may not be made at the exact time given by <i>milliseconds</i>: it will be made at the next opportunity after that time. For example, if <code>Tcl_DoOneEvent</code> is not called until long after the time has elapsed, or if there are other pending events to process before the call to <i>proc</i>, then the call to <i>proc</i> will be delayed. </p>
<p> <i>Proc</i> should have arguments and return value that match the type <code>Tcl_TimerProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_TimerProc(ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tcl_CreateTimerHandler</code> when the callback was created. Typically, <i>clientData</i> points to a data structure containing application-specific information about what to do in <i>proc</i>. </p>
<p> <code>Tcl_DeleteTimerHandler</code> may be called to delete a previously created timer handler. It deletes the handler indicated by <i>token</i> so that no call to <i>proc</i> will be made; if that handler no longer exists (e.g. because the time period has already elapsed and <i>proc</i> has been invoked then <code>Tcl_DeleteTimerHandler</code> does nothing. The tokens returned by <code>Tcl_CreateTimerHandler</code> never have a value of NULL, so if NULL is passed to <code>Tcl_DeleteTimerHandler</code> then the procedure does nothing. </p>
<h2>Keywords</h2>
<p>callback, clock, handler, timer</p>

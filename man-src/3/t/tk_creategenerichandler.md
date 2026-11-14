---
title: "tk_creategenerichandler(3)"
name: "tk_creategenerichandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_creategenerichandler/"
description: "Tk_CreateGenericHandler, Tk_DeleteGenericHandler – associate procedure callback with all X events"
---

<p>Tk_CreateGenericHandler, Tk_DeleteGenericHandler &#8211; associate procedure callback with all X events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_CreateGenericHandler</code>(<i>proc, clientData</i>)
<code>Tk_DeleteGenericHandler</code>(<i>proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_GenericProc <i>*proc</i> (in) Procedure to invoke whenever any X event occurs on any display.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_CreateGenericHandler</code> arranges for <i>proc</i> to be invoked in the future whenever any X event occurs. This mechanism is <i>not</i> intended for dispatching X events on windows managed by Tk (you should use <code>Tk_CreateEventHandler</code> for this purpose). <code>Tk_CreateGenericHandler</code> is intended for other purposes, such as tracing X events, monitoring events on windows not owned by Tk, accessing X-related libraries that were not originally designed for use with Tk, and so on. </p>
<p> The callback to <i>proc</i> will be made by <code>Tk_HandleEvent</code>; this mechanism only works in programs that dispatch events through <code>Tk_HandleEvent</code> (or through other Tk procedures that call <code>Tk_HandleEvent</code>, such as <code>Tk_DoOneEvent</code> or <code>Tk_MainLoop</code>). </p>
<p> <i>Proc</i> should have arguments and result that match the type <code>Tk_GenericProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_GenericProc(
 ClientData <i>clientData</i>,
 XEvent *<i>eventPtr</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tk_CreateGenericHandler</code> when the callback was created. Typically, <i>clientData</i> points to a data structure containing application-specific information about how to handle events. <i>EventPtr</i> is a pointer to the X event. </p>
<p> Whenever an X event is processed by <code>Tk_HandleEvent</code>, <i>proc</i> is called. The return value from <i>proc</i> is normally 0. A non-zero return value indicates that the event is not to be handled further; that is, <i>proc</i> has done all processing that is to be allowed for the event. </p>
<p> If there are multiple generic event handlers, each one is called for each event, in the order in which they were established. </p>
<p> <code>Tk_DeleteGenericHandler</code> may be called to delete a previously-created generic event handler: it deletes each handler it finds that matches the <i>proc</i> and <i>clientData</i> arguments. If no such handler exists, then <code>Tk_DeleteGenericHandler</code> returns without doing anything. Although Tk supports it, it&#8217;s probably a bad idea to have more than one callback with the same <i>proc</i> and <i>clientData</i> arguments. </p>
<p> Establishing a generic event handler does nothing to ensure that the process will actually receive the X events that the handler wants to process. For example, it is the caller&#8217;s responsibility to invoke <code>XSelectInput</code> to select the desired events, if that is necessary.</p>
<h2>Keywords</h2>
<p>bind, callback, event, handler</p>

---
title: "tk_deleteeventhandler(3)"
name: "tk_deleteeventhandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_deleteeventhandler/"
description: "Tk_CreateEventHandler, Tk_DeleteEventHandler – associate procedure callback with an X event"
---

<p>Tk_CreateEventHandler, Tk_DeleteEventHandler &#8211; associate procedure callback with an X event </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_CreateEventHandler</code>(<i>tkwin, mask, proc, clientData</i>)
<code>Tk_DeleteEventHandler</code>(<i>tkwin, mask, proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which events may occur.</p>
<dd>unsigned long <i>mask</i> (in) Bit-mask of events (such as <code>ButtonPressMask</code>) for which <i>proc</i> should be called.</p>
<dd>Tk_EventProc <i>*proc</i> (in) Procedure to invoke whenever an event in <i>mask</i> occurs in the window given by <i>tkwin</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_CreateEventHandler</code> arranges for <i>proc</i> to be invoked in the future whenever one of the event types specified by <i>mask</i> occurs in the window specified by <i>tkwin</i>. The callback to <i>proc</i> will be made by <code>Tk_HandleEvent</code>; this mechanism only works in programs that dispatch events through <code>Tk_HandleEvent</code> (or through other Tk procedures that call <code>Tk_HandleEvent</code>, such as <code>Tk_DoOneEvent</code> or <code>Tk_MainLoop</code>). </p>
<p> <i>Proc</i> should have arguments and result that match the type <code>Tk_EventProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_EventProc(
 ClientData <i>clientData</i>,
 XEvent *<i>eventPtr</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tk_CreateEventHandler</code> when the callback was created. Typically, <i>clientData</i> points to a data structure containing application-specific information about the window in which the event occurred. <i>EventPtr</i> is a pointer to the X event, which will be one of the ones specified in the <i>mask</i> argument to <code>Tk_CreateEventHandler</code>. </p>
<p> <code>Tk_DeleteEventHandler</code> may be called to delete a previously-created event handler: it deletes the first handler it finds that is associated with <i>tkwin</i> and matches the <i>mask</i>, <i>proc</i>, and <i>clientData</i> arguments. If no such handler exists, then <code>Tk_HandleEvent</code> returns without doing anything. Although Tk supports it, it&#8217;s probably a bad idea to have more than one callback with the same <i>mask</i>, <i>proc</i>, and <i>clientData</i> arguments. When a window is deleted all of its handlers will be deleted automatically; in this case there is no need to call <code>Tk_DeleteEventHandler</code>. </p>
<p> If multiple handlers are declared for the same type of X event on the same window, then the handlers will be invoked in the order they were created. </p>
<h2>Keywords</h2>
<p>bind, callback, event, handler</p>

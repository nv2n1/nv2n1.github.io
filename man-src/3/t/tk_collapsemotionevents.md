---
title: "tk_collapsemotionevents(3)"
name: "tk_collapsemotionevents"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_collapsemotionevents/"
description: "Tk_CollapseMotionEvents, Tk_QueueWindowEvent – Add a window event to the Tcl event queue"
---

<p>Tk_CollapseMotionEvents, Tk_QueueWindowEvent &#8211; Add a window event to the Tcl event queue </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_CollapseMotionEvents</code>(<i>display, collapse</i>)
<code>Tk_QueueWindowEvent</code>(<i>eventPtr, position</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Display <i>*display</i> (in) Display for which to control motion event collapsing.</p>
<dd>int <i>collapse</i> (in) Indicates whether motion events should be collapsed or not.</p>
<dd>XEvent <i>*eventPtr</i> (in) An event to add to the event queue. It is important that all unused fields of the structure be set to zero.</p>
<dd>Tcl_QueuePosition <i>position</i> (in) Where to add the new event in the queue: <code>TCL_QUEUE_TAIL</code>, <code>TCL_QUEUE_HEAD</code>, or <code>TCL_QUEUE_MARK</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_QueueWindowEvent</code> places a window event on Tcl&#8217;s internal event queue for eventual servicing. It creates a Tcl_Event structure, copies the event into that structure, and calls <code>Tcl_QueueEvent</code> to add the event to the queue. When the event is eventually removed from the queue it is processed just like all window events. </p>
<p> When multiple motion events are received for the same window in rapid succession, they are collapsed by default. This behavior can be controlled with <code>Tk_CollapseMotionEvents</code>. <code>Tk_CollapseMotionEvents</code> always returns the previous value for collapse behavior on the <i>display</i>. </p>
<p> The <i>position</i> argument to <code>Tk_QueueWindowEvent</code> has the same significance as for <code>Tcl_QueueEvent</code>; see the documentation for <code>Tcl_QueueEvent</code> for details. </p>
<h2>Keywords</h2>
<p>callback, clock, handler, modal timeout, events</p>

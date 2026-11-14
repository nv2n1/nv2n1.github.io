---
title: "tcl_dooneevent(3)"
name: "tcl_dooneevent"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_dooneevent/"
description: "Tcl_DoOneEvent – wait for events and invoke event handlers"
---

<p>Tcl_DoOneEvent &#8211; wait for events and invoke event handlers </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_DoOneEvent</code>(<i>flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>flags</i> (in) This parameter is normally zero. It may be an OR-ed combination of any of the following flag bits: <code>TCL_WINDOW_EVENTS</code>, <code>TCL_FILE_EVENTS</code>, <code>TCL_TIMER_EVENTS</code>, <code>TCL_IDLE_EVENTS</code>, <code>TCL_ALL_EVENTS</code>, or <code>TCL_DONT_WAIT</code>. </p>
</dl>
<h2>Description</h2>
<p>This procedure is the entry point to Tcl&#8217;s event loop; it is responsible for waiting for events and dispatching event handlers created with procedures such as <code>Tk_CreateEventHandler</code>, <code>Tcl_CreateFileHandler</code>, <code>Tcl_CreateTimerHandler</code>, and <code>Tcl_DoWhenIdle</code>. <code>Tcl_DoOneEvent</code> checks to see if events are already present on the Tcl event queue; if so, it calls the handler(s) for the first (oldest) event, removes it from the queue, and returns. If there are no events ready to be handled, then <code>Tcl_DoOneEvent</code> checks for new events from all possible sources. If any are found, it puts all of them on Tcl&#8217;s event queue, calls handlers for the first event on the queue, and returns. If no events are found, <code>Tcl_DoOneEvent</code> checks for <code>Tcl_DoWhenIdle</code> callbacks; if any are found, it invokes all of them and returns. Finally, if no events or idle callbacks have been found, then <code>Tcl_DoOneEvent</code> sleeps until an event occurs; then it adds any new events to the Tcl event queue, calls handlers for the first event, and returns. The normal return value is 1 to signify that some event was processed (see below for other alternatives). </p>
<p> If the <i>flags</i> argument to <code>Tcl_DoOneEvent</code> is non-zero, it restricts the kinds of events that will be processed by <code>Tcl_DoOneEvent</code>. <i>Flags</i> may be an OR-ed combination of any of the following bits:</p>
<dl COMPACT>
<dt><code>TCL_WINDOW_EVENTS</code> &#8211;</p>
<dd>Process window system events.</p>
<dt><code>TCL_FILE_EVENTS</code> &#8211;</p>
<dd>Process file events.</p>
<dt><code>TCL_TIMER_EVENTS</code> &#8211;</p>
<dd>Process timer events.</p>
<dt><code>TCL_IDLE_EVENTS</code> &#8211;</p>
<dd>Process idle callbacks.</p>
<dt><code>TCL_ALL_EVENTS</code> &#8211;</p>
<dd>Process all kinds of events: equivalent to OR-ing together all of the above flags or specifying none of them.</p>
<dt><code>TCL_DONT_WAIT</code> &#8211;</p>
<dd>Do not sleep: process only events that are ready at the time of the call.</dl>
<p> If any of the flags <code>TCL_WINDOW_EVENTS</code>, <code>TCL_FILE_EVENTS</code>, <code>TCL_TIMER_EVENTS</code>, or <code>TCL_IDLE_EVENTS</code> is set, then the only events that will be considered are those for which flags are set. Setting none of these flags is equivalent to the value <code>TCL_ALL_EVENTS</code>, which causes all event types to be processed. If an application has defined additional event sources with <code>Tcl_CreateEventSource</code>, then additional <i>flag</i> values may also be valid, depending on those event sources. </p>
<p> The <code>TCL_DONT_WAIT</code> flag causes <code>Tcl_DoOneEvent</code> not to put the process to sleep: it will check for events but if none are found then it returns immediately with a return value of 0 to indicate that no work was done. <code>Tcl_DoOneEvent</code> will also return 0 without doing anything if the only alternative is to block forever (this can happen, for example, if <i>flags</i> is <code>TCL_IDLE_EVENTS</code> and there are no <code>Tcl_DoWhenIdle</code> callbacks pending, or if no event handlers or timer handlers exist). </p>
<p> <code>Tcl_DoOneEvent</code> may be invoked recursively. For example, it is possible to invoke <code>Tcl_DoOneEvent</code> recursively from a handler called by <code>Tcl_DoOneEvent</code>. This sort of operation is useful in some modal situations, such as when a notification dialog has been popped up and an application wishes to wait for the user to click a button in the dialog before doing anything else. </p>
<h2>Keywords</h2>
<p>callback, event, handler, idle, timer</p>

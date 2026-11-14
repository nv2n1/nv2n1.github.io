---
title: "xtappprocessevent(3)"
name: "xtappprocessevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappprocessevent/"
description: "XtAppNextEvent, XtAppPending, XtAppPeekEvent, XtAppProcessEvent, XtDispatchEvent, XtAppMainLoop – query and process events and input"
---

<p>XtAppNextEvent, XtAppPending, XtAppPeekEvent, XtAppProcessEvent, XtDispatchEvent, XtAppMainLoop &#8211; query and process events and input </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppNextEvent(XtAppContext <i>app_context</i>, XEvent *<i>event_return</i>);</p>
<dd>Boolean XtAppPeekEvent(XtAppContext <i>app_context</i>, XEvent *<i>event_return</i>);</p>
<dd>XtInputMask XtAppPending(XtAppContext <i>app_context</i>);</p>
<dd>void XtAppProcessEvent(XtAppContext <i>app_context</i>, XtInputMask <i>mask</i>);</p>
<dd>Boolean XtDispatchEvent(XEvent *<i>event</i>);</p>
<dd>void XtAppMainLoop(XtAppContext <i>app_context</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context that identifies the application.</p>
<dt><i>event</i></p>
<dd>Specifies a pointer to the event structure that is to be dispatched to the appropriate event handler.</p>
<dt><i>event_return</i></p>
<dd>Returns the event information to the specified event structure.</p>
<dt><i>mask</i></p>
<dd>Specifies what types of events to process. The mask is the bitwise inclusive OR of any combination of <code>XtIMXEvent</code>, <code>XtIMTimer</code>, <code>XtIMAlternateInput</code>, and <code>XtIMSignal</code>. As a convenience, the X Toolkit defines the symbolic name <code>XtIMAll</code> to be the bitwise inclusive OR of all event types.</dl>
<h2>Description</h2>
<p>If the X event queue is empty, <code>XtAppNextEvent</code> flushes the X output buffers of each Display in the application context and waits for an event while looking at the other input sources, timeout timeout values, and signal handlers and calling any callback procedures triggered by them. This wait time can be used for background processing (see Section 7.8). </p>
<p> If there is an event in the queue, <code>XtAppPeekEvent</code> fills in the event and returns a nonzero value. If no X input is on the queue, <code>XtAppPeekEvent</code> flushes the output buffer and blocks until input is available (possibly calling some timeout callbacks in the process). If the input is an event, <code>XtAppPeekEvent</code> fills in the event and returns a nonzero value. Otherwise, the input is for an alternate input source, and <code>XtAppPeekEvent</code> returns zero. </p>
<p> The <code>XtAppPending</code> function returns a nonzero value if there are events pending from the X server, timer pending, or other input sources pending. The value returned is a bit mask that is the OR of <code>XtIMXEvent</code>, <code>XtIMTimer</code>, <code>XtIMAlternateInput</code>, and <code>XtIMSignal</code> (see <code>XtAppProcessEvent</code>). If there are no events pending, <code>XtAppPending</code> flushes the output buffer and returns zero. </p>
<p> The <code>XtAppProcessEvent</code> function processes one timer, alternate input, signal source, or X event. If there is nothing of the appropriate type to process, <code>XtAppProcessEvent</code> blocks until there is. If there is more than one type of thing available to process, it is undefined which will get processed. Usually, this procedure is not called by client applications (see <code>XtAppMainLoop</code>). <code>XtAppProcessEvent</code> processes timer events by calling any appropriate timer callbacks, alternate input by calling any appropriate alternate input callbacks, signal source by calling any appropriate signal callbacks, and X events by calling <code>XtDispatchEvent</code>. </p>
<p> When an X event is received, it is passed to <code>XtDispatchEvent</code>, which calls the appropriate event handlers and passes them the widget, the event, and client-specific data registered with each procedure. If there are no handlers for that event registered, the event is ignored and the dispatcher simply returns. The order in which the handlers are called is undefined. </p>
<p> The <code>XtDispatchEvent</code> function sends those events to the event handler functions that have been previously registered with the dispatch routine. <code>XtDispatchEvent</code> returns <code>True</code> if it dispatched the event to some handler and <code>False</code> if it found no handler to dispatch the event to. The most common use of <code>XtDispatchEvent</code> is to dispatch events acquired with the <code>XtAppNextEvent</code> procedure. However, it also can be used to dispatch user-constructed events. <code>XtDispatchEvent</code> also is responsible for implementing the grab semantics for <code>XtAddGrab</code>. </p>
<p> The <code>XtAppMainLoop</code> function processes events using <code>XtAppProcessEvent</code>, varying the <i>mask</i> parameter and using <code>XtAppPending</code> to ensure that it has a chance to handle events of all types, i.e., X events, timer events, input events and signal sources. This constitutes the main loop of X Toolkit applications, and, as such, it does not return unless <code>XtAppSetExitFlag</code> is called. Applications are expected to exit in response to some user action. There is nothing special about <code>XtAppMainLoop</code>; it is simply an loop that processes events until <code>XtAppGetExitFlag</code>() returns true. </p>
<p> Applications can provide their own version of this loop, which tests some global termination flag or tests that the number of top-level widgets is larger than zero before circling back for the next event.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

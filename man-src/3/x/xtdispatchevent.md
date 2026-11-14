---
title: "xtdispatchevent(3)"
name: "xtdispatchevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtdispatchevent/"
---

XtAppNextEvent, XtAppPending, XtAppPeekEvent, XtAppProcessEvent, XtDispatchEvent, XtAppMainLoop - query and process events and input 

<h2>Syntax</h2>#include &lt;X11/Intrinsic.h&gt;
<dl COMPACT><dd>void XtAppNextEvent(XtAppContext <i>app_context</i>, XEvent *<i>event_return</i>);
<dd>Boolean XtAppPeekEvent(XtAppContext <i>app_context</i>, XEvent *<i>event_return</i>);
<dd>XtInputMask XtAppPending(XtAppContext <i>app_context</i>);
<dd>void XtAppProcessEvent(XtAppContext <i>app_context</i>, XtInputMask <i>mask</i>);
<dd>Boolean XtDispatchEvent(XEvent *<i>event</i>);
<dd>void XtAppMainLoop(XtAppContext <i>app_context</i>);</dl><h2>Arguments</h2><dl COMPACT><dt><i>app_context</i>
<dd>Specifies the application context that identifies the application.
<dt><i>event</i>
<dd>Specifies a pointer to the event structure that is to be dispatched to the appropriate event handler.
<dt><i>event_return</i>
<dd>Returns the event information to the specified event structure.
<dt><i>mask</i>
<dd>Specifies what types of events to process. The mask is the bitwise inclusive OR of any combination of <b>XtIMXEvent</b>, <b>XtIMTimer</b>, <b>XtIMAlternateInput</b>, and <b>XtIMSignal</b>. As a convenience, the X Toolkit defines the symbolic name <b>XtIMAll</b> to be the bitwise inclusive OR of all event types.</dl><h2>Description</h2>If the X event queue is empty, <b>XtAppNextEvent</b> flushes the X output buffers of each Display in the application context and waits for an event while looking at the other input sources, timeout timeout values, and signal handlers and calling any callback procedures triggered by them. This wait time can be used for background processing (see Section 7.8). 

 If there is an event in the queue, <b>XtAppPeekEvent</b> fills in the event and returns a nonzero value. If no X input is on the queue, <b>XtAppPeekEvent</b> flushes the output buffer and blocks until input is available (possibly calling some timeout callbacks in the process). If the input is an event, <b>XtAppPeekEvent</b> fills in the event and returns a nonzero value. Otherwise, the input is for an alternate input source, and <b>XtAppPeekEvent</b> returns zero. 

 The <b>XtAppPending</b> function returns a nonzero value if there are events pending from the X server, timer pending, or other input sources pending. The value returned is a bit mask that is the OR of <b>XtIMXEvent</b>, <b>XtIMTimer</b>, <b>XtIMAlternateInput</b>, and <b>XtIMSignal</b> (see <b>XtAppProcessEvent</b>). If there are no events pending, <b>XtAppPending</b> flushes the output buffer and returns zero. 

 The <b>XtAppProcessEvent</b> function processes one timer, alternate input, signal source, or X event. If there is nothing of the appropriate type to process, <b>XtAppProcessEvent</b> blocks until there is. If there is more than one type of thing available to process, it is undefined which will get processed. Usually, this procedure is not called by client applications (see <b>XtAppMainLoop</b>). <b>XtAppProcessEvent</b> processes timer events by calling any appropriate timer callbacks, alternate input by calling any appropriate alternate input callbacks, signal source by calling any appropriate signal callbacks, and X events by calling <b>XtDispatchEvent</b>. 

 When an X event is received, it is passed to <b>XtDispatchEvent</b>, which calls the appropriate event handlers and passes them the widget, the event, and client-specific data registered with each procedure. If there are no handlers for that event registered, the event is ignored and the dispatcher simply returns. The order in which the handlers are called is undefined. 

 The <b>XtDispatchEvent</b> function sends those events to the event handler functions that have been previously registered with the dispatch routine. <b>XtDispatchEvent</b> returns <b>True</b> if it dispatched the event to some handler and <b>False</b> if it found no handler to dispatch the event to. The most common use of <b>XtDispatchEvent</b> is to dispatch events acquired with the <b>XtAppNextEvent</b> procedure. However, it also can be used to dispatch user-constructed events. <b>XtDispatchEvent</b> also is responsible for implementing the grab semantics for <b>XtAddGrab</b>. 

 The <b>XtAppMainLoop</b> function processes events using <b>XtAppProcessEvent</b>, varying the <i>mask</i> parameter and using <b>XtAppPending</b> to ensure that it has a chance to handle events of all types, i.e., X events, timer events, input events and signal sources. This constitutes the main loop of X Toolkit applications, and, as such, it does not return unless <b>XtAppSetExitFlag</b> is called. Applications are expected to exit in response to some user action. There is nothing special about <b>XtAppMainLoop</b>; it is simply an loop that processes events until <b>XtAppGetExitFlag</b>() returns true. 

 Applications can provide their own version of this loop, which tests some global termination flag or tests that the number of top-level widgets is larger than zero before circling back for the next event.
<h2>See Also</h2><i>X Toolkit Intrinsics - C Language Interface</i> 
 <i>Xlib - C Language X Interface</i>

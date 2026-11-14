---
title: "xtremoveeventtypehandler(3)"
name: "xtremoveeventtypehandler"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtremoveeventtypehandler/"
description: "XtInsertEventTypeHandler, XtRemoveEventTypeHandler, XtRegisterExtensionSelector, XtSetEventDispatcher, XtDispatchEventToWidget – extension event handling"
---

<p>XtInsertEventTypeHandler, XtRemoveEventTypeHandler, XtRegisterExtensionSelector, XtSetEventDispatcher, XtDispatchEventToWidget &#8211; extension event handling </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtInsertEventTypeHandler(Widget <i>widget</i>, int <i>event_type</i>, XtPointer <i>select_data</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>, XtListPosition <i>position</i>);</p>
<dd>void XtRemoveEventTypeHandler(Widget <i>widget</i>, int <i>event_type</i>, XtPointer <i>select_data</i>, XtEventHandler <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRegisterExtensionSelector(Display* <i>display</i>, int <i>min_event_type</i>, int <i>max_event_type</i>, XtExtensionSelectProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>XtEventDispatchProc XtSetEventDispatcher(Display* <i>display</i>, int <i>event_type</i>, XtEventDispatchProc <i>proc</i>);</p>
<dd>Boolean XtDispatchEventToWidget(Widget <i>widget</i>, XEvent* <i>event</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget for this event handler. Must be of class Core or any subclass thereof.</p>
<dt><i>event_type</i></p>
<dd>Specifies the event type.</p>
<dt><i>select_data</i></p>
<dd>Specifies data used to select or deselect events from the server.</p>
<dt><i>proc</i></p>
<dd>Specifies the proc.</p>
<dt><i>client_data</i></p>
<dd>Specifies additional data to be passed to the event handler.</p>
<dt><i>position</i></p>
<dd>Specifies when the event handler is to be called relative to other previously registered handlers.</p>
<dt><i>display</i></p>
<dd>Specifies the display.</p>
<dt><i>min_event_type, max_event_type</i></p>
<dd>Specifies the range of event types for this extension.</p>
<dt><i>event</i></p>
<dd>Specifies a pointer to the event to be dispatched.</dl>
<h2>Description</h2>
<p>The <code>XtInsertEventTypeHandler</code> function registers a procedure with the dispatch mechanism that is to be called when an event that matches the specified <i>event_type</i> is dispatched to the specified <i>widget</i>. </p>
<p> If <i>event_type</i> is one of the core X protocol events then <i>select_data</i> must be a pointer to a value of type <code>EventMask</code>, indicating the event mask to be used to select for the desired event. This event mask will be included in the value returned by <code>XtBuildEventMask</code>. If the widget is realized <code>XtInsertEventTypeHandler</code> calls <code>XSelectInput</code> if necessary. Specifying NULL for <i>select_data</i> is equivalent to specifying a pointer to an event mask containing 0. This is similar to the <code>XtInsertRawEventHandler</code> function. </p>
<p> If <i>event_type</i> specifies an extension event type then the semantics of the data pointed to by <i>select_data</i> are defined by the extension selector registered for the specified event type. </p>
<p> In either case the Intrinsics are not required to copy the data pointed to by <i>select_data</i>, so the caller must ensure that it remains valid as long as the event handler remains registered with this value of <i>select_data</i>. </p>
<p> The <i>position</i> argument allows the client to control the order of the invocation of event handlers registered for the same event type. If the client does not care about the order, it should normally specify <code>XtListTail</code>, which registers this event handler after any previously registered handlers for this event type. </p>
<p> The <code>XtRemoveEventTypeHandler</code> function unregisters an even handler registered with <code>XtInsertEventTypeHandler</code> for the specified event type. The request is ignored if <i>client_data</i> does not match the value given with the handler was registered. </p>
<p> If <i>event_type</i> specifies on of the core X protocol events, <i>select_data</i> must be a pointer to a value of type <code>EventMask</code>, indicating the mask to be used to deselect for the appropriate event. If the widget is realized, <code>XtRemoveEventTypeHandler</code> calls <code>XSelectInput</code> if necessary. Specifying NULL for <i>select_data</i> is equivalent to specifying a pointer to an event mask containing 0. This is similar to the <code>XtRemoveRawEventHandler</code> function. </p>
<p> If <i>event_type</i> specifies an extension event type then the semantics of the data pointed to by <i>select_data</i> are defined by the extension selector registered for the specified event type. </p>
<p> The <code>XtRegisterExtensionSelector</code> function registers a procedure to arrange for the delivery of extension events to widgets. </p>
<p> If <i>min_event_type</i> and <i>max_event_type</i> match the parameters to a previous call to <code>XtRegisterExtensionSelector</code> for the same display, the <i>proc</i> and <i>client_data</i> replace the previously registered values. If the range specified by <i>min_event_type</i> and <i>max_event_type</i> overlaps the range of the parameters to a previous call for the same display in any other way, an error results. </p>
<p> The <code>XtSetEventDispatcher</code> function registers the event dispatcher procedure specified by <i>proc</i> for events with the type <i>event_type</i>. The previously registered dispatcher (or the default dispatcher if there was no previously registered dispatcher) is returned. If <i>proc</i> is NULL, the default procedure is restored for the specified type. </p>
<p> In the future, when <code>XtDispatchEvent</code> is called with an event of <i>event_type</i>, the specified <i>proc</i> (or the default dispatcher) will be invoked to determine a widget ot which to dispatch the event. </p>
<p> The <code>XtDispatchEventToWidget</code> function scans the list of registered event handlers for the specified widget and calls each handler that has been registered for the specified event type, subject to the <i>continue_to_dispatch</i> value returned by each handler. The Intrinsics behave as if event handlers were registered at the head of the list for <code>Expose</code>, <code>NoExpose</code>, <code>GraphicsExpose</code>, and <code>VisibilityNotify</code> events to invoke the widget&#8217;s expose procedure according to the exposure compression rules and to update the widget&#8217;s <i>visible</i> field if <i>visible_interest</i> is <code>True</code>. These internal event handlers never set <i>continue_to_dispatch</i> to <code>False</code>. </p>
<p> <code>XtDispatchEventToWidget</code> returns <code>True</code> if any event handler was called and <code>False</code> otherwise. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtgetkeyboardfocuswidget/">XtGetKeyboardFocusWidget</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>

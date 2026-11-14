---
title: "xcheckwindowevent(3)"
name: "xcheckwindowevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcheckwindowevent/"
description: "XNextEvent, XPeekEvent, XWindowEvent, XCheckWindowEvent, XMaskEvent, XCheckMaskEvent, XCheckTypedEvent, XCheckTypedWindowEvent – select events by type"
---

<p>XNextEvent, XPeekEvent, XWindowEvent, XCheckWindowEvent, XMaskEvent, XCheckMaskEvent, XCheckTypedEvent, XCheckTypedWindowEvent &#8211; select events by type </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XNextEvent(Display *<i>display</i>, XEvent *<i>event_return</i>);</p>
<dd>int XPeekEvent(Display *<i>display</i>, XEvent *<i>event_return</i>);</p>
<dd>int XWindowEvent(Display *<i>display</i>, Window <i>w</i>, long <i>event_mask</i>, XEvent *<i>event_return</i>);</p>
<dd>Bool XCheckWindowEvent(Display *<i>display</i>, Window <i>w</i>, long <i>event_mask</i>, XEvent *<i>event_return</i>);</p>
<dd>int XMaskEvent(Display *<i>display</i>, long <i>event_mask</i>, XEvent *<i>event_return</i>);</p>
<dd>Bool XCheckMaskEvent(Display *<i>display</i>, long <i>event_mask</i>, XEvent *<i>event_return</i>);</p>
<dd>Bool XCheckTypedEvent(Display *<i>display</i>, int <i>event_type</i>, XEvent *<i>event_return</i>);</p>
<dd>Bool XCheckTypedWindowEvent(Display *<i>display</i>, Window <i>w</i>, int <i>event_type</i>, XEvent *<i>event_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mask</i></p>
<dd>Specifies the event mask.</p>
<dt><i>event_return</i></p>
<dd>Returns the matched event&#8217;s associated structure.</p>
<dt><i>event_return</i></p>
<dd>Returns the next event in the queue.</p>
<dt><i>event_return</i></p>
<dd>Returns a copy of the matched event&#8217;s associated structure.</p>
<dt><i>event_type</i></p>
<dd>Specifies the event type to be compared.</p>
<dt><i>w</i></p>
<dd>Specifies the window whose event you are interested in.</dl>
<h2>Description</h2>
<p>The <code>XNextEvent</code> function copies the first event from the event queue into the specified <code>XEvent</code> structure and then removes it from the queue. If the event queue is empty, <code>XNextEvent</code> flushes the output buffer and blocks until an event is received. </p>
<p> The <code>XPeekEvent</code> function returns the first event from the event queue, but it does not remove the event from the queue. If the queue is empty, <code>XPeekEvent</code> flushes the output buffer and blocks until an event is received. It then copies the event into the client-supplied <code>XEvent</code> structure without removing it from the event queue. </p>
<p> The <code>XWindowEvent</code> function searches the event queue for an event that matches both the specified window and event mask. When it finds a match, <code>XWindowEvent</code> removes that event from the queue and copies it into the specified <code>XEvent</code> structure. The other events stored in the queue are not discarded. If a matching event is not in the queue, <code>XWindowEvent</code> flushes the output buffer and blocks until one is received. </p>
<p> The <code>XCheckWindowEvent</code> function searches the event queue and then the events available on the server connection for the first event that matches the specified window and event mask. If it finds a match, <code>XCheckWindowEvent</code> removes that event, copies it into the specified <code>XEvent</code> structure, and returns <code>True</code>. The other events stored in the queue are not discarded. If the event you requested is not available, <code>XCheckWindowEvent</code> returns <code>False</code>, and the output buffer will have been flushed. </p>
<p> The <code>XMaskEvent</code> function searches the event queue for the events associated with the specified mask. When it finds a match, <code>XMaskEvent</code> removes that event and copies it into the specified <code>XEvent</code> structure. The other events stored in the queue are not discarded. If the event you requested is not in the queue, <code>XMaskEvent</code> flushes the output buffer and blocks until one is received. </p>
<p> The <code>XCheckMaskEvent</code> function searches the event queue and then any events available on the server connection for the first event that matches the specified mask. If it finds a match, <code>XCheckMaskEvent</code> removes that event, copies it into the specified <code>XEvent</code> structure, and returns <code>True</code>. The other events stored in the queue are not discarded. If the event you requested is not available, <code>XCheckMaskEvent</code> returns <code>False</code>, and the output buffer will have been flushed. </p>
<p> The <code>XCheckTypedEvent</code> function searches the event queue and then any events available on the server connection for the first event that matches the specified type. If it finds a match, <code>XCheckTypedEvent</code> removes that event, copies it into the specified <code>XEvent</code> structure, and returns <code>True</code>. The other events in the queue are not discarded. If the event is not available, <code>XCheckTypedEvent</code> returns <code>False</code>, and the output buffer will have been flushed. </p>
<p> The <code>XCheckTypedWindowEvent</code> function searches the event queue and then any events available on the server connection for the first event that matches the specified type and window. If it finds a match, <code>XCheckTypedWindowEvent</code> removes the event from the queue, copies it into the specified <code>XEvent</code> structure, and returns <code>True</code>. The other events in the queue are not discarded. If the event is not available, <code>XCheckTypedWindowEvent</code> returns <code>False</code>, and the output buffer will have been flushed.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xifevent/">XIfEvent</a>(3), <a href="/docs/linux/man/3-xputbackevent/">XPutBackEvent</a>(3), <a href="/docs/linux/man/3-xsendevent/">XSendEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

---
title: "xpeekifevent(3)"
name: "xpeekifevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xpeekifevent/"
description: "XIfEvent, XCheckIfEvent, XPeekIfEvent – check the event queue with a predicate procedure"
---

<p>XIfEvent, XCheckIfEvent, XPeekIfEvent &#8211; check the event queue with a predicate procedure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XIfEvent(Display *<i>display</i>, XEvent *<i>event_return</i>, Bool (*<i>predicate</i>)(), XPointer <i>arg</i>);</p>
<dd>Bool XCheckIfEvent(Display *<i>display</i>, XEvent *<i>event_return</i>, Bool (*<i>predicate</i>)(), XPointer <i>arg</i>);</p>
<dd>int XPeekIfEvent(Display *<i>display</i>, XEvent *<i>event_return</i>, Bool (*<i>predicate</i>)(), XPointer <i>arg</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>arg</i></p>
<dd>Specifies the user-supplied argument that will be passed to the predicate procedure.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_return</i></p>
<dd>Returns either a copy of or the matched event&#8217;s associated structure.</p>
<dt><i>predicate</i></p>
<dd>Specifies the procedure that is to be called to determine if the next event in the queue matches what you want.</dl>
<h2>Description</h2>
<p>The <code>XIfEvent</code> function completes only when the specified predicate procedure returns <code>True</code> for an event, which indicates an event in the queue matches. <code>XIfEvent</code> flushes the output buffer if it blocks waiting for additional events. <code>XIfEvent</code> removes the matching event from the queue and copies the structure into the client-supplied <code>XEvent</code> structure. </p>
<p> When the predicate procedure finds a match, <code>XCheckIfEvent</code> copies the matched event into the client-supplied <code>XEvent</code> structure and returns <code>True</code>. (This event is removed from the queue.) If the predicate procedure finds no match, <code>XCheckIfEvent</code> returns <code>False</code>, and the output buffer will have been flushed. All earlier events stored in the queue are not discarded. </p>
<p> The <code>XPeekIfEvent</code> function returns only when the specified predicate procedure returns <code>True</code> for an event. After the predicate procedure finds a match, <code>XPeekIfEvent</code> copies the matched event into the client-supplied <code>XEvent</code> structure without removing the event from the queue. <code>XPeekIfEvent</code> flushes the output buffer if it blocks waiting for additional events. </p>
<p> Each of these functions requires you to pass a predicate procedure that determines if an event matches what you want. Your predicate procedure must decide if the event is useful without calling any Xlib functions. If the predicate directly or indirectly causes the state of the event queue to change, the result is not defined. If Xlib has been initialized for threads, the predicate is called with the display locked and the result of a call by the predicate to any Xlib function that locks the display is not defined unless the caller has first called <code>XLockDisplay</code>. </p>
<p> The predicate procedure and its associated arguments are:</p>
<dl COMPACT>
<dd>Bool (*<i>predicate</i>)(Display *<i>display</i>, XEvent *<i>event</i>, XPointer <i>arg</i>)</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event</i></p>
<dd>Specifies the <code>XEvent</code> structure.</p>
<dt><i>arg</i></p>
<dd>Specifies the argument passed in from the <code>XIfEvent</code>, <code>XCheckIfEvent</code>, or <code>XPeekIfEvent</code> function.</dl>
<p> The predicate procedure is called once for each event in the queue until it finds a match. After finding a match, the predicate procedure must return <code>True</code>. If it did not find a match, it must return <code>False</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xnextevent/">XNextEvent</a>(3), <a href="/docs/linux/man/3-xputbackevent/">XPutBackEvent</a>(3) <a href="/docs/linux/man/3-xsendevent/">XSendEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

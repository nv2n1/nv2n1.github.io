---
title: "xgetmotionevents(3)"
name: "xgetmotionevents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetmotionevents/"
description: "XSendEvent, XDisplayMotionBufferSize, XGetMotionEvents, XTimeCoord – send events and pointer motion history structure"
---

<p>XSendEvent, XDisplayMotionBufferSize, XGetMotionEvents, XTimeCoord &#8211; send events and pointer motion history structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XSendEvent(Display *<i>display</i>, Window <i>w</i>, Bool <i>propagate</i>, long <i>event_mask</i>, XEvent *<i>event_send</i>);</p>
<dd>unsigned long XDisplayMotionBufferSize(Display *<i>display</i>);</p>
<dd>XTimeCoord *XGetMotionEvents(Display *<i>display</i>, Window <i>w</i>, Time <i>start</i>, Time <i>stop</i>, int *<i>nevents_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mask</i></p>
<dd>Specifies the event mask.</p>
<dt><i>event_send</i></p>
<dd>Specifies the event that is to be sent.</p>
<dt><i>nevents_return</i></p>
<dd>Returns the number of events from the motion history buffer.</p>
<dt><i>propagate</i></p>
<dd>Specifies a Boolean value.</p>
<dt><i>start</i></p>
<dd>
<dt><i>stop</i></p>
<dd>Specify the time interval in which the events are returned from the motion history buffer. You can pass a timestamp or <code>CurrentTime</code>. <code>PointerWindow</code>, or <code>InputFocus</code>.</p>
<dt><i>w</i></p>
<dd>Specifies the window the window the event is to be sent to.</dl>
<h2>Description</h2>
<p>The <code>XSendEvent</code> function identifies the destination window, determines which clients should receive the specified events, and ignores any active grabs. This function requires you to pass an event mask. For a discussion of the valid event mask names, see section 10.3. This function uses the w argument to identify the destination window as follows:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If w is <code>PointerWindow</code>, the destination window is the window that contains the pointer.</p>
<dt>&bull;</p>
<dd>If w is <code>InputFocus</code> and if the focus window contains the pointer, the destination window is the window that contains the pointer; otherwise, the destination window is the focus window.</dl>
<p> To determine which clients should receive the specified events, <code>XSendEvent</code> uses the propagate argument as follows:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If event_mask is the empty set, the event is sent to the client that created the destination window. If that client no longer exists, no event is sent.</p>
<dt>&bull;</p>
<dd>If propagate is <code>False</code>, the event is sent to every client selecting on destination any of the event types in the event_mask argument.</p>
<dt>&bull;</p>
<dd>If propagate is <code>True</code> and no clients have selected on destination any of the event types in event-mask, the destination is replaced with the closest ancestor of destination for which some client has selected a type in event-mask and for which no intervening window has that type in its do-not-propagate-mask. If no such window exists or if the window is an ancestor of the focus window and <code>InputFocus</code> was originally specified as the destination, the event is not sent to any clients. Otherwise, the event is reported to every client selecting on the final destination any of the types specified in event_mask.</dl>
<p> The event in the <code>XEvent</code> structure must be one of the core events or one of the events defined by an extension (or a <code>BadValue</code> error results) so that the X server can correctly byte-swap the contents as necessary. The contents of the event are otherwise unaltered and unchecked by the X server except to force send_event to <code>True</code> in the forwarded event and to set the serial number in the event correctly; therefore these fields and the display field are ignored by <code>XSendEvent</code>. </p>
<p> <code>XSendEvent</code> returns zero if the conversion to wire protocol format failed and returns nonzero otherwise. <code>XSendEvent</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors. </p>
<p> The server may retain the recent history of the pointer motion and do so to a finer granularity than is reported by <code>MotionNotify</code> events. The <code>XGetMotionEvents</code> function makes this history available. </p>
<p> The <code>XGetMotionEvents</code> function returns all events in the motion history buffer that fall between the specified start and stop times, inclusive, and that have coordinates that lie within the specified window (including its borders) at its present placement. If the server does not support motion history, if the start time is later than the stop time, or if the start time is in the future, no events are returned; <code>XGetMotionEvents</code> returns NULL. If the stop time is in the future, it is equivalent to specifying <code>CurrentTime</code>. <code>XGetMotionEvents</code> can generate a <code>BadWindow</code> error.</p>
<h2>Structures</h2>
<p>The <code>XTimeCoord</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Time time;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short x, y; } XTimeCoord; </p>
<p> The time member is set to the time, in milliseconds. The x and y members are set to the coordinates of the pointer and are reported relative to the origin of the specified window.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xifevent/">XIfEvent</a>(3), <a href="/docs/linux/man/3-xnextevent/">XNextEvent</a>(3), <a href="/docs/linux/man/3-xputbackevent/">XPutBackEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

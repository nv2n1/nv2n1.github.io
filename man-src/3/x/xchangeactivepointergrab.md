---
title: "xchangeactivepointergrab(3)"
name: "xchangeactivepointergrab"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xchangeactivepointergrab/"
description: "XGrabPointer, XUngrabPointer, XChangeActivePointerGrab – grab the pointer"
---

<p>XGrabPointer, XUngrabPointer, XChangeActivePointerGrab &#8211; grab the pointer </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XGrabPointer(Display *<i>display</i>, Window <i>grab_window</i>, Bool <i>owner_events</i>, unsigned int <i>event_mask</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>, Window <i>confine_to</i>, Cursor <i>cursor</i>, Time <i>time</i>);</p>
<dd>int XUngrabPointer(Display *<i>display</i>, Time <i>time</i>);</p>
<dd>int XChangeActivePointerGrab(Display *<i>display</i>, unsigned int <i>event_mask</i>, Cursor <i>cursor</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>confine_to</i></p>
<dd>Specifies the window to confine the pointer in or <code>None</code>.</p>
<dt><i>cursor</i></p>
<dd>Specifies the cursor that is to be displayed during the grab or <code>None</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mask</i></p>
<dd>Specifies which pointer events are reported to the client. The mask is the bitwise inclusive OR of the valid pointer event mask bits.</p>
<dt><i>grab_window</i></p>
<dd>Specifies the grab window.</p>
<dt><i>keyboard_mode</i></p>
<dd>Specifies further processing of keyboard events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</p>
<dt><i>owner_events</i></p>
<dd>Specifies a Boolean value that indicates whether the pointer events are to be reported as usual or reported with respect to the grab window if selected by the event mask.</p>
<dt><i>pointer_mode</i></p>
<dd>Specifies further processing of pointer events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</p>
<dt><i>time</i></p>
<dd>Specifies the time. You can pass either a timestamp or <code>CurrentTime</code>.</dl>
<h2>Description</h2>
<p>The <code>XGrabPointer</code> function actively grabs control of the pointer and returns <code>GrabSuccess</code> if the grab was successful. Further pointer events are reported only to the grabbing client. <code>XGrabPointer</code> overrides any active pointer grab by this client. If owner_events is <code>False</code>, all generated pointer events are reported with respect to grab_window and are reported only if selected by event_mask. If owner_events is <code>True</code> and if a generated pointer event would normally be reported to this client, it is reported as usual. Otherwise, the event is reported with respect to the grab_window and is reported only if selected by event_mask. For either value of owner_events, unreported events are discarded. </p>
<p> If the pointer_mode is <code>GrabModeAsync</code>, pointer event processing continues as usual. If the pointer is currently frozen by this client, the processing of events for the pointer is resumed. If the pointer_mode is <code>GrabModeSync</code>, the state of the pointer, as seen by client applications, appears to freeze, and the X server generates no further pointer events until the grabbing client calls <code>XAllowEvents</code> or until the pointer grab is released. Actual pointer changes are not lost while the pointer is frozen; they are simply queued in the server for later processing. </p>
<p> If the keyboard_mode is <code>GrabModeAsync</code>, keyboard event processing is unaffected by activation of the grab. If the keyboard_mode is <code>GrabModeSync</code>, the state of the keyboard, as seen by client applications, appears to freeze, and the X server generates no further keyboard events until the grabbing client calls <code>XAllowEvents</code> or until the pointer grab is released. Actual keyboard changes are not lost while the pointer is frozen; they are simply queued in the server for later processing. </p>
<p> If a cursor is specified, it is displayed regardless of what window the pointer is in. If <code>None</code> is specified, the normal cursor for that window is displayed when the pointer is in grab_window or one of its subwindows; otherwise, the cursor for grab_window is displayed. </p>
<p> If a confine_to window is specified, the pointer is restricted to stay contained in that window. The confine_to window need have no relationship to the grab_window. If the pointer is not initially in the confine_to window, it is warped automatically to the closest edge just before the grab activates and enter/leave events are generated as usual. If the confine_to window is subsequently reconfigured, the pointer is warped automatically, as necessary, to keep it contained in the window. </p>
<p> The time argument allows you to avoid certain circumstances that come up if applications take a long time to respond or if there are long network delays. Consider a situation where you have two applications, both of which normally grab the pointer when clicked on. If both applications specify the timestamp from the event, the second application may wake up faster and successfully grab the pointer before the first application. The first application then will get an indication that the other application grabbed the pointer before its request was processed. </p>
<p> <code>XGrabPointer</code> generates <code>EnterNotify</code> and <code>LeaveNotify</code> events. </p>
<p> Either if grab_window or confine_to window is not viewable or if the confine_to window lies completely outside the boundaries of the root window, <code>XGrabPointer</code> fails and returns <code>GrabNotViewable</code>. If the pointer is actively grabbed by some other client, it fails and returns <code>AlreadyGrabbed</code>. If the pointer is frozen by an active grab of another client, it fails and returns <code>GrabFrozen</code>. If the specified time is earlier than the last-pointer-grab time or later than the current X server time, it fails and returns <code>GrabInvalidTime</code>. Otherwise, the last-pointer-grab time is set to the specified time is replaced by the current X server time). </p>
<p> <code>XGrabPointer</code> can generate <code>BadCursor</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XUngrabPointer</code> function releases the pointer and any queued events if this client has actively grabbed the pointer from <code>XGrabPointer</code>, <code>XGrabButton</code>, or from a normal button press. <code>XUngrabPointer</code> does not release the pointer if the specified time is earlier than the last-pointer-grab time or is later than the current X server time. It also generates <code>EnterNotify</code> and <code>LeaveNotify</code> events. The X server performs an <code>UngrabPointer</code> request automatically if the event window or confine_to window for an active pointer grab becomes not viewable or if window reconfiguration causes the confine_to window to lie completely outside the boundaries of the root window. </p>
<p> The <code>XChangeActivePointerGrab</code> function changes the specified dynamic parameters if the pointer is actively grabbed by the client and if the specified time is no earlier than the last-pointer-grab time and no later than the current X server time. This function has no effect on the passive parameters of a <code>XGrabButton</code>. The interpretation of event_mask and cursor is the same as described in <code>XGrabPointer</code>. </p>
<p> <code>XChangeActivePointerGrab</code> can generate a <code>BadCursor</code> and <code>BadValue</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallowevents/">XAllowEvents</a>(3), <a href="/docs/linux/man/3-xgrabbutton/">XGrabButton</a>(3), <a href="/docs/linux/man/3-xgrabkey/">XGrabKey</a>(3), <a href="/docs/linux/man/3-xgrabkeyboard/">XGrabKeyboard</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

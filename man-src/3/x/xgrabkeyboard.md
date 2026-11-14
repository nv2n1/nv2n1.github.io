---
title: "xgrabkeyboard(3)"
name: "xgrabkeyboard"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgrabkeyboard/"
description: "XGrabKeyboard, XUngrabKeyboard – grab the keyboard"
---

<p>XGrabKeyboard, XUngrabKeyboard &#8211; grab the keyboard </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XGrabKeyboard(Display *<i>display</i>, Window <i>grab_window</i>, Bool <i>owner_events</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>, Time <i>time</i>);</p>
<dd>int XUngrabKeyboard(Display *<i>display</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>grab_window</i></p>
<dd>Specifies the grab window.</p>
<dt><i>keyboard_mode</i></p>
<dd>Specifies further processing of keyboard events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</p>
<dt><i>owner_events</i></p>
<dd>Specifies a Boolean value that indicates whether the keyboard events are to be reported as usual.</p>
<dt><i>pointer_mode</i></p>
<dd>Specifies further processing of pointer events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</p>
<dt><i>time</i></p>
<dd>Specifies the time. You can pass either a timestamp or <code>CurrentTime</code>.</dl>
<h2>Description</h2>
<p>The <code>XGrabKeyboard</code> function actively grabs control of the keyboard and generates <code>FocusIn</code> and <code>FocusOut</code> events. Further key events are reported only to the grabbing client. <code>XGrabKeyboard</code> overrides any active keyboard grab by this client. If owner_events is <code>False</code>, all generated key events are reported with respect to grab_window. If owner_events is <code>True</code> and if a generated key event would normally be reported to this client, it is reported normally; otherwise, the event is reported with respect to the grab_window. Both <code>KeyPress</code> and <code>KeyRelease</code> events are always reported, independent of any event selection made by the client. </p>
<p> If the keyboard_mode argument is <code>GrabModeAsync</code>, keyboard event processing continues as usual. If the keyboard is currently frozen by this client, then processing of keyboard events is resumed. If the keyboard_mode argument is <code>GrabModeSync</code>, the state of the keyboard (as seen by client applications) appears to freeze, and the X server generates no further keyboard events until the grabbing client issues a releasing <code>XAllowEvents</code> call or until the keyboard grab is released. Actual keyboard changes are not lost while the keyboard is frozen; they are simply queued in the server for later processing. </p>
<p> If pointer_mode is <code>GrabModeAsync</code>, pointer event processing is unaffected by activation of the grab. If pointer_mode is <code>GrabModeSync</code>, the state of the pointer (as seen by client applications) appears to freeze, and the X server generates no further pointer events until the grabbing client issues a releasing <code>XAllowEvents</code> call or until the keyboard grab is released. Actual pointer changes are not lost while the pointer is frozen; they are simply queued in the server for later processing. </p>
<p> If the keyboard is actively grabbed by some other client, <code>XGrabKeyboard</code> fails and returns <code>AlreadyGrabbed</code>. If grab_window is not viewable, it fails and returns <code>GrabNotViewable</code>. If the keyboard is frozen by an active grab of another client, it fails and returns <code>GrabFrozen</code>. If the specified time is earlier than the last-keyboard-grab time or later than the current X server time, it fails and returns <code>GrabInvalidTime</code>. Otherwise, the last-keyboard-grab time is set to the specified time is replaced by the current X server time). </p>
<p> <code>XGrabKeyboard</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XUngrabKeyboard</code> function releases the keyboard and any queued events if this client has it actively grabbed from either <code>XGrabKeyboard</code> or <code>XGrabKey</code>. <code>XUngrabKeyboard</code> does not release the keyboard and any queued events if the specified time is earlier than the last-keyboard-grab time or is later than the current X server time. It also generates <code>FocusIn</code> and <code>FocusOut</code> events. The X server automatically performs an <code>UngrabKeyboard</code> request if the event window for an active keyboard grab becomes not viewable.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallowevents/">XAllowEvents</a>(3), <a href="/docs/linux/man/3-xgrabbutton/">XGrabButton</a>(3), <a href="/docs/linux/man/3-xgrabkey/">XGrabKey</a>(3), <a href="/docs/linux/man/3-xgrabpointer/">XGrabPointer</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>

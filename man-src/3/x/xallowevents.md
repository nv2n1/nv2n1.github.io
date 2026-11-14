---
title: "xallowevents(3)"
name: "xallowevents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xallowevents/"
description: "XAllowEvents – release queued events"
---

<p>XAllowEvents &#8211; release queued events </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XAllowEvents(Display *<i>display</i>, int <i>event_mode</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mode</i></p>
<dd>Specifies the event mode. You can pass <code>AsyncPointer</code>, <code>SyncPointer</code>, <code>AsyncKeyboard</code>, <code>SyncKeyboard</code>, <code>ReplayPointer</code>, <code>ReplayKeyboard</code>, <code>AsyncBoth</code>, or <code>SyncBoth</code>.</p>
<dt><i>time</i></p>
<dd>Specifies the time. You can pass either a timestamp or <code>CurrentTime</code>.</dl>
<h2>Description</h2>
<p>The <code>XAllowEvents</code> function releases some queued events if the client has caused a device to freeze. It has no effect if the specified time is earlier than the last-grab time of the most recent active grab for the client or if the specified time is later than the current X server time. </p>
<p> <code>XAllowEvents</code> can generate a <code>BadValue</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>

---
title: "xigetfocus(3)"
name: "xigetfocus"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xigetfocus/"
---

XISetFocus, XIGetFocus - set or get the device's focus. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Status XISetFocus( Display *display,
 int deviceid,
 Window focus,
 Time time);</pre><pre>Status XIGetFocus( Display *display,
 Window *focus_return);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>deviceid
 Specifies the device whose focus is to be queried or
 changed.</pre><pre>focus
 The new focus window.</pre><pre>focus_return
 Returns the current focus window.</pre><pre>time
 A valid timestamp or CurrentTime.</pre><h2>Description</h2><dl COMPACT><dd><pre>XISetFocus changes the focus of the specified device ans its
last-focus-change time. It has no effect if the specified time
is earlier than the current last-focus-change time or is later
than the current X server time. Otherwise, the
last-focus-change time is set to the specified time.
CurrentTime is replaced by the current X server time).
XISetFocus causes the X server to generate core, XI and XI2
focus events.</pre></dl><dl COMPACT><dd><pre>If the focus window is None all keyboard events by this device
are discarded until a new focus window is set. Otherwise, if
focus is a window, it becomes the device's focus window. If a
generated device event would normally be reported to this
window or one of its inferiors, the event is reported as usual.
Otherwise, the event is reported relative to the focus window.</pre></dl><dl COMPACT><dd><pre>The specified focus window must be viewable at the time
XISetFocus is called, or a BadMatch error results. If the focus
window later becomes not viewable, the focus reverts to the
parent (or the closest viewable ancestor. When the focus
reverts, the X server generates core, XI and XI2 focus events
but the last-focus-change time is not affected.</pre></dl><dl COMPACT><dd><pre>Attempting to set the focus on a master pointer device or an
attached slave device will result in a BadDevice error.</pre></dl><dl COMPACT><dd><pre>XISetFocus can generate BadDevice, BadMatch, BadValue, and
BadWindow errors.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadValue
 A value is outside of the permitted range.</pre></dl><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a appropriate for the type of change.</pre></dl><dl COMPACT><dd><pre>BadMatch
 The window is not viewable.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 Window.</pre></dl>

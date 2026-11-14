---
title: "xigrabdevice(3)"
name: "xigrabdevice"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xigrabdevice/"
---

XIGrabDevice, XIUngrabDevice - grab or ungrab the device. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Status XIGrabDevice( Display *display,
 int deviceid,
 Window grab_window,
 Time time,
 Cursor cursor,
 int grab_mode,
 int paired_device_mode,
 Bool owner_events,
 XIEventMask *mask);</pre><pre>Status XIUngrabDevice( Display *display,
 int deviceid,
 Time time);</pre><pre>cursor
 Specifies the cursor image to display for the duration
 of the grab.</pre><pre>display
 Specifies the connection to the X server.</pre><pre>deviceid
 Specifies the device that should be grabbed or
 ungrabbed.</pre><pre>grab_mode, paired_device_mode
 The grab mode for this device and (if applicable) the
 paired device.</pre><pre>grab_window
 The grab window.</pre><pre>mask
 Event mask.</pre><pre>owner_events
 True if events are to be reported normally.</pre><pre>time
 A valid timestamp or CurrentTime.</pre><h2>Description</h2><dl COMPACT><dd><pre>XIGrabDevice actively grabs control of the device. Further
device events are reported only to the grabbing client.
XIGrabDevice overrides any active device grab by this client.</pre></dl><dl COMPACT><dd><pre>If the device is an attached slave device, the device is
automatically detached from the master device and reattached to
the same master device when client ungrabs the device. If the
master device is removed while the device is floating as a
result of a grab, the device remains floating once the grab
deactivates.</pre></dl><dl COMPACT><dd><pre>If owner_events is False, all generated device events are
reported with respect to grab_window if selected. If
owner_events is True and if a generated device event would
normally be reported to this client, it is reported normally;
otherwise, the event is reported with respect to the
grab_window, and is only reported if specified in the event
mask.</pre></dl><dl COMPACT><dd><pre>If the grab_mode argument is XIGrabModeAsync, device event
processing continues as usual. If the device is currently
frozen by this client, then processing of device events is
resumed. If the grab_mode argument is XIGrabModeSync, the state
of the device (as seen by client applications) appears to
freeze, and the X server generates no further device events
until the grabbing client issues a releasing XIAllowEvents call
or until the device grab is released. Actual device changes are
not lost while the device is frozen; they are simply queued in
the server for later processing.</pre></dl><dl COMPACT><dd><pre>If paired_device_mode is XIGrabModeAsync, processing of events
from the paired master device is unaffected by activation of
the grab. If paired_device_mode is XIGrabModeSync, the state of
the paired master device (as seen by client applications)
appears to freeze, and the X server generates no further events
from this device until the grabbing client issues a releasing
XIAllowEvents call or until the device grab is released. Actual
events are not lost while the devices are frozen; they are
simply queued in the server for later processing. If the device
is a slave device paired_device_mode is ignored.</pre></dl><dl COMPACT><dd><pre>If the device is actively grabbed by some other client,
XIGrabDevice fails and returns AlreadyGrabbed. If grab_window
is not viewable, it fails and returns GrabNotViewable. If the
device is frozen by an active grab of another client, it fails
and returns GrabFrozen. If the specified time is earlier than
the last-device-grab time or later than the current X server
time, it fails and returns GrabInvalidTime. Otherwise, the
last-device-grab time is set to the specified time. CurrentTime
is replaced by the current X server time.</pre></dl><dl COMPACT><dd><pre>If cursor is not None this cursor is displayed until the client
calls XIUngrabDevice.</pre></dl><dl COMPACT><dd><pre>XIGrabDevice can generate BadDevice, BadValue, and BadWindow
errors.</pre></dl><dl COMPACT><dd><pre>The XIUngrabDevice request releases the device and any queued
events if this client has it actively grabbed from either
XIGrabDevice or XIGrabKey or XIGrabButton. If other devices are
frozen by the grab, XUngrabDevice thaws them. XUngrabDevice
does not release the device and any queued events if the
specified time is earlier than the last-device-grab time or is
later than the current X server time. The X server
automatically performs an XIUngrabDevice request if the event
window for an active device grab becomes not viewable.</pre></dl><dl COMPACT><dd><pre>XIUngrabDevice can generate a BadDevice error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadValue
 A value is outside of the permitted range.</pre></dl><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a appropriate for the type of change.</pre></dl><dl COMPACT><dd><pre>BadMatch
 The window is not viewable.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 Window.</pre></dl><h2>Bugs</h2><dl COMPACT><dd><pre>The protocol headers for XI 2.0 did not provide
XIGrabModeAsync or XIGrabModeSync. Use GrabModeSync and
GrabModeAsync instead, respectively.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XIAllowEvents/">XIAllowEvents</a>(3)</pre></dl>

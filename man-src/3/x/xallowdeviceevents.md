---
title: "xallowdeviceevents(3)"
name: "xallowdeviceevents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xallowdeviceevents/"
---

XAllowDeviceEvents - release queued events 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>int XAllowDeviceEvents( Display *display,
 XDevice *device,
 int event_mode,
 Time time);
display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device from which events are to be
 allowed.</pre><pre>event_mode
 Specifies the event mode.You can pass AsyncThisDevice,
 SyncThisDevice, ReplayThisDevice, AsyncOtherDevices,
 SyncAll, or AsyncAll.</pre><pre>time
 Specifies the time. You can pass either a timestamp or
 CurrentTime.</pre><h2>Description</h2>The XAllowDeviceEvents function releases some queued events if the client has caused a device to freeze. It has no effect if the specified time is earlier than the last-grab time of the most recent active grab for the client and device, or if the specified time is later than the current X server time. 

 The following describes the processing that occurs depending on what constant you pass to the event_mode argument. 

<dl COMPACT><dd>&bull; AsyncThisDevice - If the specified device is frozen by the client, event processing for that device continues as usual. If the device is frozen multiple times by the client on behalf of multiple separate grabs, AsyncThisDevice thaws for all. AsyncThisDevice has no effect if the specified device is not frozen by the client, but the device need not be grabbed by the client.</dl><dl COMPACT><dd>&bull; SyncThisDevice - If the specified device is frozen and actively grabbed by the client, event processing for that device continues normally until the next key or button event is reported to the client. At this time, the specified device again appears to freeze. However, if the reported event causes the grab to be released, the specified device does not freeze. SyncThisDevice has no effect if the specified device is not frozen by the client or is not grabbed by the client.</dl><dl COMPACT><dd>&bull; ReplayThisDevice - If the specified device is actively grabbed by the client and is frozen as the result of an event having been sent to the client (either from the activation of a GrabDeviceButton or from a previous AllowDeviceEvents with mode SyncThisDevice, but not from a GrabDevice), the grab is released and that event is completely reprocessed. This time, however, the request ignores any passive grabs at or above (toward the root) that the grab-window of the grab just released. The request has no effect if the specified device is not grabbed by the client or if it is not frozen as the result of an event.</dl><dl COMPACT><dd>&bull; AsyncOtherDevices - If the remaining devices are frozen by the client, event processing for them continues as usual. If the other devices are frozen multiple times by the client on behalf of multiple grabs, AsyncOtherDevices &quot;thaws&quot; for all. AsyncOtherDevices has no effect if the devices are not frozen by the client.</dl><dl COMPACT><dd>&bull; SyncAll - If all devices are frozen by the client, event processing (for all devices) continues normally until the next button or key event is reported to the client for a grabbed device, at which time all devices again appear to freeze. However, if the reported event causes the grab to be released, then the devices do not freeze. If any device is still grabbed, then a subsequent event for it will still cause all devices to freeze. SyncAll has no effect unless all devices are frozen by the client. If any device is frozen twice by the client on behalf of two separate grabs, SyncAll thaws for both. A subsequent freeze for SyncAll will only freeze each device once.</dl><dl COMPACT><dd>&bull; AsyncAll - If all devices are frozen by the client, event processing for all devices continues normally. If any device is frozen multiple times by the client on behalf of multiple separate grabs, AsyncAll thaws for all. AsyncAll has no effect unless all devices are frozen by the client.</dl>
 

 AsyncThisDevice, SyncThisDevice, and ReplayThisDevice have no effect on the processing of events from the remaining devices. AsyncOtherDevices has no effect on the processing of events from the specified device. When the event_mode is SyncAll or AsyncAll, the device parameter is ignored. 

 It is possible for several grabs of different devices by the same or different clients to be active simultaneously. If a device is frozen on behalf of any grab, no event processing is performed for the device. It is possible for a single device to be frozen because of several grabs. In this case, the freeze must be released on behalf of each grab before events can again be processed. 

 XAllowDeviceEvents can generate a BadDevice or BadValue error.
<h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice. This error may also occur if the
 specified device is the X keyboard or X pointer device.</pre></dl><dl COMPACT><dd><pre>BadValue
 An invalid mode was specified on the request.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XGrabDevice/">XGrabDevice</a>(3)</pre></dl>

---
title: "xigetselectedevents(3)"
name: "xigetselectedevents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xigetselectedevents/"
---

XISelectEvents, XIGetSelectedEvents - select for or get selected XI2 events on the window. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Status XISelectEvents( Display *display,
 Window win,
 XIEventMask *masks,
 int num_masks);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>masks
 Device event mask.</pre><pre>num_masks
 Number of masks in masks.</pre><pre>win
 Specifies the window.</pre><pre>XIEventMask *XIGetSelectedEvents( Display *display,
 Window win,
 int *num_masks_return);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>num_masks_return
 Number of masks in the return value.</pre><pre>win
 Specifies the window.</pre><h2>Description</h2><dl COMPACT><dd><pre>XI2 events must be selected using XISelectEvents.</pre></dl><dl COMPACT><dd><pre>XISelectEvents sets the event mask for this client on win.
Further events are only reported to this client if the event
type matches the selected event mask. The masks overrides the
previously selected event mask for the given device.</pre></dl><dl COMPACT><dd><pre>If deviceid is a valid device, the event mask is selected only
for this device. If deviceid is XIAllDevices or
XIAllMasterDevices, the event mask is selected for all devices
or all master devices, respectively. The effective event mask
is the bit-wise OR of the XIAllDevices, XIAllMasterDevices and
the respective device's event mask.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 int deviceid;
 int mask_len;
 unsigned char* mask;
} XIEventMask;</pre></dl><dl COMPACT><dd><pre>The mask_len specifies the length of mask in bytes. mask is a
binary mask in the form of (1 &lt;&lt; event type). deviceid must be
either a device or XIAllDevices or XIAllMasterDevices. A client
may submit several masks with the same deviceid in one request
but only the last mask will be effective.</pre></dl><dl COMPACT><dd><pre>XISelectEvents can generate a BadValue, a BadDevice, and a
BadWindow error.</pre></dl><dl COMPACT><dd><pre>XIGetSelectedEvents returns the events selected by this client on the given
window. If no events were selected on this window, XIGetSelectedEvents
returns NULL and num_masks_return is set to 0. If an internal error occurs,
XIGetSelectedEvents returns NULL and num_masks_return is set to -1.
Otherwise, XIGetSelectedEvent returns the selected event masks for all
devices including the masks for XIAllDevices and XIAllMasterDevices</pre></dl><dl COMPACT><dd><pre>The caller must free the returned data using XFree().</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadValue
 A value is outside of the permitted range.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 window.</pre></dl><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist.</pre></dl>

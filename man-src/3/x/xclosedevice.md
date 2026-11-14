---
title: "xclosedevice(3)"
name: "xclosedevice"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xclosedevice/"
---

XOpenDevice, XCloseDevice - open or close an extension input device 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>XDevice *XOpenDevice( Display *display,
 XID device_id);</pre><pre>XCloseDevice( Display *display,
 XDevice *device);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device_id
 Specifies the id of the device to be opened</pre><pre>device
 Specifies the device to be closed</pre><h2>Description</h2><dl COMPACT><dd><pre>The XOpenDevice request makes an input device accessible to a
client through input extension protocol requests. If
successful, it returns a pointer to an XDevice structure.</pre></dl><dl COMPACT><dd><pre>The XCloseDevice request makes an input device inaccessible to
a client through input extension protocol requests. Before
terminating, and client that has opened input devices through
the input extension should close them via CloseDevice.</pre></dl><dl COMPACT><dd><pre>When a client makes an XCloseDevice request, any active grabs
that the client has on the device are released. Any event
selections that the client has are deleted, as well as any
passive grabs. If the requesting client is the last client
accessing the device, the server may disable all access by X to
the device.</pre></dl><dl COMPACT><dd><pre>XOpenDevice and XCloseDevice can generate a BadDevice error.</pre></dl>
 

 Structures 

<dl COMPACT><dd><pre>The XDevice structure returned by XOpenDevice contains:
 typedef struct {
 XID device_id;
 int num_classes;
 XInputClassInfo *classes;
 } XDevice;</pre></dl><dl COMPACT><dd><pre>The classes field is a pointer to an array of XInputClassInfo
structures. Each element of this array contains an event type
base for a class of input supported by the specified device.
The num_classes field indicates the number of elements in the
classes array.</pre></dl><dl COMPACT><dd><pre>The XInputClassInfo structure contains:</pre></dl><dl COMPACT><dd><pre>typedef struct {
 unsigned char input_class;
 unsigned char event_type_base;
} XInputClassInfo;</pre></dl><dl COMPACT><dd><pre>The input_class field identifies one class of input supported
by the device. Defined types include KeyClass, ButtonClass,
ValuatorClass, ProximityClass, FeedbackClass, FocusClass, and
OtherClass. The event_type_base identifies the event type of
the first event in that class.</pre></dl><dl COMPACT><dd><pre>The information contained in the XInputClassInfo structure is
used by macros to obtain the event classes that clients use in
making XSelectExtensionEvent requests. Currently defined macros
include DeviceKeyPress, DeviceKeyRelease, DeviceButtonPress,
DeviceButtonRelese, DeviceMotionNotify, DeviceFocusIn,
DeviceFocusOut, ProximityIn, ProximityOut, DeviceStateNotify,
DeviceMappingNotify, ChangeDeviceNotify,
DevicePointerMotionHint, DeviceButton1Motion,
DeviceButton2Motion, DeviceButton3Motion, DeviceButton4Motion,
DeviceButton5Motion, DeviceButtonMotion, DeviceOwnerGrabButton,
DeviceButtonPressGrab, and NoExtensionEvent.</pre></dl><dl COMPACT><dd><pre>To obtain the proper event class for a particular device, one
of the above macros is invoked using the XDevice structure for
that device. For example,
 DeviceKeyPress (*device, type, eventclass);</pre></dl><dl COMPACT><dd><pre>returns the DeviceKeyPress event type and the eventclass for
DeviceKeyPress events from the specified device.</pre></dl><dl COMPACT><dd><pre>This eventclass can then be used in an XSelectExtensionEvent
request to ask the server to send DeviceKeyPress events from
this device. When a selected event is received via XNextEvent,
the type can be used for comparison with the type in the event.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist, or is the X keyboard or X pointer. This
 error may also occur if some other client has caused the
 specified device to become the X keyboard or X pointer
 device via the XChangeKeyboardDevice or
 XChangePointerDevice requests.</pre></dl>

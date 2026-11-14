---
title: "xquerydevicestate(3)"
name: "xquerydevicestate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xquerydevicestate/"
---

XQueryDeviceState - query the state of an extension input device. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>XDeviceState* XQueryDeviceState( Display *display,
 XDevice *device);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device whose state is to be queried.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XQueryDeviceState request queries the state of an input
device. The current state of keys and buttons (up or down), and
valuators (current value) on the device is reported by this
request. Each key or button is represented by a bit in the
XDeviceState structure that is returned. Valuators on the
device report 0 if they are reporting relative information, and
the current value if they are reporting absolute information.</pre></dl><dl COMPACT><dd><pre>XQueryDeviceState can generate a BadDevice error.</pre></dl><dl COMPACT><dd><pre>Structures:</pre></dl><dl COMPACT><dd><pre>The XDeviceState structure contains:</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID device_id;
 int num_classes;
 XInputClass *data;
} XDeviceState;</pre></dl><dl COMPACT><dd><pre>The XValuatorState structure contains:</pre></dl><dl COMPACT><dd><pre>typedef struct {
 unsigned char class;
 unsigned char length;
 unsigned char num_valuators;
 unsigned char mode;
 int *valuators;
} XValuatorState;</pre></dl><dl COMPACT><dd><pre>The XKeyState structure contains:</pre></dl><dl COMPACT><dd><pre>typedef struct {
 unsigned char class;
 unsigned char length;
 short num_keys;
 char keys[32];
} XKeyState;</pre></dl><dl COMPACT><dd><pre>The XButtonState structure contains:</pre></dl><dl COMPACT><dd><pre>typedef struct {
 unsigned char class;
 unsigned char length;
 short num_buttons;
 char buttons[32];
} XButtonState;</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice. This error may also occur if some
 other client has caused the specified device to become
 the X keyboard or X pointer device via the
 XChangeKeyboardDevice or XChangePointerDevice requests.</pre></dl>

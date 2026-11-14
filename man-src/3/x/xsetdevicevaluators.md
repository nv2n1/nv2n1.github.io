---
title: "xsetdevicevaluators(3)"
name: "xsetdevicevaluators"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetdevicevaluators/"
---

XSetDeviceValuators - initialize the valuators on an extension input device 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>XSetDeviceValuators( Display *display,
 XDevice *device,
 int *valuators,
 int first_valuator,
 int num_valuators);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device whose valuators are to be
 initialized.</pre><pre>valuators
 Specifies a pointer to an array of integer values to be
 used to initialize the device valuators.</pre><pre>first_valuator
 Specifies the first valuator to be set. Valuators are
 numbered beginning with zero.</pre><pre>num_valuators
 Specifies the number of valuators to be set.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XSetDeviceValuators request sets the current values of the
valuators of an input device. The valuators in the range
first_valuator to (first_valuator + num_valuators) are set to
the specified values. Valuators are numbered beginning with 0.
Not all input devices support initialization of valuator
values. If this request is made to a device that does not
support valuators initialization, a BadMatch error will occur.</pre></dl><dl COMPACT><dd><pre>If the request succeeds, a status of Success is returned. If
another client has the device grabbed, a status of
AlreadyGrabbed is returned.</pre></dl><dl COMPACT><dd><pre>XSetDeviceValuators can generate a BadLength, BadDevice,
BadMatch, or BadValue error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice.</pre></dl><dl COMPACT><dd><pre>BadMatch
 This error may occur if an XSetDeviceValuators request
 is made specifying a device that has no valuators and
 reports no axes of motion, or if such a request is made
 specifying a device that does not support valuator
 initialization.</pre></dl><dl COMPACT><dd><pre>BadValue
 An invalid first_valuator or num_valuators values was
 specified.</pre></dl>

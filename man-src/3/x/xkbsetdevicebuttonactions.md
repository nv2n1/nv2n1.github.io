---
title: "xkbsetdevicebuttonactions(3)"
name: "xkbsetdevicebuttonactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetdevicebuttonactions/"
description: "XkbSetDeviceButtonActions – Change only the button actions for an input extension device"
---

<p>XkbSetDeviceButtonActions &#8211; Change only the button actions for an input extension device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetDeviceButtonActions</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDeviceInfoPtr </code><i>device</i><code>,</code> <code>unsigned int </code><i>first_button</i><code>,</code> <code>unsigned int </code><i>num_buttons</i><code>);</code></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device</i></p>
<dd>structure defining the device and modifications</p>
<dt><i>&#8211; first_button</i></p>
<dd>number of first button to update, 0 relative</p>
<dt><i>&#8211; num_buttons</i></p>
<dd>number of buttons to update</dl>
<h2>Description</h2>
<p><i>XkbSetDeviceButtonActions </i> assigns actions to the buttons of the device specified in <i>device_info-&gt;device_spec. </i> Actions are assigned to <i>num_buttons </i> buttons beginning with <i>first_button </i> and are taken from the actions specified in <i>device_info-&gt;btn_acts.</i> </p>
<p> If the server does not support assignment of Xkb actions to extension device buttons, <i>XkbSetDeviceButtonActions </i> has no effect and returns False. If the device has no buttons or if <i>first_button </i> or <i>num_buttons </i> specify buttons outside of the valid range as determined by <i>device_info-&gt;num_btns, </i> the function has no effect and returns False. Otherwise, <i>XkbSetDeviceButtonActions </i> sends a request to the server to change the actions for the specified buttons and returns True. </p>
<p> If the actual request sent to the server involved illegal button numbers, a BadValue protocol error is generated. If an invalid device identifier is specified in <i>device_info-&gt;device_spec, </i> a BadKeyboard protocol error results. If the actual device specified in <i>device_info-&gt;device_spec </i> does not contain buttons and a request affecting buttons is made, a BadMatch protocol error is generated.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadKeyboard</code></p>
<dd>The device specified was not a valid core or input extension device</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>

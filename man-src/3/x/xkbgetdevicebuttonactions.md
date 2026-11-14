---
title: "xkbgetdevicebuttonactions(3)"
name: "xkbgetdevicebuttonactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetdevicebuttonactions/"
description: "XkbGetDeviceButtonActions – Query the button actions associated with an X Input Extension device"
---

<p>XkbGetDeviceButtonActions &#8211; Query the button actions associated with an X Input Extension device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetDeviceButtonActions</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>Bool </code><i>all_buttons</i><code>,</code> <code>unsigned int </code><i>first_button</i><code>,</code> <code>unsigned int </code><i>num_buttons</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_info</i></p>
<dd>structure to update with results</p>
<dt><i>&#8211; all_buttons</i></p>
<dd>True =&gt; get information for all buttons</p>
<dt><i>&#8211; first_button</i></p>
<dd>number of first button for which info is desired</p>
<dt><i>&#8211; num_buttons</i></p>
<dd>number of buttons for which info is desired</dl>
<h2>Description</h2>
<p><i>XkbGetDeviceButtonActions </i> queries the server for the desired button information for the device indicated by the <i>device_spec </i> field of <i>device_info </i> and waits for a reply. If successful, <i>XkbGetDeviceButtonActions </i> backfills the button actions <i>(btn_acts </i> field of <i>device_info) </i> for only the requested buttons, updates the <i>name, type, supported, </i> and <i>unsupported </i> fields, and returns Success. </p>
<p> <i>all_buttons, first_button </i> and <i>num_buttons </i> specify the device buttons for which actions should be returned. Setting <i>all_buttons </i> to True requests actions for all device buttons; if <i>all_buttons </i> is False, <i>first_button </i> and <i>num_buttons </i> specify a range of buttons for which actions are requested. </p>
<p> If a compatible version of Xkb is not available in the server or the Xkb extension has not been properly initialized, <i>XkbGetDeviceButtonActions </i> returns BadAccess. If allocation errors occur, a BadAlloc status is returned. If the specified device <i>(device_info-&gt;device_spec) </i> is invalid, a BadKeyboard status is returned. If the device has no buttons, a BadMatch status is returned. If <i>first_button </i> and <i>num_buttons </i> specify illegal buttons, a BadValue status is returned.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadKeyboard</code></p>
<dd>The device specified was not a valid core or input extension device</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>

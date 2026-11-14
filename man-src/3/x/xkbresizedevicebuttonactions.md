---
title: "xkbresizedevicebuttonactions(3)"
name: "xkbresizedevicebuttonactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbresizedevicebuttonactions/"
description: "XkbResizeDeviceButtonActions – Allocate additional space for button actions in an XkbDeviceInfoRec structure"
---

<p>XkbResizeDeviceButtonActions &#8211; Allocate additional space for button actions in an XkbDeviceInfoRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbResizeDeviceButtonActions</code> <code>(XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>unsigned int </code><i>new_total</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; device_info</i></p>
<dd>
<dd>structure in which to allocate button actions</p>
<dt><i>&#8211; new_total</i></p>
<dd>new total number of button actions needed</dl>
<h2>Description</h2>
<p><i>XkbResizeDeviceButtonActions </i> reallocates space, if necessary, to make sure there is room for a total of <i>new_total </i> button actions in the <i>device_info </i> structure. Any new entries allocated are zeroed. If successful, <i>XkbResizeDeviceButtonActions </i> returns Success. If <i>new_total </i> is zero, all button actions are deleted, <i>device_info-&gt;num_btns </i> is set to zero, and <i>device_info-&gt;btn_acts </i> is set to NULL. If <i>device_info </i> is invalid or <i>new_total </i> is greater than 255, BadValue is returned. If a memory allocation failure occurs, a BadAlloc is returned. </p>
<p> To free an XkbDeviceInfoRec structure, use <i>XkbFreeDeviceInfo.</i></p>
<h2>Structures</h2>
<p>Information about X Input Extension devices is transferred between a client program and the Xkb extension in an XkbDeviceInfoRec structure: </p>
<pre> typedef struct {
 char * name; /* name for device */
 Atom type; /* name for class of devices */
 unsigned short device_spec; /* device of interest */
 Bool has_own_state; /* True=&gt;this device has its own state */
 unsigned short supported; /* bits indicating supported capabilities */
 unsigned short unsupported; /* bits indicating unsupported capabilities */
 unsigned short num_btns; /* number of entries in btn_acts */
 XkbAction * btn_acts; /* button actions */
 unsigned short sz_leds; /* total number of entries in LEDs vector */
 unsigned short num_leds; /* number of valid entries in LEDs vector */
 unsigned short dflt_kbd_fb; /* input extension ID of default (core kbd) indicator */
 unsigned short dflt_led_fb; /* input extension ID of default indicator feedback */
 XkbDeviceLedInfoPtr leds; /* LED descriptions */
 } XkbDeviceInfoRec, *XkbDeviceInfoPtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreedeviceinfo/">XkbFreeDeviceInfo</a></code>(3)</p>

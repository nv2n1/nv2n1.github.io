---
title: "xkbadddeviceledinfo(3)"
name: "xkbadddeviceledinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbadddeviceledinfo/"
description: "XkbAddDeviceLedInfo – Initialize an XkbDeviceLedInfoRec structure"
---

<p>XkbAddDeviceLedInfo &#8211; Initialize an XkbDeviceLedInfoRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDeviceLedInfoPtr XkbAddDeviceLedInfo</code> <code>(XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>unsigned int </code><i>led_class</i><code>,</code> <code>unsigned int </code><i>led_id</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; device_info</i></p>
<dd>
<dd>structure in which to add LED info</p>
<dt><i>&#8211; led_class</i></p>
<dd>input extension class for LED device of interest</p>
<dt><i>&#8211; led_id</i></p>
<dd>input extension ID for LED device of interest</dl>
<h2>Description</h2>
<p><i>XkbAddDeviceLedInfo </i> first checks to see whether an entry matching <i>led_class </i> and <i>led_id </i> already exists in the <i>device_info-&gt;leds </i> array. If it finds a matching entry, it returns a pointer to that entry. Otherwise, it checks to be sure there is at least one empty entry in <i>device_info-&gt;leds </i> and extends it if there is not enough room. It then increments <i>device_info-&gt;num_leds </i> and fills in the next available entry in <i>device_info-&gt;leds </i> with <i>led_class </i> and <i>led_id.</i> </p>
<p> If successful, <i>XkbAddDeviceLedInfo </i> returns a pointer to the XkbDeviceLedInfoRec structure that was initialized. If unable to allocate sufficient storage, or if <i>device_info </i> points to an invalid XkbDeviceInfoRec structure, or if <i>led_class </i> or <i>led_id </i> are inappropriate, <i>XkbAddDeviceLedInfo </i> returns NULL. </p>
<p> To allocate additional space for button actions in an XkbDeviceInfoRec structure, use <i>XkbResizeDeviceButtonActions.</i> </p>
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
 } XkbDeviceInfoRec, *XkbDeviceInfoPtr;
 
 typedef struct {
 unsigned short led_class; /* class for this LED device*/
 unsigned short led_id; /* ID for this LED device */
 unsigned int phys_indicators; /* bits for which LEDs physically present */
 unsigned int maps_present; /* bits for which LEDs have maps in maps */
 unsigned int names_present; /* bits for which LEDs are in names */
 unsigned int state; /* 1 bit =&gt; corresponding LED is on */
 Atom names[XkbNumIndicators]; /* names for LEDs */
 XkbIndicatorMapRec maps; /* indicator maps for each LED */
 } XkbDeviceLedInfoRec, *XkbDeviceLedInfoPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbresizedevicebuttonactions/">XkbResizeDeviceButtonActions</a></code>(3)</p>

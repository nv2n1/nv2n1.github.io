---
title: "xkballocdeviceinfo(3)"
name: "xkballocdeviceinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocdeviceinfo/"
description: "XkbAllocDeviceInfo – Obtain an XkbDeviceInfoRec structure"
---

<p>XkbAllocDeviceInfo &#8211; Obtain an XkbDeviceInfoRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDeviceInfoPtr XkbAllocDeviceInfo</code> <code>(unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>n_buttons</i><code>,</code> <code>unsigned int </code><i>sz_leds</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; device_spec</i></p>
<dd>
<dd>device ID with which structure will be used</p>
<dt><i>&#8211; n_buttons</i></p>
<dd>number of button actions to allocate space for</p>
<dt><i>&#8211; sz_leds</i></p>
<dd>number of LED feedbacks to allocate space for</dl>
<h2>Description</h2>
<p><i>XkbAllocDeviceInfo </i> allocates space for an XkbDeviceInfoRec structure and initializes that structure&#8217;s <i>device_spec </i> field with the device ID specified by <i>device_spec. </i> If <i>n_buttons </i> is nonzero, <i>n_buttons </i> XkbActions are linked into the XkbDeviceInfoRec structure and initialized to zero. If <i>sz_leds </i> is nonzero, <i>sz_leds </i> XkbDeviceLedInfoRec structures are also allocated and linked into the XkbDeviceInfoRec structure. If you request XkbDeviceLedInfoRec structures be allocated using this request, you must initialize them explicitly. </p>
<p> To obtain an XkbDeviceLedInfoRec structure, use <i>XkbAllocDeviceLedInfo.</i></p>
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
<p><code><a href="/docs/linux/man/3-xkballocdeviceledinfo/">XkbAllocDeviceLedInfo</a></code>(3)</p>

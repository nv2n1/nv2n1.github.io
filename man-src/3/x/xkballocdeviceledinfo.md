---
title: "xkballocdeviceledinfo(3)"
name: "xkballocdeviceledinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocdeviceledinfo/"
description: "XkbAllocDeviceLedInfo – Obtain an XkbDeviceLedInfoRec structure"
---

<p>XkbAllocDeviceLedInfo &#8211; Obtain an XkbDeviceLedInfoRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocDeviceLedInfo</code> <code>(XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>int </code><i>num_needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; device_info</i></p>
<dd>
<dd>structure in which to allocate LED space</p>
<dt><i>&#8211; num_needed</i></p>
<dd>number of indicators to allocate space for</dl>
<h2>Description</h2>
<p><i>XkbAllocDeviceLedInfo </i> allocates space for an XkbDeviceLedInfoRec and places it in <i>device_info. </i> If <i>num_needed </i> is nonzero, <i>num_needed </i> XkbIndicatorMapRec structures are also allocated and linked into the XkbDeviceLedInfoRec structure. If you request XkbIndicatorMapRec structures be allocated using this request, you must initialize them explicitly. All other fields are initialized to zero. </p>
<p> To initialize an XkbDeviceLedInfoRec structure, use <i>XkbAddDeviceLedInfo.</i></p>
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
<p>Each indicator has its own set of attributes that specify whether clients can explicitly set its state and whether it tracks the keyboard state. The attributes of each indicator are held in the maps array, which is an array of XkbIndicatorRec structures: </p>
<pre> typedef struct {
 unsigned char flags; /* how the indicator can be changed */
 unsigned char which_groups; /* match criteria for groups */
 unsigned char groups; /* which keyboard groups the indicator watches */
 unsigned char which_mods; /* match criteria for modifiers */
 XkbModsRec mods; /* which modifiers the indicator watches */
 unsigned int ctrls; /* which controls the indicator watches */
 } XkbIndicatorMapRec, *XkbIndicatorMapPtr;</pre>
<p>This indicator map specifies for each indicator: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The conditions under which the keyboard modifier state affects the indicator</p>
<dt>&bull;</p>
<dd>The conditions under which the keyboard group state affects the indicator</p>
<dt>&bull;</p>
<dd>The conditions under which the state of the boolean controls affects the indicator</p>
<dt>&bull;</p>
<dd>The effect (if any) of attempts to explicitly change the state of the indicator using the functions XkbSetControls or XChangeKeyboardControl</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbadddeviceledinfo/">XkbAddDeviceLedInfo</a></code>(3), <code><a href="/docs/linux/man/3-xkbsetcontrols/">XkbSetControls</a></code>(3)</p>

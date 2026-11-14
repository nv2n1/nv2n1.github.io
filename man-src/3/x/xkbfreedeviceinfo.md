---
title: "xkbfreedeviceinfo(3)"
name: "xkbfreedeviceinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreedeviceinfo/"
description: "XkbFreeDeviceInfo – Free an XkbDeviceInfoRec structure"
---

<p>XkbFreeDeviceInfo &#8211; Free an XkbDeviceInfoRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeDeviceInfo</code> <code>(XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; device_info</i></p>
<dd>
<dd>pointer to XkbDeviceInfoRec in which to free items</p>
<dt><i>&#8211; which</i></p>
<dd>mask of components of device_info to free</p>
<dt><i>&#8211; free_all</i></p>
<dd>True =&gt; free everything, including device_info</dl>
<h2>Description</h2>
<p>If <i>free_all </i> is True, the <i>XkbFreeDeviceInfo </i> frees all components of <i>device_info </i> and the XkbDeviceInfoRec structure pointed to by <i>device_info </i> itself. If <i>free_all </i> is False, the value of <i>which </i> determines which subcomponents are freed. <i>which </i> is an inclusive OR of one or more of the values from Table 1. If <i>which </i> contains XkbXI_ButtonActionsMask, all button actions associated with <i>device_info </i> are freed, <i>device_info-&gt;btn_acts </i> is set to NULL, and <i>device_info-&gt;num_btns </i> is set to zero. If <i>which </i> contains all bits in XkbXI_IndicatorsMask, all XkbDeviceLedInfoRec structures associated with <i>device_info </i> are freed, <i>device_info-&gt;leds </i> is set to NULL, and <i>device_info-&gt;sz_leds </i> and <i>device_info-&gt;num_leds </i> are set to zero. If <i>which </i> contains XkbXI_IndicatorMapsMask, all indicator maps associated with <i>device_info </i> are cleared, but the number of LEDs and the leds structures themselves is preserved. If <i>which </i> contains XkbXI_IndicatorNamesMask, all indicator names associated with <i>device_info </i> are cleared, but the number of LEDs and the leds structures themselves is preserved. If <i>which </i> contains XkbXI_IndicatorStateMask, the indicator state associated with the <i>device_info </i> leds are set to zeros but the number of LEDs and the leds structures themselves is preserved. </p>
<pre> Table 1 XkbDeviceInfoRec Mask Bits 
____________________________________________________________________________________
Name XkbDeviceInfoRec Value Capability If Set
 Fields Effected 
____________________________________________________________________________________
XkbXI_KeyboardsMask (1L &lt;&lt;0) Clients can use all
 Xkb requests and events
 with KeyClass devices 
 supported by the input
 device extension.
XkbXI_ButtonActionsMask num_btns (1L &lt;&lt;1) Clients can assign key 
 btn_acts actions to buttons 
 non-KeyClass input
 extension devices.
 
XkbXI_IndicatorNamesMask leds-&gt;names (1L &lt;&lt;2) Clients can assign
 names to indicators on
 non-KeyClass input
 extension devices.
 
XkbXI_IndicatorMapsMask leds-&gt;maps (1L &lt;&lt;3) Clients can assign
 indicator maps to
 indicators on 
 non-KeyClass input
 extension devices.
XkbXI_IndicatorStateMask leds-&gt;state (1L &lt;&lt;4) Clients can request 
 the status of indicators
 on non-KeyClass input
 extension devices.
XkbXI_IndicatorsMask sz_leds (0x1c) XkbXI_IndicatorNamesMask |
 num_leds XkbXI_IndicatorMapsMask |
 leds-&gt;* XkbXI_IndicatorStateMask
XkbXI_UnsupportedFeaturesMask unsupported (1L &lt;&lt;15)
XkbXI_AllDeviceFeaturesMask Those selected (0x1e) XkbXI_IndicatorsMask |
 by Value Column XkbSI_ButtonActionsMask
 masks 
XkbXI_AllFeaturesMask Those selected (0x1f) XkbSI_AllDeviceFeaturesMask |
 by Value Column XkbSI_KeyboardsMask
 masks
XkbXI_AllDetailsMask Those selected (0x801f) XkbXI_AllFeaturesMask |
 by Value column XkbXI_UnsupportedFeaturesMask
 masks</pre>
<h2>Structures</h2>
<p>Information about X Input Extension devices is transferred between a client program and the Xkb extension in an XkbDeviceInfoRec structure: </p>
<pre>typedef struct {
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

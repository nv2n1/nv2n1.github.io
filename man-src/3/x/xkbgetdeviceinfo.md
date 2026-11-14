---
title: "xkbgetdeviceinfo(3)"
name: "xkbgetdeviceinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetdeviceinfo/"
description: "XkbGetDeviceInfo – Determine whether the X server allows Xkb access to particular capabilities of input devices other than the core X keyboard, or to determine the status of indicator maps, indicat..."
---

<p>XkbGetDeviceInfo &#8211; Determine whether the X server allows Xkb access to particular capabilities of input devices other than the core X keyboard, or to determine the status of indicator maps, indicator names or button actions on a non-KeyClass extension device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDeviceInfoPtr XkbGetDeviceInfo</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>ind_class</i><code>,</code> <code>unsigned int </code><i>ind_id</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask indicating information to return</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; ind_class</i></p>
<dd>feedback class for indicator requests</p>
<dt><i>&#8211; ind_id</i></p>
<dd>feedback ID for indicator requests</dl>
<h2>Description</h2>
<p>To determine whether the X server allows Xkb access to particular capabilities of input devices other than the core X keyboard, or to determine the status of indicator maps, indicator names or button actions on a non-KeyClass extension device, use <i>XkbGetDeviceInfo. </i> </p>
<p> <i>XkbGetDeviceInfo </i> returns information about the input device specified by <i>device_spec. </i> Unlike the <i>device_spec </i> parameter of most Xkb functions, <i>device_spec </i> does not need to be a keyboard device. It must, however, indicate either the core keyboard or a valid X Input Extension device. </p>
<p> The <i>which </i> parameter is a mask specifying optional information to be returned. It is an inclusive OR of one or more of the values from Table 1 and causes the returned XkbDeviceInfoRec to contain values for the corresponding fields specified in the table. </p>
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
<p>The XkbDeviceInfoRec returned by <i>XkbGetDeviceInfo </i> always has values for <i>name </i> (may be a null string, &quot;&quot;), <i>type, supported, unsupported, has_own_state, dflt_kbd_fd, </i> and <i>dflt_kbd_fb. </i> Other fields are filled in as specified by <i>which.</i> </p>
<p> Upon return, the <i>supported </i> field will be set to the inclusive OR of zero or more bits from Table 1; each bit set indicates an optional Xkb extension device feature supported by the server implementation, and a client may modify the associated behavior. </p>
<p> If the XkbButtonActionsMask bit is set in <i>which, </i> the XkbDeviceInfoRec returned will have the button actions <i>(btn_acts </i> field) filled in for all buttons. </p>
<p> If <i>which </i> includes one of the bits in XkbXI_IndicatorsMask, the feedback class of the indicators must be specified in <i>ind_class, </i> and the feedback ID of the indicators must be specified in <i>ind_id. </i> If the request does not include any of the bits in XkbXI_IndicatorsMask, the <i>ind_class </i> and <i>ind_id </i> parameters are ignored. The class and ID can be obtained via the input device extension <i>XListInputDevices </i> request. </p>
<p> If any of the XkbXI_IndicatorsMask bits are set in <i>which, </i> the XkbDeviceInfoRec returned will have filled in the portions of the <i>leds </i> structure corresponding to the indicator feedback identified by <i>ind_class </i> and <i>ind_id. </i> The <i>leds </i> vector of the XkbDeviceInfoRec is allocated if necessary and <i>sz_leds </i> and <i>num_leds </i> filled in. The <i>led_class, led_id </i> and <i>phys_indicators </i> fields of the <i>leds </i> entry corresponding to <i>ind_class </i> and <i>ind_id </i> are always filled in. If <i>which </i> contains XkbXI_IndicatorNamesMask, the <i>names_present </i> and <i>names </i> fields of the <i>leds </i> structure corresponding to <i>ind_class </i> and <i>ind_id </i> are returned. If <i>which </i> contains XkbXI_IndicatorStateMask, the corresponding <i>state </i> field is updated. If <i>which </i> contains XkbXI_IndicatorMapsMask, the <i>maps_present </i> and <i>maps </i> fields are updated. </p>
<p> Xkb provides convenience functions to request subsets of the information available via <i>XkbGetDeviceInfo. </i> These convenience functions mirror some of the mask bits. The functions all take an XkbDeviceInfoPtr as an input argument and operate on the X Input Extension device specified by the <i>device_spec </i> field of the structure. Only the parts of the structure indicated in the function description are updated. The XkbDeviceInfoRec structure used in the function call can be obtained by calling <i>XkbGetDeviceInfo </i> or can be allocated by calling <i>XkbAllocDeviceInfo.</i></p>
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
} XkbDeviceInfoRec, *XkbDeviceInfoPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocdeviceinfo/">XkbAllocDeviceInfo</a></code>(3), <code><a href="/docs/linux/man/3-xlistinputdevices/">XListInputDevices</a></code>(3)</p>

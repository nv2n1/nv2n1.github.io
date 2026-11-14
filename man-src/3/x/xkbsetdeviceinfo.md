---
title: "xkbsetdeviceinfo(3)"
name: "xkbsetdeviceinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetdeviceinfo/"
description: "XkbSetDeviceInfo – Modify some or all of the characteristics of an X Input Extension device"
---

<p>XkbSetDeviceInfo &#8211; Modify some or all of the characteristics of an X Input Extension device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetDeviceInfo</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDeviceInfoPtr </code><i>device_info</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask indicating characteristics to modify</p>
<dt><i>&#8211; device_info</i></p>
<dd>structure defining the device and modifications</dl>
<h2>Description</h2>
<p>To change characteristics of an X Input Extension device in the server, first modify a local copy of the device structure and then use either <i>XkbSetDeviceInfo, </i> or, to save network traffic, use an XkbDeviceChangesRec structure and call <i>XkbChangeDeviceInfo </i> to download the changes to the server. </p>
<p> <i>XkbSetDeviceInfo </i> sends a request to the server to modify the characteristics of the device specified in the <i>device_info </i> structure. The particular characteristics modified are identified by the bits set in <i>which </i> and take their values from the relevant fields in device_info (see Table 1). XkbSetDeviceInfo returns True if the request was successfully sent to the server. If the X server implementation does not allow interaction between the X input extension and the Xkb Extension, the function does nothing and returns False. </p>
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
<p>The <i>which </i> parameter specifies which aspects of the device should be changed and is a bitmask composed of an inclusive OR or one or more of the following bits: XkbXI_ButtonActionsMask, XkbXI_IndicatorNamesMask, XkbXI_IndicatorMapsMask. If the features requested to be manipulated in <i>which </i> are valid for the device, but the server does not support assignment of one or more of them, that particular portion of the request is ignored.<br />
&nbsp; If the device specified in <i>device_info-&gt;device_spec </i> does not contain buttons and a request affecting buttons is made, or the device does not contain indicators and a request affecting indicators is made, a BadMatch protocol error results. </p>
<p> If the XkbXI_ButtonActionsMask bit is set in the <i>supported </i> mask returned by <i>XkbGetDeviceInfo, </i> the Xkb extension allows applications to assign key actions to buttons on input extension devices other than the core keyboard device. If the XkbXI_ButtonActionsMask is set in <i>which, </i> the actions for all buttons specified in <i>device_info </i> are set to the XkbActions specified in <i>device_info-&gt;btn_acts. </i> If the number of buttons requested to be updated is not valid for the device, <i>XkbSetDeviceInfo </i> returns False and a BadValue protocol error results. </p>
<p> If the XkbXI_IndicatorMaps and / or XkbXI_IndicatorNamesMask bit is set in the <i>supported </i> mask returned by <i>XkbGetDeviceInfo, </i> the Xkb extension allows applications to assign maps and / or names to the indicators of nonkeyboard extension devices. If supported, maps and / or names can be assigned to all extension device indicators, whether they are part of a keyboard feedback or part of an indicator feedback.<br />
&nbsp; If the XkbXI_IndicatorMapsMask and / or XkbXI_IndicatorNamesMask flag is set in <i>which, </i> the indicator maps and / or names for all <i>device_info-&gt;num_leds </i> indicator devices specified in <i>device_info-&gt;leds </i> are set to the maps and / or names specified in <i>device_info-&gt;leds. device_info-&gt;leds-&gt;led_class </i> and <i>led_id </i> specify the input extension class and device ID for each indicator device to modify; if they have invalid values, a BadValue protocol error results and <i>XkbSetDeviceInfo </i> returns False. If they have legal values but do not specify a keyboard or indicator class feedback for the device in question, a BadMatch error results. If any of the values in <i>device_info-&gt;leds-&gt;names </i> are not a valid Atom or None, a BadAtom protocol error results.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetDeviceInfo </i> function returns True if the request was successfully sent to the server.</p>
<dt>False</p>
<dd>The <i>XkbSetDeviceInfo </i> function returns False if the X server implementation does not allow interaction between the X input extension and the Xkb Extension.</dl>
<h2>Structures</h2>
<p>Changes to an Xkb extension device may be tracked by listening to XkbDeviceExtensionNotify events and accumulating the changes in an XkbDeviceChangesRec structure. The changes noted in the structure may then be used in subsequent operations to update either a server configuration or a local copy of an Xkb extension device configuration. The changes structure is defined as follows: </p>
<pre>typedef struct _XkbDeviceChanges {
 unsigned int changed; /* bits indicating what has changed */
 unsigned short first_btn; /* number of first button which changed, if any */
 unsigned short num_btns; /* number of buttons that have changed */
 XkbDeviceLedChangesRec leds;
} XkbDeviceChangesRec,*XkbDeviceChangesPtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAtom</code></p>
<dd>A name is neither a valid Atom or None</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangedeviceinfo/">XkbChangeDeviceInfo</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetdeviceinfo/">XkbGetDeviceInfo</a></code>(3)</p>

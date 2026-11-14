---
title: "xkbnotedevicechanges(3)"
name: "xkbnotedevicechanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbnotedevicechanges/"
description: "XkbNoteDeviceChanges – Note device changes reported in an XkbExtensionDeviceNotify event"
---

<p>XkbNoteDeviceChanges &#8211; Note device changes reported in an XkbExtensionDeviceNotify event </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbNoteDeviceChanges</code> <code>(XkbDeviceChangesPtr </code><i>old</i><code>,</code> <code>XkbExtensionDeviceNotifyEvent *</code><i>new</i><code>,</code> <code>unsigned int </code><i>wanted</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; old</i></p>
<dd>
<dd>structure tracking state changes</p>
<dt><i>&#8211; new</i></p>
<dd>event indicating state changes</p>
<dt><i>&#8211; wanted</i></p>
<dd>mask indicating changes to note</dl>
<h2>Description</h2>
<p>The <i>wanted </i> field specifies the changes that should be noted in <i>old, </i> and is composed of the bitwise inclusive OR of one or more of the masks from Table 1. The <i>reason </i> field of the event in <i>new </i> indicates the types of changes the event is reporting. <i>XkbNoteDeviceChanges </i> updates the XkbDeviceChangesRec specified by <i>old </i> with the changes that are both specified in <i>wanted </i> and contained in <i>new-&gt;reason.</i> </p>
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
<p>To update a local copy of the state and configuration of an X input extension device with the changes previously noted in an XkbDeviceChangesRec structure, use <i>XkbGetDeviceInfoChanges.</i></p>
<h2>Structures</h2>
<p>Changes to an Xkb extension device may be tracked by listening to XkbDeviceExtensionNotify events and accumulating the changes in an XkbDeviceChangesRec structure. The changes noted in the structure may then be used in subsequent operations to update either a server configuration or a local copy of an Xkb extension device configuration. The changes structure is defined as follows: </p>
<pre>typedef struct _XkbDeviceChanges {
 unsigned int changed; /* bits indicating what has changed */
 unsigned short first_btn; /* number of first button which changed, if any */
 unsigned short num_btns; /* number of buttons that have changed */
 XkbDeviceLedChangesRec leds;
} XkbDeviceChangesRec,*XkbDeviceChangesPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetdeviceinfochanges/">XkbGetDeviceInfoChanges</a></code>(3)</p>

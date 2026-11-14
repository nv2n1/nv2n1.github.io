---
title: "xkbgetdeviceledinfo(3)"
name: "xkbgetdeviceledinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetdeviceledinfo/"
description: "XkbGetDeviceLedInfo – Query the indicator names, maps, and state associated with an LED feedback of an input extension device"
---

<p>XkbGetDeviceLedInfo &#8211; Query the indicator names, maps, and state associated with an LED feedback of an input extension device </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetDeviceLedInfo</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>unsigned int </code><i>led_class</i><code>,</code> <code>unsigned int </code><i>led_id</i><code>,</code> <code>unsigned int </code><i>which</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_info</i></p>
<dd>structure to update with results</p>
<dt><i>&#8211; led_class</i></p>
<dd>LED feedback class assigned by input extension</p>
<dt><i>&#8211; led_id</i></p>
<dd>LED feedback ID assigned by input extension</p>
<dt><i>&#8211; which</i></p>
<dd>mask indicating desired information</dl>
<h2>Description</h2>
<p><i>XkbGetDeviceLedInfo </i> queries the server for the desired LED information for the feedback specified by <i>led_class </i> and <i>led_id </i> for the X input extension device indicated by <i>device_spec-&gt;device_info </i> and waits for a reply. If successful, <i>XkbGetDeviceLedInfo </i> backfills the relevant fields of <i>device_info </i> as determined by <i>which </i> with the results and returns Success. Valid values for <i>which </i> are the inclusive OR of any of XkbXI_IndicatorNamesMask, XkbXI_IndicatorMapsMask, and XkbXI_IndicatorStateMask. </p>
<p> The fields of <i>device_info </i> that are filled in when this request succeeds are <i>name, type, supported, </i> and <i>unsupported, </i> and portions of the <i>leds </i> structure corresponding to <i>led_class </i> and <i>led_id </i> as indicated by the bits set in <i>which. </i> The <i>device_info-&gt;leds </i> vector is allocated if necessary and <i>sz_leds </i> and <i>num_leds </i> filled in. The <i>led_class, led_id </i> and <i>phys_indicators </i> fields of the <i>device_info-&gt;leds </i> entry corresponding to <i>led_class </i> and <i>led_id </i> are always filled in. </p>
<p> If <i>which </i> contains XkbXI_IndicatorNamesMask, the <i>names_present </i> and <i>names </i> fields of the <i>device_info-&gt;leds </i> structure corresponding to <i>led_class </i> and <i>led_id </i> are updated, if <i>which </i> contains XkbXI_IndicatorStateMask, the corresponding <i>state </i> field is updated, and if <i>which </i> contains XkbXI_IndicatorMapsMask, the <i>maps_present </i> and <i>maps </i> fields are updated. </p>
<p> If a compatible version of Xkb is not available in the server or the Xkb extension has not been properly initialized, <i>XkbGetDeviceLedInfo </i> returns BadAccess. If allocation errors occur, a BadAlloc status is returned. If the device has no indicators, a BadMatch error is returned. If <i>ledClass </i> or <i>ledID </i> have illegal values, a BadValue error is returned. If they have legal values but do not specify a feedback that contains LEDs and is associated with the specified device, a BadMatch error is returned.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>

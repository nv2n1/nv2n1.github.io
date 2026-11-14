---
title: "enum_wimax_st(9)"
name: "enum_wimax_st"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_wimax_st/"
description: "enum_wimax_st – The different states of a WiMAX device"
---

<p>enum_wimax_st &#8211; The different states of a WiMAX device</p>
<h2>Synopsis</h2>
<pre>enum wimax_st {
 __WIMAX_ST_NULL,
 WIMAX_ST_DOWN,
 __WIMAX_ST_QUIESCING,
 WIMAX_ST_UNINITIALIZED,
 WIMAX_ST_RADIO_OFF,
 WIMAX_ST_READY,
 WIMAX_ST_SCANNING,
 WIMAX_ST_CONNECTING,
 WIMAX_ST_CONNECTED,
 __WIMAX_ST_INVALID
}; </pre>
<h2>Constants</h2>
<p>__WIMAX_ST_NULL</p>
<dl>
<dd>The device structure has been allocated and zeroed, but still <code>wimax_dev_add</code> hasn&#8217;t been called. There is no state.</dl>
<p> WIMAX_ST_DOWN</p>
<dl>
<dd>The device has been registered with the WiMAX and networking stacks, but it is not initialized (normally that is done with &#8216;ifconfig DEV up&#8217; [or equivalent], which can upload firmware and enable communications with the device). In this state, the device is powered down and using as less power as possible. This state is the default after a call to <code>wimax_dev_add</code>. It is ok to have drivers move directly to <code>WIMAX_ST_UNINITIALIZED</code> or <code>WIMAX_ST_RADIO_OFF</code> in <code>_probe</code> after the call to <code>wimax_dev_add</code>. It is recommended that the driver leaves this state when calling &#8216;ifconfig DEV up&#8217; and enters it back on &#8216;ifconfig DEV down&#8217;.</dl>
<p> __WIMAX_ST_QUIESCING</p>
<dl>
<dd>The device is being torn down, so no API operations are allowed to proceed except the ones needed to complete the device clean up process.</dl>
<p> WIMAX_ST_UNINITIALIZED</p>
<dl>
<dd>[optional] Communication with the device is setup, but the device still requires some configuration before being operational. Some WiMAX API calls might work.</dl>
<p> WIMAX_ST_RADIO_OFF</p>
<dl>
<dd>The device is fully up; radio is off (wether by hardware or software switches). It is recommended to always leave the device in this state after initialization.</dl>
<p> WIMAX_ST_READY</p>
<dl>
<dd>The device is fully up and radio is on.</dl>
<p> WIMAX_ST_SCANNING</p>
<dl>
<dd>[optional] The device has been instructed to scan. In this state, the device cannot be actively connected to a network.</dl>
<p> WIMAX_ST_CONNECTING</p>
<dl>
<dd>The device is connecting to a network. This state exists because in some devices, the connect process can include a number of negotiations between user space, kernel space and the device. User space needs to know what the device is doing. If the connect sequence in a device is atomic and fast, the device can transition directly to CONNECTED</dl>
<p> WIMAX_ST_CONNECTED</p>
<dl>
<dd>The device is connected to a network.</dl>
<p> __WIMAX_ST_INVALID</p>
<dl>
<dd>This is an invalid state used to mark the maximum numeric value of states.</dl>
<h2>Description</h2>
<p>Transitions from one state to another one are atomic and can only be caused in kernel space with <code>wimax_state_change</code>. To read the state, use <code>wimax_state_get</code>. </p>
<p> States starting with __ are internal and shall not be used or referred to by drivers or userspace. They look ugly, but that&#8217;s the point &#8212; if any use is made non-internal to the stack, it is easier to catch on review. </p>
<p> All API operations [with well defined exceptions] will take the device mutex before starting and then check the state. If the state is <code>__WIMAX_ST_NULL</code>, <code>WIMAX_ST_DOWN</code>, <code>WIMAX_ST_UNINITIALIZED</code> or <code>__WIMAX_ST_QUIESCING</code>, it will drop the lock and quit with &#8211;<code>EINVAL</code>, &#8211;<code>ENOMEDIUM</code>, &#8211;<code>ENOTCONN</code> or &#8211;<code>ESHUTDOWN</code>. </p>
<p> The order of the definitions is important, so we can do numerical comparisons (eg: &lt; <code>WIMAX_ST_RADIO_OFF</code> means the device is not ready to operate).</p>
<h2>Copyright</h2>

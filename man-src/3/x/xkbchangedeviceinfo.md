---
title: "xkbchangedeviceinfo(3)"
name: "xkbchangedeviceinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangedeviceinfo/"
description: "XkbChangeDeviceInfo – Update the server’s description of a device with the changes noted in an XkbDeviceChangesRec"
---

<p>XkbChangeDeviceInfo &#8211; Update the server&#8217;s description of a device with the changes noted in an XkbDeviceChangesRec </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbChangeDeviceInfo</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDeviceInfoPtr </code><i>device_info</i><code>,</code> <code>XkbDeviceChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_info</i></p>
<dd>local copy of device state and configuration</p>
<dt><i>&#8211; changes</i></p>
<dd>note specifying changes in device_info</dl>
<h2>Description</h2>
<p><i>XkbChangeDeviceInfo </i> updates the server&#8217;s description of the device specified in <i>device_info-&gt;device_spec </i> with the changes specified in <i>changes </i> and contained in <i>device_info. </i> The update is made by an <i>XkbSetDeviceInfo </i> request.</p>
<h2>Structures</h2>
<p>Changes to an Xkb extension device may be tracked by listening to XkbDeviceExtensionNotify events and accumulating the changes in an XkbDeviceChangesRec structure. The changes noted in the structure may then be used in subsequent operations to update either a server configuration or a local copy of an Xkb extension device configuration. The changes structure is defined as follows: </p>
<pre>typedef struct _XkbDeviceChanges {
 unsigned int changed; /* bits indicating what has changed */
 unsigned short first_btn; /* number of first button which changed, if any */
 unsigned short num_btns; /* number of buttons that have changed */
 XkbDeviceLedChangesRec leds;
} XkbDeviceChangesRec,*XkbDeviceChangesPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbsetdeviceinfo/">XkbSetDeviceInfo</a></code>(3)</p>

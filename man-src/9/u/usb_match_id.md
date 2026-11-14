---
title: "usb_match_id(9)"
name: "usb_match_id"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_match_id/"
description: "usb_match_id – find first usb_device_id matching device or interface"
---

<p>usb_match_id &#8211; find first usb_device_id matching device or interface</p>
<h2>Synopsis</h2>
<pre><code>const struct usb_device_id *usb_match_id(struct usb_interface *interface, const struct usb_device_id *id);</code></pre>
<h2>Arguments</h2>
<p><i>interface</i></p>
<dl>
<dd>
<dd>the interface of interest</dl>
<p> <i>id</i></p>
<dl>
<dd>array of usb_device_id structures, terminated by zero entry</dl>
<h2>Description</h2>
<p>usb_match_id searches an array of usb_device_id&#8217;s and returns the first one matching the device or interface, or null. This is used when binding (or rebinding) a driver to an interface. Most USB device drivers will use this indirectly, through the usb core, but some layered driver frameworks use it directly. These device tables are exported with MODULE_DEVICE_TABLE, through modutils, to support the driver loading functionality of USB hotplugging.</p>
<h2>Return</h2>
<p>The first matching usb_device_id, or <code>NULL</code>. </p>
<p> What Matches: </p>
<p> The &#8220;match_flags&#8221; element in a usb_device_id controls which members are used. If the corresponding bit is set, the value in the device_id must match its corresponding member in the device or interface descriptor, or else the device_id does not match. </p>
<p> &#8220;driver_info&#8221; is normally used only by device drivers, but you can create a wildcard &#8220;matches anything&#8221; usb_device_id as a driver&#8217;s &#8220;modules.usbmap&#8221; entry if you provide an id with only a nonzero &#8220;driver_info&#8221; field. If you do this, the USB device driver&#8217;s <code>probe</code> routine should use additional intelligence to decide whether to bind to the specified interface. </p>
<p> What Makes Good usb_device_id Tables: </p>
<p> The match algorithm is very simple, so that intelligence in driver selection must come from smart driver id records. Unless you have good reasons to use another selection policy, provide match elements only in related groups, and order match specifiers from specific to general. Use the macros provided for that purpose if you can. </p>
<p> The most specific match specifiers use device descriptor data. These are commonly used with product-specific matches; the USB_DEVICE macro lets you provide vendor and product IDs, and you can also match against ranges of product revisions. These are widely used for devices with application or vendor specific bDeviceClass values. </p>
<p> Matches based on device class/subclass/protocol specifications are slightly more general; use the USB_DEVICE_INFO macro, or its siblings. These are used with single-function devices where bDeviceClass doesn&#8217;t specify that each interface has its own class. </p>
<p> Matches based on interface class/subclass/protocol are the most general; they let drivers bind to any interface on a multiple-function device. Use the USB_INTERFACE_INFO macro, or its siblings, to match class-per-interface style devices (as recorded in bInterfaceClass). </p>
<p> Note that an entry created by USB_INTERFACE_INFO won&#8217;t match any interface if the device class is set to Vendor-Specific. This is deliberate; according to the USB spec the meanings of the interface class/subclass/protocol for these devices are also vendor-specific, and hence matching against a standard product class wouldn&#8217;t work anyway. If you really want to use an interface-based match for such a device, create a match record that also specifies the vendor ID. (Unforunately there isn&#8217;t a standard macro for creating records like this.) </p>
<p> Within those groups, remember that not all combinations are meaningful. For example, don&#8217;t give a product version range without vendor and product IDs; or specify a protocol without its associated class and subclass.</p>
<h2>Copyright</h2>

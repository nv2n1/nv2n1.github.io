---
title: "struct_usb_host_config(9)"
name: "struct_usb_host_config"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_host_config/"
description: "struct_usb_host_config – representation of a device’s configuration"
---

<p>struct_usb_host_config &#8211; representation of a device&#8217;s configuration</p>
<h2>Synopsis</h2>
<pre><code>struct usb_host_config {
    struct usb_config_descriptor desc;
    char *string;
    struct usb_interface_assoc_descriptor *intf_assoc[USB_MAXIADS];
    struct usb_interface *interface[USB_MAXINTERFACES];
    struct usb_interface_cache *intf_cache[USB_MAXINTERFACES];
    unsigned char *extra;
    int extralen;
};</code></pre>
<h2>Members</h2>
<p>desc</p>
<dl>
<dd>the device&#8217;s configuration descriptor.</dl>
<p> string</p>
<dl>
<dd>pointer to the cached version of the iConfiguration string, if present for this configuration.</dl>
<p> intf_assoc[USB_MAXIADS]</p>
<dl>
<dd>list of any interface association descriptors in this config</dl>
<p> interface[USB_MAXINTERFACES]</p>
<dl>
<dd>array of pointers to usb_interface structures, one for each interface in the configuration. The number of interfaces is stored in desc.bNumInterfaces. These pointers are valid only while the the configuration is active.</dl>
<p> intf_cache[USB_MAXINTERFACES]</p>
<dl>
<dd>array of pointers to usb_interface_cache structures, one for each interface in the configuration. These structures exist for the entire life of the device.</dl>
<p> extra</p>
<dl>
<dd>pointer to buffer containing all extra descriptors associated with this configuration (those preceding the first interface descriptor).</dl>
<p> extralen</p>
<dl>
<dd>length of the extra descriptors buffer.</dl>
<h2>Description</h2>
<p>USB devices may have multiple configurations, but only one can be active at any time. Each encapsulates a different operational environment; for example, a dual-speed device would have separate configurations for full-speed and high-speed operation. The number of configurations available is stored in the device descriptor as bNumConfigurations. </p>
<p> A configuration can contain multiple interfaces. Each corresponds to a different function of the USB device, and all are available whenever the configuration is active. The USB standard says that interfaces are supposed to be numbered from 0 to desc.bNumInterfaces-1, but a lot of devices get this wrong. In addition, the interface array is not guaranteed to be sorted in numerical order. Use <code>usb_ifnum_to_if</code> to look up an interface entry based on its number. </p>
<p> Device drivers should not attempt to activate configurations. The choice of which configuration to install is a policy decision based on such considerations as available power, functionality provided, and the user&#8217;s desires (expressed through userspace tools). However, drivers can call <code>usb_reset_configuration</code> to reinitialize the current configuration and all its interfaces.</p>
<h2>Copyright</h2>

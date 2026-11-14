---
title: "struct_usb_interface_cache(9)"
name: "struct_usb_interface_cache"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_interface_cache/"
---

struct_usb_interface_cache - long-term representation of a device interface

<h2>Synopsis</h2>

<pre><code>struct usb_interface_cache {
    unsigned num_altsetting;
    struct kref ref;
    struct usb_host_interface altsetting[0];
};</code></pre>

<h2>Members</h2>

num_altsetting
<dl><dd>number of altsettings defined.</dl>
 

 ref
<dl><dd>reference counter.</dl>
 

 altsetting[0]
<dl><dd>variable-length array of interface structures, one for each alternate setting that may be selected. Each one includes a set of endpoint configurations. They will be in no particular order.</dl>

<h2>Description</h2>

These structures persist for the lifetime of a usb_device, unlike struct usb_interface (which persists only as long as its configuration is installed). The altsetting arrays can be accessed through these structures at any time, permitting comparison of configurations and providing support for the /proc/bus/usb/devices pseudo-file.

<h2>Copyright</h2>



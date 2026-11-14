---
title: "struct_usbdrv_wrap(9)"
name: "struct_usbdrv_wrap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usbdrv_wrap/"
---

struct_usbdrv_wrap - wrapper for driver-model structure

<h2>Synopsis</h2>

<pre><code>struct usbdrv_wrap {
    struct device_driver driver;
    int for_devices;
};</code></pre>

<h2>Members</h2>

driver
<dl><dd>The driver-model core driver structure.</dl>
 

 for_devices
<dl><dd>Non-zero for device drivers, 0 for interface drivers.</dl>

<h2>Copyright</h2>



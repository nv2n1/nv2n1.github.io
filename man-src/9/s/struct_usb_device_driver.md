---
title: "struct_usb_device_driver(9)"
name: "struct_usb_device_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_device_driver/"
description: "struct_usb_device_driver – identifies USB device driver to usbcore"
---

<p>struct_usb_device_driver &#8211; identifies USB device driver to usbcore</p>
<h2>Synopsis</h2>
<pre><code>struct usb_device_driver {
    const char *name;
    int (*probe)(struct usb_device *udev);
    void (*disconnect)(struct usb_device *udev);
    int (*suspend)(struct usb_device *udev, pm_message_t message);
    int (*resume)(struct usb_device *udev, pm_message_t message);
    struct usbdrv_wrap drvwrap;
    unsigned int supports_autosuspend : 1;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>The driver name should be unique among USB drivers, and should normally be the same as the module name.</dl>
<p> probe</p>
<dl>
<dd>Called to see if the driver is willing to manage a particular device. If it is, probe returns zero and uses <code>dev_set_drvdata</code> to associate driver-specific data with the device. If unwilling to manage the device, return a negative errno value.</dl>
<p> disconnect</p>
<dl>
<dd>Called when the device is no longer accessible, usually because it has been (or is being) disconnected or the driver&#8217;s module is being unloaded.</dl>
<p> suspend</p>
<dl>
<dd>Called when the device is going to be suspended by the system.</dl>
<p> resume</p>
<dl>
<dd>Called when the device is being resumed by the system.</dl>
<p> drvwrap</p>
<dl>
<dd>Driver-model core structure wrapper.</dl>
<p> supports_autosuspend</p>
<dl>
<dd>if set to 0, the USB core will not allow autosuspend for devices bound to this driver.</dl>
<h2>Description</h2>
<p>USB drivers must provide all the fields listed above except drvwrap.</p>
<h2>Copyright</h2>

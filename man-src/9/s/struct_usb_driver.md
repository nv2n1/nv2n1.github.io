---
title: "struct_usb_driver(9)"
name: "struct_usb_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_driver/"
description: "struct_usb_driver – identifies USB interface driver to usbcore"
---

<p>struct_usb_driver &#8211; identifies USB interface driver to usbcore</p>
<h2>Synopsis</h2>
<pre><code>struct usb_driver {
    const char *name;
    int (*probe)(struct usb_interface *intf, const struct usb_device_id *id);
    void (*disconnect)(struct usb_interface *intf);
    int (*unlocked_ioctl)(struct usb_interface *intf, unsigned int code, void *buf);
    int (*suspend)(struct usb_interface *intf, pm_message_t message);
    int (*resume)(struct usb_interface *intf);
    int (*reset_resume)(struct usb_interface *intf);
    int (*pre_reset)(struct usb_interface *intf);
    int (*post_reset)(struct usb_interface *intf);
    const struct usb_device_id *id_table;
    struct usb_dynids dynids;
    struct usbdrv_wrap drvwrap;
    unsigned int no_dynamic_id : 1;
    unsigned int supports_autosuspend : 1;
    unsigned int disable_hub_initiated_lpm : 1;
    unsigned int soft_unbind : 1;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>The driver name should be unique among USB drivers, and should normally be the same as the module name.</dl>
<p> probe</p>
<dl>
<dd>Called to see if the driver is willing to manage a particular interface on a device. If it is, probe returns zero and uses <code>usb_set_intfdata</code> to associate driver-specific data with the interface. It may also use <code>usb_set_interface</code> to specify the appropriate altsetting. If unwilling to manage the interface, return -ENODEV, if genuine IO errors occurred, an appropriate negative errno value.</dl>
<p> disconnect</p>
<dl>
<dd>Called when the interface is no longer accessible, usually because its device has been (or is being) disconnected or the driver module is being unloaded.</dl>
<p> unlocked_ioctl</p>
<dl>
<dd>Used for drivers that want to talk to userspace through the &#8220;usbfs&#8221; filesystem. This lets devices provide ways to expose information to user space regardless of where they do (or don&#8217;t) show up otherwise in the filesystem.</dl>
<p> suspend</p>
<dl>
<dd>Called when the device is going to be suspended by the system either from system sleep or runtime suspend context. The return value will be ignored in system sleep context, so do NOT try to continue using the device if suspend fails in this case. Instead, let the resume or reset-resume routine recover from the failure.</dl>
<p> resume</p>
<dl>
<dd>Called when the device is being resumed by the system.</dl>
<p> reset_resume</p>
<dl>
<dd>Called when the suspended device has been reset instead of being resumed.</dl>
<p> pre_reset</p>
<dl>
<dd>Called by <code>usb_reset_device</code> when the device is about to be reset. This routine must not return until the driver has no active URBs for the device, and no more URBs may be submitted until the post_reset method is called.</dl>
<p> post_reset</p>
<dl>
<dd>Called by <code>usb_reset_device</code> after the device has been reset</dl>
<p> id_table</p>
<dl>
<dd>USB drivers use ID table to support hotplugging. Export this with MODULE_DEVICE_TABLE(usb,&#8230;). This must be set or your driver&#8217;s probe function will never get called.</dl>
<p> dynids</p>
<dl>
<dd>used internally to hold the list of dynamically added device ids for this driver.</dl>
<p> drvwrap</p>
<dl>
<dd>Driver-model core structure wrapper.</dl>
<p> no_dynamic_id</p>
<dl>
<dd>if set to 1, the USB core will not allow dynamic ids to be added to this driver by preventing the sysfs file from being created.</dl>
<p> supports_autosuspend</p>
<dl>
<dd>if set to 0, the USB core will not allow autosuspend for interfaces bound to this driver.</dl>
<p> disable_hub_initiated_lpm</p>
<dl>
<dd>if set to 1, the USB core will not allow hubs to initiate lower power link state transitions when an idle timeout occurs. Device-initiated USB 3.0 link PM will still be allowed.</dl>
<p> soft_unbind</p>
<dl>
<dd>if set to 1, the USB core will not kill URBs and disable endpoints before calling the driver&#8217;s disconnect method.</dl>
<h2>Description</h2>
<p>USB interface drivers must provide a name, <code>probe</code> and <code>disconnect</code> methods, and an id_table. Other driver fields are optional. </p>
<p> The id_table is used in hotplugging. It holds a set of descriptors, and specialized data may be associated with each entry. That table is used by both user and kernel mode hotplugging support. </p>
<p> The <code>probe</code> and <code>disconnect</code> methods are called in a context where they can sleep, but they should avoid abusing the privilege. Most work to connect to a device should be done when the device is opened, and undone at the last close. The disconnect code needs to address concurrency issues with respect to <code>open</code> and <code>close</code> methods, as well as forcing all pending I/O requests to complete (by unlinking them as necessary, and blocking until the unlinks complete).</p>
<h2>Copyright</h2>

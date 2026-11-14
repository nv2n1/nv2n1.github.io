---
title: "struct_usb_composite_driver(9)"
name: "struct_usb_composite_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_composite_driver/"
description: "struct_usb_composite_driver – groups configurations into a gadget"
---

<p>struct_usb_composite_driver &#8211; groups configurations into a gadget</p>
<h2>Synopsis</h2>
<pre><code>struct usb_composite_driver {
    const char *name;
    const struct usb_device_descriptor *dev;
    struct usb_gadget_strings **strings;
    enum usb_device_speed max_speed;
    unsigned needs_serial : 1;
    int (*bind)(struct usb_composite_dev *cdev);
    int (*unbind)(struct usb_composite_dev *);
    void (*disconnect)(struct usb_composite_dev *);
    void (*suspend)(struct usb_composite_dev *);
    void (*resume)(struct usb_composite_dev *);
    struct usb_gadget_driver gadget_driver;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>For diagnostics, identifies the driver.</dl>
<p> dev</p>
<dl>
<dd>Template descriptor for the device, including default device identifiers.</dl>
<p> strings</p>
<dl>
<dd>tables of strings, keyed by identifiers assigned during <i>bind</i> and language IDs provided in control requests. Note: The first entries are predefined. The first entry that may be used is USB_GADGET_FIRST_AVAIL_IDX</dl>
<p> max_speed</p>
<dl>
<dd>Highest speed the driver supports.</dl>
<p> needs_serial</p>
<dl>
<dd>set to 1 if the gadget needs userspace to provide a serial number. If one is not provided, warning will be printed.</dl>
<p> bind</p>
<dl>
<dd>(REQUIRED) Used to allocate resources that are shared across the whole device, such as string IDs, and add its configurations using <i>usb_add_config</i>(). This may fail by returning a negative errno value; it should return zero on successful initialization.</dl>
<p> unbind</p>
<dl>
<dd>Reverses <i>bind</i>; called as a side effect of unregistering this driver.</dl>
<p> disconnect</p>
<dl>
<dd>optional driver disconnect method</dl>
<p> suspend</p>
<dl>
<dd>Notifies when the host stops sending USB traffic, after function notifications</dl>
<p> resume</p>
<dl>
<dd>Notifies configuration when the host restarts USB traffic, before function notifications</dl>
<p> gadget_driver</p>
<dl>
<dd>Gadget driver controlling this driver</dl>
<h2>Description</h2>
<p>Devices default to reporting self powered operation. Devices which rely on bus powered operation should report this in their <i>bind</i> method. </p>
<p> Before returning from <i>bind</i>, various fields in the template descriptor may be overridden. These include the idVendor/idProduct/bcdDevice values normally to bind the appropriate host side driver, and the three strings (iManufacturer, iProduct, iSerialNumber) normally used to provide user meaningful device identifiers. (The strings will not be defined unless they are defined in <i>dev</i> and <i>strings</i>.) The correct ep0 maxpacket size is also reported, as defined by the underlying controller driver.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

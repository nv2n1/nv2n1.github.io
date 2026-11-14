---
title: "struct_usb_class_driver(9)"
name: "struct_usb_class_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_class_driver/"
description: "struct_usb_class_driver – identifies a USB driver that wants to use the USB major number"
---

<p>struct_usb_class_driver &#8211; identifies a USB driver that wants to use the USB major number</p>
<h2>Synopsis</h2>
<pre><code>struct usb_class_driver {
    char *name;
    char *(*devnode)(struct device *dev, umode_t *mode);
    const struct file_operations *fops;
    int minor_base;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>the usb class device name for this driver. Will show up in sysfs.</dl>
<p> devnode</p>
<dl>
<dd>Callback to provide a naming hint for a possible device node to create.</dl>
<p> fops</p>
<dl>
<dd>pointer to the struct file_operations of this driver.</dl>
<p> minor_base</p>
<dl>
<dd>the start of the minor range for this driver.</dl>
<h2>Description</h2>
<p>This structure is used for the <code>usb_register_dev</code> and <code>usb_unregister_dev</code> functions, to consolidate a number of the parameters used for them.</p>
<h2>Copyright</h2>

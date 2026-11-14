---
title: "struct_usb_interface(9)"
name: "struct_usb_interface"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_interface/"
description: "struct_usb_interface – what usb device drivers talk to"
---

<p>struct_usb_interface &#8211; what usb device drivers talk to</p>
<h2>Synopsis</h2>
<pre><code>struct usb_interface {
    struct usb_host_interface *altsetting;
    struct usb_host_interface *cur_altsetting;
    unsigned num_altsetting;
    struct usb_interface_assoc_descriptor *intf_assoc;
    int minor;
    enum usb_interface_condition condition;
    unsigned sysfs_files_created : 1;
    unsigned ep_devs_created : 1;
    unsigned unregistering : 1;
    unsigned needs_remote_wakeup : 1;
    unsigned needs_altsetting0 : 1;
    unsigned needs_binding : 1;
    unsigned resetting_device : 1;
    unsigned authorized : 1;
    struct device dev;
    struct device *usb_dev;
    atomic_t pm_usage_cnt;
    struct work_struct reset_ws;
};</code></pre>
<h2>Members</h2>
<p>altsetting</p>
<dl>
<dd>array of interface structures, one for each alternate setting that may be selected. Each one includes a set of endpoint configurations. They will be in no particular order.</dl>
<p> cur_altsetting</p>
<dl>
<dd>the current altsetting.</dl>
<p> num_altsetting</p>
<dl>
<dd>number of altsettings defined.</dl>
<p> intf_assoc</p>
<dl>
<dd>interface association descriptor</dl>
<p> minor</p>
<dl>
<dd>the minor number assigned to this interface, if this interface is bound to a driver that uses the USB major number. If this interface does not use the USB major, this field should be unused. The driver should set this value in the <code>probe</code> function of the driver, after it has been assigned a minor number from the USB core by calling <code>usb_register_dev</code>.</dl>
<p> condition</p>
<dl>
<dd>binding state of the interface: not bound, binding (in <code>probe</code>), bound to a driver, or unbinding (in <code>disconnect</code>)</dl>
<p> sysfs_files_created</p>
<dl>
<dd>sysfs attributes exist</dl>
<p> ep_devs_created</p>
<dl>
<dd>endpoint child pseudo-devices exist</dl>
<p> unregistering</p>
<dl>
<dd>flag set when the interface is being unregistered</dl>
<p> needs_remote_wakeup</p>
<dl>
<dd>flag set when the driver requires remote-wakeup capability during autosuspend.</dl>
<p> needs_altsetting0</p>
<dl>
<dd>flag set when a set-interface request for altsetting 0 has been deferred.</dl>
<p> needs_binding</p>
<dl>
<dd>flag set when the driver should be re-probed or unbound following a reset or suspend operation it doesn&#8217;t support.</dl>
<p> resetting_device</p>
<dl>
<dd>USB core reset the device, so use alt setting 0 as current; needs bandwidth alloc after reset.</dl>
<p> authorized</p>
<dl>
<dd>This allows to (de)authorize individual interfaces instead a whole device in contrast to the device authorization.</dl>
<p> dev</p>
<dl>
<dd>driver model&#8217;s view of this device</dl>
<p> usb_dev</p>
<dl>
<dd>if an interface is bound to the USB major, this will point to the sysfs representation for that device.</dl>
<p> pm_usage_cnt</p>
<dl>
<dd>PM usage counter for this interface</dl>
<p> reset_ws</p>
<dl>
<dd>Used for scheduling resets from atomic context.</dl>
<h2>Description</h2>
<p>USB device drivers attach to interfaces on a physical device. Each interface encapsulates a single high level function, such as feeding an audio stream to a speaker or reporting a change in a volume control. Many USB devices only have one interface. The protocol used to talk to an interface&#8217;s endpoints can be defined in a usb &#8220;class&#8221; specification, or by a product&#8217;s vendor. The (default) control endpoint is part of every interface, but is never listed among the interface&#8217;s descriptors. </p>
<p> The driver that is bound to the interface can use standard driver model calls such as <code>dev_get_drvdata</code> on the dev member of this structure. </p>
<p> Each interface may have alternate settings. The initial configuration of a device sets altsetting 0, but the device driver can change that setting using <code>usb_set_interface</code>. Alternate settings are often used to control the use of periodic endpoints, such as by having different endpoints use different amounts of reserved USB bandwidth. All standards-conformant USB devices that use isochronous endpoints will use them in non-default settings. </p>
<p> The USB specification says that alternate setting numbers must run from 0 to one less than the total number of alternate settings. But some devices manage to mess this up, and the structures aren&#8217;t necessarily stored in numerical order anyhow. Use <code>usb_altnum_to_altsetting</code> to look up an alternate setting in the altsetting array based on its number.</p>
<h2>Copyright</h2>

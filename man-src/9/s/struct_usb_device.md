---
title: "struct_usb_device(9)"
name: "struct_usb_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_device/"
description: "struct_usb_device – kernel’s representation of a USB device"
---

<p>struct_usb_device &#8211; kernel&#8217;s representation of a USB device</p>
<h2>Synopsis</h2>
<pre><code>struct usb_device {
    int devnum;
    char devpath[16];
    u32 route;
    enum usb_device_state state;
    enum usb_device_speed speed;
    struct usb_tt *tt;
    int ttport;
    unsigned int toggle[2];
    struct usb_device *parent;
    struct usb_bus *bus;
    struct usb_host_endpoint ep0;
    struct device dev;
    struct usb_device_descriptor descriptor;
    struct usb_host_bos *bos;
    struct usb_host_config *config;
    struct usb_host_config *actconfig;
    struct usb_host_endpoint *ep_in[16];
    struct usb_host_endpoint *ep_out[16];
    char **rawdescriptors;
    unsigned short bus_mA;
    u8 portnum;
    u8 level;
    unsigned can_submit : 1;
    unsigned persist_enabled : 1;
    unsigned have_langid : 1;
    unsigned authorized : 1;
    unsigned authenticated : 1;
    unsigned wusb : 1;
    unsigned lpm_capable : 1;
    unsigned usb2_hw_lpm_capable : 1;
    unsigned usb2_hw_lpm_besl_capable : 1;
    unsigned usb2_hw_lpm_enabled : 1;
    unsigned usb2_hw_lpm_allowed : 1;
    unsigned usb3_lpm_u1_enabled : 1;
    unsigned usb3_lpm_u2_enabled : 1;
    int string_langid;
    char *product;
    char *manufacturer;
    char *serial;
    struct list_head filelist;
    int maxchild;
    u32 quirks;
    atomic_t urbnum;
    unsigned long active_duration;
#ifdef CONFIG_PM
    unsigned long connect_time;
    unsigned do_remote_wakeup : 1;
    unsigned reset_resume : 1;
    unsigned port_is_suspended : 1;
#endif
    struct wusb_dev *wusb_dev;
    int slot_id;
    enum usb_device_removable removable;
    struct usb2_lpm_parameters l1_params;
    struct usb3_lpm_parameters u1_params;
    struct usb3_lpm_parameters u2_params;
    unsigned lpm_disable_count;
};</code></pre>
<h2>Members</h2>
<p>devnum</p>
<dl>
<dd>device number; address on a USB bus</dl>
<p> devpath[16]</p>
<dl>
<dd>device ID string for use in messages (e.g., /port/&#8230;)</dl>
<p> route</p>
<dl>
<dd>tree topology hex string for use with xHCI</dl>
<p> state</p>
<dl>
<dd>device state: configured, not attached, etc.</dl>
<p> speed</p>
<dl>
<dd>device speed: high/full/low (or error)</dl>
<p> tt</p>
<dl>
<dd>Transaction Translator info; used with low/full speed dev, highspeed hub</dl>
<p> ttport</p>
<dl>
<dd>device port on that tt hub</dl>
<p> toggle[2]</p>
<dl>
<dd>one bit for each endpoint, with ([0] = IN, [1] = OUT) endpoints</dl>
<p> parent</p>
<dl>
<dd>our hub, unless we&#8217;re the root</dl>
<p> bus</p>
<dl>
<dd>bus we&#8217;re part of</dl>
<p> ep0</p>
<dl>
<dd>endpoint 0 data (default control pipe)</dl>
<p> dev</p>
<dl>
<dd>generic device interface</dl>
<p> descriptor</p>
<dl>
<dd>USB device descriptor</dl>
<p> bos</p>
<dl>
<dd>USB device BOS descriptor set</dl>
<p> config</p>
<dl>
<dd>all of the device&#8217;s configs</dl>
<p> actconfig</p>
<dl>
<dd>the active configuration</dl>
<p> ep_in[16]</p>
<dl>
<dd>array of IN endpoints</dl>
<p> ep_out[16]</p>
<dl>
<dd>array of OUT endpoints</dl>
<p> rawdescriptors</p>
<dl>
<dd>raw descriptors for each config</dl>
<p> bus_mA</p>
<dl>
<dd>Current available from the bus</dl>
<p> portnum</p>
<dl>
<dd>parent port number (origin 1)</dl>
<p> level</p>
<dl>
<dd>number of USB hub ancestors</dl>
<p> can_submit</p>
<dl>
<dd>URBs may be submitted</dl>
<p> persist_enabled</p>
<dl>
<dd>USB_PERSIST enabled for this device</dl>
<p> have_langid</p>
<dl>
<dd>whether string_langid is valid</dl>
<p> authorized</p>
<dl>
<dd>policy has said we can use it; (user space) policy determines if we authorize this device to be used or not. By default, wired USB devices are authorized. WUSB devices are not, until we authorize them from user space. FIXME &#8212; complete doc</dl>
<p> authenticated</p>
<dl>
<dd>Crypto authentication passed</dl>
<p> wusb</p>
<dl>
<dd>device is Wireless USB</dl>
<p> lpm_capable</p>
<dl>
<dd>device supports LPM</dl>
<p> usb2_hw_lpm_capable</p>
<dl>
<dd>device can perform USB2 hardware LPM</dl>
<p> usb2_hw_lpm_besl_capable</p>
<dl>
<dd>device can perform USB2 hardware BESL LPM</dl>
<p> usb2_hw_lpm_enabled</p>
<dl>
<dd>USB2 hardware LPM is enabled</dl>
<p> usb2_hw_lpm_allowed</p>
<dl>
<dd>Userspace allows USB 2.0 LPM to be enabled</dl>
<p> usb3_lpm_u1_enabled</p>
<dl>
<dd>USB3 hardware U1 LPM enabled</dl>
<p> usb3_lpm_u2_enabled</p>
<dl>
<dd>USB3 hardware U2 LPM enabled</dl>
<p> string_langid</p>
<dl>
<dd>language ID for strings</dl>
<p> product</p>
<dl>
<dd>iProduct string, if present (static)</dl>
<p> manufacturer</p>
<dl>
<dd>iManufacturer string, if present (static)</dl>
<p> serial</p>
<dl>
<dd>iSerialNumber string, if present (static)</dl>
<p> filelist</p>
<dl>
<dd>usbfs files that are open to this device</dl>
<p> maxchild</p>
<dl>
<dd>number of ports if hub</dl>
<p> quirks</p>
<dl>
<dd>quirks of the whole device</dl>
<p> urbnum</p>
<dl>
<dd>number of URBs submitted for the whole device</dl>
<p> active_duration</p>
<dl>
<dd>total time device is not suspended</dl>
<p> connect_time</p>
<dl>
<dd>time device was first connected</dl>
<p> do_remote_wakeup</p>
<dl>
<dd>remote wakeup should be enabled</dl>
<p> reset_resume</p>
<dl>
<dd>needs reset instead of resume</dl>
<p> port_is_suspended</p>
<dl>
<dd>the upstream port is suspended (L2 or U3)</dl>
<p> wusb_dev</p>
<dl>
<dd>if this is a Wireless USB device, link to the WUSB specific data for the device.</dl>
<p> slot_id</p>
<dl>
<dd>Slot ID assigned by xHCI</dl>
<p> removable</p>
<dl>
<dd>Device can be physically removed from this port</dl>
<p> l1_params</p>
<dl>
<dd>best effor service latency for USB2 L1 LPM state, and L1 timeout.</dl>
<p> u1_params</p>
<dl>
<dd>exit latencies for USB3 U1 LPM state, and hub-initiated timeout.</dl>
<p> u2_params</p>
<dl>
<dd>exit latencies for USB3 U2 LPM state, and hub-initiated timeout.</dl>
<p> lpm_disable_count</p>
<dl>
<dd>Ref count used by <code>usb_disable_lpm</code> and <code>usb_enable_lpm</code> to keep track of the number of functions that require USB 3.0 Link Power Management to be disabled for this usb_device. This count should only be manipulated by those functions, with the bandwidth_mutex is held.</dl>
<h2>Notes</h2>
<p>Usbcore drivers should not set usbdev-&gt;state directly. Instead use <code>usb_set_device_state</code>.</p>
<h2>Copyright</h2>

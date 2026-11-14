---
title: "struct_usb_gadget(9)"
name: "struct_usb_gadget"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_gadget/"
description: "struct_usb_gadget – represents a usb slave device"
---

<p>struct_usb_gadget &#8211; represents a usb slave device</p>
<h2>Synopsis</h2>
<pre><code>struct usb_gadget {
    struct work_struct work;
    struct usb_udc *udc;
    const struct usb_gadget_ops *ops;
    struct usb_ep *ep0;
    struct list_head ep_list;
    enum usb_device_speed speed;
    enum usb_device_speed max_speed;
    enum usb_device_state state;
    const char *name;
    struct device dev;
    unsigned out_epnum;
    unsigned in_epnum;
    unsigned mA;
    struct usb_otg_caps *otg_caps;
    unsigned sg_supported : 1;
    unsigned is_otg : 1;
    unsigned is_a_peripheral : 1;
    unsigned b_hnp_enable : 1;
    unsigned a_hnp_support : 1;
    unsigned a_alt_hnp_support : 1;
    unsigned hnp_polling_support : 1;
    unsigned host_request_flag : 1;
    unsigned quirk_ep_out_aligned_size : 1;
    unsigned quirk_avoids_skb_reserve : 1;
    unsigned is_selfpowered : 1;
    unsigned deactivated : 1;
    unsigned connected : 1;
};</code></pre>
<h2>Members</h2>
<p>work</p>
<dl>
<dd>(internal use) Workqueue to be used for <code>sysfs_notify</code></dl>
<p> udc</p>
<dl>
<dd>struct usb_udc pointer for this gadget</dl>
<p> ops</p>
<dl>
<dd>Function pointers used to access hardware-specific operations.</dl>
<p> ep0</p>
<dl>
<dd>Endpoint zero, used when reading or writing responses to driver <code>setup</code> requests</dl>
<p> ep_list</p>
<dl>
<dd>List of other endpoints supported by the device.</dl>
<p> speed</p>
<dl>
<dd>Speed of current connection to USB host.</dl>
<p> max_speed</p>
<dl>
<dd>Maximal speed the UDC can handle. UDC must support this and all slower speeds.</dl>
<p> state</p>
<dl>
<dd>the state we are now (attached, suspended, configured, etc)</dl>
<p> name</p>
<dl>
<dd>Identifies the controller hardware type. Used in diagnostics and sometimes configuration.</dl>
<p> dev</p>
<dl>
<dd>Driver model state for this abstract device.</dl>
<p> out_epnum</p>
<dl>
<dd>last used out ep number</dl>
<p> in_epnum</p>
<dl>
<dd>last used in ep number</dl>
<p> mA</p>
<dl>
<dd>last set mA value</dl>
<p> otg_caps</p>
<dl>
<dd>OTG capabilities of this gadget.</dl>
<p> sg_supported</p>
<dl>
<dd>true if we can handle scatter-gather</dl>
<p> is_otg</p>
<dl>
<dd>True if the USB device port uses a Mini-AB jack, so that the gadget driver must provide a USB OTG descriptor.</dl>
<p> is_a_peripheral</p>
<dl>
<dd>False unless is_otg, the &#8220;A&#8221; end of a USB cable is in the Mini-AB jack, and HNP has been used to switch roles so that the &#8220;A&#8221; device currently acts as A-Peripheral, not A-Host.</dl>
<p> b_hnp_enable</p>
<dl>
<dd>OTG device feature flag, indicating that the A-Host enabled HNP support.</dl>
<p> a_hnp_support</p>
<dl>
<dd>OTG device feature flag, indicating that the A-Host supports HNP at this port.</dl>
<p> a_alt_hnp_support</p>
<dl>
<dd>OTG device feature flag, indicating that the A-Host only supports HNP on a different root port.</dl>
<p> hnp_polling_support</p>
<dl>
<dd>OTG device feature flag, indicating if the OTG device in peripheral mode can support HNP polling.</dl>
<p> host_request_flag</p>
<dl>
<dd>OTG device feature flag, indicating if A-Peripheral or B-Peripheral wants to take host role.</dl>
<p> quirk_ep_out_aligned_size</p>
<dl>
<dd>epout requires buffer size to be aligned to MaxPacketSize.</dl>
<p> quirk_avoids_skb_reserve</p>
<dl>
<dd>udc/platform wants to avoid <code>skb_reserve</code> in u_ether.c to improve performance.</dl>
<p> is_selfpowered</p>
<dl>
<dd>if the gadget is self-powered.</dl>
<p> deactivated</p>
<dl>
<dd>True if gadget is deactivated &#8211; in deactivated state it cannot be connected.</dl>
<p> connected</p>
<dl>
<dd>True if gadget is connected.</dl>
<h2>Description</h2>
<p>Gadgets have a mostly-portable &#8220;gadget driver&#8221; implementing device functions, handling all usb configurations and interfaces. Gadget drivers talk to hardware-specific code indirectly, through ops vectors. That insulates the gadget driver from hardware details, and packages the hardware endpoints through generic i/o queues. The &#8220;usb_gadget&#8221; and &#8220;usb_ep&#8221; interfaces provide that insulation from the hardware. </p>
<p> Except for the driver data, all fields in this structure are read-only to the gadget driver. That driver data is part of the &#8220;driver model&#8221; infrastructure in 2.6 (and later) kernels, and for earlier systems is grouped in a similar structure that&#8217;s not known to the rest of the kernel. </p>
<p> Values of the three OTG device feature flags are updated before the <code>setup</code> call corresponding to USB_REQ_SET_CONFIGURATION, and before driver <code>suspend</code> calls. They are valid only when is_otg, and when the device is acting as a B-Peripheral (so is_a_peripheral is false).</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

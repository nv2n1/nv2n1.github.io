---
title: "struct_usb_gadget_driver(9)"
name: "struct_usb_gadget_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_gadget_driver/"
description: "struct_usb_gadget_driver – driver for usb ‘slave’ devices"
---

<p>struct_usb_gadget_driver &#8211; driver for usb &#8216;slave&#8217; devices</p>
<h2>Synopsis</h2>
<pre><code>struct usb_gadget_driver {
    char *function;
    enum usb_device_speed max_speed;
    int (*bind)(struct usb_gadget *gadget, struct usb_gadget_driver *driver);
    void (*unbind)(struct usb_gadget *);
    int (*setup)(struct usb_gadget *, const struct usb_ctrlrequest *);
    void (*disconnect)(struct usb_gadget *);
    void (*suspend)(struct usb_gadget *);
    void (*resume)(struct usb_gadget *);
    void (*reset)(struct usb_gadget *);
    struct device_driver driver;
    char *udc_name;
    struct list_head pending;
    unsigned match_existing_only : 1;
};</code></pre>
<h2>Members</h2>
<p>function</p>
<dl>
<dd>String describing the gadget&#8217;s function</dl>
<p> max_speed</p>
<dl>
<dd>Highest speed the driver handles.</dl>
<p> bind</p>
<dl>
<dd>the driver&#8217;s bind callback</dl>
<p> unbind</p>
<dl>
<dd>Invoked when the driver is unbound from a gadget, usually from rmmod (after a disconnect is reported). Called in a context that permits sleeping.</dl>
<p> setup</p>
<dl>
<dd>Invoked for ep0 control requests that aren&#8217;t handled by the hardware level driver. Most calls must be handled by the gadget driver, including descriptor and configuration management. The 16 bit members of the setup data are in USB byte order. Called in_interrupt; this may not sleep. Driver queues a response to ep0, or returns negative to stall.</dl>
<p> disconnect</p>
<dl>
<dd>Invoked after all transfers have been stopped, when the host is disconnected. May be called in_interrupt; this may not sleep. Some devices can&#8217;t detect disconnect, so this might not be called except as part of controller shutdown.</dl>
<p> suspend</p>
<dl>
<dd>Invoked on USB suspend. May be called in_interrupt.</dl>
<p> resume</p>
<dl>
<dd>Invoked on USB resume. May be called in_interrupt.</dl>
<p> reset</p>
<dl>
<dd>Invoked on USB bus reset. It is mandatory for all gadget drivers and should be called in_interrupt.</dl>
<p> driver</p>
<dl>
<dd>Driver model state for this driver.</dl>
<p> udc_name</p>
<dl>
<dd>A name of UDC this driver should be bound to. If udc_name is NULL, this driver will be bound to any available UDC.</dl>
<p> pending</p>
<dl>
<dd>UDC core private data used for deferred probe of this driver.</dl>
<p> match_existing_only</p>
<dl>
<dd>If udc is not found, return an error and don&#8217;t add this gadget driver to list of pending driver</dl>
<h2>Description</h2>
<p>Devices are disabled till a gadget driver successfully <code>bind</code>s, which means the driver will handle <code>setup</code> requests needed to enumerate (and meet &#8220;chapter 9&#8221; requirements) then do some useful work. </p>
<p> If gadget-&gt;is_otg is true, the gadget driver must provide an OTG descriptor during enumeration, or else fail the <code>bind</code> call. In such cases, no USB traffic may flow until both <code>bind</code> returns without having called <code>usb_gadget_disconnect</code>, and the USB host stack has initialized. </p>
<p> Drivers use hardware-specific knowledge to configure the usb hardware. endpoint addressing is only one of several hardware characteristics that are in descriptors the ep0 implementation returns from <code>setup</code> calls. </p>
<p> Except for ep0 implementation, most driver code shouldn&#8217;t need change to run on top of different usb controllers. It&#8217;ll use endpoints set up by that ep0 implementation. </p>
<p> The usb controller driver handles a few standard usb requests. Those include set_address, and feature flags for devices, interfaces, and endpoints (the get_status, set_feature, and clear_feature requests). </p>
<p> Accordingly, the driver&#8217;s <code>setup</code> callback must always implement all get_descriptor requests, returning at least a device descriptor and a configuration descriptor. Drivers must make sure the endpoint descriptors match any hardware constraints. Some hardware also constrains other descriptors. (The pxa250 allows only configurations 1, 2, or 3). </p>
<p> The driver&#8217;s <code>setup</code> callback must also implement set_configuration, and should also implement set_interface, get_configuration, and get_interface. Setting a configuration (or interface) is where endpoints should be activated or (config 0) shut down. </p>
<p> (Note that only the default control endpoint is supported. Neither hosts nor devices generally support control traffic except to ep0.) </p>
<p> Most devices will ignore USB suspend/resume operations, and so will not provide those callbacks. However, some may need to change modes when the host is not longer directing those activities. For example, local controls (buttons, dials, etc) may need to be re-enabled since the (remote) host can&#8217;t do that any longer; or an error state might be cleared, to make the device behave identically whether or not power is maintained.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

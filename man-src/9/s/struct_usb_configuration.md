---
title: "struct_usb_configuration(9)"
name: "struct_usb_configuration"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_configuration/"
description: "struct_usb_configuration – represents one gadget configuration"
---

<p>struct_usb_configuration &#8211; represents one gadget configuration</p>
<h2>Synopsis</h2>
<pre><code>struct usb_configuration {
    const char *label;
    struct usb_gadget_strings **strings;
    const struct usb_descriptor_header **descriptors;
    void (*unbind)(struct usb_configuration *);
    int (*setup)(struct usb_configuration *, const struct usb_ctrlrequest *);
    u8 bConfigurationValue;
    u8 iConfiguration;
    u8 bmAttributes;
    u16 MaxPower;
    struct usb_composite_dev *cdev;
};</code></pre>
<h2>Members</h2>
<p>label</p>
<dl>
<dd>For diagnostics, describes the configuration.</dl>
<p> strings</p>
<dl>
<dd>Tables of strings, keyed by identifiers assigned during <i>bind</i>() and by language IDs provided in control requests.</dl>
<p> descriptors</p>
<dl>
<dd>Table of descriptors preceding all function descriptors. Examples include OTG and vendor-specific descriptors.</dl>
<p> unbind</p>
<dl>
<dd>Reverses <i>bind</i>; called as a side effect of unregistering the driver which added this configuration.</dl>
<p> setup</p>
<dl>
<dd>Used to delegate control requests that aren&#8217;t handled by standard device infrastructure or directed at a specific interface.</dl>
<p> bConfigurationValue</p>
<dl>
<dd>Copied into configuration descriptor.</dl>
<p> iConfiguration</p>
<dl>
<dd>Copied into configuration descriptor.</dl>
<p> bmAttributes</p>
<dl>
<dd>Copied into configuration descriptor.</dl>
<p> MaxPower</p>
<dl>
<dd>Power consumtion in mA. Used to compute bMaxPower in the configuration descriptor after considering the bus speed.</dl>
<p> cdev</p>
<dl>
<dd>assigned by <i>usb_add_config</i>() before calling <i>bind</i>(); this is the device associated with this configuration.</dl>
<h2>Description</h2>
<p>Configurations are building blocks for gadget drivers structured around function drivers. Simple USB gadgets require only one function and one configuration, and handle dual-speed hardware by always providing the same functionality. Slightly more complex gadgets may have more than one single-function configuration at a given speed; or have configurations that only work at one speed. </p>
<p> Composite devices are, by definition, ones with configurations which include more than one function. </p>
<p> The lifecycle of a usb_configuration includes allocation, initialization of the fields described above, and calling <i>usb_add_config</i>() to set up internal data and bind it to a specific device. The configuration&#8217;s <i>bind</i>() method is then used to initialize all the functions and then call <i>usb_add_function</i>() for them. </p>
<p> Those functions would normally be independent of each other, but that&#8217;s not mandatory. CDC WMC devices are an example where functions often depend on other functions, with some functions subsidiary to others. Such interdependency may be managed in any way, so long as all of the descriptors complete by the time the composite driver returns from its <code>bind</code> routine.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

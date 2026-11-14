---
title: "usb_gadget_config_buf(9)"
name: "usb_gadget_config_buf"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_gadget_config_buf/"
description: "usb_gadget_config_buf – builts a complete configuration descriptor"
---

<p>usb_gadget_config_buf &#8211; builts a complete configuration descriptor</p>
<h2>Synopsis</h2>
<pre><code>int usb_gadget_config_buf(const struct usb_config_descriptor *config, void *buf, unsigned length, const struct usb_descriptor_header **desc);</code></pre>
<h2>Arguments</h2>
<p><i>config</i></p>
<dl>
<dd>
<dd>Header for the descriptor, including characteristics such as power requirements and number of interfaces.</dl>
<p> <i>buf</i></p>
<dl>
<dd>Buffer for the resulting configuration descriptor.</dl>
<p> <i>length</i></p>
<dl>
<dd>Length of buffer. If this is not big enough to hold the entire configuration descriptor, an error code will be returned.</dl>
<p> <i>desc</i></p>
<dl>
<dd>Null-terminated vector of pointers to the descriptors (interface, endpoint, etc) defining all functions in this device configuration.</dl>
<h2>Description</h2>
<p>This copies descriptors into the response buffer, building a descriptor for that configuration. It returns the buffer length or a negative status code. The config.wTotalLength field is set to match the length of the result, but other descriptor fields (including power usage and interface count) must be set by the caller. </p>
<p> Gadget drivers could use this when constructing a config descriptor in response to USB_REQ_GET_DESCRIPTOR. They will need to patch the resulting bDescriptorType value if USB_DT_OTHER_SPEED_CONFIG is needed.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

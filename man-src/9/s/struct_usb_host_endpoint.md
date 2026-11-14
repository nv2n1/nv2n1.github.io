---
title: "struct_usb_host_endpoint(9)"
name: "struct_usb_host_endpoint"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_host_endpoint/"
---

struct_usb_host_endpoint - host-side endpoint descriptor and queue

<h2>Synopsis</h2>

<pre><code>struct usb_host_endpoint {
    struct usb_endpoint_descriptor desc;
    struct usb_ss_ep_comp_descriptor ss_ep_comp;
    struct usb_ssp_isoc_ep_comp_descriptor ssp_isoc_ep_comp;
    struct list_head urb_list;
    void *hcpriv;
    struct ep_device *ep_dev;
    unsigned char *extra;
    int extralen;
    int enabled;
    int streams;
};</code></pre>

<h2>Members</h2>

desc
<dl><dd>descriptor for this endpoint, wMaxPacketSize in native byteorder</dl>
 

 ss_ep_comp
<dl><dd>SuperSpeed companion descriptor for this endpoint</dl>
 

 ssp_isoc_ep_comp
<dl><dd>SuperSpeedPlus isoc companion descriptor for this endpoint</dl>
 

 urb_list
<dl><dd>urbs queued to this endpoint; maintained by usbcore</dl>
 

 hcpriv
<dl><dd>for use by HCD; typically holds hardware dma queue head (QH) with one or more transfer descriptors (TDs) per urb</dl>
 

 ep_dev
<dl><dd>ep_device for sysfs info</dl>
 

 extra
<dl><dd>descriptors following this endpoint in the configuration</dl>
 

 extralen
<dl><dd>how many bytes of "extra" are valid</dl>
 

 enabled
<dl><dd>URBs may be submitted to this endpoint</dl>
 

 streams
<dl><dd>number of USB-3 streams allocated on the endpoint</dl>

<h2>Description</h2>

USB requests are always queued to a given endpoint, identified by a descriptor within an active interface in a given USB configuration.

<h2>Copyright</h2>



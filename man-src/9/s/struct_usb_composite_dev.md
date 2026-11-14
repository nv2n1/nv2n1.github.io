---
title: "struct_usb_composite_dev(9)"
name: "struct_usb_composite_dev"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_composite_dev/"
description: "struct_usb_composite_dev – represents one composite usb gadget"
---

<p>struct_usb_composite_dev &#8211; represents one composite usb gadget</p>
<h2>Synopsis</h2>
<pre><code>struct usb_composite_dev {
    struct usb_gadget *gadget;
    struct usb_request *req;
    struct usb_request *os_desc_req;
    struct usb_configuration *config;
    u8 qw_sign[OS_STRING_QW_SIGN_LEN];
    u8 b_vendor_code;
    struct usb_configuration *os_desc_config;
    unsigned int use_os_string : 1;
};</code></pre>
<h2>Members</h2>
<p>gadget</p>
<dl>
<dd>read-only, abstracts the gadget&#8217;s usb peripheral controller</dl>
<p> req</p>
<dl>
<dd>used for control responses; buffer is pre-allocated</dl>
<p> os_desc_req</p>
<dl>
<dd>used for OS descriptors responses; buffer is pre-allocated</dl>
<p> config</p>
<dl>
<dd>the currently active configuration</dl>
<p> qw_sign[OS_STRING_QW_SIGN_LEN]</p>
<dl>
<dd>qwSignature part of the OS string</dl>
<p> b_vendor_code</p>
<dl>
<dd>bMS_VendorCode part of the OS string</dl>
<p> os_desc_config</p>
<dl>
<dd>the configuration to be used with OS descriptors</dl>
<p> use_os_string</p>
<dl>
<dd>false by default, interested gadgets set it</dl>
<h2>Description</h2>
<p>One of these devices is allocated and initialized before the associated device driver&#8217;s <code>bind</code> is called. </p>
<p> OPEN ISSUE: it appears that some WUSB devices will need to be built by combining a normal (wired) gadget with a wireless one. This revision of the gadget framework should probably try to make sure doing that won&#8217;t hurt too much. </p>
<p> One notion for how to handle Wireless USB devices involves: (a) a second gadget here, discovery mechanism TBD, but likely needing separate &#8220;register/unregister WUSB gadget&#8221; calls; (b) updates to usb_gadget to include flags &#8220;is it wireless&#8221;, &#8220;is it wired&#8221;, plus (presumably in a wrapper structure) bandgroup and PHY info; (c) presumably a wireless_ep wrapping a usb_ep, and reporting wireless-specific parameters like maxburst and maxsequence; (d) configurations that are specific to wireless links; (e) function drivers that understand wireless configs and will support wireless for (additional) function instances; (f) a function to support association setup (like CBAF), not necessarily requiring a wireless adapter; (g) composite device setup that can create one or more wireless configs, including appropriate association setup support; (h) more, TBD.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

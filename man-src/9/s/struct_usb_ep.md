---
title: "struct_usb_ep(9)"
name: "struct_usb_ep"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_ep/"
description: "struct_usb_ep – device side representation of USB endpoint"
---

<p>struct_usb_ep &#8211; device side representation of USB endpoint</p>
<h2>Synopsis</h2>
<pre><code>struct usb_ep {
    void *driver_data;
    const char *name;
    const struct usb_ep_ops *ops;
    struct list_head ep_list;
    struct usb_ep_caps caps;
    unsigned maxpacket : 16;
    unsigned maxpacket_limit : 16;
    unsigned max_streams : 16;
    unsigned mult : 2;
    unsigned maxburst : 5;
    u8 address;
    const struct usb_endpoint_descriptor *desc;
    const struct usb_ss_ep_comp_descriptor *comp_desc;
};</code></pre>
<h2>Members</h2>
<p>driver_data</p>
<dl>
<dd>for use by the gadget driver.</dl>
<p> name</p>
<dl>
<dd>identifier for the endpoint, such as &#8220;ep-a&#8221; or &#8220;ep9in-bulk&#8221;</dl>
<p> ops</p>
<dl>
<dd>Function pointers used to access hardware-specific operations.</dl>
<p> ep_list</p>
<dl>
<dd>the gadget&#8217;s ep_list holds all of its endpoints</dl>
<p> caps</p>
<dl>
<dd>The structure describing types and directions supported by endoint.</dl>
<p> maxpacket</p>
<dl>
<dd>The maximum packet size used on this endpoint. The initial value can sometimes be reduced (hardware allowing), according to the endpoint descriptor used to configure the endpoint.</dl>
<p> maxpacket_limit</p>
<dl>
<dd>The maximum packet size value which can be handled by this endpoint. It&#8217;s set once by UDC driver when endpoint is initialized, and should not be changed. Should not be confused with maxpacket.</dl>
<p> max_streams</p>
<dl>
<dd>The maximum number of streams supported by this EP (0 &#8211; 16, actual number is 2^n)</dl>
<p> mult</p>
<dl>
<dd>multiplier, &#8216;mult&#8217; value for SS Isoc EPs</dl>
<p> maxburst</p>
<dl>
<dd>the maximum number of bursts supported by this EP (for usb3)</dl>
<p> address</p>
<dl>
<dd>used to identify the endpoint when finding descriptor that matches connection speed</dl>
<p> desc</p>
<dl>
<dd>endpoint descriptor. This pointer is set before the endpoint is enabled and remains valid until the endpoint is disabled.</dl>
<p> comp_desc</p>
<dl>
<dd>In case of SuperSpeed support, this is the endpoint companion descriptor that is used to configure the endpoint</dl>
<h2>Description</h2>
<p>the bus controller driver lists all the general purpose endpoints in gadget-&gt;ep_list. the control endpoint (gadget-&gt;ep0) is not in that list, and is accessed only in response to a driver <code>setup</code> callback.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

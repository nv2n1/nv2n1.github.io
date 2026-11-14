---
title: "config_ep_by_speed(9)"
name: "config_ep_by_speed"
section: "9"
letter: "c"
url: "/docs/linux/man/9-config_ep_by_speed/"
description: "config_ep_by_speed – configures the given endpoint according to gadget speed."
---

<p>config_ep_by_speed &#8211; configures the given endpoint according to gadget speed.</p>
<h2>Synopsis</h2>
<pre><code>int config_ep_by_speed(struct usb_gadget *g, struct usb_function *f, struct usb_ep *_ep);</code></pre>
<h2>Arguments</h2>
<p><i>g</i></p>
<dl>
<dd>
<dd>pointer to the gadget</dl>
<p> <i>f</i></p>
<dl>
<dd>usb function</dl>
<p> <i>_ep</i></p>
<dl>
<dd>the endpoint to configure</dl>
<h2>Return</h2>
<p>error code, 0 on success </p>
<p> This function chooses the right descriptors for a given endpoint according to gadget speed and saves it in the endpoint desc field. If the endpoint already has a descriptor assigned to it &#8211; overwrites it with currently corresponding descriptor. The endpoint maxpacket field is updated according to the chosen descriptor.</p>
<h2>Note</h2>
<p>the supplied function should hold all the descriptors for supported speeds</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

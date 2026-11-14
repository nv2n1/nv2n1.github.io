---
title: "usb_ifnum_to_if(9)"
name: "usb_ifnum_to_if"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_ifnum_to_if/"
description: "usb_ifnum_to_if – get the interface object with a given interface number"
---

<p>usb_ifnum_to_if &#8211; get the interface object with a given interface number</p>
<h2>Synopsis</h2>
<pre><code>struct usb_interface *usb_ifnum_to_if(const struct usb_device *dev, unsigned ifnum);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device whose current configuration is considered</dl>
<p> <i>ifnum</i></p>
<dl>
<dd>the desired interface</dl>
<h2>Description</h2>
<p>This walks the device descriptor for the currently active configuration to find the interface object with the particular interface number. </p>
<p> Note that configuration descriptors are not required to assign interface numbers sequentially, so that it would be incorrect to assume that the first interface in that descriptor corresponds to interface zero. This routine helps device drivers avoid such mistakes. However, you should make sure that you do the right thing with any alternate settings available for this interfaces. </p>
<p> Don&#8217;t call this function unless you are bound to one of the interfaces on this device or you have locked the device!</p>
<h2>Return</h2>
<p>A pointer to the interface that has <i>ifnum</i> as interface number, if found. <code>NULL</code> otherwise.</p>
<h2>Copyright</h2>

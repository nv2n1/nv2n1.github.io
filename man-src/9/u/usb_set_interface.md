---
title: "usb_set_interface(9)"
name: "usb_set_interface"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_set_interface/"
description: "usb_set_interface – Makes a particular alternate setting be current"
---

<p>usb_set_interface &#8211; Makes a particular alternate setting be current</p>
<h2>Synopsis</h2>
<pre><code>int usb_set_interface(struct usb_device *dev, int interface, int alternate);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device whose interface is being updated</dl>
<p> <i>interface</i></p>
<dl>
<dd>the interface being updated</dl>
<p> <i>alternate</i></p>
<dl>
<dd>the setting being chosen.</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>This is used to enable data transfers on interfaces that may not be enabled by default. Not all devices support such configurability. Only the driver bound to an interface may change its setting. </p>
<p> Within any given configuration, each interface may have several alternative settings. These are often used to control levels of bandwidth consumption. For example, the default setting for a high speed interrupt endpoint may not send more than 64 bytes per microframe, while interrupt transfers of up to 3KBytes per microframe are legal. Also, isochronous endpoints may never be part of an interface&#8217;s default setting. To access such bandwidth, alternate interface settings must be made current. </p>
<p> Note that in the Linux USB subsystem, bandwidth associated with an endpoint in a given alternate setting is not reserved until an URB is submitted that needs that bandwidth. Some other operating systems allocate bandwidth early, when a configuration is chosen. </p>
<p> This call is synchronous, and may not be used in an interrupt context. Also, drivers must not change altsettings while urbs are scheduled for endpoints in that interface; all such urbs must first be completed (perhaps forced by unlinking).</p>
<h2>Return</h2>
<p>Zero on success, or else the status code returned by the underlying <code>usb_control_msg</code> call.</p>
<h2>Copyright</h2>

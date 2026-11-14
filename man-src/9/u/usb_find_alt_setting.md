---
title: "usb_find_alt_setting(9)"
name: "usb_find_alt_setting"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_find_alt_setting/"
description: "usb_find_alt_setting – Given a configuration, find the alternate setting for the given interface."
---

<p>usb_find_alt_setting &#8211; Given a configuration, find the alternate setting for the given interface.</p>
<h2>Synopsis</h2>
<pre><code>struct usb_host_interface *usb_find_alt_setting(struct usb_host_config *config, unsigned int iface_num, unsigned int alt_num);</code></pre>
<h2>Arguments</h2>
<p><i>config</i></p>
<dl>
<dd>
<dd>the configuration to search (not necessarily the current config).</dl>
<p> <i>iface_num</i></p>
<dl>
<dd>interface number to search in</dl>
<p> <i>alt_num</i></p>
<dl>
<dd>alternate interface setting number to search for.</dl>
<h2>Description</h2>
<p>Search the configuration&#8217;s interface cache for the given alt setting.</p>
<h2>Return</h2>
<p>The alternate setting, if found. <code>NULL</code> otherwise.</p>
<h2>Copyright</h2>

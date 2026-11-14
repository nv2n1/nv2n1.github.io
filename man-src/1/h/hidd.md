---
title: "hidd(1)"
name: "hidd"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hidd/"
description: "hidd – Bluetooth HID daemon"
---

<h2>NAME</h2>
<p> hidd &#8211; Bluetooth HID daemon</p>
<h2>DESCRIPTION</h2>
<p> hidd &#8211; Bluetooth HID daemon</p>
<h3>Usage:</h3>
<dl>
<dt>
<dd> hidd [options] [commands]</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;hciX|bdaddr&gt;</p>
<dd> Local HCI device or BD Address</p>
<dt><code>-t</code> &lt;timeout&gt;</p>
<dd> Set idle timeout (in minutes)</p>
<dt><code>-n</code>, <code>&#8211;nodaemon</code></p>
<dd> Don&#8217;t fork daemon to background</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help</dl>
<h3>Commands:</h3>
<dl>
<dt><code>&#8211;server</code></p>
<dd> Start HID server</p>
<dt><code>&#8211;search</code></p>
<dd> Search for HID devices</p>
<dt><code>&#8211;connect</code> &lt;bdaddr&gt;</p>
<dd> Connect remote HID device</p>
<dt><code>&#8211;kill</code> &lt;bdaddr&gt;</p>
<dd> Terminate HID connection</p>
<dt><code>&#8211;killall</code></p>
<dd> Terminate all connections</p>
<dt><code>&#8211;show</code></p>
<dd> List current HID connections </p>
</dl>
<h2>Index</h2>

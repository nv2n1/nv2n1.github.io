---

title: "hidd(1)"
name: "hidd"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hidd/"
description: "hidd – Bluetooth HID daemon"
---

<p> hidd &#8211; Bluetooth HID daemon</p>
<h2>DESCRIPTION</h2>
<p> hidd &#8211; Bluetooth HID daemon</p>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> hidd [options] [commands]</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;hciX|bdaddr&gt;</dt>
<dd> Local HCI device or BD Address</dd>
<dt><code>-t</code> &lt;timeout&gt;</dt>
<dd> Set idle timeout (in minutes)</dd>
<dt><code>-n</code>, <code>&#8211;nodaemon</code></dt>
<dd> Don&#8217;t fork daemon to background</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display help</dd></dl>
<h3>Commands:</h3>
<dl>
<dt><code>&#8211;server</code></dt>
<dd> Start HID server</dd>
<dt><code>&#8211;search</code></dt>
<dd> Search for HID devices</dd>
<dt><code>&#8211;connect</code> &lt;bdaddr&gt;</dt>
<dd> Connect remote HID device</dd>
<dt><code>&#8211;kill</code> &lt;bdaddr&gt;</dt>
<dd> Terminate HID connection</dd>
<dt><code>&#8211;killall</code></dt>
<dd> Terminate all connections</dd>
<dt><code>&#8211;show</code></dt>
<dd> List current HID connections </dd>
</dl>

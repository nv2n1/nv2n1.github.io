---
title: "hid2hci(1)"
name: "hid2hci"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hid2hci/"
description: "hid2hci – Bluetooth HID to HCI mode switching utility"
---

<h2 class="name">NAME</h2>
<p> hid2hci &#8211; Bluetooth HID to HCI mode switching utility </p>
<h2>SYNOPSIS</h2>
<p> <code>hid2hci</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-hid2hci/">hid2hci</a>(1)</code> is used to set up switch supported Bluetooth devices into the HCI mode and back.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;mode=[</code><i>mode</i>] Sets the mode to the device into. The possible values</p>
<dd> for <i>mode</i> are <code>hid</code>, <code>hci</code>.</p>
<dt><code>&#8211;method=[</code><i>method</i>] Which vendor method to use for switching the device.</p>
<dd> The possible values for <i>method</i> are <code>csr</code>, <code>csr2</code>, <code>logitech-hdi</code>, <code>dell</code>.</p>
<dt><code>&#8211;devpath</code></p>
<dd> Specifies the device path in /sys</p>
<dt><code>&#8211;help</code></p>
<dd> Gives a list of possible options.</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Marcel Holtmann &lt;marcel [at] holtmann.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>

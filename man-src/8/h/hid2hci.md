---
title: "hid2hci(8)"
name: "hid2hci"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hid2hci/"
description: "hid2hci – Bluetooth HID to HCI mode switching utility"
---

<p>hid2hci &#8211; Bluetooth HID to HCI mode switching utility</p>
<h2>Synopsis</h2>
<p><code>hid2hci</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p><code>hid2hci</code> is used to set up switch supported Bluetooth devices into the HCI mode and back.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;mode= [hid, hci]</code></p>
<dd>Sets the mode to switch the device into</p>
<dt><code>&#8211;method= [csr, logitech-hid, dell]</code></p>
<dd>Which vendor method to use for switching the device.</p>
<dt><code>&#8211;devpath=</code></p>
<dd>Specifies the device path in /sys</p>
<dt><code>&#8211;help</code></p>
<dd>Gives a list of possible options.</p>
<dt></dl>
<h2>Author</h2>
<dd>Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt;.</p>

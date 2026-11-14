---
title: "tripplitesu(8)"
name: "tripplitesu"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tripplitesu/"
description: "tripplitesu – Driver for Tripp-Lite SmartOnline (SU) UPS equipment"
---

<p>tripplitesu &#8211; Driver for Tripp-Lite SmartOnline (SU) UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the tripplitesu driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports the Tripp Lite SmartOnline family (via the serial port).</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>lowbatt</code>=<i>num</i></p>
<dl>
<dd>Set the low battery warning threshold in percent at which shutdown is initiated by <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). By default, the UPS may not report low battery until there are only a few seconds left. Common values are around 25&#8212;30.</dl>
<h2>Author</h2>
<p>Allan N. Hessenflow &lt;allanh [at] kallisti.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Other drivers for Tripp-Lite hardware:</h3>
<p><code><a href="/docs/linux/man/8-tripplite/">tripplite</a></code>(8), <code><a href="/docs/linux/man/8-tripplite_usb/">tripplite_usb</a></code>(8), <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

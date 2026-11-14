---
title: "tripplite(8)"
name: "tripplite"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tripplite/"
description: "tripplite – Driver for Tripp-Lite SmartPro UPS equipment"
---

<p>tripplite &#8211; Driver for Tripp-Lite SmartPro UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the tripplite driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver should work on the SmartPro line, including the SMART700 and SMART700SER. It only supports SmartPro models that communicate using the serial port.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>offdelay</code>=<i>num</i></p>
<dl>
<dd>Time to wait before the UPS is turned off after the kill power command is sent. The default value is 64 (in seconds).</dl>
<p> <code>rebootdelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer before the UPS is cycled after the reboot command is sent. The default value is 64 (in seconds).</dl>
<p> <code>startdelay</code>=<i>num</i></p>
<dl>
<dd>Set the time that the UPS waits before it turns itself back on after a reboot command. The default value is 60 (in seconds).</dl>
<h2>Known Issues And Bugs</h2>
<p>Battery charge information may not be correct for all UPSes. It is tuned to be correct for a SMART700SER. Other models may not provide correct information. Information from the manufacturer would be helpful.</p>
<h2>Authors</h2>
<p>Rickard E. (Rik) Faith, Nicholas Kain</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Other drivers for Tripp-Lite hardware:</h3>
<p><code><a href="/docs/linux/man/8-tripplitesu/">tripplitesu</a></code>(8), <code><a href="/docs/linux/man/8-tripplite_usb/">tripplite_usb</a></code>(8), <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

---
title: "liebert-esp2(8)"
name: "liebert-esp2"
section: "8"
letter: "l"
url: "/docs/linux/man/8-liebert-esp2/"
description: "liebert-esp2 – Driver for Liebert UPS, using the ESP-II serial protocol"
---

<p>liebert-esp2 &#8211; Driver for Liebert UPS, using the ESP-II serial protocol</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the liebert-esp2 driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This is an experimental driver. You have been warned.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>baudrate=</code><i>num</i></p>
<dl>
<dd>Set the speed of the serial connection &#8211; 1200, 2400 (default), 4800, 9600 or 19200.</dl>
<h2>Author</h2>
<p>Richard Gregory &lt;R.Gregory at liverpool.ac.uk&gt;, Arjen de Korte &lt;adkorte-guest at alioth.debian.org&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

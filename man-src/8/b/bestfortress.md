---
title: "bestfortress(8)"
name: "bestfortress"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bestfortress/"
description: "bestfortress – Driver for old Best Fortress UPS equipment"
---

<p>bestfortress &#8211; Driver for old Best Fortress UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the bestfortress driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports old Best Fortress UPS equipment using a serial connection.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>baudrate</code>=<i>num</i></p>
<dl>
<dd>Set the speed of the serial connection &#8211; 1200, 2400, 4800 or 9600.</dl>
<p> <code>max_load</code>=<i>VA</i></p>
<dl>
<dd>Set the full-scale value of the <code>ups.load</code> variable.</dl>
<h2>Author</h2>
<p>Holger Dietze &lt;holger.dietze [at] advis.de&gt;, Stuart D. Gathman &lt;stuart [at] bmsi.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>The newer Best Power drivers:</h3>
<p><code><a href="/docs/linux/man/8-bestups/">bestups</a></code>(8), <code><a href="/docs/linux/man/8-bestuferrups/">bestuferrups</a></code>(8), <code><a href="/docs/linux/man/8-bestfcom/">bestfcom</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

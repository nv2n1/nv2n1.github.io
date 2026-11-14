---
title: "metasys(8)"
name: "metasys"
section: "8"
letter: "m"
url: "/docs/linux/man/8-metasys/"
description: "metasys – Driver for Meta System UPS equipment"
---

<p>metasys &#8211; Driver for Meta System UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the metasys driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The <code>metasys</code> driver was written with the &quot;Meta System UPS Protocol Rev.1.12&quot; kindly supplied from Meta System. </p>
<p> The driver should support all the common features of the ups models: </p>
<dl>
<dd>&bull; HF Line (/2) 1-8 boards</dl>
<dl>
<dd>&bull; HF Millennium (810, 820)</dl>
<dl>
<dd>&bull; HF TOP Line (910, 920, 930, 940, 950, 970, 980)</dl>
<dl>
<dd>&bull; ECO Network (750, 1000, 1050, 1500, 1800, 2000, 2100, 2500, 3000)</dl>
<dl>
<dd>&bull; ECO (305, 308, 311, 511, 516, 519, 522, SX, SXI)</dl>
<dl>
<dd>&bull; ally HF (800, 1000, 1250, 1600, 2000, 2500)</dl>
<dl>
<dd>&bull; Megaline (1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000)</dl>
<h2>Cabling</h2>
<p>The needed cable is a standard pin-to-pin serial cable with at least pins 2, 3, and 5 (on DB9 connector) connected.</p>
<h2>Extra Arguments</h2>
<p>This driver supports no extra arguments from <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>Bugs</h2>
<p>This driver has been tested on Meta System HF Millennium 820 and ally HF 1000 only. </p>
<p> Any information about the use of the driver with the other listed UPS are really welcome.</p>
<h2>Author</h2>
<p>Fabio Di Niro &lt;blaxwan [at] users.sourceforge.net&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

---
title: "solis(8)"
name: "solis"
section: "8"
letter: "s"
url: "/docs/linux/man/8-solis/"
description: "solis – Driver for Brazilian Microsol SOLIS UPS equipment"
---

<p>solis &#8211; Driver for Brazilian Microsol SOLIS UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the solis driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver has been tested with : </p>
<dl>
<dd>&bull; Solis 1000 VA</dl>
<dl>
<dd>&bull; Solis 1500 VA</dl>
<dl>
<dd>&bull; Solis 2000 VA</dl>
<dl>
<dd>&bull; Solis 3000 VA</dl>
<p> All Solis models are sinusoidal on-line</p>
<h2>Extra Arguments</h2>
<p>This driver support the following extra optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5). </p>
<p> <code>battext = n</code> &#8211; (default = 0, no extra battery, where n = Ampere*hour ) </p>
<p> <code>prgshut = 1</code> &#8211; (default = 0, no programable shutdown )</p>
<h2>Commands</h2>
<dl>
<dd>&bull; shutdown.return &#8211; Shut down in .3 minutes and restart in .3 minutes</dl>
<dl>
<dd>&bull; shutdown.stayoff &#8211; Shut down in .3 minutes and do not return</dl>
<h2>Author</h2>
<p>Silvino B. Magalhães &lt;sbm2yk [at] gmail.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

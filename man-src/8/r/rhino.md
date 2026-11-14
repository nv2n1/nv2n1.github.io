---
title: "rhino(8)"
name: "rhino"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhino/"
description: "rhino – Driver for Brazilian Microsol RHINO UPS equipment"
---

<p>rhino &#8211; Driver for Brazilian Microsol RHINO UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the rhino driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver has been tested with : </p>
<dl>
<dd>&bull; Rhino 6000 VA</dl>
<dl>
<dd>&bull; Rhino 7500 VA</dl>
<dl>
<dd>&bull; Rhino 10000 VA</dl>
<dl>
<dd>&bull; Rhino 20000 VA</dl>
<p> All Rhino models are sinusoidal on-line.</p>
<h2>Extra Arguments</h2>
<p>This driver support the following extra optional settings in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>battext = n</code> &#8211; (default = 0, no extra battery, where n = Ampere*hour )</p>
<h2>Commands</h2>
<dl>
<dd>&bull; load.on &#8211; Turn on the load immediately</dl>
<dl>
<dd>&bull; load.off &#8211; Turn off the load immediately</dl>
<dl>
<dd>&bull; bypass.start &#8211; Put the UPS in bypass mode</dl>
<dl>
<dd>&bull; bypass.stop &#8211; Put the UPS out of bypass mode</dl>
<dl>
<dd>&bull; shutdown.stayoff &#8211; Shut down in 3 minutes and do not return</dl>
<h2>Author</h2>
<p>Silvino B. Magalhães &lt;sbm2yk [at] gmail.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

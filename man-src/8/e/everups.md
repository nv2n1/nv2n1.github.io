---
title: "everups(8)"
name: "everups"
section: "8"
letter: "e"
url: "/docs/linux/man/8-everups/"
description: "everups – Driver for Ever UPS models"
---

<p>everups &#8211; Driver for Ever UPS models</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the everups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver should recognize the NET *-DPC and AP *-PRO models.</p>
<h2>Extra Arguments</h2>
<p>This driver does not support any extra settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>Bugs</h2>
<p>This UPS can only switch off the load if it&#8217;s running on battery. This means you may be vulnerable to power races if your shutdown scripts don&#8217;t sleep and force a reboot.</p>
<h2>Author</h2>
<p>Bartek Szady &lt;bszx [at] bszxdomain.edu.eu.org&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

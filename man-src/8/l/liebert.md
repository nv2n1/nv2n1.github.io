---
title: "liebert(8)"
name: "liebert"
section: "8"
letter: "l"
url: "/docs/linux/man/8-liebert/"
description: "liebert – Driver for Liebert contact-closure UPS equipment"
---

<p>liebert &#8211; Driver for Liebert contact-closure UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the liebert driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports some Liebert UPS equipment with a contact-closure interface. This includes the UPStation GXT2 with their contact-closure cable. The smart mode (&quot;Multilink&quot;) cable is not supported by this driver.</p>
<h2>Extra Arguments</h2>
<p>This driver does not support any extra settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>Bugs</h2>
<p>This driver does not yet support shutdowns by raising DTR. Be aware that shutdowns are not possible with the stock contact-closure cable. You may have to build another cable with DTR connected through to the UPS for it to work. </p>
<p> There is no way for this driver to detect the hardware or cable. It will start up successfully even if no UPS is present. This is a fundamental limitation of any contact-closure driver.</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

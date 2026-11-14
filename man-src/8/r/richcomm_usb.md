---
title: "richcomm_usb(8)"
name: "richcomm_usb"
section: "8"
letter: "r"
url: "/docs/linux/man/8-richcomm_usb/"
description: "richcomm_usb – Driver UPS equipment using Richcomm dry-contact to USB solution"
---

<p>richcomm_usb &#8211; Driver UPS equipment using Richcomm dry-contact to USB solution</p>
<h2>Note</h2>
<p>This man page only documents the specific features of the richcomm_usb driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The Richcomm dry-contact to USB solution is a generic interface that is used to upgrade an existing (RS-232) contact closure UPS interface to USB. As such, all the limitations of the underlying contact closure interface apply. This means that you will only get the essentials in ups.status: OL, OB, and LB. See also <code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8).</p>
<h2>Bugs</h2>
<p>Most contact-closure UPSes will not power down the load if the line power is present. This can create a race when using slave <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) systems. See the <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) man page for more information. </p>
<p> The solution to both of these problems is to upgrade to a smart protocol UPS of some kind that allows detection and proper load cycling on command.</p>
<h2>Authors</h2>
<p>Peter van Valderen &lt;p.v.valderen at probu.nl&gt;, Dirk Teurlings &lt;dirk at upexia.nl&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>The generic serial driver:</h3>
<p><code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

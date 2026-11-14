---
title: "belkin(8)"
name: "belkin"
section: "8"
letter: "b"
url: "/docs/linux/man/8-belkin/"
description: "belkin – Driver for Belkin serial UPS equipment"
---

<p>belkin &#8211; Driver for Belkin serial UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the belkin driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The <code>belkin</code> driver is known to support the Regulator Pro 525 (F6C525-SER). Other similar models such as the 425 and 625 should also work. </p>
<p> The Trust UPS and older Belkin units are not supported.</p>
<h2>Extra Arguments</h2>
<p>This driver does not support any extra settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>Bugs</h2>
<p>There are dragons lurking within the protocol to this UPS. I have one that essentially behaves like a glorified power strip due to some invasive probing on my part. Don&#8217;t mess with it directly.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 the driver doesn&#8217;t go anywhere near these character sequences, so it won&#8217;t zap your UPS. I only mention this here as yet another reminder of the perils of closed hardware. </p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>

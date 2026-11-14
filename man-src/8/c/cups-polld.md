---
title: "cups-polld(8)"
name: "cups-polld"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups-polld/"
description: "cups-polld – cups printer polling daemon"
---

<p>cups-polld &#8211; cups printer polling daemon</p>
<h2>Synopsis</h2>
<p><code>cups-polld</code> <i>address ipp-port interval browse-port</i></p>
<h2>Description</h2>
<p><i>cups-polld</i> polls remote servers for a list of available printers and printer classes every <i>interval</i> seconds. Printer and class information is then broadcast to the localhost interface (127.0.0.1) on the specified browse port for reception by <i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>. </p>
<p> This program is started automatically by <i>cupsd</i> for every <i>BrowsePoll</i> directive found in the <i><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i> file.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>Copyright</h2>
<p>Copyright 2007-2011 by Apple Inc.</p>

---
title: "regulatory(5)"
name: "regulatory"
section: "5"
letter: "r"
url: "/docs/linux/man/5-regulatory/"
description: "regulatory.bin – The Linux wireless regulatory database"
---

<p>regulatory.bin &#8211; The Linux wireless regulatory database </p>
<h2>Description</h2>
</h3>
<p><code>regulatory.bin</code> is the file used by the Linux wireless subsystem to keep its regulatory database information. It is read by <code>crda</code> upon the Linux kernel&#8217;s request for regulatory information for a specific ISO / IEC 3166 alpha2 country code. The regulatory database is kept in a small binary format for size and code efficiency. The <code>regulatory.bin</code> file can be parsed and read in human format by using the <code>regdbdump</code> command. The <code>regulatory.bin</code> file should be updated upon regulatory changes or corrections. </p>
<h2>Upkeeping</h2>
<p>The regulatory database is maintained by the community as such you are encouraged to send any corrections or updates to the linux-wireless mailing list: <code>linux-wireless [at] vger.kernel.org</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-regdbdump/">regdbdump</a></code>(8) <code><a href="/docs/linux/man/8-crda/">crda</a></code>(8) <code><a href="/docs/linux/man/8-iw/">iw</a></code>(8) <code><a rel="nofollow" href="http://wireless.kernel.org/en/developers/Regulatory/">http://wireless.kernel.org/en/developers/Regulatory/</a></code> </p>

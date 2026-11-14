---
title: "regulatory-db(5)"
name: "regulatory-db"
section: "5"
letter: "r"
url: "/docs/linux/man/5-regulatory-db/"
description: "regulatory.bin, regulatory.db – The Linux wireless regulatory database"
---

<p>regulatory.bin, regulatory.db &#8211; The Linux wireless regulatory database </p>
<h2>Description</h2>
</h3>
<p><code>regulatory.bin</code> and <code>regulatory.db</code> are the files used by the Linux wireless subsystem to keep its regulatory database information. <code>regulatory.bin</code> is read by <code>crda</code> upon the Linux kernel&#8217;s request for regulatory information for a specific ISO / IEC 3166 alpha2 country code. <code>regulatory.db</code> is a newer, extensible database format which (since Linux 4.15) is read by the kernel directly as a firmware file. The regulatory database is kept in a small binary format for size and code efficiency. The <code>regulatory.bin</code> file can be parsed and read in human format by using the <code>regdbdump</code> command. The regulatory database files should be updated upon regulatory changes or corrections. </p>
<h2>Upkeeping</h2>
<p>The regulatory database is maintained by the community as such you are encouraged to send any corrections or updates to the linux-wireless and wireless-regdb mailing lists: <code>linux-wireless [at] vger.kernel.org</code> and <code>wireless-regdb [at] lists.infradead.org</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-regdbdump/">regdbdump</a></code>(8) <code><a href="/docs/linux/man/8-crda/">crda</a></code>(8) <code><a href="/docs/linux/man/8-iw/">iw</a></code>(8) <code><a rel="nofollow" href="http://wireless.kernel.org/en/developers/Regulatory/">http://wireless.kernel.org/en/developers/Regulatory/</a></code> </p>

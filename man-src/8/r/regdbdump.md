---
title: "regdbdump(8)"
name: "regdbdump"
section: "8"
letter: "r"
url: "/docs/linux/man/8-regdbdump/"
description: "regdbdump – parse and print out regulatory rules file"
---

<p>regdbdump &#8211; parse and print out regulatory rules file</p>
<h2>Synopsis</h2>
<p><code>regdbdump</code> &lt;path-to-regulatory.bin&gt; </p>
<h2>Description</h2>
</h3>
<p><code>regdbdump</code> can be used to parse the <code>regulatory.bin</code> file, the Linux wireless regulatory database used by <code>crda,</code> and print out its contents in human readable format. <code>regdbdump</code> will return non zero if the digital signature <code>regdbdump</code> was built with cannot verify the signature of the regulatory database. Should this happen unintentionally chances are your regulatory.bin file is corrupted or has been tampered with. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-regulatory-bin/">regulatory.bin</a></code>(5) <code><a href="/docs/linux/man/8-crda/">crda</a></code>(8) <code><a href="/docs/linux/man/8-iw/">iw</a></code>(8) <code><a rel="nofollow" href="http://wireless.kernel.org/en/developers/Regulatory/">http://wireless.kernel.org/en/developers/Regulatory/</a></code> </p>

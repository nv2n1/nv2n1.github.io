---
title: "btcflash(8)"
name: "btcflash"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btcflash/"
description: "BTCFLASH – firmware flash utility for BTC DRW1008 DVD+/-RW recorder."
---

<p>BTCFLASH &#8211; firmware flash utility for BTC DRW1008 DVD+/-RW recorder.</p>
<h2>Synopsis</h2>
<p><code>btcflash</code> DEVICE FILE </p>
<h2>Description</h2>
<p><code>BTCFLASH</code> may also work with other BTC DVD recorders, such as the DRW1004 and DRW1108, but they have not been tested. USE AT YOUR OWN RISK! Firmware files may be obtained by running BTC&#8217;s Windows flash utility, then searching in the WINDOWSTEMP or WINNTTEMP directory for a *.HEX file. It will probably be in a subdirectory named PAC*.tmp.DIR, and the HEX file will be named Vnnnn.HEX, where nnnn is the firmware version number. You&#8217;ll also find IDEFLASH.EXE or BTCFLASH.EXE in the same directory. </p>
<h2>Options</h2>
<dl>
<dt><code>DEVICE</code></p>
<dd>Write the firmware to the given device.</p>
<dt><code>FILE</code></p>
<dd>Read the firmware from the given file. This utility will also accept firmware files in &quot;.BIN&quot; format. </p>
</dl>
<h2>Author</h2>
<p>BTCFLASH was written by David Huang &lt;khym [at] azeotrope.org&gt;. </p>
<p> This manual page was written by Daniel Baumann &lt;daniel [at] debian.org&gt;, for the Debian project (but may be used by others).</p>

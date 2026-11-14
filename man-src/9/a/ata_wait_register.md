---
title: "ata_wait_register(9)"
name: "ata_wait_register"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_wait_register/"
description: "ata_wait_register – wait until register value changes"
---

<p>ata_wait_register &#8211; wait until register value changes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 ata_wait_register(struct ata_port&nbsp;<wbr>*&nbsp;<wbr></code><i>ap</i><code>, void&nbsp;<wbr>__iomem&nbsp;<wbr>*&nbsp;<wbr></code><i>reg</i><code>, u32&nbsp;<wbr></code><i>mask</i><code>, u32&nbsp;<wbr></code><i>val</i><code>, unsigned long&nbsp;<wbr></code><i>interval</i><code>, unsigned long&nbsp;<wbr></code><i>timeout</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>ATA port to wait register for, can be NULL</dl>
<p> <i>reg</i></p>
<dl>
<dd>IO-mapped register</dl>
<p> <i>mask</i></p>
<dl>
<dd>Mask to apply to read register value</dl>
<p> <i>val</i></p>
<dl>
<dd>Wait condition</dl>
<p> <i>interval</i></p>
<dl>
<dd>polling interval in milliseconds</dl>
<p> <i>timeout</i></p>
<dl>
<dd>timeout in milliseconds</dl>
<h2>Description</h2>
<p>Waiting for some bits of register to change is a common operation for ATA controllers. This function reads 32bit LE IO-mapped register <i>reg</i> and tests for the following condition. </p>
<p> (*<i>reg</i> &amp; mask) != val </p>
<p> If the condition is met, it returns; otherwise, the process is repeated after <i>interval_msec</i> until timeout. </p>
<p> LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>The final register value.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

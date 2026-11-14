---
title: "linux-boot-prober(1)"
name: "linux-boot-prober"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linux-boot-prober/"
description: "linux-boot-prober — Determine boot characteristics of a specified device."
---

<h2>NAME</h2>
<p> linux-boot-prober &#8212; Determine boot characteristics of a specified device.</p>
<h2>SYNOPSIS</h2>
<p> <code>linux-boot-prober</code> <i>&lt;partition&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>linux-boot-prober</code> utility will try to work out how to boot the linux root partition specified by <i>&lt;partition&gt;</i>. If successful, it will outoput one or more lines of the form: </p>
<p> &lt;root partition&gt;:&lt;boot partition&gt;:&lt;label&gt;:&lt;kernel path&gt;:&lt;initrd path&gt;:&lt;kernel parameters&gt; </p>
<p> For example, for a system with a kernel at <i>/boot/vmlinuz</i> and an initramfs at <i>/boot/initrd.gz</i>, and with <i>/</i> on <i>/dev/sda2</i> and <i>/boot</i> on <i>/dev/sda1</i>, the command &quot;linux-boot-prober /dev/sda1&quot; will display: </p>
<p> /dev/sda2:/dev/sda1:Linux:/vmlinuz:/initrd.gz:root=/dev/sda1 </p>
<p> Some partitions will not be displayed by <code>linux-boot-prober</code><i>. If a partition is mounted on /</i>, <i>/target</i>, or <i>/target/boot</i>, it will be skipped.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-os-prober/">os-prober</a></code>(1) </p>
<h2>Index</h2>

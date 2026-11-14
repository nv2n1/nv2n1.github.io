---
title: "os-prober(1)"
name: "os-prober"
section: "1"
letter: "o"
url: "/docs/linux/man/1-os-prober/"
description: "os-prober — Discover bootable partitions on the local system."
---

<h2>NAME</h2>
<p> os-prober &#8212; Discover bootable partitions on the local system.</p>
<h2>SYNOPSIS</h2>
<p> <code>os-prober</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>os-prober</code> utility will scan all disks available on the system for other operating systems. For each discovered OS, it will output a line of the form: </p>
<p> &lt;partition&gt;:&lt;descriptive name&gt;:&lt;short name&gt;:&lt;kind of loader&gt; </p>
<p> For example, on system with Windows XP installed on <i>/dev/sda1</i>, <code>os-prober</code> will display: </p>
<p> /dev/sda1:Windows NT/2000/XP:WinNT:chain </p>
<p> Note that for Linux systems that are discovered, a call to <code>linux-boot-prober</code><i> may be required in order to fully discover the necessary information to boot the system. </i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-linux-boot-prober/">linux-boot-prober</a></code>(1) </p>
<h2>Index</h2>

---
title: "loadndisdriver-1(8)"
name: "loadndisdriver-1"
section: "8"
letter: "l"
url: "/docs/linux/man/8-loadndisdriver-1/"
description: "loadndisdriver – Userspace ndis driver loader for the ndiswrapper Linux kernel module"
---

<p>loadndisdriver &#8211; Userspace ndis driver loader for the ndiswrapper Linux kernel module</p>
<h2>Synopsis</h2>
<p><code>loadndisdriver</code></p>
<h2>Description</h2>
<p><code>loadndisdriver</code> is a support program for the ndiswrapper Linux kernel module. The ndiswrapper kernel module uses it to load ndis drivers that have been installed via the <code><a href="/docs/linux/man/8-ndiswrapper/">ndiswrapper</a></code>(8) tool. <code>loadndisdriver</code> should not be used directly, only the kernel module should use it. Therefore, it&#8217;s options are volatile, and subject to change during the development of the ndiswrapper kernel module. The <i>/etc/ndiswrapper</i> directory is expected to contain the ndis files that <code>loadndisdriver</code> requires. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ndiswrapper/">ndiswrapper</a></code>(8)</p>
<h2>Author</h2>
<p>This manual page was written by Kel Modderman &lt;kelrin [at] tpg.com.au&gt;, for the Debian project (but may be used by others).</p>

---
title: "kvm(1)"
name: "kvm"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kvm/"
description: "kvm – kvm-enabling wrapper for qemu-system-x86_64"
---

<h2 class="name">NAME</h2>
<p> kvm &#8211; kvm-enabling wrapper for qemu-system-x86_64 </p>
<h2>DESCRIPTION</h2>
<p> The <code>kvm</code> wrapper script is used to provide compatibility with old qemu-kvm package which has been merged into qemu as of version 1.3. </p>
<p> The script executes</p>
<dl>
<dt>
<dd> <code>qemu-system-x86_64 -enable-kvm</code></dl>
<p> passing all other command-line arguments to the qemu binary. This is not the same as old kvm binary, which was using less strict construct, similar to</p>
<dl>
<dt>
<dd> <code>qemu-system-x86_64 -machine accel=kvm:tcg</code></dl>
<p> New wrapper ensures that kvm mode is enabled, or the VM will not start, while old code falled back to emulation (tcg) mode if kvm isn&#8217;t available.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-qemu-system/">qemu-system</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Tokarev &lt;mjt [at] tls.msk.ru&gt;. </p>
<h2>Index</h2>

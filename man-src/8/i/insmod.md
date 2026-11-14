---
title: "insmod(8)"
name: "insmod"
section: "8"
letter: "i"
url: "/docs/linux/man/8-insmod/"
description: "insmod – Simple program to insert a module into the Linux Kernel"
---

<p>insmod &#8211; Simple program to insert a module into the Linux Kernel</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>insmod</code> [<i>filename</i>] [<i>module options</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>insmod</code></p>
<dd>is a trivial program to insert a module into the kernel. Most users will want to use <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) instead, which is more clever and can handle module dependencies. </p>
<p> Only the most general of error messages are reported: as the work of trying to link the module is now done inside the kernel, the <code>dmesg</code> usually gives more information about errors.</p>
<h2>Copyright</h2>
<p>This manual page originally Copyright 2002, Rusty Russell, IBM Corporation. Maintained by Jon Masters and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/8-rmmod/">rmmod</a></code>(8), <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-modinfo/">modinfo</a></code>(8) <code><a href="/docs/linux/man/8-depmod/">depmod</a></code>(8)</p>
<h2>Authors</h2>
<p><code>Jon Masters</code> &lt;jcm [at] jonmasters.org&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>

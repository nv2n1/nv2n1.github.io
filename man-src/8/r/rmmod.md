---
title: "rmmod(8)"
name: "rmmod"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rmmod/"
description: "rmmod – Simple program to remove a module from the Linux Kernel"
---

<p>rmmod &#8211; Simple program to remove a module from the Linux Kernel</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rmmod</code> [<code>-f</code>] [<code>-s</code>] [<code>-v</code>] [<i>modulename</i>]</dl>
<h2>Description</h2>
<p><code>rmmod</code></p>
<dd>is a trivial program to remove a module (when module unloading support is provided) from the kernel. Most users will want to use <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) with the <code>-r</code> option instead.</p>
<h2>Options</h2>
<p><code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Print messages about what the program is doing. Usually <code>rmmod</code> prints messages only if something goes wrong.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>This option can be extremely dangerous: it has no effect unless CONFIG_MODULE_FORCE_UNLOAD was set when the kernel was compiled. With this option, you can remove modules which are being used, or which are not designed to be removed, or have been marked as unsafe (see <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8)).</dl>
<p> <code>-s</code>, <code>&#8211;syslog</code></p>
<dl>
<dd>Send errors to syslog instead of standard error.</dl>
<p> <code>-V</code> <code>&#8211;version</code></p>
<dl>
<dd>Show version of program and exit.</dl>
<h2>Copyright</h2>
<p>This manual page originally Copyright 2002, Rusty Russell, IBM Corporation. Maintained by Jon Masters and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/8-insmod/">insmod</a></code>(8), <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-modinfo/">modinfo</a></code>(8) <code><a href="/docs/linux/man/8-depmod/">depmod</a></code>(8)</p>
<h2>Authors</h2>
<p><code>Jon Masters</code> &lt;jcm [at] jonmasters.org&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>

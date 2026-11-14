---
title: "kmod(8)"
name: "kmod"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kmod/"
description: "kmod – Program to manage Linux Kernel modules"
---

<p>kmod &#8211; Program to manage Linux Kernel modules</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kmod</code> [<code>OPTIONS</code>&#8230;] [<i>COMMAND</i>] [<code>COMMAND_OPTIONS</code>&#8230;]</dl>
<h2>Description</h2>
<p><code>kmod</code></p>
<dd>is a multi-call binary which implements the programs used to control Linux Kernel modules. Most users will only run it using its other names.</p>
<h2>Options</h2>
<p><code>-V</code> <code>&#8211;version</code></p>
<dl>
<dd>Show the program version and exit.</dl>
<p> <code>-h</code> <code>&#8211;help</code></p>
<dl>
<dd>Show the help message.</dl>
<h2>Commands</h2>
<p><code>help</code></p>
<dl>
<dd>Show the help message.</dl>
<p> <code>list</code></p>
<dl>
<dd>List the currently loaded modules.</dl>
<p> <code>static-nodes</code></p>
<dl>
<dd>Output the static device nodes information provided by the modules of the currently running kernel version.</dl>
<h2>Copyright</h2>
<p>This manual page originally Copyright 2014, Marco d&#8217;Itri. Maintained by Lucas De Marchi and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-rmmod/">rmmod</a></code>(8), <code><a href="/docs/linux/man/8-insmod/">insmod</a></code>(8), <code><a href="/docs/linux/man/8-modinfo/">modinfo</a></code>(8), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/8-depmod/">depmod</a></code>(8)</p>
<h2>Author</h2>
<p><code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>

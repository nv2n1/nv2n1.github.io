---
title: "installkernel(8)"
name: "installkernel"
section: "8"
letter: "i"
url: "/docs/linux/man/8-installkernel/"
description: "installkernel – install a new kernel image"
---

<p>installkernel &#8211; install a new kernel image</p>
<h2>Synopsis</h2>
<p><code>installkernel </code><i>version zImage System.map [directory]</i></p>
<h2>Description</h2>
<p><code>installkernel</code> installs a new kernel image onto the system from the Linux source tree. It is called by the Linux kernel makefiles when <code>make install</code> is invoked there. </p>
<p> The new kernel is installed into <i>{directory}/vmlinuz-{version}</i>. If a symbolic link <i>{directory}/vmlinuz</i> already exists, it is refreshed by making a link from <i>{directory}/vmlinuz</i> to the new kernel, and the previously installed kernel is available as <i>{directory}/vmlinuz.old</i>.</p>
<h2>Bugs</h2>
<p><code>installkernel</code> resides in /sbin only because the Linux kernel makefiles call it from there. It should really be in /usr/sbin. It isn&#8217;t needed to boot a system. </p>

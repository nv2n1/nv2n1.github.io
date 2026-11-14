---
title: "qemu-make-debian-root(8)"
name: "qemu-make-debian-root"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qemu-make-debian-root/"
description: "qemu-make-debian-root – Create a debian root image for qemu"
---

<p>qemu-make-debian-root &#8211; Create a debian root image for qemu</p>
<h2>Synopsis</h2>
<p><code>qemu-make-debian-root</code> [<i>-k</i>] [<i>-s</i>] <i>size-in-MiB distrib deburl image</i> [<i>files-to-copy-in-/root</i>]</p>
<h2>Description</h2>
<p><code>qemu-make-debian-root</code> is a command to ease the creation of a debian root image for qemu. The generated image is not bootable by itself, and an external kernel is needed. It can be run with a command like:</p>
<dl>
<dd>
<pre><code>qemu disk.img -kernel /boot/vmlinuz</code></pre>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-k</code></p>
<dd>Keep file system.</p>
<dt><code>-s</code></p>
<dd>Create a sparse image.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-qemu/">qemu</a></code>(1), <code><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></code>(1).</p>
<h2>Author</h2>
<p>This manual page was written by Guillem Jover &lt;guillem [at] debian.org&gt;.</p>

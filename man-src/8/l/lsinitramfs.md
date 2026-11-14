---
title: "lsinitramfs(8)"
name: "lsinitramfs"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lsinitramfs/"
description: "lsinitramfs – list content of an initramfs image"
---

<p>lsinitramfs &#8211; list content of an initramfs image</p>
<h2>Synopsis</h2>
<p><code>lsinitramfs</code> [<code>-l</code>] <i>initramfs-file</i>&#8230;<br />
 <code>lsinitramfs</code> <code>-h</code> </p>
<h2>Description</h2>
<p>The <code>lsinitramfs</code> command lists the content of given initramfs images. It allows one to quickly check the content of one (or multiple) specified initramfs files. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display usage information and exit. </p>
<dt><code>-l</code></p>
<dd>Display long and more verbose listing of initramfs content. </p>
</dl>
<h2>Usage Examples</h2>
<p>List initramfs content of current running kernel: </p>
<p> <code>lsinitramfs /boot/initrd.img-$(uname -r)</code> </p>
<p> List content of two initramfs files in verbose mode: </p>
<p> <code>lsinitramfs -l /boot/vmlinuz-2.6.31-grml64 /boot/vmlinuz-2.6.33-grml64</code></p>
<h2>Bugs</h2>
<p><code>lsinitramfs</code> cannot deal with multiple-segmented initramfs images, except where an early (uncompressed) initramfs with system firmware is prepended to the regular compressed initramfs. </p>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt; and numerous others.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-initramfs-tools/">initramfs-tools</a></i>(7), <i><a href="/docs/linux/man/8-mkinitramfs/">mkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-unmkinitramfs/">unmkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-update-initramfs/">update-initramfs</a></i>(8). </p>

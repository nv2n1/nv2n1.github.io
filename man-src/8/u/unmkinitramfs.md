---
title: "unmkinitramfs(8)"
name: "unmkinitramfs"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unmkinitramfs/"
description: "unmkinitramfs – extract content from an initramfs image"
---

<p>unmkinitramfs &#8211; extract content from an initramfs image</p>
<h2>Synopsis</h2>
<p><code>unmkinitramfs</code> [<code>-v</code>] <i>initramfs-file</i> <i>directory</i><br />
 <code>unmkinitramfs</code> <code>-h</code> </p>
<h2>Description</h2>
<p>The <code>unmkinitramfs</code> command extracts the content of a given initramfs image using <code>cpio</code>. If the image contains multiple segments, each are passed to <code>cpio</code> in order. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display usage information and exit. </p>
<dt><code>-v</code></p>
<dd>Display verbose messages about extraction. </p>
</dl>
<h2>Usage Examples</h2>
<p>Extract initramfs content of current running kernel: </p>
<p> <code>unmkinitramfs /boot/initrd.img-$(uname -r) initramfs/</code></p>
<h2>Bugs</h2>
<p><code>unmkinitramfs</code> cannot deal with multiple-segmented initramfs images, except where an early (uncompressed) initramfs with system firmware is prepended to the regular compressed initramfs. </p>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt; and numerous others.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-initramfs-tools/">initramfs-tools</a></i>(7), <i><a href="/docs/linux/man/8-lsinitramfs/">lsinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-mkinitramfs/">mkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-update-initramfs/">update-initramfs</a></i>(8). </p>

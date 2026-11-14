---
title: "luksformat(8)"
name: "luksformat"
section: "8"
letter: "l"
url: "/docs/linux/man/8-luksformat/"
description: "luksformat – Create and format an encrypted LUKS device"
---

<p>luksformat &#8211; Create and format an encrypted LUKS device</p>
<h2>Synopsis</h2>
<p><code>luksformat</code> [<code>-t</code> <i>fstype</i>] <i>device</i> [ mkfs options ]</p>
<h2>Description</h2>
<p><code>luksformat</code> is a wrapper around <code>cryptsetup</code> and <code>mkfs</code> which provides an easy interface for creating an encrypted device that follows the <font SIZE="-1">LUKS</font> standard and for putting a file system onto the encrypted device. </p>
<p> The default file system is <code>vfat</code> since that is most commonly used on removable devices. However, you can specify any available file system with the <code>-t</code> option.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></i>(8), <i><a href="/docs/linux/man/8-mkfs/">mkfs</a></i>(8)</p>
<h2>Author</h2>
<p>This program was written by Martin Pitt &lt;martin.pitt [at] ubuntu.com&gt;.</p>

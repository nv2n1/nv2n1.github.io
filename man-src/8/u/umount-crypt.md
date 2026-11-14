---
title: "umount-crypt(8)"
name: "umount-crypt"
section: "8"
letter: "u"
url: "/docs/linux/man/8-umount-crypt/"
description: "umount.crypt – unmount a dm-crypt encrypted volume"
---

<p>umount.crypt &#8211; unmount a dm-crypt encrypted volume</p>
<h2>Syntax</h2>
<p><code>umount.crypt</code> [<code>-n</code>] <i>directory</i></p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>This option is ignored (originally is &quot;force unmount for NFS&quot;).</p>
<dt><code>-n</code></p>
<dd>Do not update /etc/mtab.</p>
<dt><code>-r</code></p>
<dd>Try mounting read-only if unmounting fails. This option is currently not implemented and is ignored.</dl>
<h2>Description</h2>
<p>umount.crypt will unmount <i>directory</i> and disassociates the underlying crypto device, and loop device if such was used. </p>

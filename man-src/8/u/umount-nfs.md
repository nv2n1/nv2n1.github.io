---
title: "umount-nfs(8)"
name: "umount-nfs"
section: "8"
letter: "u"
url: "/docs/linux/man/8-umount-nfs/"
description: "umount.nfs, umount.nfs4 – unmount a Network File System"
---

<p>umount.nfs, umount.nfs4 &#8211; unmount a Network File System</p>
<h2>Synopsis</h2>
<p><code>umount.nfs</code><i> dir</i><code> [-fvnrlh ]</code></p>
<h2>Description</h2>
<p><code>umount.nfs</code> and <code>umount.nfs4</code> are a part of <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) utilities package, which provides NFS client functionality. <code>umount.nfs4</code> and <code>umount.nfs</code> are meant to be used by the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command for unmounting NFS shares. This subcommand, however, can also be used as a standalone command with limited functionality. <i>dir </i> is the directory on which the file system is mounted. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Force unmount the file system in case of unreachable NFS system.</p>
<dt><code>-v</code></p>
<dd>Be verbose.</p>
<dt><code>-n</code></p>
<dd>Do not update <i>/etc/mtab. </i> By default, an entry is created in <i>/etc/mtab </i> for every mounted file system. Use this option to skip deleting an entry.</p>
<dt><code>-r</code></p>
<dd>In case unmounting fails, try to mount read-only.</p>
<dt><code>-l</code></p>
<dd>Lazy unmount. Detach the file system from the file system hierarchy now, and cleanup all references to the file system as soon as it is not busy anymore.</p>
<dt><code>-h</code></p>
<dd>Print help message. </p>
</dl>
<h2>Note</h2>
<p>For further information please refer <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) and <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) manual pages.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/fstab</i></p>
<dd>file system table</p>
<dt><i>/etc/mtab</i></p>
<dd>table of mounted file systems </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), </p>
<h2>Author</h2>
<p>Amit Gud &lt;agud [at] redhat.com&gt;</p>

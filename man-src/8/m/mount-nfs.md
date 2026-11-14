---
title: "mount-nfs(8)"
name: "mount-nfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-nfs/"
description: "mount.nfs, mount.nfs4 – mount a Network File System"
---

<p>mount.nfs, mount.nfs4 &#8211; mount a Network File System</p>
<h2>Synopsis</h2>
<p><code>mount.nfs</code><i> remotetarget dir</i><code> [-rvVwfnsh ] [-o </code><i>options</i><code>]</code></p>
<h2>Description</h2>
<p><code>mount.nfs</code> is a part of <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) utilities package, which provides NFS client functionality. <code>mount.nfs</code> is meant to be used by the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command for mounting NFS shares. This subcommand, however, can also be used as a standalone command with limited functionality. <i>remotetarget </i> is a server share usually in the form of <code>servername:/path/to/share.</code> <i>dir </i> is the directory on which the file system is to be mounted. Under Linux 2.6.32 and later kernel versions, <code>mount.nfs</code> can mount all NFS file system versions. Under earlier Linux kernel versions, <code>mount.nfs4</code> must be used for mounting NFSv4 file systems while <code>mount.nfs</code> must be used for NFSv3 and v2. </p>
<h2>Options</h2>
<dl>
<dt><code>-r</code></p>
<dd>Mount file system readonly.</p>
<dt><code>-v</code></p>
<dd>Be verbose.</p>
<dt><code>-V</code></p>
<dd>Print version.</p>
<dt><code>-w</code></p>
<dd>Mount file system read-write.</p>
<dt><code>-f</code></p>
<dd>Fake mount. Don&#8217;t actually call the mount system call.</p>
<dt><code>-n</code></p>
<dd>Do not update <i>/etc/mtab. </i> By default, an entry is created in <i>/etc/mtab </i> for every mounted file system. Use this option to skip making an entry.</p>
<dt><code>-s</code></p>
<dd>Tolerate sloppy mount options rather than fail.</p>
<dt><code>-h</code></p>
<dd>Print help message.</p>
<dt><code>nfsoptions</code></p>
<dd>Refer to <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) or <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manual pages. </p>
</dl>
<h2>Note</h2>
<p>For further information please refer <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) and <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manual pages.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/fstab</i></p>
<dd>file system table</p>
<dt><i>/etc/mtab</i></p>
<dd>table of mounted file systems</p>
<dt><i>/etc/nfsmount.conf</i></p>
<dd>Configuration file for NFS mounts</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-nfsmount-conf/">nfsmount.conf</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), </p>
<h2>Author</h2>
<p>Amit Gud &lt;agud [at] redhat.com&gt;</p>

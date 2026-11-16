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
<dt><code>-r</code></dt>
<dd>Mount file system readonly.</dd>
<dt><code>-v</code></dt>
<dd>Be verbose.</dd>
<dt><code>-V</code></dt>
<dd>Print version.</dd>
<dt><code>-w</code></dt>
<dd>Mount file system read-write.</dd>
<dt><code>-f</code></dt>
<dd>Fake mount. Don&#8217;t actually call the mount system call.</dd>
<dt><code>-n</code></dt>
<dd>Do not update <i>/etc/mtab. </i> By default, an entry is created in <i>/etc/mtab </i> for every mounted file system. Use this option to skip making an entry.</dd>
<dt><code>-s</code></dt>
<dd>Tolerate sloppy mount options rather than fail.</dd>
<dt><code>-h</code></dt>
<dd>Print help message.</dd>
<dt><code>nfsoptions</code></dt>
<dd>Refer to <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) or <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manual pages. </dd>
</dl>
<h2>Note</h2>
<p>For further information please refer <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5) and <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) manual pages.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/fstab</i></dt>
<dd>file system table</dd>
<dt><i>/etc/mtab</i></dt>
<dd>table of mounted file systems</dd>
<dt><i>/etc/nfsmount.conf</i></dt>
<dd>Configuration file for NFS mounts</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/5-nfsmount-conf/">nfsmount.conf</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), </p>
<h2>Author</h2>
<p>Amit Gud &lt;agud [at] redhat.com&gt;</p>

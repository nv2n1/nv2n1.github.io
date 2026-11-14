---
title: "umount2(2)"
name: "umount2"
section: "2"
letter: "u"
url: "/docs/linux/man/2-umount2/"
description: "umount, umount2 – unmount filesystem"
---

<h2 class="name">NAME</h2>
<p> umount, umount2 &#8211; unmount filesystem </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/mount.h&gt;
int umount(const char *target);
int umount2(const char *target, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>umount</code>() and <code>umount2</code>() remove the attachment of the (topmost) filesystem mounted on <i>target</i>. </p>
<p> Appropriate privilege (Linux: the <code>CAP_SYS_ADMIN</code> capability) is required to unmount filesystems. </p>
<p> Linux 2.1.116 added the <code>umount2</code>() system call, which, like <code>umount</code>(), unmounts a target, but allows additional <i>flags</i> controlling the behavior of the operation:</p>
<dl>
<dt><code>MNT_FORCE</code> (since Linux 2.1.116)</p>
<dd> Ask the filesystem to abort pending requests before attempting the unmount. This may allow the unmount to complete without waiting for an inaccessible server, but could cause data loss. If, after aborting requests, some processes still have active references to the filesystem, the unmount will still fail. As at Linux 4.12, <code>MNT_FORCE</code> is supported only on the following filesystems: 9p (since Linux 2.6.16), ceph (since Linux 2.6.34), cifs (since Linux 2.6.12), fuse (since Linux 2.6.16), lustre (since Linux 3.11), and NFS (since Linux 2.1.116).</p>
<dt><code>MNT_DETACH</code> (since Linux 2.4.11)</p>
<dd> Perform a lazy unmount: make the mount point unavailable for new accesses, immediately disconnect the filesystem and all filesystems mounted below it from each other and from the mount table, and actually perform the unmount when the mount point ceases to be busy.</p>
<dt><code>MNT_EXPIRE</code> (since Linux 2.6.8)</p>
<dd> Mark the mount point as expired. If a mount point is not currently in use, then an initial call to <code>umount2</code>() with this flag fails with the error <code>EAGAIN</code>, but marks the mount point as expired. The mount point remains expired as long as it isn&#8217;t accessed by any process. A second <code>umount2</code>() call specifying <code>MNT_EXPIRE</code> unmounts an expired mount point. This flag cannot be specified with either <code>MNT_FORCE</code> or <code>MNT_DETACH</code>.</p>
<dt><code>UMOUNT_NOFOLLOW</code> (since Linux 2.6.34)</p>
<dd> Don&#8217;t dereference <i>target</i> if it is a symbolic link. This flag allows security problems to be avoided in set-user-ID-<i>root</i> programs that allow unprivileged users to unmount filesystems.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> The error values given below result from filesystem type independent errors. Each filesystem type may have its own special errors and its own special behavior. See the Linux kernel source code for details.</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd> A call to <code>umount2</code>() specifying <code>MNT_EXPIRE</code> successfully marked an unbusy filesystem as expired.</p>
<dt><code>EBUSY</code></p>
<dd> <i>target</i> could not be unmounted because it is busy.</p>
<dt><code>EFAULT</code></p>
<dd> <i>target</i> points outside the user address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>target</i> is not a mount point.</p>
<dt><code>EINVAL</code></p>
<dd> <code>umount2</code>() was called with <code>MNT_EXPIRE</code> and either <code>MNT_DETACH</code> or <code>MNT_FORCE</code>.</p>
<dt><code>EINVAL</code> (since Linux 2.6.34)</p>
<dd> <code>umount2</code>() was called with an invalid flag value in <i>flags</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> A pathname was longer than <code>MAXPATHLEN</code>.</p>
<dt><code>ENOENT</code></p>
<dd> A pathname was empty or had a nonexistent component.</p>
<dt><code>ENOMEM</code></p>
<dd> The kernel could not allocate a free page to copy filenames or data into.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have the required privileges.</dl>
<h2>VERSIONS</h2>
<p> <code>MNT_DETACH</code> and <code>MNT_EXPIRE</code> are available in glibc since version 2.11.</p>
<h2>CONFORMING TO</h2>
<p> These functions are Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<h3>umount() and shared mount points</h3>
<p> Shared mount points cause any mount activity on a mount point, including <code>umount</code>() operations, to be forwarded to every shared mount point in the peer group and every slave mount of that peer group. This means that <code>umount</code>() of any peer in a set of shared mounts will cause all of its peers to be unmounted and all of their slaves to be unmounted as well. </p>
<p> This propagation of unmount activity can be particularly surprising on systems where every mount point is shared by default. On such systems, recursively bind mounting the root directory of the filesystem onto a subdirectory and then later unmounting that subdirectory with <code>MNT_DETACH</code> will cause every mount in the mount namespace to be lazily unmounted. </p>
<p> To ensure <code>umount</code>() does not propagate in this fashion, the mount point may be remounted using a <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) call with a <i>mount_flags</i> argument that includes both <code>MS_REC</code> and <code>MS_PRIVATE</code> prior to <code>umount</code>() being called.</p>
<h3>Historical details</h3>
<p> The original <code>umount</code>() function was called as <i>umount(device)</i> and would return <code>ENOTBLK</code> when called with something other than a block device. In Linux 0.98p4, a call <i>umount(dir)</i> was added, in order to support anonymous devices. In Linux 2.3.99-pre7, the call <i>umount(device)</i> was removed, leaving only <i>umount(dir)</i> (since now devices can be mounted in more than one place, so specifying the device does not suffice).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>

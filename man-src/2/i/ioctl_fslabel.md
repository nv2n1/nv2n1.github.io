---
title: "ioctl_fslabel(2)"
name: "ioctl_fslabel"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_fslabel/"
description: "ioctl_fslabel – get or set a filesystem label"
---

<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ioctl.h&gt;</code><br />
 <code>#include &lt;linux/fs.h&gt;</code> </p>
<p> <code>int ioctl(int </code><i>fd</i><code>, FS_IOC_GETFSLABEL, char </code><i>label</i><code>[FSLABEL_MAX]);</code><br />
 <code>int ioctl(int </code><i>fd</i><code>, FS_IOC_SETFSLABEL, char </code><i>label</i><code>[FSLABEL_MAX]);</code></p>
<h2>DESCRIPTION</h2>
<p> If a filesystem supports online label manipulation, these <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations can be used to get or set the filesystem label for the filesystem on which <code>fd</code> resides. The <code>FS_IOC_SETFSLABEL</code> operation requires privilege (<code>CAP_SYS_ADMIN</code>).</p>
<h2>RETURN VALUE</h2>
<p> On success zero is returned. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> Error can include (but are not limited to) the following:</p>
<dl>
<dt><code>EFAULT</code></dt>
<dd> <i>label</i> references an inaccessible memory area.</dd>
<dt><code>EINVAL</code></dt>
<dd> The specified label exceeds the maximum label length for the filesystem.</dd>
<dt><code>ENOTTY</code></dt>
<dd> This can appear if the filesystem does not support online label manipulation.</dd>
<dt><code>EPERM</code></dt>
<dd> The calling process does not have sufficient permissions to set the label.</dd></dl>
<h2>VERSIONS</h2>
<p> These <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations first appeared in Linux 4.18. They were previously known as <code>BTRFS_IOC_GET_FSLABEL</code> and <code>BTRFS_IOC_SET_FSLABEL</code> and were private to Btrfs.</p>
<h2>CONFORMING TO</h2>
<p> This API is Linux-specific.</p>
<h2>NOTES</h2>
<p> The maximum string length for this interface is <code>FSLABEL_MAX</code>, including the terminating null byte (&#8216;\0&#8217;). Filesystems have differing maximum label lengths, which may or may not include the terminating null. The string provided to <code>FS_IOC_SETFSLABEL</code> must always be null-terminated, and the string returned by <code>FS_IOC_GETFSLABEL</code> will always be null-terminated.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>

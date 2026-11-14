---
title: "ioctl_fslabel(2)"
name: "ioctl_fslabel"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_fslabel/"
description: "ioctl_fslabel – get or set a filesystem label"
---

<h2 class="name">NAME</h2>
<p> ioctl_fslabel &#8211; get or set a filesystem label </p>
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
<dt><code>EFAULT</code></p>
<dd> <i>label</i> references an inaccessible memory area.</p>
<dt><code>EINVAL</code></p>
<dd> The specified label exceeds the maximum label length for the filesystem.</p>
<dt><code>ENOTTY</code></p>
<dd> This can appear if the filesystem does not support online label manipulation.</p>
<dt><code>EPERM</code></p>
<dd> The calling process does not have sufficient permissions to set the label.</dl>
<h2>VERSIONS</h2>
<p> These <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations first appeared in Linux 4.18. They were previously known as <code>BTRFS_IOC_GET_FSLABEL</code> and <code>BTRFS_IOC_SET_FSLABEL</code> and were private to Btrfs.</p>
<h2>CONFORMING TO</h2>
<p> This API is Linux-specific.</p>
<h2>NOTES</h2>
<p> The maximum string length for this interface is <code>FSLABEL_MAX</code>, including the terminating null byte (&#8216;

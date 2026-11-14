---
title: "linux-update-symlinks(1)"
name: "linux-update-symlinks"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linux-update-symlinks/"
description: "linux-update-symlinks – maintain symlinks to default kernel and initramfs"
---

<h2 class="name">NAME</h2>
<p> linux-update-symlinks &#8211; maintain symlinks to default kernel and initramfs</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>linux-update-symlinks</code>&nbsp;{<code>install</code>|<code>upgrade</code>|<code>remove</code>} <i>VERSION IMAGE-PATH</i> </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>linux-update-symlinks</code> is intended to be called from the</p>
<dd>postinst and postrm maintainer scripts of Linux kernel packages. The postinst script must pass the first argument <code>install</code> or <code>upgrade</code> depending on whether a fresh installation or an upgrade has taken place. </p>
<p> The <i>VERSION</i> argument must be the kernel version string as shown by <code>uname -r</code> and used in filenames. </p>
<p> The <i>IMAGE-PATH</i> argument must be the absolute filename of the kernel image. </p>
<p> By default, this command maintains symlinks in the root directory. This behaviour can be modified by settings in <i>/etc/kernel-img.conf</i>:</p>
<dl>
<dt><code>image_dest</code></p>
<dd> Specifies the directory in which to maintain symlinks</p>
<dt><code>link_in_boot</code></p>
<dd> If set to a true value, specifies that the directory is <i>/boot</i></p>
<dt><code>no_symlinks</code></p>
<dd> If set to a false value, disables maintenance of symlinks</dl>
<p> The symlinks for the primary default kernel version are named <i>vmlinuz</i> or <i>vmlinux</i> (depending on whether the architecture normally uses compressed kernel images) and <i>initrd.img</i> (if it uses an initramfs). The symlinks for the secondary default have the same names with the suffix <i>.old</i>. </p>
<p> If symlink maintenance is disabled, <code>linux-update-symlinks</code> does nothing, successfully. Otherwise it makes a list of kernel versions in decreasing order of priority:</p>
<dl>
<dt>&bull;</p>
<dd> The given <i>VERSION</i>, if the first argument is <code>install</code></p>
<dt>&bull;</p>
<dd> The current primary default version, if it exists and is not already listed</p>
<dt>&bull;</p>
<dd> The current secondary default version, if it exists and is not already listed</p>
<dt>&bull;</p>
<dd> All other versions whose files are installed, excluding the specified <i>VERSION</i> if the first argument is <code>remove</code>, in decreasing version order</dl>
<p> The top two entries on the list are the new primary and secondary default versions, and it updates the symlinks accordingly. In case there is only one entry, this is both the primary and secondary default version. If there are no entries, there are no default versions and it removes the default symlinks. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>INITRD</i></p>
<dd> When the first argument is <code>install</code> or <code>upgrade</code>, <code>linux-update-symlinks</code> assumes that the given <i>VERSION</i> will use an initramfs unless this variable is set to <code>No</code>. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/boot/initrd.img-</i>*</p>
<dd> Installed initramfs images</p>
<dt><i>/boot/vmlinuz-</i>*&nbsp;|&nbsp;<i>/boot/vmlinux-</i>*</p>
<dd> Installed kernel images</p>
<dt><i>/etc/kernel-img.conf</i></p>
<dd> Configuration file specifying whether and where to create symlinks</p>
<dt><i>/initrd.img</i></p>
<dd> Symlink to the initramfs image for the primary default version</p>
<dt><i>/initrd.img.old</i></p>
<dd> Symlink to the initramfs image for the secondary default version</p>
<dt><i>/vmlinuz</i>&nbsp;|&nbsp;<i>/vmlinux</i></p>
<dd> Symlink to the kernel image for the primary default version</p>
<dt><i>/vmlinuz.old</i>&nbsp;|&nbsp;<i>/vmlinux.old</i></p>
<dd> Symlink to the kernel image for the secondary default version </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>linux-update-symlinks</code> and this manual page were written by Ben Hutchings as part of the Debian <code>linux-base</code> package. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-kernel-img-conf/">kernel-img.conf</a></i>(5), <i><a href="/docs/linux/man/1-linux-version/">linux-version</a></i>(1). </p>
<h2>Index</h2>

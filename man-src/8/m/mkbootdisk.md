---
title: "mkbootdisk(8)"
name: "mkbootdisk"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkbootdisk/"
description: "mkbootdisk – creates a stand-alone boot floppy for the running system"
---

<p>mkbootdisk &#8211; creates a stand-alone boot floppy for the running system</p>
<h2>Synopsis</h2>
<p><code>mkbootdisk</code> [<code>&#8211;version</code>] [<code>&#8211;noprompt</code>] [<code>&#8211;verbose</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;device&nbsp;<wbr></code><i>devicefile</i>]&nbsp;<wbr>[<code>&#8211;size&nbsp;<wbr></code><i>size</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;kernelargs&nbsp;<wbr></code><i>&lt;args&gt;</i>]&nbsp;<wbr>[<code>&#8211;iso</code>]&nbsp;<wbr><i>kernel</i> </p>
<h2>Description</h2>
<p><code>mkbootdisk</code> creates a boot floppy appropriate for the running system. The boot disk is entirely self-contained, and includes an initial ramdisk image which loads any necessary SCSI modules for the system. The created boot disk looks for the root filesystem on the device suggested by /etc/fstab. The only required argument is the kernel version to put onto the boot floppy. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;device </code><i>devicefile</i></p>
<dd>The boot image is created on <i>devicefile</i>. If <code>&#8211;device</code> is not specified, /dev/fd0 is used. If <i>devicefile</i> does not exist <code>mkinitrd</code> creates a 1.44Mb floppy image using <i>devicefile</i> as the filename. </p>
<dt><code>&#8211;noprompt</code></p>
<dd>Normally, <code>mkbootdisk</code> instructs the user to insert a floppy and waits for confirmation before continuing. If <code>&#8211;noprompt</code> is specified, no prompt is displayed. </p>
<dt><code>&#8211;verbose</code></p>
<dd>Instructs <code>mkbootdisk</code> to talk about what it&#8217;s doing as it&#8217;s doing it. Normally, there is no output from <code>mkbootdisk</code>. </p>
<dt><code>&#8211;iso</code></p>
<dd>Instructs <code>mkbootdisk</code> to make a bootable ISO image as <i>devicefile</i>. </p>
<dt><code>&#8211;version</code></p>
<dd>Displays the version of <code>mkbootdisk</code> and exits. </p>
<dt><code>&#8211;kernelargs </code><i>args</i></p>
<dd>Adds <i>args</i> to the arguments appended on the kernel command line. If this is not specified <code>mkbootdisk</code> uses <code>grubby</code> to parse the arguments for the default kernel from <code>grub.conf</code>, if possible. </p>
<dt><code>&#8211;size </code><i>size</i></p>
<dd>Uses <i>size</i> (in kilobytes) as the size of the image to use for the boot disk. If this is not specified, <code>mkbootdisk</code> will assume a standard 1.44Mb floppy device. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grubby/">grubby</a></code>(8) <code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>
<h2>Author</h2>
<pre>Erik Troan &lt;ewt [at] redhat.com&gt;</pre>

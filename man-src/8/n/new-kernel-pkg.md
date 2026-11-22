---
title: "new-kernel-pkg(8)"
name: "new-kernel-pkg"
section: "8"
letter: "n"
url: "/docs/linux/man/8-new-kernel-pkg/"
description: "new-kernel-pkg – tool to script kernel installation"
---

<p>new-kernel-pkg &#8211; tool to script kernel installation </p>
<h2>Synopsis</h2>
<p><code>new-kernel-pkg</code> [-v] [&#8211;mkinitrd] [&#8211;rminitrd] [&#8211;dracut]<br/>
&nbsp;<wbr>[&#8211;initrdfile=<i>initrd-image</i>&nbsp;<wbr>[&#8211;depmod]&nbsp;<wbr>[&#8211;rmmoddep]<br/>
&nbsp;<wbr>[&#8211;kernel-args=<i>args</i>]&nbsp;<wbr>[&#8211;remove-args=<i>args</i>]<br/>
&nbsp;<wbr>[&#8211;banner=<i>banner</i>]&nbsp;<wbr>[&#8211;multiboot=<i>multiboot</i>]<br/>
&nbsp;<wbr>[&#8211;mbargs=<i>mbargs</i>]&nbsp;<wbr>[&#8211;make-default]&nbsp;<wbr>[&#8211;add-dracut-args]<br/>
&nbsp;<wbr>[&#8211;add-plymouth-initrd]&nbsp;<wbr>[&#8211;host-only]<br/>
&nbsp;<wbr>&lt;&#8211;install | &#8211;remove | &#8211;update | &#8211;rpmposttrans&gt;&nbsp;<wbr>&lt;kernel-version&gt; </p>
<h2>Description</h2>
<p><code>new-kernel-pkg</code> is a tool used in packaging to automate the installation of a new kernel, including the creation of an initial ram filesystem image, updating of bootloader configuration, and other associated tasks. </p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></dt>
<dd>Be verbose. </dd>
<dt><code>&#8211;mkinitrd</code></dt>
<dd>Create a new initial ram filesystem image. </dd>
<dt><code>&#8211;rminitrd</code></dt>
<dd>Remove an initial ram filesystem image. </dd>
<dt><code>&#8211;dracut</code></dt>
<dd>When creating a new initial ram filesystem image, use <a href="/docs/linux/man/8-dracut/">dracut</a>(8) rather than <a href="/docs/linux/man/8-mkinitrd/">mkinitrd</a>(8). Used in conjunction with &#8211;mkinitrd . </dd>
<dt><code>&#8211;initrdfile</code>=<i>initrd-image</i></dt>
<dd>Use the specified file as the initial ram filesystem image. </dd>
<dt><code>&#8211;depmod</code></dt>
<dd>Create modules.dep and related files. </dd>
<dt><code>&#8211;rmmoddep</code></dt>
<dd>Remove modules.dep and related files. </dd>
<dt><code>&#8211;kernel-args</code>=<i>args</i></dt>
<dd>Use <i>args</i> as the boot command line for this kernel. </dd>
<dt><code>&#8211;remove-args</code>=<i>args</i></dt>
<dd>Remove specified kernel arguments for this kernel. </dd>
<dt><code>&#8211;banner</code>=<i>banner</i></dt>
<dd>Display <i>banner</i> as the banner text in the bootloader. </dd>
<dt><code>&#8211;multiboot</code>=<i>multiboot-image</i></dt>
<dd>Use <i>multiboot-image</i> as a multiboot image. </dd>
<dt><code>&#8211;mbargs</code>=<i>mbargs</i></dt>
<dd>Use <i>mbargs</i> as arguments to the multiboot image. </dd>
<dt><code>&#8211;make-default</code></dt>
<dd>Make this kernel the default boot option. </dd>
<dt><code>&#8211;add-dracut-args</code></dt>
<dd>Automatically generate dracut options and add them to the kernel command line. </dd>
<dt><code>&#8211;add-plymouth-initrd</code></dt>
<dd>Automatically add plymouth to the initial ram filesystem image. </dd>
<dt><code>&#8211;host-only</code></dt>
<dd>Make an initial ram filesystem image that is specific to the running system. </dd>
<dt><code>&#8211;install</code> <i>kernel-version</i></dt>
<dd>Install a new kernel. </dd>
<dt><code>&#8211;remove</code> <i>kernel-version</i></dt>
<dd>Remove an installed kernel. </dd>
<dt><code>&#8211;update</code> <i>kernel-version</i></dt>
<dd>Update the specified kernel. </dd>
<dt><code>&#8211;rpmposttrans</code> <i>kernel-version</i></dt>
<dd>Run the rpmposttrans for the specified kernel. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grubby/">grubby</a>(8)</code> <code><a href="/docs/linux/man/8-installkernel/">installkernel</a>(8)</code> </p>
<h2>Authors</h2>
<pre>Erik Troan
Jeremy Katz
Peter Jones</pre>

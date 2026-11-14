---
title: "mkinitrd(8)"
name: "mkinitrd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkinitrd/"
description: "mkinitrd – is a compat wrapper, which calls dracut to generate an initramfs"
---

<p>mkinitrd &#8211; is a compat wrapper, which calls dracut to generate an initramfs</p>
<h2>Synopsis</h2>
<p><code>mkinitrd</code> [<i>OPTION&#8230;</i>] [&lt;initrd-image&gt;] &lt;kernel-version&gt;</p>
<h2>Description</h2>
<p>mkinitrd creates an initramfs image &lt;initrd-image&gt; for the kernel with version &lt;kernel-version&gt; by calling &quot;dracut&quot;.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 If a more fine grained control over the resulting image is needed, &quot;dracut&quot; should be called directly. </p>
<h2>Options</h2>
<p><code>&#8211;version</code></p>
<dl>
<dd>print info about the version</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>increase verbosity level</dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dd>overwrite existing initramfs file.</dl>
<p> <code>*&#8211;image-version</code></p>
<dl>
<dd>append the kernel version to the target image &lt;initrd-image&gt;-&lt;kernel-version&gt;.</dl>
<p> <code>&#8211;with=&lt;module&gt;</code></p>
<dl>
<dd>add the kernel module &lt;module&gt; to the initramfs.</dl>
<p> <code>&#8211;preload=&lt;module&gt;</code></p>
<dl>
<dd>preload the kernel module &lt;module&gt; in the initramfs before any other kernel modules are loaded. This can be used to ensure a certain device naming, which should in theory be avoided and the use of symbolic links in /dev is encouraged.</dl>
<p> <code>&#8211;nocompress</code></p>
<dl>
<dd>do not compress the resulting image.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>print a help message and exit.</dl>
<h2>Availability</h2>
<p>The mkinitrd command is part of the dracut package and is available from m[blue]<code><a rel="nofollow" href="https://dracut.wiki.kernel.org">https://dracut.wiki.kernel.org</a></code>m[]</p>
<h2>Authors</h2>
<p>Harald Hoyer</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>

---
title: "dracut-catimages(8)"
name: "dracut-catimages"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dracut-catimages/"
description: "dracut-catimages – creates initial ramdisk image by concatenating images"
---

<p>dracut-catimages &#8211; creates initial ramdisk image by concatenating images</p>
<h2>Synopsis</h2>
<p><code>dracut-catimages</code> [<i>OPTION</i>&#8230;] <i>&lt;initramfs base image&gt;</i> [<i>&lt;image&gt;</i>&#8230;]</p>
<h2>Description</h2>
<p>dracut-catimages creates an initial ramdisk image by concatenating several images from the command line and /boot/dracut/*.img</p>
<h2>Options</h2>
<p><code>-f, &#8211;force</code></p>
<dl>
<dd>overwrite existing initramfs file.</dl>
<p> <code>-i, &#8211;imagedir</code></p>
<dl>
<dd>Directory with additional images to add (default: /boot/dracut/)</dl>
<p> <code>-o, &#8211;overlaydir</code></p>
<dl>
<dd>Overlay directory, which contains additional files that will be used to create an additional image</dl>
<p> <code>&#8211;nooverlay</code></p>
<dl>
<dd>Do not use the overlay directory</dl>
<p> <code>&#8211;noimagedir</code></p>
<dl>
<dd>Do not use the additional image directory</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dd>display help text and exit.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dd>output debug information of the build process</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>verbose output during the build process</dl>
<h2>Files</h2>
<p><i>/boot/dracut/*.img</i></p>
<dl>
<dd>images to work with</dl>
<h2>Authors</h2>
<p>Harald Hoyer</p>
<h2>Availability</h2>
<p>The dracut-catimages command is part of the dracut package and is available from m[blue]<code><a rel="nofollow" href="https://dracut.wiki.kernel.org">https://dracut.wiki.kernel.org</a></code>m[]</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>

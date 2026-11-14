---
title: "grub2-bios-setup(8)"
name: "grub2-bios-setup"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub2-bios-setup/"
description: "grub-bios-setup — Set up images to boot from a device."
---

<p><code>grub-bios-setup</code> &#8212; Set up images to boot from a device. </p>
<h2>Synopsis</h2>
<p><code>grub-bios-setup</code> [-a | &#8211;allow-floppy] [-b | &#8211;boot-image=<i>FILE</i>]</p>
<dl>
<dd>[-c | &#8211;core-image=<i>FILE</i>] [-d | &#8211;directory=<i>DIR</i>]</dl>
<dl>
<dd>[-f | &#8211;force] [-m | &#8211;device-map=<i>FILE</i>]</dl>
<dl>
<dd>[-s | &#8211;skip-fs-probe] [-v | &#8211;verbose] <i>DEVICE</i> </p>
<h2>Description</h2>
<p>You should not normally run this program directly. Use grub-install instead. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;allow-floppy</code></p>
<dd>Make the device also bootable as a floppy. This option is the default for /dev/fdX devices. Some BIOSes will not boot images created with this option. </p>
<dt><code>&#8211;boot-image</code>=<i>FILE</i></p>
<dd>Use FILE as the boot image. The default value is <code>boot.img</code>. </p>
<dt><code>&#8211;core-image</code>=<i>FILE</i></p>
<dd>Use FILE as ther core image. The default value is <code>core.img</code>. </p>
<dt><code>&#8211;directory</code>=<i>DIR</i></p>
<dd>Use GRUB files in the directory DIR. The default value is <code>/boot/grub</code>. </p>
<dt><code>&#8211;force</code></p>
<dd>Install even if problems are detected. </p>
<dt><code>&#8211;device-map</code>=<i>FILE</i></p>
<dd>Use FILE as the device map. The default value is /boot/grub/device.map . </p>
<dt><code>&#8211;skip-fs-probe</code></p>
<dd>Do not probe DEVICE for filesystems. </p>
<dt><code>&#8211;verbose</code></p>
<dd>Print verbose messages. </p>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> </p>

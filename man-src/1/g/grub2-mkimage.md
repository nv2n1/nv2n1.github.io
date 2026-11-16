---
title: "grub2-mkimage(1)"
name: "grub2-mkimage"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-mkimage/"
description: "grub-mkimage — Make a bootable GRUB image."
---

<h2>NAME</h2>
<p> <code>grub-mkimage</code> &#8212; Make a bootable GRUB image. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkimage</code> [-c | &#8211;config=FILE<i>] [-C | &#8211;compression=(xz</i>,<i>none</i>,<i>auto</i>)]</p>
<dl>
<dt>
</dt><dd> [-d | &#8211;directory=DIR] [-k | &#8211;pubkey=<i>FILE</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-m | &#8211;memdisk=<i>FILE</i>] [-n | &#8211;note] [-o | &#8211;output=<i>FILE</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-O | &#8211;format=<i>FORMAT</i>] [-p | &#8211;prefix=<i>DIR</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-v | &#8211;verbose] <i>MODULES</i> </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-mkimage</code> builds a bootable image of GRUB. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;config=<i>FILE</i></dt>
<dd> Embed <i>FILE</i> as the image&#8217;s initial configuration file. </dd>
<dt>&#8211;compression=(<i>xz</i>,<i>none</i>,<i>auto</i>)</dt>
<dd> Use one of <i>xz</i>, <i>none</i>, or <i>auto</i> as the compression method for the core image. </dd>
<dt>&#8211;directory=<i>DIR</i></dt>
<dd> Use images and modules from <i>DIR</i>. The default value is <code>/usr/lib/grub/&lt;platform&gt;</code>. </dd>
<dt>&#8211;pubkey=<i>FILE</i></dt>
<dd> Embed the public key <i>FILE</i> for signature checking. </dd>
<dt>&#8211;memdisk=<i>FILE</i></dt>
<dd> Embed the memdisk image <i>FILE</i>. If no <code>-p</code> option is also specified, this implies <i>-p (memdisk)/boot/grub</i>. </dd>
<dt>&#8211;note</dt>
<dd> Add a CHRP <i>NOTE</i> section. This option is only valid on IEEE1275 platforms. </dd>
<dt>&#8211;output=<i>FILE</i></dt>
<dd> Write the generated file to <i>FILE</i>. The default is to write to standard output. </dd>
<dt>&#8211;format=<i>FORMAT</i></dt>
<dd> Generate an image in the specified <i>FORMAT</i>. Valid values are:</dd>
<dl>
<dl>
<dt>
</dt><dd>
<p> i386-coreboot, i386-multiboot, i386-pc, i386-pc-pxe, i386-efi, i386-ieee1275, i386-qemu, x86_64-efi, mipsel-yeeloong-flash, mipsel-fuloong2f-flash, mipself-loongson-elf, powerpc-ieee1275, sparc64-ieee1275-raw, sparc64-ieee1275-cdcore, sparc64-ieee1275-aout, ia64-efi, mips-arc, mipsel-arc, mipsel-qemu_mips-elf, mips-qemu_mips-flash, mipsel-qemu_mips-flash, mips-qemu_mips-elf</dd></dl>
</dl>
<dt>&#8211;prefix=<i>DIR</i></dt>
<dd> Set prefix directory. The default value is <i>/boot/grub</i>. </dd>
<dt>&#8211;verbose</dt>
<dd> Print verbose messages. </dd>
<dt><i>MODULES</i></dt>
<dd> Include <i>MODULES</i>. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>

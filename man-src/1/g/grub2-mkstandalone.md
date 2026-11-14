---
title: "grub2-mkstandalone(1)"
name: "grub2-mkstandalone"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-mkstandalone/"
description: "grub-mkstandalone — Generate a standalone image in the selected format."
---

<h2>NAME</h2>
<p> <code>grub-mkstandalone</code> &#8212; Generate a standalone image in the selected format. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkstandalone</code> [-o | &#8211;output=<i>FILE</i>] [-O | &#8211;format=<i>FORMAT</i>]</p>
<dl>
<dt>
<dd> [-C | &#8211;compression=(<i>xz</i>|<i>none</i>|<i>auto</i>)]</dl>
<dl>
<dt>
<dd> [&#8211;modules=<i>MODULES</i>] [&#8211;install-modules=<i>MODULES</i>]</dl>
<dl>
<dt>
<dd> [&#8211;themes=<i>THEMES</i>] [&#8211;fonts=<i>FONTS</i>]</dl>
<dl>
<dt>
<dd> [&#8211;locales=<i>LOCALES</i>] [&#8211;compress[=<i>no</i>,<i>xz</i>,<i>gz</i>,<i>lzo</i>]]</dl>
<dl>
<dt>
<dd> [-d | &#8211;directory=<i>DIR</i>] [&#8211;grub-mkimage=<i>FILE</i>]</dl>
<dl>
<dt>
<dd> <i>SOURCE&#8230;</i> </p>
</dl>
<h2>DESCRIPTION</h2>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;output=<i>FILE</i></p>
<dd> Write the generated file to <i>FILE</i>. The default is to write to standard output. </p>
<dt>&#8211;format=<i>FORMAT</i></p>
<dd> Generate an image in the specified <i>FORMAT</i>. Valid values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> i386-coreboot, i386-multiboot, i386-pc, i386-pc-pxe, i386-efi, i386-ieee1275, i386-qemu, x86_64-efi, mipsel-yeeloong-flash, mipsel-fuloong2f-flash, mipself-loongson-elf, powerpc-ieee1275, sparc64-ieee1275-raw, sparc64-ieee1275-cdcore, sparc64-ieee1275-aout, ia64-efi, mips-arc, mipsel-arc, mipsel-qemu_mips-elf, mips-qemu_mips-flash, mipsel-qemu_mips-flash, mips-qemu_mips-elf</dl>
</dl>
<dt>&#8211;compression=(<i>xz</i>|<i>none</i>|<i>auto</i>)</p>
<dd> Use one of <i>xz</i>, <i>none</i>, or <i>auto</i> as the compression method for the core image. </p>
<dt>&#8211;modules=<i>MODULES</i></p>
<dd> Pre-load modules specified by <i>MODULES</i>. </p>
<dt>&#8211;install-modules=<i>MODULES</i></p>
<dd> Install only <i>MODULES</i> and their dependencies. The default is to install all available modules. </p>
<dt>&#8211;themes=<i>THEMES</i></p>
<dd> Install <i>THEMES</i>. The default is to install the <i>starfield</i> theme, if available. </p>
<dt>&#8211;fonts=<i>FONTS</i></p>
<dd> Install <i>FONTS</i>. The default is to install the <i>unicode</i> font. </p>
<dt>&#8211;locales=<i>LOCALES</i></p>
<dd> Install only locales listed in <i>LOCALES</i>. The default is to install all available locales. </p>
<dt>&#8211;compress[=<i>no</i>,<i>xz</i>,<i>gz</i>,<i>lzo</i>]</p>
<dd> Compress GRUB files using the specified compression algorithm. </p>
<dt>&#8211;directory=<i>DIR</i></p>
<dd> Use images and modules in <i>DIR</i>. </p>
<dt>&#8211;grub-mkimage=<i>FILE</i></p>
<dd> Use <i>FILE</i> as <code>grub-mkimage</code>. The default is <i>/usr/bin/grub-mkimage</i>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>

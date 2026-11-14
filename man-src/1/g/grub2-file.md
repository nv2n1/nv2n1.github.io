---
title: "grub2-file(1)"
name: "grub2-file"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-file/"
description: "grub-file — Check if FILE is of specified type."
---

<h2>NAME</h2>
<p> <code>grub-file</code> &#8212; Check if FILE is of specified type. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-file</code> (&#8211;is-i386-xen-pae-domu | &#8211;is-x86_64-xen-domu |</p>
<dl>
<dt>
<dd> &#8211;is-x86-xen-dom0 | &#8211;is-x86-multiboot |</dl>
<dl>
<dt>
<dd> &#8211;is-x86-multiboot2 | &#8211;is-arm-linux | &#8211;is-arm64-linux |</dl>
<dl>
<dt>
<dd> &#8211;is-ia64-linux | &#8211;is-mips-linux | &#8211;is-mipsel-linux |</dl>
<dl>
<dt>
<dd> &#8211;is-sparc64-linux | &#8211;is-powerpc-linux | &#8211;is-x86-linux |</dl>
<dl>
<dt>
<dd> &#8211;is-x86-linux32 | &#8211;is-x86-kfreebsd | &#8211;is-i386-kfreebsd |</dl>
<dl>
<dt>
<dd> &#8211;is-x86_64-kfreebsd | &#8211;is-x86-knetbsd |</dl>
<dl>
<dt>
<dd> &#8211;is-i386-knetbsd | &#8211;is-x86_64-knetbsd | &#8211;is-i386-efi |</dl>
<dl>
<dt>
<dd> &#8211;is-x86_64-efi | &#8211;is-ia64-efi | &#8211;is-arm64-efi |</dl>
<dl>
<dt>
<dd> &#8211;is-arm-efi | &#8211;is-hibernated-hiberfil | &#8211;is-x86_64-xnu |</dl>
<dl>
<dt>
<dd> &#8211;is-i386-xnu | &#8211;is-xnu-hibr | &#8211;is-x86-bios-bootsector)</dl>
<dl>
<dt>
<dd> <i>FILE</i> </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-file</code> is used to check if <i>FILE</i> is of a specified type. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;is-i386-xen-pae-domu</p>
<dd> Check if FILE can be booted as i386 PAE Xen unprivileged guest kernel </p>
<dt>&#8211;is-x86_64-xen-domu</p>
<dd> Check if FILE can be booted as x86_64 Xen unprivileged guest kernel </p>
<dt>&#8211;is-x86-xen-dom0</p>
<dd> Check if FILE can be used as Xen x86 privileged guest kernel </p>
<dt>&#8211;is-x86-multiboot</p>
<dd> Check if FILE can be used as x86 multiboot kernel </p>
<dt>&#8211;is-x86-multiboot2</p>
<dd> Check if FILE can be used as x86 multiboot2 kernel </p>
<dt>&#8211;is-arm-linux</p>
<dd> Check if FILE is ARM Linux </p>
<dt>&#8211;is-arm64-linux</p>
<dd> Check if FILE is ARM64 Linux </p>
<dt>&#8211;is-ia64-linux</p>
<dd> Check if FILE is IA64 Linux </p>
<dt>&#8211;is-mips-linux</p>
<dd> Check if FILE is MIPS Linux </p>
<dt>&#8211;is-mipsel-linux</p>
<dd> Check if FILE is MIPSEL Linux </p>
<dt>&#8211;is-sparc64-linux</p>
<dd> Check if FILE is SPARC64 Linux </p>
<dt>&#8211;is-powerpc-linux</p>
<dd> Check if FILE is POWERPC Linux </p>
<dt>&#8211;is-x86-linux</p>
<dd> Check if FILE is x86 Linux </p>
<dt>&#8211;is-x86-linux32</p>
<dd> Check if FILE is x86 Linux supporting 32-bit protocol </p>
<dt>&#8211;is-x86-kfreebsd</p>
<dd> Check if FILE is x86 kFreeBSD </p>
<dt>&#8211;is-i386-kfreebsd</p>
<dd> Check if FILE is i386 kFreeBSD </p>
<dt>&#8211;is-x86_64-kfreebsd</p>
<dd> Check if FILE is x86_64 kFreeBSD </p>
<dt>&#8211;is-x86-knetbsd</p>
<dd> Check if FILE is x86 kNetBSD </p>
<dt>&#8211;is-i386-knetbsd</p>
<dd> Check if FILE is i386 kNetBSD </p>
<dt>&#8211;is-x86_64-knetbsd</p>
<dd> Check if FILE is x86_64 kNetBSD </p>
<dt>&#8211;is-i386-efi</p>
<dd> Check if FILE is i386 EFI file </p>
<dt>&#8211;is-x86_64-efi</p>
<dd> Check if FILE is x86_64 EFI file </p>
<dt>&#8211;is-ia64-efi</p>
<dd> Check if FILE is IA64 EFI file </p>
<dt>&#8211;is-arm64-efi</p>
<dd> Check if FILE is ARM64 EFI file </p>
<dt>&#8211;is-arm-efi</p>
<dd> Check if FILE is ARM EFI file </p>
<dt>&#8211;is-hibernated-hiberfil</p>
<dd> Check if FILE is hiberfil.sys in hibernated state </p>
<dt>&#8211;is-x86_64-xnu</p>
<dd> Check if FILE is x86_64 XNU (Mac OS X kernel) </p>
<dt>&#8211;is-i386-xnu</p>
<dd> Check if FILE is i386 XNU (Mac OS X kernel) </p>
<dt>&#8211;is-xnu-hibr</p>
<dd> Check if FILE is XNU (Mac OS X kernel) hibernated image </p>
<dt>&#8211;is-x86-bios-bootsector</p>
<dd> Check if FILE is BIOS bootsector </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>

---
title: "grub-file(1)"
name: "grub-file"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-file/"
description: "grub-file – check file type"
---

<h2 class="name">NAME</h2>
<p> grub-file &#8211; check file type </p>
<h2>SYNOPSIS</h2>
<p> <code>file</code> <i>,OPTIONS FILE/</i></p>
<h2>DESCRIPTION</h2>
<p> Check if FILE is of specified type.</p>
<dl>
<dt><code>&#8211;is-i386-xen-pae-domu</code></p>
<dd> Check if FILE can be booted as i386 PAE Xen unprivileged guest kernel</p>
<dt><code>&#8211;is-x86_64-xen-domu</code></p>
<dd> Check if FILE can be booted as x86_64 Xen unprivileged guest kernel</p>
<dt><code>&#8211;is-x86-xen-dom0</code></p>
<dd> Check if FILE can be used as Xen x86 privileged guest kernel</p>
<dt><code>&#8211;is-x86-multiboot</code></p>
<dd> Check if FILE can be used as x86 multiboot kernel</p>
<dt> <code>&#8211;is-x86-multiboot2</code> Check if FILE can be used as x86 multiboot2 kernel</p>
<dt><code>&#8211;is-arm-linux</code></p>
<dd>
<dd>Check if FILE is ARM Linux</p>
<dt><code>&#8211;is-arm64-linux</code></p>
<dd> Check if FILE is ARM64 Linux</p>
<dt><code>&#8211;is-ia64-linux</code></p>
<dd> Check if FILE is IA64 Linux</p>
<dt><code>&#8211;is-mips-linux</code></p>
<dd> Check if FILE is MIPS Linux</p>
<dt><code>&#8211;is-mipsel-linux</code></p>
<dd> Check if FILE is MIPSEL Linux</p>
<dt><code>&#8211;is-sparc64-linux</code></p>
<dd> Check if FILE is SPARC64 Linux</p>
<dt><code>&#8211;is-powerpc-linux</code></p>
<dd> Check if FILE is POWERPC Linux</p>
<dt><code>&#8211;is-x86-linux</code></p>
<dd> Check if FILE is x86 Linux</p>
<dt><code>&#8211;is-x86-linux32</code></p>
<dd> Check if FILE is x86 Linux supporting 32-bit protocol</p>
<dt><code>&#8211;is-x86-kfreebsd</code></p>
<dd> Check if FILE is x86 kFreeBSD</p>
<dt><code>&#8211;is-i386-kfreebsd</code></p>
<dd> Check if FILE is i386 kFreeBSD</p>
<dt><code>&#8211;is-x86_64-kfreebsd</code></p>
<dd> Check if FILE is x86_64 kFreeBSD</p>
<dt><code>&#8211;is-x86-knetbsd</code></p>
<dd> Check if FILE is x86 kNetBSD</p>
<dt><code>&#8211;is-i386-knetbsd</code></p>
<dd> Check if FILE is i386 kNetBSD</p>
<dt> <code>&#8211;is-x86_64-knetbsd</code> Check if FILE is x86_64 kNetBSD</p>
<dt><code>&#8211;is-i386-efi</code></p>
<dd>
<dd>Check if FILE is i386 EFI file</p>
<dt><code>&#8211;is-x86_64-efi</code></p>
<dd> Check if FILE is x86_64 EFI file</p>
<dt><code>&#8211;is-ia64-efi</code></p>
<dd> Check if FILE is IA64 EFI file</p>
<dt><code>&#8211;is-arm64-efi</code></p>
<dd> Check if FILE is ARM64 EFI file</p>
<dt><code>&#8211;is-arm-efi</code></p>
<dd> Check if FILE is ARM EFI file</p>
<dt><code>&#8211;is-riscv32-efi</code></p>
<dd> Check if FILE is RISC-V 32bit EFI file</p>
<dt><code>&#8211;is-riscv64-efi</code></p>
<dd> Check if FILE is RISC-V 64bit EFI file</p>
<dt><code>&#8211;is-hibernated-hiberfil</code></p>
<dd> Check if FILE is hiberfil.sys in hibernated state</p>
<dt><code>&#8211;is-x86_64-xnu</code></p>
<dd> Check if FILE is x86_64 XNU (Mac OS X kernel)</p>
<dt><code>&#8211;is-i386-xnu</code></p>
<dd> Check if FILE is i386 XNU (Mac OS X kernel)</p>
<dt><code>&#8211;is-xnu-hibr</code></p>
<dd> Check if FILE is XNU (Mac OS X kernel) hibernated image</p>
<dt><code>&#8211;is-x86-bios-bootsector</code></p>
<dd> Check if FILE is BIOS bootsector</dl>
<p> <code>-h</code>, <code>&#8211;help</code> Display this help and exit. <code>-u</code>, <code>&#8211;usage</code> Display the usage of this command and exit.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>grub-file</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-file</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-file</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>

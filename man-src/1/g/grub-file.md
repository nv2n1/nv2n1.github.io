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
<dt><code>&#8211;is-i386-xen-pae-domu</code></dt>
<dd> Check if FILE can be booted as i386 PAE Xen unprivileged guest kernel</dd>
<dt><code>&#8211;is-x86_64-xen-domu</code></dt>
<dd> Check if FILE can be booted as x86_64 Xen unprivileged guest kernel</dd>
<dt><code>&#8211;is-x86-xen-dom0</code></dt>
<dd> Check if FILE can be used as Xen x86 privileged guest kernel</dd>
<dt><code>&#8211;is-x86-multiboot</code></dt>
<dd> Check if FILE can be used as x86 multiboot kernel</dd>
<dt> <code>&#8211;is-x86-multiboot2</code> Check if FILE can be used as x86 multiboot2 kernel</dt>
<dt><code>&#8211;is-arm-linux</code></dt>
<dd>
</dd><dd>Check if FILE is ARM Linux</dd>
<dt><code>&#8211;is-arm64-linux</code></dt>
<dd> Check if FILE is ARM64 Linux</dd>
<dt><code>&#8211;is-ia64-linux</code></dt>
<dd> Check if FILE is IA64 Linux</dd>
<dt><code>&#8211;is-mips-linux</code></dt>
<dd> Check if FILE is MIPS Linux</dd>
<dt><code>&#8211;is-mipsel-linux</code></dt>
<dd> Check if FILE is MIPSEL Linux</dd>
<dt><code>&#8211;is-sparc64-linux</code></dt>
<dd> Check if FILE is SPARC64 Linux</dd>
<dt><code>&#8211;is-powerpc-linux</code></dt>
<dd> Check if FILE is POWERPC Linux</dd>
<dt><code>&#8211;is-x86-linux</code></dt>
<dd> Check if FILE is x86 Linux</dd>
<dt><code>&#8211;is-x86-linux32</code></dt>
<dd> Check if FILE is x86 Linux supporting 32-bit protocol</dd>
<dt><code>&#8211;is-x86-kfreebsd</code></dt>
<dd> Check if FILE is x86 kFreeBSD</dd>
<dt><code>&#8211;is-i386-kfreebsd</code></dt>
<dd> Check if FILE is i386 kFreeBSD</dd>
<dt><code>&#8211;is-x86_64-kfreebsd</code></dt>
<dd> Check if FILE is x86_64 kFreeBSD</dd>
<dt><code>&#8211;is-x86-knetbsd</code></dt>
<dd> Check if FILE is x86 kNetBSD</dd>
<dt><code>&#8211;is-i386-knetbsd</code></dt>
<dd> Check if FILE is i386 kNetBSD</dd>
<dt> <code>&#8211;is-x86_64-knetbsd</code> Check if FILE is x86_64 kNetBSD</dt>
<dt><code>&#8211;is-i386-efi</code></dt>
<dd>
</dd><dd>Check if FILE is i386 EFI file</dd>
<dt><code>&#8211;is-x86_64-efi</code></dt>
<dd> Check if FILE is x86_64 EFI file</dd>
<dt><code>&#8211;is-ia64-efi</code></dt>
<dd> Check if FILE is IA64 EFI file</dd>
<dt><code>&#8211;is-arm64-efi</code></dt>
<dd> Check if FILE is ARM64 EFI file</dd>
<dt><code>&#8211;is-arm-efi</code></dt>
<dd> Check if FILE is ARM EFI file</dd>
<dt><code>&#8211;is-riscv32-efi</code></dt>
<dd> Check if FILE is RISC-V 32bit EFI file</dd>
<dt><code>&#8211;is-riscv64-efi</code></dt>
<dd> Check if FILE is RISC-V 64bit EFI file</dd>
<dt><code>&#8211;is-hibernated-hiberfil</code></dt>
<dd> Check if FILE is hiberfil.sys in hibernated state</dd>
<dt><code>&#8211;is-x86_64-xnu</code></dt>
<dd> Check if FILE is x86_64 XNU (Mac OS X kernel)</dd>
<dt><code>&#8211;is-i386-xnu</code></dt>
<dd> Check if FILE is i386 XNU (Mac OS X kernel)</dd>
<dt><code>&#8211;is-xnu-hibr</code></dt>
<dd> Check if FILE is XNU (Mac OS X kernel) hibernated image</dd>
<dt><code>&#8211;is-x86-bios-bootsector</code></dt>
<dd> Check if FILE is BIOS bootsector</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code> Display this help and exit. <code>-u</code>, <code>&#8211;usage</code> Display the usage of this command and exit.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>grub-file</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-file</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-file</code></dd></dl>
<p> should give you access to the complete manual. </p>

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
<p> <code>grub-file</code> (&#8211;is-i386-xen-pae-domu | &#8211;is-x86_64-xen-domu |</p>
<dl>
<dt>
</dt><dd> &#8211;is-x86-xen-dom0 | &#8211;is-x86-multiboot |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-x86-multiboot2 | &#8211;is-arm-linux | &#8211;is-arm64-linux |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-ia64-linux | &#8211;is-mips-linux | &#8211;is-mipsel-linux |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-sparc64-linux | &#8211;is-powerpc-linux | &#8211;is-x86-linux |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-x86-linux32 | &#8211;is-x86-kfreebsd | &#8211;is-i386-kfreebsd |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-x86_64-kfreebsd | &#8211;is-x86-knetbsd |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-i386-knetbsd | &#8211;is-x86_64-knetbsd | &#8211;is-i386-efi |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-x86_64-efi | &#8211;is-ia64-efi | &#8211;is-arm64-efi |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-arm-efi | &#8211;is-hibernated-hiberfil | &#8211;is-x86_64-xnu |</dd></dl>
<dl>
<dt>
</dt><dd> &#8211;is-i386-xnu | &#8211;is-xnu-hibr | &#8211;is-x86-bios-bootsector)</dd></dl>
<dl>
<dt>
</dt><dd> <i>FILE</i> </dd>
</dl>
<p> <code>grub-file</code> is used to check if <i>FILE</i> is of a specified type. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;is-i386-xen-pae-domu</dt>
<dd> Check if FILE can be booted as i386 PAE Xen unprivileged guest kernel </dd>
<dt>&#8211;is-x86_64-xen-domu</dt>
<dd> Check if FILE can be booted as x86_64 Xen unprivileged guest kernel </dd>
<dt>&#8211;is-x86-xen-dom0</dt>
<dd> Check if FILE can be used as Xen x86 privileged guest kernel </dd>
<dt>&#8211;is-x86-multiboot</dt>
<dd> Check if FILE can be used as x86 multiboot kernel </dd>
<dt>&#8211;is-x86-multiboot2</dt>
<dd> Check if FILE can be used as x86 multiboot2 kernel </dd>
<dt>&#8211;is-arm-linux</dt>
<dd> Check if FILE is ARM Linux </dd>
<dt>&#8211;is-arm64-linux</dt>
<dd> Check if FILE is ARM64 Linux </dd>
<dt>&#8211;is-ia64-linux</dt>
<dd> Check if FILE is IA64 Linux </dd>
<dt>&#8211;is-mips-linux</dt>
<dd> Check if FILE is MIPS Linux </dd>
<dt>&#8211;is-mipsel-linux</dt>
<dd> Check if FILE is MIPSEL Linux </dd>
<dt>&#8211;is-sparc64-linux</dt>
<dd> Check if FILE is SPARC64 Linux </dd>
<dt>&#8211;is-powerpc-linux</dt>
<dd> Check if FILE is POWERPC Linux </dd>
<dt>&#8211;is-x86-linux</dt>
<dd> Check if FILE is x86 Linux </dd>
<dt>&#8211;is-x86-linux32</dt>
<dd> Check if FILE is x86 Linux supporting 32-bit protocol </dd>
<dt>&#8211;is-x86-kfreebsd</dt>
<dd> Check if FILE is x86 kFreeBSD </dd>
<dt>&#8211;is-i386-kfreebsd</dt>
<dd> Check if FILE is i386 kFreeBSD </dd>
<dt>&#8211;is-x86_64-kfreebsd</dt>
<dd> Check if FILE is x86_64 kFreeBSD </dd>
<dt>&#8211;is-x86-knetbsd</dt>
<dd> Check if FILE is x86 kNetBSD </dd>
<dt>&#8211;is-i386-knetbsd</dt>
<dd> Check if FILE is i386 kNetBSD </dd>
<dt>&#8211;is-x86_64-knetbsd</dt>
<dd> Check if FILE is x86_64 kNetBSD </dd>
<dt>&#8211;is-i386-efi</dt>
<dd> Check if FILE is i386 EFI file </dd>
<dt>&#8211;is-x86_64-efi</dt>
<dd> Check if FILE is x86_64 EFI file </dd>
<dt>&#8211;is-ia64-efi</dt>
<dd> Check if FILE is IA64 EFI file </dd>
<dt>&#8211;is-arm64-efi</dt>
<dd> Check if FILE is ARM64 EFI file </dd>
<dt>&#8211;is-arm-efi</dt>
<dd> Check if FILE is ARM EFI file </dd>
<dt>&#8211;is-hibernated-hiberfil</dt>
<dd> Check if FILE is hiberfil.sys in hibernated state </dd>
<dt>&#8211;is-x86_64-xnu</dt>
<dd> Check if FILE is x86_64 XNU (Mac OS X kernel) </dd>
<dt>&#8211;is-i386-xnu</dt>
<dd> Check if FILE is i386 XNU (Mac OS X kernel) </dd>
<dt>&#8211;is-xnu-hibr</dt>
<dd> Check if FILE is XNU (Mac OS X kernel) hibernated image </dd>
<dt>&#8211;is-x86-bios-bootsector</dt>
<dd> Check if FILE is BIOS bootsector </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>

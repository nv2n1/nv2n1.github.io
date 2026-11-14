---
title: "grub-install(8)"
name: "grub-install"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub-install/"
description: "grub-install – install GRUB to a device"
---

<p>grub-install &#8211; install GRUB to a device</p>
<h2>Synopsis</h2>
<p><code>grub-install</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>] [<i>,INSTALL_DEVICE/</i>]</p>
<h2>Description</h2>
<p>Install GRUB on your drive.</p>
<dl>
<dt><code>&#8211;compress</code>=<i>,no/</i>|xz|gz|lzo</p>
<dd>compress GRUB files [optional]</p>
<dt><code>&#8211;disable-shim-lock</code></p>
<dd>disable shim_lock verifier</p>
<dt><code>&#8211;dtb</code>=<i>,FILE/</i></p>
<dd>embed a specific DTB</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></p>
<dd>use images and modules under DIR [default=/usr/lib/grub/&lt;platform&gt;]</p>
<dt><code>&#8211;fonts</code>=<i>,FONTS/</i></p>
<dd>install FONTS [default=unicode]</p>
<dt><code>&#8211;install-modules</code>=<i>,MODULES/</i></p>
<dd>install only MODULES and their dependencies [default=all]</p>
<dt><code>-k</code>, <code>&#8211;pubkey</code>=<i>,FILE/</i></p>
<dd>embed FILE as public key for signature checking</p>
<dt><code>&#8211;locale-directory</code>=<i>,DIR/</i> use translations under DIR</p>
<dd>[default=/usr/share/locale]</p>
<dt><code>&#8211;locales</code>=<i>,LOCALES/</i></p>
<dd>install only LOCALES [default=all]</p>
<dt><code>&#8211;modules</code>=<i>,MODULES/</i></p>
<dd>pre-load specified modules MODULES</p>
<dt><code>&#8211;sbat</code>=<i>,FILE/</i></p>
<dd>SBAT metadata</p>
<dt><code>&#8211;themes</code>=<i>,THEMES/</i></p>
<dd>install THEMES [default=starfield]</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>print verbose messages.</p>
<dt><code>&#8211;allow-floppy</code></p>
<dd>make the drive also bootable as floppy (default for fdX devices). May break on some BIOSes.</p>
<dt><code>&#8211;boot-directory</code>=<i>,DIR/</i></p>
<dd>install GRUB images under the directory DIR/grub instead of the boot/grub directory</p>
<dt><code>&#8211;bootloader-id</code>=<i>,ID/</i></p>
<dd>the ID of bootloader. This option is only available on EFI and Macs.</p>
<dt><code>&#8211;core-compress</code>=<i>,xz/</i>|none|auto</p>
<dd>choose the compression to use for core image</p>
<dt><code>&#8211;disk-module</code>=<i>,MODULE/</i></p>
<dd>disk module to use (biosdisk or native). This option is only available on BIOS target.</p>
<dt><code>&#8211;efi-directory</code>=<i>,DIR/</i></p>
<dd>use DIR as the EFI System Partition root.</p>
<dt><code>&#8211;force</code></p>
<dd>install even if problems are detected</p>
<dt><code>&#8211;force-file-id</code></p>
<dd>use identifier file even if UUID is available</p>
<dt><code>&#8211;label-bgcolor</code>=<i>,COLOR/</i></p>
<dd>use COLOR for label background</p>
<dt><code>&#8211;label-color</code>=<i>,COLOR/</i></p>
<dd>use COLOR for label</p>
<dt><code>&#8211;label-font</code>=<i>,FILE/</i></p>
<dd>use FILE as font for label</p>
<dt> <code>&#8211;macppc-directory</code>=<i>,DIR/</i> use DIR for PPC MAC install.</p>
<dt><code>&#8211;no-bootsector</code></p>
<dd>
<dd>do not install bootsector</p>
<dt><code>&#8211;no-extra-removable</code></p>
<dd>Do not install bootloader code to the removable media path. This option is only available on EFI.</p>
<dt><code>&#8211;no-nvram</code></p>
<dd>don&#8217;t update the `boot-device&#8217;/`Boot*&#8217; NVRAM variables. This option is only available on EFI and IEEE1275 targets.</p>
<dt><code>&#8211;no-rs-codes</code></p>
<dd>Do not apply any reed-solomon codes when embedding core.img. This option is only available on x86 BIOS targets.</p>
<dt><code>&#8211;no-uefi-secure-boot</code></p>
<dd>do not install an image usable with UEFI Secure Boot, even if the system was currently started using it. This option is only available on EFI.</p>
<dt><code>&#8211;product-version</code>=<i>,STRING/</i></p>
<dd>use STRING as product version</p>
<dt><code>&#8211;recheck</code></p>
<dd>delete device map if it already exists</p>
<dt><code>&#8211;removable</code></p>
<dd>the installation device is removable. This option is only available on EFI.</p>
<dt><code>-s</code>, <code>&#8211;skip-fs-probe</code></p>
<dd>do not probe for filesystems in DEVICE</p>
<dt><code>&#8211;target</code>=<i>,TARGET/</i></p>
<dd>install GRUB for TARGET platform [default=i386-pc]; available targets: arm-coreboot, arm-efi, arm-uboot, arm64-efi, i386-coreboot, i386-efi, i386-ieee1275, i386-multiboot, i386-pc, i386-qemu, i386-xen, i386-xen_pvh, ia64-efi, mips-arc, mips-qemu_mips, mipsel-arc, mipsel-loongson, mipsel-qemu_mips, powerpc-ieee1275, riscv32-efi, riscv64-efi, sparc64-ieee1275, x86_64-efi, x86_64-xen</p>
<dt><code>&#8211;uefi-secure-boot</code></p>
<dd>install an image usable with UEFI Secure Boot. This option is only available on EFI and if the grub-efi-amd64-signed package is installed.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd>give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd>give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> INSTALL_DEVICE must be system device filename. grub-install copies GRUB images into boot/grub. On some platforms, it may also install GRUB into the boot sector.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub-mkconfig/">grub-mkconfig</a></code>(8), <code><a href="/docs/linux/man/1-grub-mkimage/">grub-mkimage</a></code>(1), <code><a href="/docs/linux/man/1-grub-mkrescue/">grub-mkrescue</a></code>(1) The full documentation for <code>grub-install</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-install</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub-install</code></dl>
<p> should give you access to the complete manual. </p>

---
title: "grub2-install(8)"
name: "grub2-install"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub2-install/"
description: "grub-install — Install GRUB on a device."
---

<p><code>grub-install</code> &#8212; Install GRUB on a device. </p>
<h2>Synopsis</h2>
<p><code>grub-install</code> [&#8211;modules=<i>MODULES</i>] [&#8211;install-modules=<i>MODULES</i>]</p>
<dl>
<dd>[&#8211;themes=<i>THEMES</i>] [&#8211;fonts=<i>FONTS</i>] [&#8211;locales=<i>LOCALES</i>]</dl>
<dl>
<dd>[&#8211;compress[=<i>no</i>,<i>xz</i>,<i>gz</i>,<i>lzo</i>]] [-d | &#8211;directory=<i>DIR</i>]</dl>
<dl>
<dd>[&#8211;grub-mkimage=<i>FILE</i>] [&#8211;boot-directory=<i>DIR</i>]</dl>
<dl>
<dd>[&#8211;target=<i>TARGET</i>] [&#8211;grub-setup=<i>FILE</i>]</dl>
<dl>
<dd>[&#8211;grub-mkrelpath=<i>FILE</i>] [&#8211;grub-probe=<i>FILE</i>]</dl>
<dl>
<dd>[&#8211;allow-floppy] [&#8211;recheck] [&#8211;force] [&#8211;force-file-id]</dl>
<dl>
<dd>[&#8211;disk-module=<i>MODULE</i>] [&#8211;no-nvram] [&#8211;removable]</dl>
<dl>
<dd>[&#8211;bootloader-id=<i>ID</i>] [&#8211;efi-directory=<i>DIR</i>] <i>INSTALL_DEVICE</i> </p>
<h2>Description</h2>
<p><code>grub-install</code> installs GRUB onto a device. This includes copying GRUB images into the target directory (generally <i>/boot/grub</i>), and on some platforms may also include installing GRUB onto a boot sector. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;modules</code>=<i>MODULES</i></p>
<dd>Pre-load modules specified by <i>MODULES</i>. </p>
<dt><code>&#8211;install-modules</code>=<i>MODULES</i></p>
<dd>Install only <i>MODULES</i> and their dependencies. The default is to install all available modules. </p>
<dt><code>&#8211;themes</code>=<i>THEMES</i></p>
<dd>Install <i>THEMES</i>. The default is to install the <i>starfield</i> theme, if available. </p>
<dt><code>&#8211;fonts</code>=<i>FONTS</i></p>
<dd>Install <i>FONTS</i>. The default is to install the <i>unicode</i> font. </p>
<dt><code>&#8211;locales</code>=<i>LOCALES</i></p>
<dd>Install only locales listed in <i>LOCALES</i>. The default is to install all available locales. </p>
<dt><code>&#8211;compress</code>=<i>no</i>,<i>xz</i>,<i>gz</i>,<i>lzo</i></p>
<dd>Compress GRUB files using the specified compression algorithm. </p>
<dt><code>&#8211;directory</code>=<i>DIR</i></p>
<dd>Use images and modules in <i>DIR</i>. </p>
<dt><code>&#8211;grub-mkimage</code>=<i>FILE</i></p>
<dd>Use <i>FILE</i> as <code>grub-mkimage</code>. The default is <i>/usr/bin/grub-mkimage</i>. </p>
<dt><code>&#8211;boot-directory</code>=<i>DIR</i></p>
<dd>Use <i>DIR</i> as the boot directory. The default is <i>/boot</i>. GRUB will put its files in a subdirectory of this directory named <i>grub</i>. </p>
<dt><code>&#8211;target</code>=<i>TARGET</i></p>
<dd>Install GRUB for <i>TARGET</i> platform. The default is the platform <code>grub-install</code> is running on. </p>
<dt><code>&#8211;grub-setup</code>=<i>FILE</i></p>
<dd>Use <i>FILE</i> as <code>grub-setup</code>. The default is <i>/usr/bin/grub-setup</i>. </p>
<dt><code>&#8211;grub-mkrelpath</code>=<i>FILE</i></p>
<dd>Use <i>FILE</i> as <code>grub-mkrelpath</code>. The default is <i>/usr/bin/grub-mkrelpath</i>. </p>
<dt><code>&#8211;grub-probe</code>=<i>FILE</i></p>
<dd>Use <i>FILE</i> as <code>grub-probe</code>. The default is <i>/usr/bin/grub-mkrelpath</i>. </p>
<dt><code>&#8211;allow-floppy</p>
<dd>Make the device also bootable as a floppy. This option is the default for /dev/fdX devices. Some BIOSes will not boot images created with this option. </p>
<dt>&#8211;recheck</p>
<dd>Delete any existing device map and create a new one if necessary. </p>
<dt>&#8211;force</p>
<dd>Install even if problems are detected. </p>
<dt>&#8211;force-file-id</p>
<dd>Use identifier file even if UUID is available. </p>
<dt>&#8211;disk-module</code>=<i>MODULE</i></p>
<dd>Use <i>MODULE</i> for disk access. This allows you to manually specify either <i>biosdisk</i> or <i>native</i> disk access. This option is only available on the BIOS target platform. </p>
<dt><code>&#8211;no-nvram</p>
<dd>Do not update the </code><i>boot-device</i> NVRAM variable. This option is only available on IEEE1275 target platforms. </p>
<dt><code>&#8211;removable</p>
<dd>Treat the target device as if it is removeable. This option is only available on the EFI target platform. </p>
<dt>&#8211;bootloader-id</code>=<i>ID</i></p>
<dd>Use <i>ID</i> as the bootloader ID. This opption is only available on the EFI target platform. </p>
<dt><code>&#8211;efi-directory</code>=<i>DIR</i></p>
<dd>Use <i>DIR</i> as the EFI System Partition root. This opption is only available on the EFI ta rget platform. </p>
<dt><i>INSTALL_DEVICE</i></p>
<dd>Install GRUB to the block device <i>INSTALL_DEVICE</i>. </p>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> </p>

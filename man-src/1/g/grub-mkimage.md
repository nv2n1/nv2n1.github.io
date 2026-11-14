---
title: "grub-mkimage(1)"
name: "grub-mkimage"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mkimage/"
description: "grub-mkimage – make a bootable image of GRUB"
---

<h2 class="name">NAME</h2>
<p> grub-mkimage &#8211; make a bootable image of GRUB </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkimage</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>]&#8230; [<i>,MODULES/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Make a bootable image of GRUB.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code>=<i>,FILE/</i></p>
<dd> embed FILE as an early config</p>
<dt><code>-C</code>, <code>&#8211;compression=</code>(xz|none|auto)</p>
<dd> choose the compression to use for core image</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></p>
<dd> use images and modules under DIR [default=/usr/lib/grub/&lt;platform&gt;]</p>
<dt><code>&#8211;disable-shim-lock</code></p>
<dd> disable shim_lock verifier</p>
<dt><code>-D</code>, <code>&#8211;dtb</code>=<i>,FILE/</i></p>
<dd> embed FILE as a device tree (DTB)</p>
<dt><code>-k</code>, <code>&#8211;pubkey</code>=<i>,FILE/</i></p>
<dd> embed FILE as public key for signature checking</p>
<dt><code>-m</code>, <code>&#8211;memdisk</code>=<i>,FILE/</i></p>
<dd> embed FILE as a memdisk image</dl>
<p> Implies `-p (memdisk)/boot/grub&#8217; and overrides</p>
<dl>
<dt>any prefix supplied previously, but the prefix</p>
<dd> itself can be overridden by later options</p>
<dt><code>-n</code>, <code>&#8211;note</code></p>
<dd> add NOTE segment for CHRP IEEE1275</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> output a generated image to FILE [default=stdout]</p>
<dt><code>-O</code>, <code>&#8211;format</code>=<i>,FORMAT/</i></p>
<dd> generate an image in FORMAT available formats: i386-coreboot, i386-multiboot, i386-pc, i386-xen_pvh, i386-pc-pxe, i386-pc-eltorito, i386-efi, i386-ieee1275, i386-qemu, x86_64-efi, i386-xen, x86_64-xen, mipsel-yeeloong-flash, mipsel-fuloong2f-flash, mipsel-loongson-elf, powerpc-ieee1275, sparc64-ieee1275-raw, sparc64-ieee1275-cdcore, sparc64-ieee1275-aout, ia64-efi, mips-arc, mipsel-arc, mipsel-qemu_mips-elf, mips-qemu_mips-flash, mipsel-qemu_mips-flash, mips-qemu_mips-elf, arm-uboot, arm-coreboot-vexpress, arm-coreboot-veyron, arm-efi, arm64-efi, riscv32-efi, riscv64-efi</p>
<dt><code>-p</code>, <code>&#8211;prefix</code>=<i>,DIR/</i></p>
<dd> set prefix directory</p>
<dt><code>-s</code>, <code>&#8211;sbat</code>=<i>,FILE/</i></p>
<dd> SBAT metadata</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print verbose messages.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub-install/">grub-install</a></code>(8), <code><a href="/docs/linux/man/1-grub-mkrescue/">grub-mkrescue</a></code>(1), <code><a href="/docs/linux/man/8-grub-mknetdir/">grub-mknetdir</a></code>(8) </p>
<p> The full documentation for <code>grub-mkimage</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mkimage</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-mkimage</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>

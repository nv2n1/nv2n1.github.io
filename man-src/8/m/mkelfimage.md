---
title: "mkelfimage(8)"
name: "mkelfimage"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkelfimage/"
description: "mkelfImage – make an elf network bootable image for linux"
---

<p>mkelfImage &#8211; make an elf network bootable image for linux</p>
<h2>Synopsis</h2>
<p><code>mkelfImage</code> [&#8211;command-line=<i>command line</i>] [&#8211;kernel=<i>path to vmlinux</i>] [&#8211;ramdisk=<i>path to ramdisk</i>] [&#8211;output=<i>file</i>] [&#8211;ramdisk-base=&lt;start addr&gt;]</p>
<h2>Description</h2>
<p><code>mkelfImage</code> is a program that makes a elf boot image for linux kernel images. The image should work with any i386 multiboot compliant boot loader, an <font SIZE="-1">ELF</font> bootloader that passes no options, a loader compliant with the linuxBIOS elf booting spec or with the linux kexec kernel patch. A key feature here is that nothing relies upon <font SIZE="-1">BIOS</font> calls, but they are made when necessary. This is useful for systems running linuxbios.</p>
<h2>Bugs</h2>
<p>Not all kernel parameters can be passed with the multiboot image format. ip configuration is not automatically passed to a node. The ramdisk base is hard coded to 8MB by default. This man page need to be updated.</p>
<h2>See Also</h2>
<p>The kexec kernel patch. LinuxBIOS. Etherboot. The multiboot standard.</p>
<h2>Copyright</h2>
<p>mkelfImage is under the <font SIZE="-1">GNU</font> Public License version 2</p>
<h2>Author</h2>
<p>Eric Biederman &lt;ebiederman [at] lnxi.com&gt;</p>

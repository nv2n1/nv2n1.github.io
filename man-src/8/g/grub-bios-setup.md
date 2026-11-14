---
title: "grub-bios-setup(8)"
name: "grub-bios-setup"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub-bios-setup/"
description: "grub-bios-setup – set up a device to boot using GRUB"
---

<p>grub-bios-setup &#8211; set up a device to boot using GRUB</p>
<h2>Synopsis</h2>
<p><code>grub-bios-setup</code> [<i>,OPTION/</i>&#8230;] <i>,DEVICE/</i></p>
<h2>Description</h2>
<p>Set up images to boot from DEVICE. </p>
<p> You should not normally run this program directly. Use grub-install instead.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;allow-floppy</code></p>
<dd>make the drive also bootable as floppy (default for fdX devices). May break on some BIOSes.</p>
<dt><code>-b</code>, <code>&#8211;boot-image</code>=<i>,FILE/</i></p>
<dd>use FILE as the boot image [default=boot.img]</p>
<dt><code>-c</code>, <code>&#8211;core-image</code>=<i>,FILE/</i></p>
<dd>use FILE as the core image [default=core.img]</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></p>
<dd>use GRUB files in the directory DIR [default=/boot/grub]</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>install even if problems are detected</p>
<dt><code>-m</code>, <code>&#8211;device-map</code>=<i>,FILE/</i></p>
<dd>use FILE as the device map [default=/boot/grub/device.map]</p>
<dt><code>&#8211;no-rs-codes</code></p>
<dd>Do not apply any reed-solomon codes when embedding core.img. This option is only available on x86 BIOS targets.</p>
<dt><code>-s</code>, <code>&#8211;skip-fs-probe</code></p>
<dd>do not probe for filesystems in DEVICE</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>print verbose messages.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd>give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd>give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> DEVICE must be an OS device (e.g. <i>,/dev/sda/</i>).</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub-install/">grub-install</a></code>(8), <code><a href="/docs/linux/man/1-grub-mkimage/">grub-mkimage</a></code>(1), <code><a href="/docs/linux/man/1-grub-mkrescue/">grub-mkrescue</a></code>(1) The full documentation for <code>grub-bios-setup</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-bios-setup</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub-bios-setup</code></dl>
<p> should give you access to the complete manual. </p>

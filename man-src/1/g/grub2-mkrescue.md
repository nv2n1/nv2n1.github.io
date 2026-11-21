---
title: "grub2-mkrescue(1)"
name: "grub2-mkrescue"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-mkrescue/"
description: "grub-mkrescue — Generate a GRUB rescue image using GNU Xorriso."
---

<h2>NAME</h2>
<p> grub-mkrescue &#8212; Generate a GRUB rescue image using GNU Xorriso. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkrescue</code> [-o | &#8211;output=<i>FILE</i>] [&#8211;modules=<i>MODULES</i>]</p>
<dl>
<dt>
</dt><dd> [&#8211;install-modules=<i>MODULES</i>] [&#8211;themes=<i>THEMES</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;fonts=<i>FONTS</i>] [&#8211;locales=<i>LOCALES</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;compress[=<i>no</i>,<i>xz</i>,<i>gz</i>,<i>lzo</i>]] [-d | &#8211;directory=<i>DIR</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;grub-mkimage=<i>FILE</i>] [&#8211;rom-directory=<i>DIR</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;xorriso=<i>FILE</i>] [&#8211;grub-glue-efi=<i>FILE</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;grub-render-label=<i>FILE</i>] [&#8211;label-font=<i>FILE</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;label-color=<i>COLOR</i>] [&#8211;label-bgcolor=<i>FILE</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;product-name=<i>STRING</i>] [&#8211;product-version=<i>STRING</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;sparc-boot] [&#8211;arcs-boot] </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-mkrescue</code> can be used to generate a rescue image with the GRUB bootloader. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;output</code>=<i>FILE</i></dt>
<dd> Write the generated file to <i>FILE</i>. The default is to write to standard output. </dd>
<dt><code>&#8211;modules</code>=<i>MODULES</i></dt>
<dd> Pre-load modules specified by <i>MODULES</i>. </dd>
<dt><code>&#8211;install-modules</code>=<i>MODULES</i></dt>
<dd> Install only <i>MODULES</i> and their dependencies. The default is to install all available modules. </dd>
<dt><code>&#8211;themes</code>=<i>THEMES</i></dt>
<dd> Install <i>THEMES</i>. The default is to install the <i>starfield</i> theme, if available. </dd>
<dt><code>&#8211;fonts</code>=<i>FONTS</i></dt>
<dd> Install <i>FONTS</i>. The default is to install the <i>unicode</i> font. </dd>
<dt><code>&#8211;locales</code>=<i>LOCALES</i></dt>
<dd> Install only locales listed in <i>LOCALES</i>. The default is to install all available locales. </dd>
<dt><code>&#8211;compress</code>[=<i>no</i>,<i>xz</i>,<i>gz</i>,<i>lzo</i>]</dt>
<dd> Compress GRUB files using the specified compression algorithm. </dd>
<dt><code>&#8211;directory</code>=<i>DIR</i></dt>
<dd> Use images and modules in <i>DIR</i>. </dd>
<dt><code>&#8211;grub-mkimage</code>=<i>FILE</i></dt>
<dd> Use <i>FILE</i> as <code><a href="/docs/linux/man/1-grub-mkimage/">grub-mkimage</a></code>(1). The default is <i>/usr/bin/grub-mkimage</i>. </dd>
<dt><code>&#8211;rom-directory</code>=<i>DIR</i></dt>
<dd> Save ROM images in <i>DIR</i>. </dd>
<dt><code>&#8211;xorriso</code>=<i>FILE</i></dt>
<dd> Use <i>FILE</i> as <code>xorriso</code><i>. </dd>
<dt></i><code>&#8211;grub-glue-efi</code>=<i>FILE</i></dt>
<dd> Use <i>FILE</i> as <code>grub-glue-efi</code>(3). </dd>
<dt><code>&#8211;grub-render-label</code>=<i>FILE</i></dt>
<dd> Use <i>FILE</i> as <code>grub-render-label</code>(3). </dd>
<dt><code>&#8211;label-font</code>=<i>FILE</i></dt>
<dd> Use <i>FILE</i> as the font file for generated labels. </dd>
<dt><code>&#8211;label-color</code>=<i>COLOR</i></dt>
<dd> Use <i>COLOR as the color for generated labels. </dd>
<dt></i><code>&#8211;label-bgcolor</code>=<i>COLOR</i></dt>
<dd> Use <i>COLOR</i> as the background color for generated labels. </dd>
<dt><code>&#8211;product-name</code>=<i>STRING</i></dt>
<dd> Use <i>STRING</i> as the product name in generated labels. </dd>
<dt><code>&#8211;product-version</code>=<i>STRING</i></dt>
<dd> Use <i>STRING</i> as the product version in generated labels. </dd>
<dt><code>&#8211;sparc-boot</code></dt>
<dd> Enable booting the SPARC platform. This disables HFS+, APM, ARCS, and &quot;boot as disk image&quot; on the <i>i386-pc</i> target platform. </dd>
<dt><code>&#8211;arcs-boot</code></dt>
<dd> Enable ARCS booting. This is typically for big-endian MIPS machines, and disables HFS+, APM, sparc64, and &quot;boot as disk image&quot; on the <i>i386-pc</i> target platform. </dd>
<dt><code>&#8212;</code></dt>
<dd> All options after a <code>&#8212;</code> will be passed directly to xorriso&#8217;s command line when generating the image. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>

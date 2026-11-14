---
title: "mkimage(1)"
name: "mkimage"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkimage/"
description: "mkimage – Generate image for U-Boot"
---

<h2 class="name">NAME</h2>
<p> mkimage &#8211; Generate image for U-Boot </p>
<h2>SYNOPSIS</h2>
<p> <code>mkimage</code> -l [<code>uimage file name</code>] </p>
<p> <code>mkimage</code> [<i>options</i>]<code> -f [</code>image tree source file<code>]</code> [<code>uimage file name</code>] </p>
<p> <code>mkimage</code> [<i>options</i>]<code> -F [</code>uimage file name<code>]</code> </p>
<p> <code>mkimage</code> [<i>options</i>]<code> (legacy mode)</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>mkimage</code> command is used to create images for use with the U-Boot boot loader. These images can contain the linux kernel, device tree blob, root file system image, firmware images etc., either separate or combined. </p>
<p> <code>mkimage</code> supports two different formats: </p>
<p> The old <i>legacy image</i> format concatenates the individual parts (for example, kernel image, device tree blob and ramdisk image) and adds a 64 bytes header containing information about target architecture, operating system, image type, compression method, entry points, time stamp, checksums, etc. </p>
<p> The new <i>FIT (Flattened Image Tree) format</i> allows for more flexibility in handling images of various types and also enhances integrity protection of images with stronger checksums. It also supports verified boot. </p>
<h2>OPTIONS</h2>
<p> <code>List image information:</code> </p>
<dl>
<dt><code>-l [</code><i>uimage file name</i><code>]</code></p>
<dd> mkimage lists the information contained in the header of an existing U-Boot image. </p>
</dl>
<p> <code>Create old legacy image:</code> </p>
<dl>
<dt><code>-A [</code><i>architecture</i><code>]</code></p>
<dd> Set architecture. Pass -h as the architecture to see the list of supported architectures. </p>
<dt><code>-O [</code><i>os</i><code>]</code></p>
<dd> Set operating system. bootm command of u-boot changes boot method by os type. Pass -h as the OS to see the list of supported OS. </p>
<dt><code>-T [</code><i>image type</i><code>]</code></p>
<dd> Set image type. Pass -h as the image to see the list of supported image type. </p>
<dt><code>-C [</code><i>compression type</i><code>]</code></p>
<dd> Set compression type. Pass -h as the compression to see the list of supported compression type. </p>
<dt><code>-a [</code><i>load addess</i><code>]</code></p>
<dd> Set load address with a hex number. </p>
<dt><code>-e [</code><i>entry point</i><code>]</code></p>
<dd> Set entry point with a hex number. </p>
<dt><code>-l</code></p>
<dd> List the contents of an image. </p>
<dt><code>-n [</code><i>image name</i><code>]</code></p>
<dd> Set image name to &#8216;image name&#8217;. </p>
<dt><code>-d [</code><i>image data file</i><code>]</code></p>
<dd> Use image data from &#8216;image data file&#8217;. </p>
<dt><code>-x</code></p>
<dd> Set XIP (execute in place) flag. </p>
</dl>
<p> <code>Create FIT image:</code> </p>
<dl>
<dt><code>-c [</code><i>comment</i><code>]</code></p>
<dd> Specifies a comment to be added when signing. This is typically a useful message which describes how the image was signed or some other useful information. </p>
<dt><code>-D [</code><i>dtc options</i><code>]</code></p>
<dd> Provide special options to the device tree compiler that is used to create the image. </p>
<dt><code>-f [</code><i>image tree source file</i><code>]</code></p>
<dd> Image tree source file that describes the structure and contents of the FIT image. </p>
<dt><code>-F</code></p>
<dd> Indicates that an existing FIT image should be modified. No dtc compilation is performed and the -f flag should not be given. This can be used to sign images with additional keys after initial image creation. </p>
<dt><code>-k [</code><i>key_directory</i><code>]</code></p>
<dd> Specifies the directory containing keys to use for signing. This directory should contain a private key file &lt;name&gt;.key for use with signing and a certificate &lt;name&gt;.crt (containing the public key) for use with verification. </p>
<dt><code>-K [</code><i>key_destination</i><code>]</code></p>
<dd> Specifies a compiled device tree binary file (typically .dtb) to write public key information into. When a private key is used to sign an image, the corresponding public key is written into this file for for run-time verification. Typically the file here is the device tree binary used by CONFIG_OF_CONTROL in U-Boot. </p>
<dt><code>-r</code></p>
<dd> Specifies that keys used to sign the FIT are required. This means that they must be verified for the image to boot. Without this option, the verification will be optional (useful for testing but not for release). </p>
</dl>
<h2>EXAMPLES</h2>
<p> List image information: </p>
<pre>
<code>mkimage -l uImage</code>
</pre>
<p> Create legacy image with compressed PowerPC Linux kernel: </p>
<pre>
<code>mkimage -A powerpc -O linux -T kernel -C gzip \</code>
<br>
<code>-a 0 -e 0 -n Linux -d vmlinux.gz uImage</code>
</pre>
<p> Create FIT image with compressed PowerPC Linux kernel: </p>
<pre>
<code>mkimage -f kernel.its kernel.itb</code>
</pre>
<p> Create FIT image with compressed kernel and sign it with keys in the /public/signing-keys directory. Add corresponding public keys into u-boot.dtb, skipping those for which keys cannot be found. Also add a comment. </p>
<pre>
<code>mkimage -f kernel.its -k /public/signing-keys -K u-boot.dtb \</code>
<br>
<code>-c Kernel 3.8 image for production devices kernel.itb</code>
</pre>
<p> Update an existing FIT image, signing it with additional keys. Add corresponding public keys into u-boot.dtb. This will resign all images with keys that are available in the new directory. Images that request signing with unavailable keys are skipped. </p>
<pre>
<code>mkimage -F -k /secret/signing-keys -K u-boot.dtb \</code>
<br>
<code>-c Kernel 3.8 image for production devices kernel.itb</code>
</pre>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://www.denx.de/wiki/U-Boot/WebHome">http://www.denx.de/wiki/U-Boot/WebHome</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Nobuhiro Iwamatsu &lt;iwamatsu [at] nigauri.org&gt; and Wolfgang Denk &lt;wd [at] denx.de&gt;. It was updated for image signing by Simon Glass &lt;sjg [at] chromium.org&gt;. </p>
<h2>Index</h2>

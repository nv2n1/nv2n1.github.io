---
title: "grub2-setpassword(8)"
name: "grub2-setpassword"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub2-setpassword/"
description: "grub-setpassword — Generate the user.cfg file containing the hashed grub bootloader password."
---

<p><code>grub-setpassword</code> &#8212; Generate the user.cfg file containing the hashed grub bootloader password. </p>
<h2>Synopsis</h2>
<p><code>grub-setpassword</code> [OPTION] </p>
<h2>Description</h2>
<p><code>grub-setpassword</code> outputs the user.cfg file which contains the hashed GRUB bootloader password. This utility only supports configurations where there is a single root user. The file has the format: GRUB2_PASSWORD=&lt;<i>hashed password</i>&gt;. </p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd>Display program usage and exit.</p>
<dt>-v, &#8211;version</p>
<dd>Display the current version.</p>
<dt>-o, &#8211;output=&lt;<i>DIRECTORY</i>&gt;</p>
<dd>Choose the file path to which user.cfg will be written. </p>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> <code>info grub2-mkpasswd-pbkdf2</code> </p>

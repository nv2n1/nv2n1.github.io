---
title: "isohybrid(1)"
name: "isohybrid"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isohybrid/"
description: "isohybrid — Post-process an ISO 9660 image generated with mkisofs or genisoimage to allow hybrid booting as a CD-ROM or as a hard disk."
---

<h2>NAME</h2>
<p> isohybrid &#8212; Post-process an ISO 9660 image generated with mkisofs or genisoimage to allow hybrid booting as a CD-ROM or as a hard disk.</p>
<h2>SYNOPSIS</h2>
<p> <code>isohybrid</code> [<code>OPTIONS</code>] <i>&lt;boot.iso&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>isohybrid</code> utility modifies a an ISO 9660 image generated with mkisofs, genisoimage, or compatible utilities, to be bootable as a CD-ROM or as a hard disk.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <i>&lt;X&gt;</i></p>
<dd>
 Number of default geometry heads</p>
<dt><code>-s</code> <i>&lt;X&gt;</i></p>
<dd>
 Number of default geometry sectors</p>
<dt><code>-e</code> <i>&lt;X&gt;</i>, <code>&#8211;entry</code> <i>&lt;X&gt;</i></p>
<dd> Specify parititon entry number (1-4)</p>
<dt><code>-o</code> <i>&lt;X&gt;</i>, <code>&#8211;offset</code> <i>&lt;X&gt;</i></p>
<dd>
 Specify partition offset (default 0)</p>
<dt><code>-t</code> <i>&lt;X&gt;</i>, <code>&#8211;type</code> <i>&lt;X&gt;</i></p>
<dd>
 Specify MBR ID (default random)</p>
<dt><code>-u</code>, <code>&#8211;uefi</p>
<dd> Build EFI bootable image</p>
<dt>-m</code>, <code>&#8211;mac</p>
<dd> Add Apple File Protocol partition table support</p>
<dt>&#8211;forcehd0</code></p>
<dd> Assume we are laoded as disk ID 0</p>
<dt><code>&#8211;ctrlhd0</code></p>
<dd> Assume disk ID 0 if the Ctrl key is pressed</p>
<dt><code>&#8211;partok</code></p>
<dd> Allow booting from within a partition</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display help</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display verbose output</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkisofs/">mkisofs</a></code>(1) </p>
<h2>Index</h2>

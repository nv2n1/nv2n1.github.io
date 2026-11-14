---
title: "grub2-probe(8)"
name: "grub2-probe"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub2-probe/"
description: "grub-probe — Probe device information for a given path."
---

<p><code>grub-probe</code> &#8212; Probe device information for a given path. </p>
<h2>Synopsis</h2>
<p><code>grub-probe</code> ce [-m | &#8211;device-map=<i>FILE</i>]</p>
<dl>
<dd>[-t | &#8211;target=(fs|fs_uuid|fs_label|drive|device|partmap|</dl>
<dl>
<dd>abstraction|cryptodisk_uuid|</dl>
<dl>
<dd>msdos_parttype)]</dl>
<dl>
<dd>[-v | &#8211;verbose] (PATH|DEVICE) </p>
<h2>Description</h2>
<p><code>grub-probe</code> probes a path or device for filesystem and related information. </p>
<h2>Options</h2>
<dl>
<dt>&#8211;device</p>
<dd>Final option represents a <i>DEVICE</i>, rather than a filesystem <i>PATH</i>.</p>
<dt>&#8211;device-map=<i>FILE</i></p>
<dd>Use <i>FILE</i> as the device map. The default value is <i>/boot/grub/device.map</i>. </p>
<dt>&#8211;target=(fs|fs_uuid|fs_label|drive|device|partmap|msdos_parttype)</p>
<dd>Select among various output definitions. The default is <i>fs</i>.</p>
<dl>
<dd>
<dl>
<dt><i>fs</i></p>
<dd>filesystem module </p>
<dt><i>fs_uuid</i></p>
<dd>filesystem UUID </p>
<dt><i>fs_label</i></p>
<dd>filesystem label </p>
<dt><i>drive</i></p>
<dd>GRUB drive name </p>
<dt><i>device</i></p>
<dd>System device </p>
<dt><i>partmap</i></p>
<dd>partition map module </p>
<dt><i>abstraction</i></p>
<dd>abstraction module </p>
<dt><i>cryptodisk_uuid</i></p>
<dd>cryptographic container </p>
<dt><i>msdos_partmap</i></p>
<dd>MS-DOS partition map</dl>
</dl>
<dt>&#8211;verbose</p>
<dd>Print verbose output. </p>
<dt>(<i>PATH</i>|<i>DEVICE</i>)</p>
<dd>If &#8211;device is passed, a block <i>DEVICE</i>. Otherwise, the <i>PATH</i> of a file on the filesystem. </p>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> </p>

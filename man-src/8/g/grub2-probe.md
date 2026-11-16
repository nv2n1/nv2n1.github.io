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
<dd>[-t | &#8211;target=(fs|fs_uuid|fs_label|drive|device|partmap|</dd></dl>
<dl>
<dd>abstraction|cryptodisk_uuid|</dd></dl>
<dl>
<dd>msdos_parttype)]</dd></dl>
<dl>
<dd>[-v | &#8211;verbose] (PATH|DEVICE) </dd>
<h2>Description</h2>
<p><code>grub-probe</code> probes a path or device for filesystem and related information. </p>
<h2>Options</h2>
<dl>
<dt>&#8211;device</dt>
<dd>Final option represents a <i>DEVICE</i>, rather than a filesystem <i>PATH</i>.</dd>
<dt>&#8211;device-map=<i>FILE</i></dt>
<dd>Use <i>FILE</i> as the device map. The default value is <i>/boot/grub/device.map</i>. </dd>
<dt>&#8211;target=(fs|fs_uuid|fs_label|drive|device|partmap|msdos_parttype)</dt>
<dd>Select among various output definitions. The default is <i>fs</i>.</dd>
<dl>
<dd>
</dd><dl>
<dt><i>fs</i></dt>
<dd>filesystem module </dd>
<dt><i>fs_uuid</i></dt>
<dd>filesystem UUID </dd>
<dt><i>fs_label</i></dt>
<dd>filesystem label </dd>
<dt><i>drive</i></dt>
<dd>GRUB drive name </dd>
<dt><i>device</i></dt>
<dd>System device </dd>
<dt><i>partmap</i></dt>
<dd>partition map module </dd>
<dt><i>abstraction</i></dt>
<dd>abstraction module </dd>
<dt><i>cryptodisk_uuid</i></dt>
<dd>cryptographic container </dd>
<dt><i>msdos_partmap</i></dt>
<dd>MS-DOS partition map</dd></dl>
</dl>
<dt>&#8211;verbose</dt>
<dd>Print verbose output. </dd>
<dt>(<i>PATH</i>|<i>DEVICE</i>)</dt>
<dd>If &#8211;device is passed, a block <i>DEVICE</i>. Otherwise, the <i>PATH</i> of a file on the filesystem. </dd>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> </p>
</dl>
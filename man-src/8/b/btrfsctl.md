---
title: "btrfsctl(8)"
name: "btrfsctl"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfsctl/"
description: "btrfsctl – control a btrfs filesystem"
---

<p>btrfsctl &#8211; control a btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfsctl</code> [ <code>-d</code><i> file|directory </i> ] [ <code>-s</code><i> snapshot-name directory</i> ] [ <code> -S</code><i> subvolume-name directory</i> ] [ <code> -r</code><i> [+-]size</i> ] [ <code> -A</code><i> device</i> ] [ <code> -a</code> ] [ <code> -c</code> ]</p>
<h2>Note</h2>
<p>B btrfsctl is deprecated. Please consider to switch to the btrfs utility.</p>
<h2>Description</h2>
<p><code>btrfsctl</code> is used to control the filesystem and the files and directories stored. It is the tool to create a new snapshot for the filesystem.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code> <i>file|directory</i></dt>
<dd>Defragment a file or a directory. If the argument is a directory, the entire b-tree under the directory is defragged.</dd>
<dt><code>-s</code> <i>snapshot-name directory</i></dt>
<dd>Creates a new <i>snapshot</i> of the <i>directory</i> specified.</dd>
<dt><code>-S</code> <i>subvolume-name directory</i></dt>
<dd>Creates a new subvolume.</dd>
<dt><code>-r</code> <i>[+|-]size</i></dt>
<dd>Resizes the filesystem with the <i>size</i> specified. If the value is preceded with a signed symbol, the filesystem is resized with respect to the current filesystem size. <i>size</i> can be suffixed by k,m or g to represent kilobytes, megabytes, or gigabytes respectively.</dd>
<dt><code>-A</code> <i>device</i></dt>
<dd>Scans the <i>device</i> for btrfs filesystem.</dd>
<dt><code>-a</code></dt>
<dd>Scans all devices present in the system for btrfs filesystem.</dd>
<dt><code>-c</code></dt>
<dd>Forces a filesystem sync.</dd></dl>
<h2>Availability</h2>
<p><code>btrfsctl</code> is part of btrfs-progs. Btrfs is currently under heavy development, and not suitable for any uses other than benchmarking and review. Please refer to the btrfs wiki <a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a> for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>

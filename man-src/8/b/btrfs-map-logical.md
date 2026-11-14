---
title: "btrfs-map-logical(8)"
name: "btrfs-map-logical"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-map-logical/"
description: "btrfs-map-logical – map btrfs logical extent to physical extent"
---

<p>btrfs-map-logical &#8211; map btrfs logical extent to physical extent</p>
<h2>Synopsis</h2>
<p><code>btrfs-map-logical</code> <i>&lt;options&gt;</i> <i>&lt;device&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs-map-logical</code> can be used to find out what the physical offsets are on the mirrors, the result is dumped to stdout by default. </p>
<p> Mainly used for debug purpose.</p>
<h2>Options</h2>
<p>-l|&#8211;logical <i>&lt;logical_num&gt;</i></p>
<dl>
<dd>Logical extent to map.</dl>
<p> -c|&#8211;copy <i>&lt;copy&gt;</i></p>
<dl>
<dd>Copy of the extent to read(usually 1 or 2).</dl>
<p> -o|&#8211;output <i>&lt;filename&gt;</i></p>
<dl>
<dd>Output file to hold the extent.</dl>
<p> -b|&#8211;bytes <i>&lt;bytes&gt;</i></p>
<dl>
<dd>Number of bytes to read.</dl>
<h2>Exit Status</h2>
<p><code>btrfs-map-logical</code> will return 0 if no error happened. If any problems happened, 1 will be returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>

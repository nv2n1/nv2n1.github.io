---
title: "btrfs-find-root(8)"
name: "btrfs-find-root"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-find-root/"
description: "btrfs-find-root – filter to find btrfs root"
---

<p>btrfs-find-root &#8211; filter to find btrfs root</p>
<h2>Synopsis</h2>
<p><code>btrfs-find-root</code> [options] <i>&lt;device&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs-find-root</code> is used to find the satisfied root, you can filter by root tree&#8217;s objectid, generation, level.</p>
<h2>Options</h2>
<p>-a</p>
<dl>
<dd>Search through all metadata extents, even the root has been already found.</dl>
<p> -g <i>&lt;generation&gt;</i></p>
<dl>
<dd>Filter root tree by it&#8217;s original transaction id, tree root&#8217;s generation in default.</dl>
<p> -o <i>&lt;objectid&gt;</i></p>
<dl>
<dd>Filter root tree by it&#8217;s objectid,tree root&#8217;s objectid in default.</dl>
<p> -l <i>&lt;level&gt;</i></p>
<dl>
<dd>Filter root tree by B-+ tree&#8217;s level, level 0 in default.</dl>
<h2>Exit Status</h2>
<p><code>btrfs-find-root</code> will return 0 if no error happened. If any problems happened, 1 will be returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>

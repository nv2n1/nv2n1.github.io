---
title: "btrfs(8)"
name: "btrfs"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs/"
description: "btrfs – a toolbox to manage btrfs filesystems"
---

<p>btrfs &#8211; a toolbox to manage btrfs filesystems</p>
<h2>Synopsis</h2>
<p><code>btrfs</code> <i>&lt;command&gt;</i> [<i>&lt;args&gt;</i>]</p>
<h2>Description</h2>
<p>The <code>btrfs</code> utility is a toolbox for managing btrfs filesystems. There are command groups to work with subvolumes, devices, for whole filesystem or other specific actions. See section <code>COMMANDS</code>. </p>
<p> There are also standalone tools for some tasks like <code>btrfs-convert</code> or <code>btrfstune</code> that were separate historically and/or haven&#8217;t been merged to the main utility. See section <i>STANDALONE TOOLS</i> for more details. </p>
<p> For other topics (mount options, etc) please refer to the separate manual page <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5).</p>
<h2>Command Syntax</h2>
<p>Any command name can be shortened so long as the shortened form is unambiguous, however, it is recommended to use full command names in scripts. All command groups have their manual page named <code>btrfs-</code><i>&lt;group&gt;</i>. </p>
<p> For example: it is possible to run <code>btrfs sub snaps</code> instead of <code>btrfs subvolume snapshot</code>. But <code>btrfs file s</code> is not allowed, because <code>file s</code> may be interpreted both as <code>filesystem show</code> and as <code>filesystem sync</code>. </p>
<p> If the command name is ambiguous, the list of conflicting options is printed. </p>
<p> For an overview of a given command use <i>btrfs command &#8211;help</i> or <i>btrfs [command&#8230;] &#8211;help &#8211;full</i> to print all available options.</p>
<h2>Commands</h2>
<p><code>balance</code></p>
<dl>
<dd>Balance btrfs filesystem chunks across single or several devices. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-balance/">btrfs-balance</a></code>(8) for details.</dl>
<p> <code>check</code></p>
<dl>
<dd>Do off-line check on a btrfs filesystem. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-check/">btrfs-check</a></code>(8) for details.</dl>
<p> <code>device</code></p>
<dl>
<dd>Manage devices managed by btrfs, including add/delete/scan and so on. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-device/">btrfs-device</a></code>(8) for details.</dl>
<p> <code>filesystem</code></p>
<dl>
<dd>Manage a btrfs filesystem, including label setting/sync and so on. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-filesystem/">btrfs-filesystem</a></code>(8) for details.</dl>
<p> <code>inspect-internal</code></p>
<dl>
<dd>Debug tools for developers/hackers. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-inspect-internal/">btrfs-inspect-internal</a></code>(8) for details.</dl>
<p> <code>property</code></p>
<dl>
<dd>Get/set a property from/to a btrfs object. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-property/">btrfs-property</a></code>(8) for details.</dl>
<p> <code>qgroup</code></p>
<dl>
<dd>Manage quota group(qgroup) for btrfs filesystem. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-qgroup/">btrfs-qgroup</a></code>(8) for details.</dl>
<p> <code>quota</code></p>
<dl>
<dd>Manage quota on btrfs filesystem like enabling/rescan and etc. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-quota/">btrfs-quota</a></code>(8) and <code><a href="/docs/linux/man/8-btrfs-qgroup/">btrfs-qgroup</a></code>(8) for details.</dl>
<p> <code>receive</code></p>
<dl>
<dd>Receive subvolume data from stdin/file for restore and etc. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-receive/">btrfs-receive</a></code>(8) for details.</dl>
<p> <code>replace</code></p>
<dl>
<dd>Replace btrfs devices. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-replace/">btrfs-replace</a></code>(8) for details.</dl>
<p> <code>rescue</code></p>
<dl>
<dd>Try to rescue damaged btrfs filesystem. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-rescue/">btrfs-rescue</a></code>(8) for details.</dl>
<p> <code>restore</code></p>
<dl>
<dd>Try to restore files from a damaged btrfs filesystem. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-restore/">btrfs-restore</a></code>(8) for details.</dl>
<p> <code>scrub</code></p>
<dl>
<dd>Scrub a btrfs filesystem. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-scrub/">btrfs-scrub</a></code>(8) for details.</dl>
<p> <code>send</code></p>
<dl>
<dd>Send subvolume data to stdout/file for backup and etc. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-send/">btrfs-send</a></code>(8) for details.</dl>
<p> <code>subvolume</code></p>
<dl>
<dd>Create/delete/list/manage btrfs subvolume. </p>
<p> See <code><a href="/docs/linux/man/8-btrfs-subvolume/">btrfs-subvolume</a></code>(8) for details.</dl>
<h2>Standalone Tools</h2>
<p>New functionality could be provided using a standalone tool. If the functionality proves to be useful, then the standalone tool is declared obsolete and its functionality is copied to the main tool. Obsolete tools are removed after a long (years) depreciation period. </p>
<p> Tools that are still in active use without an equivalent in <code>btrfs</code>: </p>
<p> <code>btrfs-convert</code></p>
<dl>
<dd>in-place conversion from ext2/3/4 filesystems to btrfs</dl>
<p> <code>btrfstune</code></p>
<dl>
<dd>tweak some filesystem properties on a unmounted filesystem</dl>
<p> <code>btrfs-select-super</code></p>
<dl>
<dd>rescue tool to overwrite primary superblock from a spare copy</dl>
<p> <code>btrfs-find-root</code></p>
<dl>
<dd>rescue helper to find tree roots in a filesystem</dl>
<p> Deprecated and obsolete tools: </p>
<p> <code>btrfs-debug-tree</code></p>
<dl>
<dd>moved to <code>btrfs inspect-internal dump-tree</code>. Removed from source distribution.</dl>
<p> <code>btrfs-show-super</code></p>
<dl>
<dd>moved to <code>btrfs inspect-internal dump-super</code>, standalone removed.</dl>
<p> <code>btrfs-zero-log</code></p>
<dl>
<dd>moved to <code>btrfs rescue zero-log</code>, standalone removed.</dl>
<p> For space-constrained environments, it&#8217;s possible to build a single binary with functionality of several standalone tools. This is following the concept of busybox where the file name selects the functionality. This works for symlinks or hardlinks. The full list can be obtained by <code>btrfs help &#8211;box</code>.</p>
<h2>Exit Status</h2>
<p><code>btrfs</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/8-btrfs-balance/">btrfs-balance</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-check/">btrfs-check</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-convert/">btrfs-convert</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-device/">btrfs-device</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-filesystem/">btrfs-filesystem</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-inspect-internal/">btrfs-inspect-internal</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-property/">btrfs-property</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-qgroup/">btrfs-qgroup</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-quota/">btrfs-quota</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-receive/">btrfs-receive</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-replace/">btrfs-replace</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-rescue/">btrfs-rescue</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-restore/">btrfs-restore</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-scrub/">btrfs-scrub</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-send/">btrfs-send</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-subvolume/">btrfs-subvolume</a></code>(8), <code><a href="/docs/linux/man/8-btrfstune/">btrfstune</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8) </p>

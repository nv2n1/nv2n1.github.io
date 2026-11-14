---
title: "btrfs-send(8)"
name: "btrfs-send"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-send/"
description: "btrfs-send – generate a stream of changes between two subvolume snapshots"
---

<p>btrfs-send &#8211; generate a stream of changes between two subvolume snapshots</p>
<h2>Synopsis</h2>
<p><code>btrfs send</code> [-ve] [-p <i>&lt;parent&gt;</i>] [-c <i>&lt;clone-src&gt;</i>] [-f <i>&lt;outfile&gt;</i>] <i>&lt;subvol&gt;</i> [<i>&lt;subvol&gt;</i>&#8230;]</p>
<h2>Description</h2>
<p>This command will generate a stream of instructions that describe changes between two subvolume snapshots. The stream can be consumed by the <code>btrfs receive</code> command to replicate the sent snapshot on a different filesystem. The command operates in two modes: full and incremental. </p>
<p> All snapshots involved in one send command must be read-only, and this status cannot be changed as long as there&#8217;s a running send operation that uses the snapshot. </p>
<p> In the full mode, the entire snapshot data and metadata will end up in the stream. </p>
<p> In the incremental mode (options <i>-p</i> and <i>-c</i>), previously sent snapshots that are available on both the sending and receiving side can be used to reduce the amount of information that has to be sent to reconstruct the sent snapshot on a different filesystem. </p>
<p> The <i>-p </i><i>&lt;parent&gt;</i> option can be omitted when <i>-c </i><i>&lt;clone-src&gt;</i> options are given, in which case <code>btrfs send</code> will determine a suitable parent from among the clone sources. </p>
<p> You must not specify clone sources unless you guarantee that these snapshots are exactly in the same state on both sides&#8212;both for the sender and the receiver. </p>
<p> <code>Options</code> </p>
<p> -e</p>
<dl>
<dd>if sending multiple subvolumes at once, use the new format and omit the <i>end cmd</i> marker in the stream separating the subvolumes</dl>
<p> -p <i>&lt;parent&gt;</i></p>
<dl>
<dd>send an incremental stream from <i>parent</i> to <i>subvol</i></dl>
<p> -c <i>&lt;clone-src&gt;</i></p>
<dl>
<dd>use this snapshot as a clone source for an incremental send (multiple allowed)</dl>
<p> -f <i>&lt;outfile&gt;</i></p>
<dl>
<dd>output is normally written to standard output so it can be, for example, piped to btrfs receive. Use this option to write it to a file instead.</dl>
<p> &#8211;no-data</p>
<dl>
<dd>send in <i>NO_FILE_DATA</i> mode </p>
<p> The output stream does not contain any file data and thus cannot be used to transfer changes. This mode is faster and is useful to show the differences in metadata.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>enable verbose output, print generated commands in a readable form, (each occurrence of this option increases the verbosity level)</dl>
<p> -q|&#8211;quiet</p>
<dl>
<dd>suppress all messages except errors</dl>
<h2>Exit Status</h2>
<p><code>btrfs send</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-receive/">btrfs-receive</a></code>(8) </p>

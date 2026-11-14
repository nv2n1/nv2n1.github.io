---
title: "btrfs-rescue(8)"
name: "btrfs-rescue"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrfs-rescue/"
description: "btrfs-rescue – Recover a damaged btrfs filesystem"
---

<p>btrfs-rescue &#8211; Recover a damaged btrfs filesystem</p>
<h2>Synopsis</h2>
<p><code>btrfs rescue</code> <i>&lt;subcommand&gt;</i> <i>&lt;args&gt;</i></p>
<h2>Description</h2>
<p><code>btrfs rescue</code> is used to try to recover a damaged btrfs filesystem.</p>
<h2>Subcommand</h2>
<p><code>chunk-recover</code> [options] <i>&lt;device&gt;</i></p>
<dl>
<dd>Recover the chunk tree by scanning the devices </p>
<p> <code>Options</code> </p>
<p> -y</p>
<dl>
<dd>assume an answer of <i>yes</i> to all questions.</dl>
<p> -v</p>
<dl>
<dd>verbose mode.</dl>
<p> -h</p>
<dl>
<dd>help.</dl>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Since <code>chunk-recover</code> will scan the whole device, it will be <code>VERY</code> slow especially executed on a large device. </p>
</dl>
<p> <code>fix-device-size</code> <i>&lt;device&gt;</i></p>
<dl>
<dd>fix device size and super block total bytes values that are do not match </p>
<p> Kernel 4.11 starts to check the device size more strictly and this might mismatch the stored value of total bytes. See the exact error message below. Newer kernel will refuse to mount the filesystem where the values do not match. This error is not fatal and can be fixed. This command will fix the device size values if possible. </p>
<dl>
<dd>
<pre>BTRFS error (device sdb): super_total_bytes 92017859088384 mismatch with fs_devices total_rw_bytes 92017859094528</pre>
</dl>
<p> The mismatch may also exhibit as a kernel warning: </p>
<dl>
<dd>
<pre>WARNING: CPU: 3 PID: 439 at fs/btrfs/ctree.h:1559 btrfs_update_device+0x1c5/0x1d0 [btrfs]</pre>
</dl>
</dl>
<p> <code>super-recover</code> [options] <i>&lt;device&gt;</i></p>
<dl>
<dd>Recover bad superblocks from good copies. </p>
<p> <code>Options</code> </p>
<p> -y</p>
<dl>
<dd>assume an answer of <i>yes</i> to all questions.</dl>
<p> -v</p>
<dl>
<dd>verbose mode.</dl>
</dl>
<p> <code>zero-log</code> <i>&lt;device&gt;</i></p>
<dl>
<dd>clear the filesystem log tree </p>
<p> This command will clear the filesystem log tree. This may fix a specific set of problem when the filesystem mount fails due to the log replay. See below for sample stacktraces that may show up in system log. </p>
<p> The common case where this happens was fixed a long time ago, so it is unlikely that you will see this particular problem, but the command is kept around. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 clearing the log may lead to loss of changes that were made since the last transaction commit. This may be up to 30 seconds (default commit period) or less if the commit was implied by other filesystem activity. </p>
</dl>
<p> One can determine whether <code>zero-log</code> is needed according to the kernel backtrace: </p>
<dl>
<dd>
<pre>? replay_one_dir_item+0xb5/0xb5 [btrfs]
? walk_log_tree+0x9c/0x19d [btrfs]
? btrfs_read_fs_root_no_radix+0x169/0x1a1 [btrfs]
? btrfs_recover_log_trees+0x195/0x29c [btrfs]
? replay_one_dir_item+0xb5/0xb5 [btrfs]
? btree_read_extent_buffer_pages+0x76/0xbc [btrfs]
? open_ctree+0xff6/0x132c [btrfs]</pre>
</dl>
<p> If the errors are like above, then <code>zero-log</code> should be used to clear the log and the filesystem may be mounted normally again. The keywords to look for are <i>open_ctree</i> which says that it&#8217;s during mount and function names that contain <i>replay</i>, <i>recover</i> or <i>log_tree</i>.</dl>
<h2>Exit Status</h2>
<p><code>btrfs rescue</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>Availability</h2>
<p><code>btrfs</code> is part of btrfs-progs. Please refer to the btrfs wiki m[blue]<code><a rel="nofollow" href="http://btrfs.wiki.kernel.org">http://btrfs.wiki.kernel.org</a></code>m[] for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-btrfs/">mkfs.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-scrub/">btrfs-scrub</a></code>(8), <code><a href="/docs/linux/man/8-btrfs-check/">btrfs-check</a></code>(8) </p>

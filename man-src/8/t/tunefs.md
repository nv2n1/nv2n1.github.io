---
title: "tunefs(8)"
name: "tunefs"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tunefs/"
description: "tunefs.ocfs2 – Change OCFS2 file system parameters."
---

<p>tunefs.ocfs2 &#8211; Change <i>OCFS2</i> file system parameters.</p>
<h2>Synopsis</h2>
<p><code>tunefs.ocfs2</code> [<code>&#8211;cloned-volume</code>[=<i>new-label</i>] [<code>&#8211;fs-features=</code><i>list-of-features</i>] [<code>-J</code> <i>journal-options</i>] [<code>-L</code> <i>volume-label</i>] [<code>-N</code> <i>number-of-node-slots</i>] [<code>-Q</code> <i>query-format</i>] [<code>-ipqnSUvVy</code>] [<code>&#8211;backup-super</code>] [<code>&#8211;list-sparse</code>] <i>device</i> [<i>blocks-count</i>] </p>
<h2>Description</h2>
<p><code>tunefs.ocfs2</code> is used to adjust <i>OCFS2</i> file system parameters on disk. The tool expects the cluster to be online as it needs to take the appropriate cluster locks to write safely to disk. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;cloned-volume</code>[=<i>new-label]</i></p>
<dd>Change the volume UUID (auto-generated) and the label, if provided, of a cloned <i>OCFS2</i> volume. This option does <code>not</code> perform volume cloning. It only changes the UUID and label on a cloned volume so that it can be mounted on the node that has the original volume mounted. </p>
<dt><code>&#8211;fs-features=</code><i>[no]sparse&#8230;</i></p>
<dd>Turn specific file system features on or off. <i>tunefs.ocfs2</i> will attempt to enable or disable the feature list provided. To enable a feature, include it in the list. To disable a feature, prepend <code>no</code> to the name. For a list of feature names, see the man page for <code>mkfs.ocfs2</code>. </p>
<dt><code>-J, &#8211;journal-options</code> <i>options</i></p>
<dd>Modify the journal using options specified on the command-line. Journal options are comma separated, and may take an argument using the equals (&#8216;=&#8217;) sign. For a list of possible options, see the man page for <code>mkfs.ocfs2</code>. </p>
<dt><code>-L, &#8211;label</code> <i>volume-label</i></p>
<dd>Change the volume label of the file system. Limit the label to under 64 bytes. </p>
<dt><code>-N, &#8211;node-slots</code> <i>number-of-node-slots</i></p>
<dd>Valid number ranges from 1 to 255. This number specifies the maximum number of nodes that can concurrently mount the partition. Use this to increase or decrease the number of node slots. One reason to decrease could be to release the space consumed by the journals for those slots. </p>
<dt><code>-S, &#8211;volume-size</code></p>
<dd>Grow the size of the <i>OCFS2</i> file system. If <i>blocks-count</i> is not specified, <i>tunefs.ocfs2</i> extends the volume to the current size of the device. </p>
<dt><code>-Q, &#8211;query</code> <i>query-format</i></p>
<dd>Query the file system for its attributes like block size, label, etc. Query formats are modified versions of the standard <a href="/docs/linux/man/3-printf/">printf</a>(3) formatting. The format is made up of static strings (which may include standard C character escapes for newlines, tabs, and other special characters) and <a href="/docs/linux/man/3-printf/">printf</a>(3) type formatters. The list of type specifiers is as follows:</p>
<dl>
<dd>
<dl>
<dt><code>B</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Block size in bytes</p>
<dd>
<dt><code>T</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Cluster size in bytes</p>
<dd>
<dt><code>N</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Number of node slots</p>
<dd>
<dt><code>R</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Root directory block number</p>
<dd>
<dt><code>Y</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>System directory block number</p>
<dd>
<dt><code>P</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>First cluster group block number</p>
<dd>
<dt><code>V</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Volume label</p>
<dd>
<dt><code>U</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Volume uuid</p>
<dd>
<dt><code>M</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Compat flags</p>
<dd>
<dt><code>H</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Incompat flags</p>
<dd>
<dt><code>O</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>RO Compat flags</p>
<dd></dl>
</dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Quiet mode. </p>
<dt><code>-U, &#8211;uuid-reset</code></p>
<dd>Change the volume UUID (auto-generated) for the file system. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Verbose mode. </p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show version and exit. </p>
<dt><code>-y, &#8211;yes</code></p>
<dd>Always answer Yes in interactive command line. </p>
<dt><code>-n, &#8211;no</code></p>
<dd>Always answer No in interactive command line. </p>
<dt><code>&#8211;backup-super</code></p>
<dd>Backs up the superblock to fixed offsets (1G, 4G, 16G, 64G, 256G and 1T) on disk. This option is useful for users to backup the superblock on volumes that the user either explicitly disallowed while formatting, or, used a version of <i>mkfs.ocfs2</i> (1.2.2 or older) that did not provide this facility. </p>
<dt><code>&#8211;list-sparse</code></p>
<dd>Lists the files having holes. This option is useful when disabling the <i>sparse</i> feature. </p>
<dt><code>&#8211;update-cluster-stack</code></p>
<dd>Updating on-disk cluster information to match the running cluster. </p>
<dt><i>blocks-count</i></p>
<dd>During resize, <i>tunefs.ocfs2</i> automatically determines the size of the given device and grows the file system such that it uses all of the available space on the device. This optional argument specifies that the file system should be extended to consume only the given number of file system blocks on the device. </p>
</dl>
<h2>Examples</h2>
<p>[root [at] node1 ~]# tunefs.ocfs2 -Q &quot;UUID = %U
NumSlots = %N
&quot; /dev/sda1<br />
 UUID = CBB8D5E0C169497C8B52A0FD555C7A3E<br />
 NumSlots = 4 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-ocfs2/">mkfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-fsck-ocfs2/">fsck.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-debugfs-ocfs2/">debugfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-mounted-ocfs2/">mounted.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-ocfs2console/">ocfs2console</a>(8)</code> <code><a href="/docs/linux/man/7-o2cb/">o2cb</a>(7)</code> </p>
<h2>Authors</h2>
<p>Oracle Corporation</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2009 Oracle. All rights reserved.</p>

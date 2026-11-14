---
title: "mounted(8)"
name: "mounted"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mounted/"
description: "mounted.ocfs2 – Detects all OCFS2 volumes on a system."
---

<p>mounted.ocfs2 &#8211; Detects all <i>OCFS2</i> volumes on a system.</p>
<h2>Synopsis</h2>
<p><code>mounted.ocfs2</code> [<code>-d</code>] [<code>-f</code>] [<i>device</i>]</p>
<h2>Description</h2>
<p><code>mounted.ocfs2</code> is used to detect <i>OCFS2</i> volume(s) on a system. This tool assumes that the nodes detected on the system are part of the same cluster as the one specified in <i>/etc/ocfs2/cluster.conf</i>. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Lists the <i>OCFS2</i> volumes along with their labels and uuids. If a device is not specified, it scans all the devices in /proc/partitions. </p>
<dt><code>-f</code></p>
<dd>Lists the <i>OCFS2</i> volumes along with the list of nodes that have mounted the volume. The node names are listed if the <i>O2CB</i> cluster is online. <code>Note:</code> As this information is gathered using dirty-read, the information may be stale. </p>
</dl>
<h2>Examples</h2>
<p>[root [at] node1 ~]# mounted.ocfs2 -d<br />
 Device FS UUID Label<br />
 /dev/sdb1 ocfs2 26d5dcdf-6d87-45a7-b01a-b98a7791bd61 logs_0405<br />
 [root [at] node1 ~]# mounted.ocfs2 -f<br />
 Device FS Nodes<br />
 /dev/sdb1 ocfs2 node15, node1 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-ocfs2/">mkfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-fsck-ocfs2/">fsck.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-tunefs-ocfs2/">tunefs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-debugfs-ocfs2/">debugfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-ocfs2console/">ocfs2console</a>(8)</code> <code><a href="/docs/linux/man/7-o2cb/">o2cb</a>(7)</code> </p>
<h2>Authors</h2>
<p>Oracle Corporation</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2009 Oracle. All rights reserved.</p>

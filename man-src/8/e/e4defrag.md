---
title: "e4defrag(8)"
name: "e4defrag"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e4defrag/"
description: "e4defrag – online defragmenter for ext4 file system"
---

<p>e4defrag &#8211; online defragmenter for ext4 file system</p>
<h2>Synopsis</h2>
<p><code>e4defrag</code> [ <code>-c</code> ] [ <code>-v</code> ] <i>target</i> &#8230;</p>
<h2>Description</h2>
<p><code>e4defrag</code> reduces fragmentation of extent based file. The file targeted by <code>e4defrag</code> is created on ext4 file system made with &quot;-O extent&quot; option (see <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8)). The targeted file gets more contiguous blocks and improves the file access speed. </p>
<p> <i>target</i> is a regular file, a directory, or a device that is mounted as ext4 file system. If <i>target</i> is a directory, <code>e4defrag</code> reduces fragmentation of all files in it. If <i>target</i> is a device, <code>e4defrag</code> gets the mount point of it and reduces fragmentation of all files in this mount point.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Get a current fragmentation count and an ideal fragmentation count, and calculate fragmentation score based on them. By seeing this score, we can determine whether we should execute <code>e4defrag</code> to <i>target</i>. When used with <code>-v</code> option, the current fragmentation count and the ideal fragmentation count are printed for each file.</p>
<dd>Also this option outputs the average data size in one extent. If you see it, you&#8217;ll find the file has ideal extents or not. Note that the maximum extent size is 131072KB in ext4 file system (if block size is 4KB).</p>
<dd>If this option is specified, <i>target</i> is never defragmented.</p>
<dt><code>-v</code></p>
<dd>Print error messages and the fragmentation count before and after defrag for each file.</dl>
<h2>Notes</h2>
<p><code>e4defrag</code> does not support swap file, files in lost+found directory, and files allocated in indirect blocks. When <i>target</i> is a device or a mount point, <code>e4defrag</code> doesn&#8217;t defragment files in mount point of other device. </p>
<p> It is safe to run e4defrag on a file while it is actively in use by another application. Since the contents of file blocks are copied using the page cache, this can result in a performance slowdown to both e4defrag and the application due to contention over the system&#8217;s memory and disk bandwidth. </p>
<p> If the file system&#8217;s free space is fragmented, or if there is insufficient free space available, e4defrag may not be able to improve the file&#8217;s fragmentation. </p>
<p> Non-privileged users can execute <code>e4defrag</code> to their own file, but the score is not printed if <code>-c</code> option is specified. Therefore, it is desirable to be executed by root user.</p>
<h2>Author</h2>
<p>Written by Akira Fujita &lt;a-fujita [at] rs.jp.nec.com&gt; and Takashi Sato &lt;t-sato [at] yk.jp.nec.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>

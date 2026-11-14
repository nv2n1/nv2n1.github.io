---
title: "xfs_logprint(8)"
name: "xfs_logprint"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_logprint/"
description: "xfs_logprint – print the log of an XFS filesystem"
---

<p>xfs_logprint &#8211; print the log of an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_logprint</code> [ <i>options</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>xfs_logprint</code> prints the log of an XFS filesystem (see <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5)). The <i>device</i> argument is the pathname of the partition or logical volume containing the filesystem. The <i>device</i> can be a regular file if the <code>-f</code> option is used. The contents of the filesystem remain undisturbed. There are two major modes of operation in <code>xfs_logprint</code>. </p>
<p> One mode is better for filesystem operation debugging. It is called the transactional view and is enabled through the <code>-t</code> option. The transactional view prints only the portion of the log that pertains to recovery. In other words, it prints out complete transactions between the tail and the head. This view tries to display each transaction without regard to how they are split across log records. </p>
<p> The second mode starts printing out information from the beginning of the log. Some error blocks might print out in the beginning because the last log record usually overlaps the oldest log record. A message is printed when the physical end of the log is reached and when the logical end of the log is reached. A log record view is displayed one record at a time. Transactions that span log records may not be decoded fully.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Extract and print buffer information. Only used in transactional view.</p>
<dt><code>-c</code></p>
<dd>Attempt to continue when an error is detected.</p>
<dt><code>-C</code><i> filename</i></p>
<dd>Copy the log from the filesystem to the file <i>filename</i>. The log itself is not printed.</p>
<dt><code>-d</code></p>
<dd>Dump the log from front to end, printing where each log record is located on disk.</p>
<dt><code>-D</code></p>
<dd>Do not decode anything; just print data.</p>
<dt><code>-e</code></p>
<dd>Exit when an error is found in the log. Normally, <code>xfs_logprint</code> tries to continue and unwind from bad logs. However, sometimes it just dies in bad ways. Using this option prevents core dumps.</p>
<dt><code>-f</code></p>
<dd>Specifies that the filesystem image to be processed is stored in a regular file at <i>device</i> (see the <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8) <code>-d</code> <i>file</i> option). This might happen if an image copy of a filesystem has been made into an ordinary file with <code><a href="/docs/linux/man/8-xfs_copy/">xfs_copy</a></code>(8).</p>
<dt><code>-l</code><i> logdev</i></p>
<dd>External log device. Only for those filesystems which use an external log.</p>
<dt><code>-i</code></p>
<dd>Extract and print inode information. Only used in transactional view.</p>
<dt><code>-q</code></p>
<dd>Extract and print quota information. Only used in transactional view.</p>
<dt><code>-n</code></p>
<dd>Do not try and interpret log data; just interpret log header information.</p>
<dt><code>-o</code></p>
<dd>Also print buffer data in hex. Normally, buffer data is just decoded, so better information can be printed.</p>
<dt><code>-s</code><i> start-block</i></p>
<dd>Override any notion of where to start printing.</p>
<dt><code>-t</code></p>
<dd>Print out the transactional view.</p>
<dt><code>-v</code></p>
<dd>Print &quot;overwrite&quot; data.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>

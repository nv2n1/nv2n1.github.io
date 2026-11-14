---
title: "jfs_mkfs(8)"
name: "jfs_mkfs"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jfs_mkfs/"
description: "jfs_mkfs – create a JFS formatted partition"
---

<p><code>jfs_mkfs</code> &#8211; create a JFS formatted partition</p>
<h2>Synopsis</h2>
<p><code>jfs_mkfs</code> [options] <i>device</i> [ blocks ] </p>
<h2>Description</h2>
<p><code>jfs_mkfs</code> is used to create (format) a JFS partition. <code>jfs_mkfs</code> must be run as root. <i>device</i> is the special file name corresponding to the actual device (e.g.<i> /dev/hdb1</i>) on which a JFS file system and/or JFS journal will be created. <i>blocks</i> is the number of blocks to be used for the file system. If omitted, <code>jfs_mkfs</code> automatically figures the file system size. The default block size is <code>4096</code>. </p>
<h2>Warning</h2>
<p><code>jfs_mkfs</code> will destroy all data on the specified device!</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Check the device for bad blocks before building the file system. </p>
<dt><code>-j</code><i> journal_device</i></p>
<dd>Create the external JFS journal on <i>journal_device</i> , create the JFS file system on <i>device</i> , and attach the external journal to the file system. </p>
<dt><code>-J</code><i> journal-options</i></p>
<dd>Create the JFS journal on its own device or attach an external JFS journal to the JFS file system using options specified on the command-line. The following journal options are supported:</p>
<dl>
<dd>
<dl>
<dt><code>journal_dev</code></p>
<dd>Create an external JFS journal on the given device.</p>
<dt><code>device=</code><i>external-journal</i></p>
<dd>Attach an existing external JFS journal located on <i>external-journal</i> to the JFS file system that will be created on <i>device</i>. The external journal must already have been created using the command</p>
<dd><code>jfs_mkfs -J journal_dev</code> <i>external-journal</i></p>
<dd>Attach the external journal to the file system being created by using the command</p>
<dd><code>jfs_mkfs -J device=external-journal</code> <i>device</i></p>
<dd>Instead of specifying a device name directly, <i>external-journal</i> can also be specified by either <code>LABEL=</code><i>label</i> or <code>UUID=</code><i>UUID</i> to locate the external journal by either the volume label or UUID stored in the JFS external log superblock at the start of the journal. Use <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8) to display a journal device&#8217;s volume label and UUID. (See the <code>-l</code>, <code>-L</code>, and <code>-U</code> options of <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8).)</dl>
</dl>
<dd>Only one of the <code>journal_dev</code> or <code>device=</code> options can be given per <code>jfs_mkfs</code> issuance. </p>
<dt><code>-L</code><i> volume_label</i></p>
<dd>Set the volume label for the newly formatted device.</p>
<dd>If <code>-L</code><i> volume_label</i> is used along with <code>-J journal_device</code>, the volume label of the specified external journal device will be set to <i>volume_label</i>. Otherwise, the volume label of the JFS file system will be set to <i>volume_label</i>. </p>
<dt><code>-O</code></p>
<dd>Provide case-insensitive support for compatibility with OS/2. </p>
<dt><code>-q</code></p>
<dd>Quiet execution &#8211; do not ask for confirmation before creating the file system. </p>
<dt><code>-s</code><i> log_size</i></p>
<dd>Set the log size (in megabytes) of the inline log. If the <code>-s</code> option is not used, the default log size is 0.4% of the aggregate size. </p>
<dt><code>-V</code></p>
<dd>Print version information and exit (regardless of any other chosen options). </p>
</dl>
<h2>Examples</h2>
<p>Format 3rd partition on 2nd hard disk with the volume label &quot;JFS_hdb3&quot;:</p>
<dl>
<dd><code>jfs_mkfs -L JFS_hdb3 /dev/hdb3</code></p>
<dd></dl>
<p> Format 5th partition on 1st hard disk, verifying each block created:</p>
<dl>
<dd><code>jfs_mkfs -c /dev/hda5</code></p>
<dd></dl>
<p> Format 3rd partition on 2nd hard disk as external journal, format 4th partition on 1st hard disk as JFS file system, and attach the external journal to the file system:</p>
<dl>
<dd><code>jfs_mkfs -j /dev/hdb3 /dev/hda4</code></p>
<dd>
<h2>Reporting Bugs</h2>
<p>If you find a bug in <code>JFS</code> or <code>jfs_mkfs</code>, please report it via the bug tracking system (&quot;Report Bugs&quot; section) of the JFS project web site: </p>
<pre><a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
<p>Please send as much pertinent information as possible including any error messages resulting from running <code>jfs_mkfs</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_fsck/">jfs_fsck</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_fscklog/">jfs_fscklog</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_logdump/">jfs_logdump</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_debugfs/">jfs_debugfs</a></code>(8) </p>
<h2>Authors</h2>
<pre>Barry Arndt (barndt [at] us.ibm.com)
William Braswell, Jr.</pre>
<p><code>jfs_mkfs</code> is maintained by IBM. </p>
<pre>See the JFS project web site for more details:
<a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>

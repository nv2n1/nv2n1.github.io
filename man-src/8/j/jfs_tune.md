---
title: "jfs_tune(8)"
name: "jfs_tune"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jfs_tune/"
description: "jfs_tune – adjust tunable file system parameters on JFS"
---

<p><code>jfs_tune</code> &#8211; adjust tunable file system parameters on JFS</p>
<h2>Synopsis</h2>
<p><code>jfs_tune</code> [options] <i>device</i> </p>
<h2>Description</h2>
<p><code>jfs_tune</code> adjusts tunable parameters on a Linux JFS file system or external journal. <code>jfs_tune</code> must be run as root. <i>device</i> is the special file name corresponding to the actual device (e.g.<i> /dev/hdb1</i>) on which a JFS file system or JFS external journal has been created. </p>
<h2>Options</h2>
<dl>
<dt><code>-J device=external-journal</code></p>
<dd>Attach the JFS external journal located on <i>external-journal</i> to the JFS file system on <i>device</i>.</p>
<dd>The external journal must already have been created using the command. More than one file system may share the same external journal.</p>
<dd><code>mkfs.jfs -J journal_dev</code> <i>external-journal</i></p>
<dd>Attach the external journal to the file system by using the command</p>
<dd><code>jfs_tune -J device=external-journal</code> <i>device</i></p>
<dd>Instead of specifying a device name directly, <i>external-journal</i> can also be specified by either <code>LABEL=</code><i>label</i> or <code>UUID=</code><i>UUID</i> (Use <code>jfs_tune -l device</code> to display a journal device&#8217;s volume label and UUID.) </p>
<dt><code>-l</code></p>
<dd>List the contents of the JFS file system or external journal superblock that resides on <i>device</i>. </p>
<dt><code>-L</code><i> volume-label</i></p>
<dd>Set the volume label of the JFS file system or external journal. JFS labels can be at most 16 characters long; if <i>volume-label</i> is longer than 16 characters, <code>jfs_tune</code> will truncate it and print a warning. The volume label can be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), and <code>/etc/<a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) (and possibly others) by specifying <code>LABEL=</code><i>volume_label</i> instead of a block special device name like <code>/dev/hda5</code>. </p>
<dt><code>-U</code><i> UUID</i></p>
<dd>Set the universally unique identifier (UUID) of the file system or external journal device to <i>UUID</i>. The format of the UUID is a series of hex digits separated by hyphens, like this: &quot;c1b9d5a2-f162-11cf-9ece-0020afc76f16&quot;. The <i>UUID</i> parameter may also be one of the following:</p>
<dl>
<dd>
<dl>
<dt><i>clear</i></p>
<dd>clear the file system UUID</p>
<dt><i>random</i></p>
<dd>generate a new randomly-generated UUID</p>
<dt><i>time</i></p>
<dd>generate a new time-based UUID</dl>
</dl>
<dd>The UUID may be used by <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), and <code>/etc/<a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) (and possibly others) by specifying <code>UUID=</code><i>uuid</i> instead of a block special device name like <code>/dev/hda1</code>.</p>
<dd>See <code><a href="/docs/linux/man/8-uuidgen/">uuidgen</a></code>(8) for more information. </p>
<dt><code>-V</code></p>
<dd>Print version information and exit (regardless of any other chosen options). </p>
</dl>
<h2>Examples</h2>
<p>Set a randomly-generated UUID for the JFS file system on the 3rd partition of the 2nd hard disk, and view the resultant superblock:</p>
<dl>
<dd><code>jfs_tune -l -U random /dev/hdb3</code></p>
<dd> Attach an already existing external journal on a device labeled JFSLog to a JFS file system on /dev/hda8:</p>
<dl>
<dd><code>jfs_tune -J device=LABEL=JFSLog /dev/hda8</code></p>
<dd>
<h2>Reporting Bugs</h2>
<p>If you find a bug in <code>JFS</code> or <code>jfs_tune</code>, please report it via the bug tracking system (&quot;Report Bugs&quot; section) of the JFS project web site: </p>
<pre><a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
<p>Please send as much pertinent information as possible including any error messages resulting from running <code>jfs_tune</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jfs_fsck/">jfs_fsck</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_mkfs/">jfs_mkfs</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_fscklog/">jfs_fscklog</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_logdump/">jfs_logdump</a></code>(8)<code>,</code> <code><a href="/docs/linux/man/8-jfs_debugfs/">jfs_debugfs</a></code>(8) </p>
<h2>Author</h2>
<pre>Barry Arndt (barndt [at] us.ibm.com)</pre>
<p><code>jfs_tune</code> is maintained by IBM. </p>
<pre>See the JFS project web site for more details:
<a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>

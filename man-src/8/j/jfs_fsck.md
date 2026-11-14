---
title: "jfs_fsck(8)"
name: "jfs_fsck"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jfs_fsck/"
description: "jfs_fsck – initiate replay of the JFS transaction log, and check and repair a JFS formatted device"
---

<p><code>jfs_fsck</code> &#8211; initiate replay of the JFS transaction log, and check and repair a JFS formatted device</p>
<h2>Synopsis</h2>
<p><code>jfs_fsck</code> [ <code>-afnpvV</code> ] [ <code>-j</code> <i>journal_device</i> ] [ <code>&#8211;omit_journal_replay</code> ] [ <code>&#8211;replay_journal_only</code> ] <i>device</i> </p>
<h2>Description</h2>
<p><code>jfs_fsck</code> is used to replay the JFS transaction log, check a JFS formatted device for errors, and fix any errors found. <i>device</i> is the special file name corresponding to the actual device to be checked (e.g.<code> /dev/hdb1</code>). <code>jfs_fsck</code> must be run as root. </p>
<h2>Warning</h2>
<p><code>jfs_fsck</code> should only be used to check an <code>unmounted</code> file system or a file system that is mounted READ ONLY. Using <code>jfs_fsck</code> to check a file system mounted other than READ ONLY could seriously damage the file system!</p>
<h2>Options</h2>
<p>If no options are selected, the default is <code>-p.</code></p>
<dl>
<dt><code>-a</code></p>
<dd>Autocheck mode &#8211; Replay the transaction log. Do not continue fsck processing unless the aggregate state is dirty or the log replay failed. Functionally equivalent to <code>-p.</code> Autocheck mode is typically the default mode used when <code>jfs_fsck</code> is called at boot time.</p>
<dt><code>-f</code></p>
<dd>Replay the transaction log and force checking even if the file system appears clean. Repair all problems automatically.</p>
<dt><code>-j</code><i> journal_device</i></p>
<dd>Specify the journal device.</p>
<dt><code>-n</code></p>
<dd>Open the file system read only. Do not replay the transaction log. Report errors, but do not repair them.</p>
<dt><code>&#8211;omit_journal_replay</code></p>
<dd>Omit the replay of the transaction log. This option should not be used unless as a last resort (i.e. the log has been severely corrupted and replaying it causes further problems).</p>
<dt><code>-p</code></p>
<dd>Automatically repair (&quot;preen&quot;) the file system. Replay the transaction log. Do not continue fsck processing unless the aggregate state is dirty or the log replay failed. Functionally equivalent to <code>-a.</code></p>
<dt><code>&#8211;replay_journal_only</code></p>
<dd>Only replay the transaction log. Do not continue with a full file system check if the replay fails or if the file system is still dirty even after a journal replay. In general, this option should only be used for debugging purposes as it could leave the file system in an unmountable state. This option cannot be used with <code>-f</code>, <code>-n</code>, or <code>&#8211;omit_journal_replay</code>.</p>
<dt><code>-v</code></p>
<dd>Verbose messaging &#8211; print details and debug statements to stdout.</p>
<dt><code>-V</code></p>
<dd>Print version information and exit (regardless of any other chosen options).</dl>
<h2>Examples</h2>
<p>Check the 3rd partition on the 2nd hard disk, print extended information to stdout, replay the transaction log, force complete jfs_fsck checking, and give permission to repair all errors:</p>
<dl>
<dd><code>jfs_fsck -v -f /dev/hdb3</code></p>
<dd></dl>
<p> Check the 5th partition on the 1st hard disk, and report, but do not repair, any errors:</p>
<dl>
<dd><code>jfs_fsck -n /dev/hda5</code></p>
<dd>
<h2>Exit Code</h2>
<p>The exit code returned by <code>jfs_fsck</code> represents one of the following conditions:</p>
<dl>
<dt><code>&nbsp;<wbr>0</code></p>
<dd>No errors</p>
<dt><code>&nbsp;<wbr>1</code></p>
<dd>File system errors corrected and/or transaction log replayed successfully</p>
<dt><code>&nbsp;<wbr>2</code></p>
<dd>File system errors corrected, system should be rebooted if file system was mounted</p>
<dt><code>&nbsp;<wbr>4</code></p>
<dd>File system errors left uncorrected</p>
<dt><code>&nbsp;<wbr>8</code></p>
<dd>Operational error</p>
<dt><code>&nbsp;<wbr>16</code></p>
<dd>Usage or syntax error</p>
<dt><code>&nbsp;<wbr>128</code></p>
<dd>Shared library error </p>
</dl>
<h2>Reporting Bugs</h2>
<p>If you find a bug in <code>JFS</code> or <code>jfs_fsck</code>, please report it via the bug tracking system (&quot;Report Bugs&quot; section) of the JFS project web site: </p>
<pre><a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
<p>Please send as much pertinent information as possible, including the complete output of running <code>jfs_fsck</code> with the <code>-v</code> option on the JFS device.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-jfs_mkfs/">jfs_mkfs</a></code>(8), <code><a href="/docs/linux/man/8-jfs_fscklog/">jfs_fscklog</a></code>(8), <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8), <code><a href="/docs/linux/man/8-jfs_logdump/">jfs_logdump</a></code>(8), <code><a href="/docs/linux/man/8-jfs_debugfs/">jfs_debugfs</a></code>(8) </p>
<h2>Authors</h2>
<pre>Barry Arndt (barndt [at] us.ibm.com)
William Braswell, Jr.</pre>
<p><code>jfs_fsck</code> is maintained by IBM. </p>
<pre>See the JFS project web site for more details:
<a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>

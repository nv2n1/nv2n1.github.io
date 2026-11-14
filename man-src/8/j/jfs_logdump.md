---
title: "jfs_logdump(8)"
name: "jfs_logdump"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jfs_logdump/"
description: "jfs_logdump – dump a JFS formatted device’s journal log"
---

<p><code>jfs_logdump</code> &#8211; dump a JFS formatted device&#8217;s journal log</p>
<h2>Synopsis</h2>
<p><code>jfs_logdump [ -a ]</code> <i>device</i> </p>
<h2>Description</h2>
<p><code>jfs_logdump</code> dumps the contents of the journal log from the specified JFS formatted device into output file <i>./jfslog.dmp</i>. <i>device</i> is the special file name corresponding to the actual device from which the journal log will be dumped (e.g. <code>/dev/hdb1</code> ). <code>jfs_logdump</code> must be run as root. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Dump the entire contents of the journal log instead of just the committed transactions since the last synch point. </p>
</dl>
<h2>Example</h2>
<p>Dump the entire JFS journal log from the 3rd partition of the 2nd hard disk into <i>./jfslog.dmp</i>:</p>
<dl>
<dd><code>jfs_logdump -a /dev/hdb3</code></p>
<dd>
<h2>Reporting Bugs</h2>
<p>If you find a bug in <code>JFS</code> or <code>jfs_logdump</code>, please report it via the bug tracking system (&quot;Report Bugs&quot; section) of the JFS project web site: </p>
<pre><a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
<p>Please send as much pertinent information as possible, including any <code>jfs_logdump</code> error messages and the complete output of running <code>jfs_fsck</code> with the <code>-v</code> option on the JFS device.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jfs_fsck/">jfs_fsck</a></code>(8), <code><a href="/docs/linux/man/8-jfs_mkfs/">jfs_mkfs</a></code>(8), <code><a href="/docs/linux/man/8-jfs_fscklog/">jfs_fscklog</a></code>(8), <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8), <code><a href="/docs/linux/man/8-jfs_debugfs/">jfs_debugfs</a></code>(8) </p>
<h2>Authors</h2>
<pre>Barry Arndt (barndt [at] us.ibm.com)
William Braswell, Jr.</pre>
<p><code>jfs_logdump</code> is maintained by IBM. </p>
<pre>See the JFS project web site for more details:
<a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>

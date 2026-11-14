---
title: "jfs_fscklog(8)"
name: "jfs_fscklog"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jfs_fscklog/"
description: "jfs_fscklog – extract a JFS fsck service log into a file and/or format and display the extracted file"
---

<p><code>jfs_fscklog</code> &#8211; extract a JFS fsck service log into a file and/or format and display the extracted file</p>
<h2>Synopsis</h2>
<p><code>jfs_fscklog</code> [ <code>-d</code> ] [ <code>-e</code><i> device</i> ] [ <code>-f</code><i> output.file</i> ] [ <code>-p</code> ] [ <code>-V</code> ] </p>
<h2>Description</h2>
<p><code>jfs_fscklog</code> with option <code>-e</code><i> device</i> extracts the contents of either the most recent or immediately prior (specified with option <code>-p</code>) JFS fsck service log from the specified device, and writes the output to a file. The file name may be specified with the <code>-f</code> option, or the default file name is <i>&lt;pwd&gt;fscklog.new</i>. If the <code>-p</code> option is used, the default file name is <i>&lt;pwd&gt;fscklog.old</i>. <code>jfs_fscklog</code> with option <code>-d</code> formats and displays the contents of the extracted file. <code>jfs_fscklog</code> with options <code>-d</code> and <code>-e</code><i> device</i> extracts and displays the JFS fsck service log. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Format and display a previously extracted JFS fsck service log.</p>
<dt><code>-e</code><i> device</i></p>
<dd>Extract the JFS fsck service log from <i>device</i> and store it in a file. (<i>device</i> is the special file name corresponding to the actual device from which the fsck log will be extracted (e.g. <code>/dev/hdb1</code> )).</p>
<dt><code>-f</code><i> file.name</i></p>
<dd>Specify the file name, overriding the default file name. When used with <code>-e</code> <i>device</i>, file.name specifies the name of the file into which the JFS fsck log will be extracted. When used with <code>-d</code>, file.name specifies the name of the extracted file whose contents will be formatted and displayed.</p>
<dl>
<dd><i>file.name</i> must be 127 characters or less in length. </p>
<p> <i>file.name</i> will be created in the present working directory unless it is fully qualified.</dl>
<dt><code>-p</code></p>
<dd>Extract the prior log (as opposed to the most recent log).</p>
<dt><code>-V</code></p>
<dd>Print version information and exit (regardless of any other chosen options).</dl>
<h2>Examples</h2>
<p>&nbsp;<wbr>Extract the most recent JFS fsck log on&nbsp;<wbr>/dev/hda5 into <i>&lt;pwd&gt;fscklog.new</i>:</p>
<dl>
<dd><code>jfs_fscklog -e /dev/hda5</code></p>
<dd></dl>
<p> Extract the most recent JFS fsck log on /dev/hdb3 into <i>/temp/l9651107.log</i>:</p>
<dl>
<dd><code>jfs_fscklog -e /dev/hdb3 -f /temp/l9651107.log</code></p>
<dd></dl>
<p> Display the JFS fsck log that was extracted into <i>/temp/l9651107.log</i>:</p>
<dl>
<dd><code>jfs_fscklog -d -f /temp/l9651107.log</code></p>
<dd></dl>
<p> Extract and display the previous JFS fsck log from /dev/hda8:</p>
<dl>
<dd><code>jfs_fscklog -e /dev/hda8 -d -p</code></p>
<dd>
<h2>Reporting Bugs</h2>
<p>If you find a bug in <code>JFS</code> or <code>jfs_fscklog,</code> please report it via the bug tracking system (&quot;Report Bugs&quot; section) of the JFS project web site: </p>
<pre><a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
<p>Please send as much pertinent information as possible, including any <code>jfs_fscklog</code> error messages and the complete output of running <code>jfs_fsck</code> with the <code>-v</code> option on the JFS device.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jfs_fsck/">jfs_fsck</a></code>(8), <code><a href="/docs/linux/man/8-jfs_mkfs/">jfs_mkfs</a></code>(8), <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8), <code><a href="/docs/linux/man/8-jfs_logdump/">jfs_logdump</a></code>(8), <code><a href="/docs/linux/man/8-jfs_debugfs/">jfs_debugfs</a></code>(8) </p>
<h2>Author</h2>
<pre>Barry Arndt (barndt [at] us.ibm.com)</pre>
<p><code>jfs_fscklog</code> is maintained by IBM. </p>
<pre>See the JFS project web site for more details:
<a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>

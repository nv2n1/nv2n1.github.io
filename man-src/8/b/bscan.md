---
title: "bscan(8)"
name: "bscan"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bscan/"
description: "bscan – Bacula’s ‘Scan tape’"
---

<p>&nbsp;<wbr>bscan &#8211; Bacula&#8217;s&nbsp;<wbr>&#8216;Scan tape&#8217;</p>
<h2>Synopsis</h2>
<p><code>bscan</code> [<i>options</i>] <i>bacula-archive</i></p>
<h2>Description</h2>
<p>The purpose of bscan is to read (scan) a Bacula Volume and to recreate or update the database contents with the information found on the Volume. This is done in a non-destructive way. This permits restoring database entries that have been lost by pruning, purging, deleting, or a database corruption problem.<br />
&nbsp;<wbr> Normally, it should not be necessary to run the bscan command because the database is self maintaining, and most corrupted databases can be repaired by the tools provided by the database vendors. In addition, if you have maintained bootstrap files during backups, you should be able to recover all your data from the bootstrap file without needed an up to date catalog. <code>bscan</code> command. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></p>
<dd>Show version and usage of program.</p>
<dt><code>-b&nbsp;<wbr></code><i>bootstrap</i></p>
<dd>Specify a bootstrap file.</p>
<dt><code>-c&nbsp;<wbr></code><i>config</i></p>
<dd>Specify configuration file.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd>Set debug level to <i>nn</i>.</p>
<dt><code>-dt</code></p>
<dd>Print timestamp in debug output.</p>
<dt><code>-m</code></p>
<dd>Update media info in database.</p>
<dt><code>-D</code></p>
<dd>Specify the driver database name (default: <i>NULL</i>)</p>
<dt><code>-n&nbsp;<wbr></code><i>name</i></p>
<dd>Specify the database name (default: <i>bacula</i>)</p>
<dt><code>-u&nbsp;<wbr></code><i>username</i></p>
<dd>Specify database username (default: <i>bacula</i>)</p>
<dt><code>-P&nbsp;<wbr></code><i>password</i></p>
<dd>Specify database password (default: <i>none</i>)</p>
<dt><code>-h&nbsp;<wbr></code><i>host</i></p>
<dd>Specify database host (default: <i>NULL</i>)</p>
<dt><code>-t&nbsp;<wbr></code><i>port</i></p>
<dd>Specify database port (default: 0)</p>
<dt><code>-p</code></p>
<dd>Proceed in spite of I/O errors.</p>
<dt><code>-r</code></p>
<dd>List records.</p>
<dt><code>-s</code></p>
<dd>Synchronize or store in Database.</p>
<dt><code>-S</code></p>
<dd>Show scan progress periodically.</p>
<dt><code>-v</code></p>
<dd>Verbose output mode.</p>
<dt><code>-V&nbsp;<wbr></code><i>volume</i></p>
<dd>Specify volume names (separated by &#8216;|&#8217;)</p>
<dt><code>-w&nbsp;<wbr></code><i>dir</i></p>
<dd>Specify working directory (default from conf file)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bls/">bls</a></code>(8), <code><a href="/docs/linux/man/8-bextract/">bextract</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;, for the Debian GNU/Linux system (but may be used by others).<br />
&nbsp;<wbr></p>

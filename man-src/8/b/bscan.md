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
<p>The purpose of bscan is to read (scan) a Bacula Volume and to recreate or update the database contents with the information found on the Volume. This is done in a non-destructive way. This permits restoring database entries that have been lost by pruning, purging, deleting, or a database corruption problem.<br/>
&nbsp;<wbr> Normally, it should not be necessary to run the bscan command because the database is self maintaining, and most corrupted databases can be repaired by the tools provided by the database vendors. In addition, if you have maintained bootstrap files during backups, you should be able to recover all your data from the bootstrap file without needed an up to date catalog. <code>bscan</code> command. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></dt>
<dd>Show version and usage of program.</dd>
<dt><code>-b&nbsp;<wbr></code><i>bootstrap</i></dt>
<dd>Specify a bootstrap file.</dd>
<dt><code>-c&nbsp;<wbr></code><i>config</i></dt>
<dd>Specify configuration file.</dd>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></dt>
<dd>Set debug level to <i>nn</i>.</dd>
<dt><code>-dt</code></dt>
<dd>Print timestamp in debug output.</dd>
<dt><code>-m</code></dt>
<dd>Update media info in database.</dd>
<dt><code>-D</code></dt>
<dd>Specify the driver database name (default: <i>NULL</i>)</dd>
<dt><code>-n&nbsp;<wbr></code><i>name</i></dt>
<dd>Specify the database name (default: <i>bacula</i>)</dd>
<dt><code>-u&nbsp;<wbr></code><i>username</i></dt>
<dd>Specify database username (default: <i>bacula</i>)</dd>
<dt><code>-P&nbsp;<wbr></code><i>password</i></dt>
<dd>Specify database password (default: <i>none</i>)</dd>
<dt><code>-h&nbsp;<wbr></code><i>host</i></dt>
<dd>Specify database host (default: <i>NULL</i>)</dd>
<dt><code>-t&nbsp;<wbr></code><i>port</i></dt>
<dd>Specify database port (default: 0)</dd>
<dt><code>-p</code></dt>
<dd>Proceed in spite of I/O errors.</dd>
<dt><code>-r</code></dt>
<dd>List records.</dd>
<dt><code>-s</code></dt>
<dd>Synchronize or store in Database.</dd>
<dt><code>-S</code></dt>
<dd>Show scan progress periodically.</dd>
<dt><code>-v</code></dt>
<dd>Verbose output mode.</dd>
<dt><code>-V&nbsp;<wbr></code><i>volume</i></dt>
<dd>Specify volume names (separated by &#8216;|&#8217;)</dd>
<dt><code>-w&nbsp;<wbr></code><i>dir</i></dt>
<dd>Specify working directory (default from conf file)</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bls/">bls</a></code>(8), <code><a href="/docs/linux/man/8-bextract/">bextract</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;, for the Debian GNU/Linux system (but may be used by others).<br/>
&nbsp;<wbr></p>

---
title: "rlmgr(1)"
name: "rlmgr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rlmgr/"
description: "rlmgr – administration utility for QDBM Relic"
---

<h2 class="name">NAME</h2>
<p> rlmgr &#8211; administration utility for QDBM Relic </p>
<h2>SYNOPSIS</h2>
<p> <code>rlmgr create</code> <i>name</i><br />
 <code>rlmgr store</code> [-kx] [-vx|-vf] [-insert] <i>name</i> <i>key</i> <i>val</i><br />
 <code>rlmgr delete</code> [-kx] <i>name</i> <i>key</i><br />
 <code>rlmgr fetch</code> [-kx] [-ox] [-n] <i>name</i> <i>key</i><br />
 <code>rlmgr list</code> [-ox] <i>name</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>rlmgr</code> commands. </p>
<p> <code>rlmgr</code> is a utility for debugging Relic and its applications. It features editing and checking of a database. It can be used for database applications with shell scripts. This command is used in the above format. <i>name</i> specifies a database name. <i>key</i> specifies the key of a record. <i>val</i> specifies the value of a record.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#reliccli.</p>
<dl>
<dt><code>-kx</code></p>
<dd> treat <i>key</i> as a binary expression of hexadecimal notation.</p>
<dt><code>-vx</code></p>
<dd> treat <i>val</i> as a binary expression of hexadecimal notation.</p>
<dt><code>-vf</code></p>
<dd> read the value from a file specified with <i>val</i>.</p>
<dt><code>-insert</code></p>
<dd> specify the storing mode for `DBM_INSERT&#8217;.</p>
<dt><code>-ox</code></p>
<dd> treat the output as a binary expression of hexadecimal notation.</p>
<dt><code>-n</code></p>
<dd> do not output the tailing newline.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3), <code><a href="/docs/linux/man/3-relic/">relic</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

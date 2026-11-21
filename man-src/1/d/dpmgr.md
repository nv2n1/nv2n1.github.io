---
title: "dpmgr(1)"
name: "dpmgr"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpmgr/"
description: "dpmgr – administration utility for QDBM Depot"
---

<h2>SYNOPSIS</h2>
<p> <code>dpmgr create</code> [-s] [-bnum <i>num</i>] <i>name</i><br />
 <code>dpmgr put</code> [-kx|-ki] [-vx|-vi|-vf] [-keep|-cat] [-na] <i>name</i> <i>key</i> <i>val</i><br />
 <code>dpmgr out</code> [-kx|-ki] <i>name</i> <i>key</i><br />
 <code>dpmgr get</code> [-nl] [-kx|-ki] [-start <i>num</i>] [-max <i>num</i>] [-ox] [-n] <i>name</i> <i>key</i><br />
 <code>dpmgr list</code> [-nl] [-k|-v] [-ox] <i>name</i><br />
 <code>dpmgr optimize</code> [-bnum <i>num</i>] [-na] <i>name</i><br />
 <code>dpmgr inform</code> [-nl] <i>name</i><br />
 <code>dpmgr remove</code> <i>name</i><br />
 <code>dpmgr repair</code> <i>name</i><br />
 <code>dpmgr exportdb</code> <i>name file</i><br />
 <code>dpmgr importdb</code> <i>name file</i><br />
 <code>dpmgr snaffle</code> [-kx|-ki] [-ox] [-n] <i>name</i> <i>key</i><br />
 <code>dpmgr version</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>dpmgr</code> commands. </p>
<p> <code>dpmgr</code> is a utility for debugging Depot and its applications. It features editing and checking of a database. It can be used for database applications with shell scripts. This command is used in the above format. <i>name</i> specifies a database name. <i>key</i> specifies the key of a record. <i>val</i> specifies the value of a record.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#depotcli.</p>
<dl>
<dt><code>-s</code></dt>
<dd> make the file sparse.</dd>
<dt><code>-bnum </code><i>num</i></dt>
<dd> specify the number of the elements of the bucket array.</dd>
<dt><code>-kx</code></dt>
<dd> treat <i>key</i> as a binary expression of hexadecimal notation.</dd>
<dt><code>-ki</code></dt>
<dd> treat <i>key</i> as an integer expression of decimal notation.</dd>
<dt><code>-vx</code></dt>
<dd> treat <i>val</i> as a binary expression of hexadecimal notation.</dd>
<dt><code>-vi</code></dt>
<dd> treat <i>val</i> as an integer expression of decimal notation.</dd>
<dt><code>-vf</code></dt>
<dd> read the value from a file specified with <i>val</i>.</dd>
<dt><code>-keep</code></dt>
<dd> specify the storing mode for `DP_DKEEP&#8217;.</dd>
<dt><code>-cat</code></dt>
<dd> specify the storing mode for `DP_DCAT&#8217;.</dd>
<dt><code>-na</code></dt>
<dd> do not set alignment.</dd>
<dt><code>-nl</code></dt>
<dd> open the database without file locking.</dd>
<dt><code>-start</code></dt>
<dd> specify the beginning offset of a value to fetch.</dd>
<dt><code>-max</code></dt>
<dd> specify the max size of a value to fetch.</dd>
<dt><code>-ox</code></dt>
<dd> treat the output as a binary expression of hexadecimal notation.</dd>
<dt><code>-n</code></dt>
<dd> do not output the tailing newline.</dd>
<dt><code>-k</code></dt>
<dd> output keys only.</dd>
<dt><code>-v</code></dt>
<dd> output values only.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>qdbm</code>(3), <code><a href="/docs/linux/man/1-dptsv/">dptsv</a></code>(1), <code>dpopen</code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>

---
title: "vlmgr(1)"
name: "vlmgr"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vlmgr/"
description: "vlmgr – administration utility for QDBM Villa"
---

<h2 class="name">NAME</h2>
<p> vlmgr &#8211; administration utility for QDBM Villa </p>
<h2>SYNOPSIS</h2>
<p> <code>vlmgr create</code> [-cz|-cy|-cx] <i>name</i><br />
 <code>vlmgr put</code> [-kx|-ki] [-vx|-vi|-vf] [-keep|-cat|-dup] <i>name</i> <i>key</i> <i>val</i><br />
 <code>vlmgr out</code> [-l] [-kx|-ki] <i>name</i> <i>key</i><br />
 <code>vlmgr get</code> [-nl] [-l] [-kx|-ki] [-ox] [-n] <i>name</i> <i>key</i><br />
 <code>vlmgr list</code> [-nl] [-k|-v] [-kx|-ki] [-ox] [-top <i>key</i>] [-bot <i>key</i>] [-gt] [-lt] [-max <i>num</i>] [-desc] <i>name</i><br />
 <code>vlmgr optimize</code> <i>name</i><br />
 <code>vlmgr inform</code> [-nl] <i>name</i><br />
 <code>vlmgr remove</code> <i>name</i><br />
 <code>vlmgr repair</code> [-ki] <i>name</i><br />
 <code>vlmgr exportdb</code> [-ki] <i>name</i> <i>file</i><br />
 <code>vlmgr importdb</code> [-ki] <i>name</i> <i>file</i><br />
 <code>vlmgr version</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>vlmgr</code> commands. </p>
<p> <code>vlmgr</code> is a utility for debugging Villa and its applications. It features editing and checking of a database. It can be used for database applications with shell scripts. This command is used in the above format. <i>name</i> specifies a database name. <i>key</i> specifies the key of a record. <i>val</i> specifies the value of a record.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#villacli.</p>
<dl>
<dt><code>-cz</code></p>
<dd> compress leaves in the database with ZLIB.</p>
<dt><code>-cy</code></p>
<dd> compress leaves in the database with LZO.</p>
<dt><code>-cx</code></p>
<dd> compress leaves in the database with BZIP2.</p>
<dt><code>-l</code></p>
<dd> all records corresponding the key are dealt.</p>
<dt><code>-kx</code></p>
<dd> treat <i>key</i> as a binary expression of hexadecimal notation.</p>
<dt><code>-ki</code></p>
<dd> treat <i>key</i> as an integer expression of decimal notation.</p>
<dt><code>-vx</code></p>
<dd> treat <i>val</i> as a binary expression of hexadecimal notation.</p>
<dt><code>-vi</code></p>
<dd> treat <i>val</i> as an integer expression of decimal notation.</p>
<dt><code>-vf</code></p>
<dd> read the value from a file specified with <i>val</i>.</p>
<dt><code>-keep</code></p>
<dd> specify the storing mode for `VL_DKEEP&#8217;.</p>
<dt><code>-cat</code></p>
<dd> specify the storing mode for `VL_DCAT&#8217;.</p>
<dt><code>-dup</code></p>
<dd> specify the storing mode for `VL_DDUP&#8217;.</p>
<dt><code>-nl</code></p>
<dd> open the database without file locking.</p>
<dt><code>-top </code><i>key</i></p>
<dd> specify the top key of listing.</p>
<dt><code>-bot </code><i>key</i></p>
<dd> specify the bottom key of listing.</p>
<dt><code>-gt</code></p>
<dd> do not include the top key of listing.</p>
<dt><code>-lt</code></p>
<dd> do not include the bottom key of listing.</p>
<dt><code>-max </code><i>num</i></p>
<dd> specify the max number of listing.</p>
<dt><code>-desc</code></p>
<dd> list in descending order.</p>
<dt><code>-ox</code></p>
<dd> treat the output as a binary expression of hexadecimal notation.</p>
<dt><code>-n</code></p>
<dd> do not output the tailing newline.</p>
<dt><code>-k</code></p>
<dd> output keys only.</p>
<dt><code>-v</code></p>
<dd> output values only.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3) <code><a href="/docs/linux/man/1-vltsv/">vltsv</a></code>(1), <code><a href="/docs/linux/man/3-villa/">villa</a></code>(3), <code><a href="/docs/linux/man/3-vlopen/">vlopen</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

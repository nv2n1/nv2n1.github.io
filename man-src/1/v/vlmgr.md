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
<dt><code>-cz</code></dt>
<dd> compress leaves in the database with ZLIB.</dd>
<dt><code>-cy</code></dt>
<dd> compress leaves in the database with LZO.</dd>
<dt><code>-cx</code></dt>
<dd> compress leaves in the database with BZIP2.</dd>
<dt><code>-l</code></dt>
<dd> all records corresponding the key are dealt.</dd>
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
<dd> specify the storing mode for `VL_DKEEP&#8217;.</dd>
<dt><code>-cat</code></dt>
<dd> specify the storing mode for `VL_DCAT&#8217;.</dd>
<dt><code>-dup</code></dt>
<dd> specify the storing mode for `VL_DDUP&#8217;.</dd>
<dt><code>-nl</code></dt>
<dd> open the database without file locking.</dd>
<dt><code>-top </code><i>key</i></dt>
<dd> specify the top key of listing.</dd>
<dt><code>-bot </code><i>key</i></dt>
<dd> specify the bottom key of listing.</dd>
<dt><code>-gt</code></dt>
<dd> do not include the top key of listing.</dd>
<dt><code>-lt</code></dt>
<dd> do not include the bottom key of listing.</dd>
<dt><code>-max </code><i>num</i></dt>
<dd> specify the max number of listing.</dd>
<dt><code>-desc</code></dt>
<dd> list in descending order.</dd>
<dt><code>-ox</code></dt>
<dd> treat the output as a binary expression of hexadecimal notation.</dd>
<dt><code>-n</code></dt>
<dd> do not output the tailing newline.</dd>
<dt><code>-k</code></dt>
<dd> output keys only.</dd>
<dt><code>-v</code></dt>
<dd> output values only.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>qdbm</code>(3) <code><a href="/docs/linux/man/1-vltsv/">vltsv</a></code>(1), <code>villa</code>(3), <code>vlopen</code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

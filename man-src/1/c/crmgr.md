---
title: "crmgr(1)"
name: "crmgr"
section: "1"
letter: "c"
url: "/docs/linux/man/1-crmgr/"
description: "crmgr – administration utility for QDBM Curia"
---

<h2 class="name">NAME</h2>
<p> crmgr &#8211; administration utility for QDBM Curia </p>
<h2>SYNOPSIS</h2>
<p> <code>crmgr create</code> [-s] [-bnum <i>num</i> ] [-dnum <i>num</i>] <i>name</i><br />
 <code>crmgr put</code> [-kx|-ki] [-vx|-vi|-vf] [-keep|-cat] [-lob] [-na] <i>name</i> <i>key</i> <i>val</i><br />
 <code>crmgr out</code> [-kx|-ki] [-lob] <i>name</i> <i>key</i><br />
 <code>crmgr get</code> [-nl] [-kx|-ki] [-start <i>num</i>] [-max <i>num</i>] [-ox] [-lob] [-n] <i>name</i> <i>key</i><br />
 <code>crmgr list</code> [-nl] [-k|-v] [-ox] <i>name</i><br />
 <code>crmgr optimize</code> [-bnum <i>num</i>] [-na] <i>name</i><br />
 <code>crmgr inform</code> [-nl] <i>name</i><br />
 <code>crmgr remove</code> <i>name</i><br />
 <code>crmgr repair</code> <i>name</i><br />
 <code>crmgr exportdb</code> <i>name dir</i><br />
 <code>crmgr importdb</code> <i>name dir</i><br />
 <code>crmgr snaffle</code> [-kx|-ki] [-ox] [-n] <i>name</i> <i>key</i><br />
 <code>crmgr version</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>crmgr</code> commands. </p>
<p> <code>crmgr</code> is a utility for debugging Curia and its applications. It features editing and checking of a database. It can be used for the database applications with shell scripts. This command is used in the above format. <i>name</i> specifies a database name. <i>key</i> specifies the key of a record. <i>val</i> specifies the value of a record.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#curiacli.</p>
<dl>
<dt><code>-s</code></p>
<dd> make the file sparse.</p>
<dt><code>-bnum </code><i>num</i></p>
<dd> specify the number of the elements of the bucket array.</p>
<dt><code>-dnum </code><i>num</i></p>
<dd> specify the number of division of the database.</p>
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
<dd> specify the storing mode for `CR_DKEEP&#8217;.</p>
<dt><code>-cat</code></p>
<dd> specify the storing mode for `CR_DCAT&#8217;.</p>
<dt><code>-na</code></p>
<dd> do not set alignment.</p>
<dt><code>-nl</code></p>
<dd> open the database without file locking.</p>
<dt><code>-start</code></p>
<dd> specify the beginning offset of a value to fetch.</p>
<dt><code>-max</code></p>
<dd> specify the max size of a value to fetch.</p>
<dt><code>-ox</code></p>
<dd> treat the output as a binary expression of hexadecimal notation.</p>
<dt><code>-lob</code></p>
<dd> handle large objects.</p>
<dt><code>-n</code></p>
<dd> do not output the tailing newline.</p>
<dt><code>-k</code></p>
<dd> output keys only.</p>
<dt><code>-v</code></p>
<dd> output values only.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3), <code><a href="/docs/linux/man/1-crtsv/">crtsv</a></code>(1), <code><a href="/docs/linux/man/3-curia/">curia</a></code>(3), <code><a href="/docs/linux/man/3-cropen/">cropen</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

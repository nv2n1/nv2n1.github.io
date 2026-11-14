---
title: "odmgr(1)"
name: "odmgr"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odmgr/"
description: "odmgr – administration utility for QDBM Odeum"
---

<h2 class="name">NAME</h2>
<p> odmgr &#8211; administration utility for QDBM Odeum </p>
<h2>SYNOPSIS</h2>
<p> <code>odmgr create</code> <i>name</i><br />
 <code>odmgr put</code> [-uri <i>str</i>] [-title <i>str</i>] [-author <i>str</i>] [-date <i>str</i>] [-wmax <i>num</i>] [-keep] <i>name</i> [<i>file</i>]<br />
 <code>odmgr out</code> [-id] <i>name</i> <i>expr</i><br />
 <code>odmgr get</code> [-id] [-t|-h] <i>name</i> <i>expr</i><br />
 <code>odmgr search</code> [-max <i>num</i>] [-or] [-idf] [-t|-h|-n] <i>name</i> <i>words&#8230;</i><br />
 <code>odmgr list</code> [-t|-h] <i>name</i><br />
 <code>odmgr optimize</code> <i>name</i><br />
 <code>odmgr inform</code> <i>name</i><br />
 <code>odmgr merge</code> <i>name elems&#8230;</i><br />
 <code>odmgr remove</code> <i>name</i><br />
 <code>odmgr break</code> [-h|-k|-s] [<i>file</i>]<br />
 <code>odmgr version</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>odmgr</code> commands. </p>
<p> <code>odmgr</code> is a utility for debugging Odeum and its applications. It features editing and checking of a database. It can be used for full-text search systems with shell scripts. This command is used in the above format. <i>name</i> specifies a database name. <i>file</i> specifies a file name, <i>expr</i> specifies the URI or the ID number of a document, <i>words</i> specifies searching words. <i>elems</i> specifies element databases.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#odeumcli .</p>
<dl>
<dt><code>-uri </code></p>
<dd> specify the URI of the document explicitly.</p>
<dt><code>-title </code><i>str</i></p>
<dd> specify the title of the document.</p>
<dt><code>-author </code><i>str</i></p>
<dd> specify the author of the document.</p>
<dt><code>-date </code><i>str</i></p>
<dd> specify the modified date of the document.</p>
<dt><code>-wmax </code><i>num</i></p>
<dd> specify the max number of words to be stored.</p>
<dt><code>-keep</code></p>
<dd> the storing mode is not to be overwrite.</p>
<dt><code>-id</code></p>
<dd> specify a document not by a URI but by an ID number.</p>
<dt><code>-t</code></p>
<dd> output the details of a document in tab separated format.</p>
<dt><code>-h</code></p>
<dd> output the details of a document in human-readable format.</p>
<dt><code>-k</code></p>
<dd> output keywords of a document.</p>
<dt><code>-s</code></p>
<dd> output summary of a document.</p>
<dt><code>-max </code><i>num</i></p>
<dd> specify the max number of documents of the output.</p>
<dt><code>-or</code></p>
<dd> perform OR search, nut AND search.</p>
<dt><code>-idf</code></p>
<dd> tune scores with IDF.</p>
<dt><code>-n</code></p>
<dd> show ID numbers and scores only.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3), <code><a href="/docs/linux/man/1-odidx/">odidx</a></code>(1), <code><a href="/docs/linux/man/3-odeum/">odeum</a></code>(3). <code><a href="/docs/linux/man/3-odopen/">odopen</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

---

title: "odmgr(1)"
name: "odmgr"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odmgr/"
description: "odmgr – administration utility for QDBM Odeum"
---

<p> odmgr &#8211; administration utility for QDBM Odeum </p>
<h2>SYNOPSIS</h2>
<p> <code>odmgr create</code> <i>name</i><br/>
 <code>odmgr put</code> [-uri <i>str</i>] [-title <i>str</i>] [-author <i>str</i>] [-date <i>str</i>] [-wmax <i>num</i>] [-keep] <i>name</i> [<i>file</i>]<br/>
 <code>odmgr out</code> [-id] <i>name</i> <i>expr</i><br/>
 <code>odmgr get</code> [-id] [-t|-h] <i>name</i> <i>expr</i><br/>
 <code>odmgr search</code> [-max <i>num</i>] [-or] [-idf] [-t|-h|-n] <i>name</i> <i>words&#8230;</i><br/>
 <code>odmgr list</code> [-t|-h] <i>name</i><br/>
 <code>odmgr optimize</code> <i>name</i><br/>
 <code>odmgr inform</code> <i>name</i><br/>
 <code>odmgr merge</code> <i>name elems&#8230;</i><br/>
 <code>odmgr remove</code> <i>name</i><br/>
 <code>odmgr break</code> [-h|-k|-s] [<i>file</i>]<br/>
 <code>odmgr version</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>odmgr</code> commands. </p>
<p> <code>odmgr</code> is a utility for debugging Odeum and its applications. It features editing and checking of a database. It can be used for full-text search systems with shell scripts. This command is used in the above format. <i>name</i> specifies a database name. <i>file</i> specifies a file name, <i>expr</i> specifies the URI or the ID number of a document, <i>words</i> specifies searching words. <i>elems</i> specifies element databases.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#odeumcli .</p>
<dl>
<dt><code>-uri </code></dt>
<dd> specify the URI of the document explicitly.</dd>
<dt><code>-title </code><i>str</i></dt>
<dd> specify the title of the document.</dd>
<dt><code>-author </code><i>str</i></dt>
<dd> specify the author of the document.</dd>
<dt><code>-date </code><i>str</i></dt>
<dd> specify the modified date of the document.</dd>
<dt><code>-wmax </code><i>num</i></dt>
<dd> specify the max number of words to be stored.</dd>
<dt><code>-keep</code></dt>
<dd> the storing mode is not to be overwrite.</dd>
<dt><code>-id</code></dt>
<dd> specify a document not by a URI but by an ID number.</dd>
<dt><code>-t</code></dt>
<dd> output the details of a document in tab separated format.</dd>
<dt><code>-h</code></dt>
<dd> output the details of a document in human-readable format.</dd>
<dt><code>-k</code></dt>
<dd> output keywords of a document.</dd>
<dt><code>-s</code></dt>
<dd> output summary of a document.</dd>
<dt><code>-max </code><i>num</i></dt>
<dd> specify the max number of documents of the output.</dd>
<dt><code>-or</code></dt>
<dd> perform OR search, nut AND search.</dd>
<dt><code>-idf</code></dt>
<dd> tune scores with IDF.</dd>
<dt><code>-n</code></dt>
<dd> show ID numbers and scores only.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>qdbm</code>(3), <code><a href="/docs/linux/man/1-odidx/">odidx</a></code>(1), <code>odeum</code>(3). <code>odopen</code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>

---
title: "odidx(1)"
name: "odidx"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odidx/"
description: "odidx – indexer of document files"
---

<h2 class="name">NAME</h2>
<p> odidx &#8211; indexer of document files </p>
<h2>SYNOPSIS</h2>
<p> <code>odidx register</code> [-l <i>file</i>] [-wmax <i>num</i>] [-tsuf <i>sufs</i>] [-hsuf <i>sufs</i>] <i>name</i>[<i>dir</i>]<br />
 <code>odidx relate</code> <i>name</i><br />
 <code>odidx purge</code> <i>name</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>odidx</code> commands. </p>
<p> The command <code>odidx</code> is a utility for indexing files on the local file system. This command is useful for a full-text search system of a Web site. Supported file format are plain text and HTML. Supported character encoding are US-ASCII and ISO-8859-1. The URI of each document is specified with the path of its file. Attributes named as <i>title</i> and <i>date</i> are given to each documents. When a document is already existing in the database, it is registered if its last modification time is newer, or it is ignored. Modification times are stored in the sub database `_mtime&#8217; in the main database directory. Score information are stored in the sub database `_score&#8217; in the main database directory. This command is used in the above format. <i>name</i> specifies a database name. <i>dir</i> specifies a directory name.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the file:///usr/share/doc/qdbm-doc/spex.html#odeumcli.</p>
<dl>
<dt><code>-l </code><i>file</i></p>
<dd> read a file and get list of paths of files to register. If `-&#8216; is specified, the standard input is read.</p>
<dt><code>-wmax </code><i>num</i></p>
<dd> specify the max number of words to be stored in the document database.</p>
<dt><code>-tsuf </code><i>sufs</i></p>
<dd> specify suffixes of plain text files in comma separated format. The default is `-tsuf .txt,.text&#8217;.</p>
<dt><code>-hsuf </code><i>sufs</i></p>
<dd> specify suffixes of HTML files in comma separated format. The default is `-hsuf .html,.htm&#8217;.</dl>
<h2>EXAMPLES</h2>
<p> For example, to register files which are under `/home/mikio&#8217; and whose suffix are `.txt&#8217;, `.c&#8217;, or `.h&#8217;, perform the following command.<br />
 <code> odidx register -tsuf &quot;.txt,.c,.h&quot; -hsuf &quot;&quot; casket /home/mikio</code> </p>
<p> Thus, to retrieve documents which include `unix&#8217; and `posix&#8217; and show the top 8 terms, perform the following command.<br />
 <code> odmgr search -max 8 -h casket &quot;unix posix&quot;</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-qdbm/">qdbm</a></code>(3), <code><a href="/docs/linux/man/1-odmgr/">odmgr</a></code>(1), <code><a href="/docs/linux/man/3-odeum/">odeum</a></code>(3), <code><a href="/docs/linux/man/3-odopen/">odopen</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

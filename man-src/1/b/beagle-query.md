---
title: "beagle-query(1)"
name: "beagle-query"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beagle-query/"
description: "beagle-query – search your personal information space"
---

<h2>NAME</h2>
<p> beagle-query &#8211; search your personal information space</p>
<h2>SYNOPSIS</h2>
<p> <code>beagle-query</code> [<i>options</i>] <i>query</i></p>
<h2>DESCRIPTION</h2>
<p> <code>beagle-query</code> is used to search your personal information space via Beagle, on the command line. It is a command-line form of the beagle-search GNOME program.</p>
<h2>OPTIONS</h2>
<h3>Search options</h3>
<dl>
<dt><code>&#8211;max-hits</code></p>
<dd> Reduce the number of search results returned per backend. The default is 100. Increasing this will slow down overall search speed.</p>
<dt><code>&#8211;verbose </code></p>
<dd> Print detailed information about each hit.</p>
<dt><code>&#8211;cache</code></p>
<dd> Show the entire cached text for each result. Only works with <i>&#8211;verbose</i>.<br />
 Note that for large documents this will produce extremely large output, so use this with uri queries or queries returning only a few results Not recommended for live-queries or stats-only queries.</p>
<dt><code>&#8211;live-query </code></p>
<dd> Enable live queries. This argument keeps beagle-query running, continuously feeding new matching hits as the system gets aware of them.</p>
<dt><code>&#8211;stats-only</code></p>
<dd> Show only statistics on the number of search results and how long it took to get them, and not the results themselves.</dl>
<h3>Other options</h3>
<dl>
<dt><code>&#8211;keywords</code></p>
<dd> Lists the keywords allowed in <i>query</i>. Keyword queries can be specified as <i>keywordname:value e.g. ext:jpg</i></p>
<dt><code>&#8211;help</code></p>
<dd> Print the usage message.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version information.</dl>
<h2>QUERY</h2>
<p> You can query for a word, several words or a quoted phrase. When several words are searched, only documents which contain all the words are matched. To specify a phrase, enclose it in shell-escaped quotes (\&quot;search term\&quot;). </p>
<p> Besides these beagle supports an advanced query syntax. See <a rel="nofollow" href="http://beagle-project.org/Searching_Data#Search_Syntax">http://beagle-project.org/Searching_Data#Search_Syntax</a> for more information.</p>
<h2>AUTHOR</h2>
<p> Novell, Inc.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;dashboard-hackers [at] gnome.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Novell, Inc., &#169; 2008 D Bera </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-beagled/">beagled</a></code>(1), <code><a href="/docs/linux/man/1-beagle-shutdown/">beagle-shutdown</a></code>(1), <code><a href="/docs/linux/man/1-beagle-status/">beagle-status</a></code>(1), </p>
<h2>Index</h2>

---
title: "tracker3-status(1)"
name: "tracker3-status"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-status/"
description: "tracker3-status – Provide status and statistics on the data indexed"
---

<h2 class="name">NAME</h2>
<p> tracker3-status &#8211; Provide status and statistics on the data indexed </p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker3 status
    tracker3 status [[expression1]...] tracker3 status-- stat[-a] [[expression1]...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Display the status of the current index and data set. A summary of recorded failures during file metadata indexing is also displayed. </p>
<p> Providing a search expression will list the full details of the recorded failures matching the filename. </p>
<p> With the <code>&#8211;stat</code> option, displays statistics about the RDF classes and how many of each exist for data set that has been indexed. For example, &quot;10 Folders&quot;.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;stat[=</code><i>expression</i><code>]</code></p>
<dl>
<dt>
<dd> By default, only common and useful classes are shown, e.g. &quot;nfo:Document&quot; or &quot;nfo:Folder&quot;, for a full set of statistics, see the <code>&#8211;all</code> option.</dl>
<p> If one or more <i>expression</i> arguments is given, the statistics returned are filtered to only show information those RDF types matching <i>expression</i> (case folded and matching accented variants). The RDF classes are detailed by the Nepomuk otology specification. A list of possible classes matching <i>expression</i>, see <code>tracker3 sparql -c</code>. </p>
<p> <code>-a, &#8211;all</code></p>
<dl>
<dt>
<dd> Display statistics about ALL RDF classes that exist in the database. Without this option only the common RDF classes will be shown, for example &quot;nfo:Document&quot; and &quot;nfo:FileDataObject&quot;.</dl>
<p> This option is implied if search terms are provided to filter ALL possible statistics.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-daemon/">tracker3-daemon</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-info/">tracker3-info</a></code>(1). </p>
<dl>
<dt>
<dd> &bull; <code><a rel="nofollow" href="http://nepomuk.semanticdesktop.org/">http://nepomuk.semanticdesktop.org/</a></code></dl>
<dl>
<dt>
<dd> &bull; <code><a rel="nofollow" href="http://www.w3.org/TR/rdf-sparql-query/">http://www.w3.org/TR/rdf-sparql-query/</a></code></dl>
<h2>Index</h2>

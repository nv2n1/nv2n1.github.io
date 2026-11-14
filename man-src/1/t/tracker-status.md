---
title: "tracker-status(1)"
name: "tracker-status"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-status/"
description: "tracker-status – Provide status and statistics on the data indexed"
---

<h2 class="name">NAME</h2>
<p> tracker-status &#8211; Provide status and statistics on the data indexed</p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker status
        tracker status-- stat[-a] [[expression1]...] tracker status-- collect -
    debug - info
</code></pre>
<h2>DESCRIPTION</h2>
<p> Display the status of the current index and data set. </p>
<p> With the <code>&#8211;stat</code> option, displays statistics about the RDF classes and how many of each exist for data set that has been indexed. For example, &quot;10 Folders&quot;. </p>
<p> This command also provides a way to collect information for debug purposes using the <code>&#8211;collect-debug-info</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;stat</code>[=<i>expression</i>]</p>
<dd> By default, only common and useful classes are shown, e.g. &quot;nfo:Document&quot; or &quot;nfo:Folder&quot;, for a full set of statistics, see the <code>&#8211;all</code> option. </p>
<p> If one or more <i>expression</i> arguments is given, the statistics returned are filtered to only show information those RDF types matching <i>expression</i> (case folded and matching accented variants). The RDF classes are detailed by the Nepomuk otology specification. A list of possible classes matching <i>expression</i>, see <code>tracker sparql -c</code>.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Display statistics about ALL RDF classes that exist in the database. Without this option only the common RDF classes will be shown, for example &quot;nfo:Document&quot; and &quot;nfo:FileDataObject&quot;. </p>
<p> This option is implied if search terms are provided to filter ALL possible statistics.</p>
<dt><code>&#8211;collect-debug-info</code></p>
<dd> Useful when debugging problems to diagnose the state of Tracker on your system. The data is output to stdout. Useful if bugs are filed against the project itself. </p>
<p> Data collected includes Tracker version in use, disk space available, size of the databases on the disk, the configuration in use, states of the index (e.g. last filesystem crawl, data set locale, etc.) and finally statistics about the data in the database (e.g. how many &quot;nfo:FileDataObject&quot; resources exist). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-control/">tracker-control</a></code>(1), <code><a href="/docs/linux/man/1-tracker-sparql/">tracker-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1).</p>
<dl>
<dt><code><a rel="nofollow" href="http://nepomuk.semanticdesktop.org/">http://nepomuk.semanticdesktop.org/</a></code></p>
<dd>
<dt><code><a rel="nofollow" href="http://www.w3.org/TR/rdf-sparql-query/">http://www.w3.org/TR/rdf-sparql-query/</a></code></p>
<dd>
</dl>
<h2>Index</h2>

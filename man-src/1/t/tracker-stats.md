---
title: "tracker-stats(1)"
name: "tracker-stats"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-stats/"
description: "tracker-stats – Provides statistics on the data indexed"
---

<h2 class="name">NAME</h2>
<p> tracker-stats &#8211; Provides statistics on the data indexed</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-stats</code> [<i>OPTION</i>&#8230;] [[<i>EXPRESSION</i>&#8230;] [<i>EXPRESSION</i>&#8230;]] </p>
<h2>DESCRIPTION</h2>
<p> Display statistics about RDF classes in and how many of each exist for the data set that has been indexed. </p>
<p> By default, only common and useful classes are shown, e.g. nfo:Document or nfo:Folder, for a full set of statistics, see the option. </p>
<p> If one or more <i>EXPRESSION</i> is given, the statistics returned are filtered to only include information about RDF types matching <i>EXPRESSION</i> (case folded and matching accented variants). </p>
<p> The RDF classes are detailed by the <code>Nepomuk</code> ontology specification. These classes can be used to further query more information using <code>SparQL</code> with <code>tracker-sparql.</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a brief help message.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Display statistics about ALL RDF classes that exist in the database. Without this option only the common RDF classes will be shown, for example nfo:Document and nfo:FileDataObject. </p>
<p> This option is implied if search terms are provided to filter ALL possible statistics.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version. </p>
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

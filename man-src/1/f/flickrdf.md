---
title: "flickrdf(1)"
name: "flickrdf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flickrdf/"
description: "flickrdf – call Flickr API"
---

<h2>NAME</h2>
<p> flickrdf &#8211; call Flickr API</p>
<h2>SYNOPSIS</h2>
<p> <code>flickrdf</code> [<code>-d </code><i>DELAY</i>] [<code>-a </code><i>FROB</i>] [<code>-h</code>] [<code>-v</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>flickrdf</code> is a utility that uses the <i>photos.getInfo</i> API to interpret the description fields and the tags for a photo URI into RDF triples. If raptor is present, it will be used to provide proper serializing to RDF rather than the built in and hacky ntriples/turtle output. </p>
<p> Machine tags when they are found are scanned for <i>xmlns:prefix=uri</i> and then all other machine tags with that prefix turn into triples. Several prefixes are also pre-defined by the library to automatically get turned into triples without an xmlns, such as <i>blue:</i>, <i>cell:</i>, <i>filter:</i> and <i>geo:</i>. Non-machine tags are not yet interpreted. </p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the version of the program and exit.</p>
<dt><code>-d </code><i>DELAY</i>, &#8211;delay <i>DELAY</i></p>
<dd> Set delay between requests to <i>DELAY</i> milliseconds.</p>
<dt><code>-D, &#8211;debug</code></p>
<dd> Print lots of debugging output.</p>
<dt><code>-o, &#8211;output </code><i>FORMAT</i></p>
<dd> Set output format to <i>FORMAT</i>. <i>FORMAT</i> is one of:<br />
<i>ntriples</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>N-Triples&nbsp;<wbr>(default)<br />
<i>turtle</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Turtle<br />
<i>rdfxml</i>-xmp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>RDF/XML&nbsp;<wbr>(XMP Profile)<br />
<i>rdfxml</i>-abbrev&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>RDF/XML&nbsp;<wbr>(Abbreviated)<br />
<i>rdfxml</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>RDF/XML<br />
<i>rss-1.0</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>RSS 1.0<br />
<i>dot</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GraphViz DOT format The exact list depends on the version of Raptor that flickcurl is linked against.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flickcurl/">flickcurl</a>(1),</code><a href="/docs/linux/man/3-libraptor/">libraptor</a>(3). </p>
<h2>AUTHOR</h2>
<p> flickrdf was written by David Beckett. </p>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>

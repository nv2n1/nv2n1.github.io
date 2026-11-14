---
title: "rdfproc(1)"
name: "rdfproc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdfproc/"
description: "rdfproc – Redland RDF processor utility"
---

<h2 class="name">NAME</h2>
<p> rdfproc &#8211; Redland RDF processor utility </p>
<h2>SYNOPSIS</h2>
<p> <code>rdfproc</code> [<code>options</code>] <i>store-name</i> <i>command</i> <i>arg&#8230;</i></p>
<h2>EXAMPLE</h2>
<pre>
<code>rdfproc test parse <a rel="nofollow" href="http://planetrdf.com/guide/rss.rdf">http://planetrdf.com/guide/rss.rdf</a></code>
<br>
<code>rdfproc test print</code>
<br>
<code>rdfproc test serialize ntriples</code>
<br>
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>rdfproc</code> utility allows parsing, querying, manipulating and serializing of RDF content using the <code>Redland</code> RDF library. The <i>store-name</i> is a Redland store name, typically a short identifier. The arguments to <i>command</i> vary and are explained in section COMMANDS below.</p>
<h2>OPTIONS</h2>
<p> rdfproc uses the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;) if supported by the getopt_long function. Otherwise the short options are only available.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a summary of the options.</p>
<dt><code>-c, &#8211;contexts</code></p>
<dd> Use a store with Redland contexts.</p>
<dt><code>-n, &#8211;new</code></p>
<dd> Make a new store, overwriting any existing one.</p>
<dt><code>-o, &#8211;output </code><i>FORMAT</i></p>
<dd> Set the output FORMAT for sequences of triples, such as from a search (find command) to a Redland serializer. Use -h or -o help to see the full list of supported formats.</p>
<dt><code>-p, &#8211;password</code></p>
<dd> Read the storage option &#8216;password&#8217; from standard input. Terminated by end of line (&#8216;
&#8217;) or end of file. This is equivalent to setting it using -t or &#8211;storage-options but does not require exposing the password in the argument list.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress informational messages (that go to stderr)</p>
<dt><code>-r, &#8211;results </code><i>FORMAT</i></p>
<dd> Set the query results syntax format. Use -h or -r help to see the full list of query result formats.</p>
<dt>
<dd> The exact list of formats depends on what <a href="/docs/linux/man/3-libraptor/">libraptor</a>(3) was built with but is given correct in the usage message with -h.</p>
<dt><code>-s, &#8211;storage </code><i>TYPE</i></p>
<dd> Set the Redland storage type (default &#8216;hashes&#8217;). If environment variable RDFPROC_STORAGE_TYPE is set, the storage type given here will override it. Use -h or -s help to see the full list of query result formats.</p>
<dt><code>-t, &#8211;storage-options </code><i>OPTIONS</i></p>
<dd> Set options for the the Redland storage, default is &quot;hash-type=&#8217;bdb&#8217;,dir=&#8217;.&#8217;&quot; to match the default storage &quot;hashes&quot;. For storages types such as &#8216;mysql&#8217; that need extra options this would typically be something like &quot;host=&#8217;hostname&#8217;,database=&#8217;dbname&#8217;,user=&#8217;abc&#8217;,password=&#8217;pass&#8217;&quot;. If environment variable RDFPROC_STORAGE_OPTIONS is set, the storage options given here will be applied afterwards.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the Redland version and exit.</p>
<dt><code>-V, &#8211;verbose</code></p>
<dd> Show informational messages on stderr.</dl>
<h2>COMMANDS</h2>
<p> Where a node is allowed, such as <i>NODE</i>, <i>SUBJECT</i>, <i>PREDICATE</i> or <i>OBJECT</i> below, simple heuristics are used to guess which are blank node identifiers, URIs or literals (to add a statement with a literal, use add-typed). If the item starts with _: then it is assumed to be a blank node identifier, otherwise if it matches something:// it is assumed to be a URI, otherwise it is a literal. Literals are only allowed as objects of statements and blank nodes are not allowed as predicates.</p>
<dl>
<dt><code>add </code><i>SUBJECT</i> <i>PREDICATE</i> <i>OBJECT</i> <i>[CONTEXT]</i></p>
<dd> Add the given triple to graph, in the optional Redland context if the <i>CONTEXT</i> node is given. </p>
<dt><code>add-typed </code><i>SUBJECT</i> <i>PREDICATE</i> <i>OBJECT</i> <i>OBJECT-LANG</i> <i>OBJECT-URI</i> <i>[CONTEXT]</i></p>
<dd> Add the triple with the datatyped literal object to the graph, in the optional Redland context if <i>CONTEXT</i> is given. </p>
<dt><code>arc </code><i>SUBJECT</i> <i>OBJECT</i></p>
<dd>
<dt><code>arcs </code><i>SUBJECT</i> <i>OBJECT</i></p>
<dd> Show one node/all nodes that match triples (<i>SUBJECT</i>, ?, <i>OBJECT</i>) </p>
<dt><code>arcs-in </code><i>NODE</i></p>
<dd> Show all properties of triples with <i>NODE</i> as a subject. </p>
<dt><code>arcs-out </code><i>NODE</i></p>
<dd> Show all properties of triples with <i>NODE</i> as an object. </p>
<dt><code>contains </code><i>SUBJECT</i> <i>PREDICATE</i> <i>OBJECT</i></p>
<dd> Check if the given triple is in the graph. </p>
<dt><code>contexts</code></p>
<dd> List all the contexts in the graph (if contexts are enabled). </p>
<dt><code>find </code><i>SUBJECT</i>|- <i>PREDICATE</i>|- <i>OBJECT</i>|- [<i>CONTEXT</i>]</p>
<dd> Find matching triples to the given statement where &#8211; stands for a blank that matches any node. If <i>CONTEXT</i> is given, only search for triples in that context node. </p>
<dt><code>has-arc-in </code><i>NODE</i> <i>ARC</i></p>
<dd> Check that there is a triple with <i>NODE</i> as a subject and <i>ARC</i> as a predicate. </p>
<dt><code>has-arc-out </code>NODE <i>ARC</i></p>
<dd> Check that there is a triple with <i>NODE</i> as a object and <i>ARC</i> as a predicate. </p>
<dt><code>parse </code><i>URI|FILENAME</i> [<i>SYNTAX|</i> [<i>BASE URI</i>]]</p>
<dd> Parse syntax at <i>URI</i> into the graph using <i>SYNTAX</i> which can be one of <i>rdfxml</i> (RDF/XML, default), <i>ntriples</i>, <i>turtle</i>, <i>rss-tag-soup</i> (for all RSS and Atoms), <i>grddl</i> and <i>guess</i> to use content hints and protocol information to work it out. (This list changes faster than this manual page) If <i>FILENAME</i> is a existing file, the appropriate URI will be generated for it. If parsing returns errors, the return code will be non-0. </p>
<dt><code>parse-stream </code><i>URI|FILENAME</i> [<i>SYNTAX</i> [<i>BASE URI</i> [<i>CONTEXT</i>]]</p>
<dd> Streaming parse syntax at URI into the graph using <i>SYNTAX</i> which can be one of <i>rdfxml</i> (RDF/XML, default) or <i>ntriples</i>. If <i>FILENAME</i> is an existing file, the appropriate URI will be generated for it. If the optional <i>CONTEXT URI is given, the triples are added to that context. If parsing returns errors, the return code will be non-0. </p>
<dt></i><code>print</code></p>
<dd> Print the graph triples in a simple format showing context nodes if present. </p>
<dt><code>query </code><i>NAME</i>|- <i>URI</i>|- <i>QUERY-STRING</i></p>
<dd> Run <i>QUERY-STRING query in language NAME</i> returning variable bindings, a boolean or RDF graph depending on the query. Query language can be &#8216;sparql&#8217; or &#8216;rdql&#8217;. </p>
<dt><code>remove </code><i>SUBJECT</i> <i>PREDICATE</i> <i>OBJECT</i> <i>[CONTEXT]</i></p>
<dd> Remove the given triple graph, in the optional Redland context if <i>CONTEXT</i> is given. </p>
<dt><code>remove-context </code><i>CONTEXT</i></p>
<dd> Remove all triples in the graph with the Redland context <i>CONTEXT</i>. </p>
<dt><code>serialize [</code><i>SYNTAX</i> [<i>URI</i> [<i>MIME-TYPE</i>]]]</p>
<dd> Serializes the graph to a syntax with a particular ISYNTAX <i>URI</i> or Internet Media Type/MIME Type. The default is RDF/XML (<i>NAME</i> &quot;rdfxml&quot;, MIME Type &quot;application/rdf/xml&quot;) if none of the above are given. Other alternatives are &quot;ntriples&quot; (no MIME Type). </p>
<dt><code>source </code><i>PREDICATE</i> <i>OBJECT</i></p>
<dd>
<dt><code>sources </code><i>PREDICATE</i> <i>OBJECT</i></p>
<dd> Show one node/all nodes that match triples (?, <i>PREDICATE</i>, <i>OBJECT</i>) </p>
<dt><code>target </code><i>SUBJECT</i> <i>PREDICATE</i></p>
<dd>
<dt><code>targets </code><i>SUBJECT</i> <i>PREDICATE</i></p>
<dd> Show one node/all nodes that match triples (<i>SUBJECT</i>, <i>PREDICATE</i>, ?) </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> RDFPROC_STORAGE_OPTIONS can be set to provide storage options instead of using the option -t, &#8211;storage-options <i>OPTIONS</i>. When both are given, command options are applied last. </p>
<p> RDFPROC_STORAGE_TYPE can be set to provide a storage type instead of using the option -s, &#8211;storage <i>TYPE</i>. When both are given, the storage type from the command is used.</p>
<h2>CONFORMING TO</h2>
<p> <i>RDF/XML Syntax (Revised)</i>, W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-syntax-grammar/">http://www.w3.org/TR/rdf-syntax-grammar/</a> </p>
<p> <i>N-Triples</i>, in <i>RDF Test Cases</i>, Jan Grant and Dave Beckett (eds.) W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-redland/">redland</a>(3), <a href="/docs/linux/man/3-libraptor/">libraptor</a>(3), <a href="/docs/linux/man/1-rapper/">rapper</a>(1)</p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
<h2>Index</h2>

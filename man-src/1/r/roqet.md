---
title: "roqet(1)"
name: "roqet"
section: "1"
letter: "r"
url: "/docs/linux/man/1-roqet/"
description: "roqet – Rasqal RDF query utility"
---

<h2 class="name">NAME</h2>
<p> roqet &#8211; Rasqal RDF query utility </p>
<h2>SYNOPSIS</h2>
<p> <code>roqet</code> [<code>OPTIONS</code>] <i>&lt;query-URI&gt;</i> <i>[base-URI]</i><br />
 <code>roqet</code> [<code>OPTIONS</code>]<code>-e</code> <i>query-string</i> <i>[base-URI]</i><br />
 <code>roqet</code> [<code>OPTIONS</code>]<code>-p</code> <i>sparql-protocol-service-URI</i> [<code>-e</code> <i>query-string</i> ] <i>[base-URI]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>roqet</code> utility allows querying of RDF content using the <code>Rasqal</code> RDF query library, printing the results in variable bindings, RDF graph or boolean format. The query is read from <i>query-URI</i> and the optional <i>base-URI</i> is used as the base URI of the query if present.</p>
<h2>MAIN OPTIONS</h2>
<p> roqet uses the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;) if supported by the getopt_long function. Otherwise only the short options are available.</p>
<dl>
<dt><code>-e, &#8211;exec QUERY</code></p>
<dd> Execute the query in the argument <i>QUERY</i> instead of reading the query from a URI (when <code>-e</code> / <code>&#8211;exec</code> is not given).</p>
<dt><code>-i, &#8211;input LANGUAGE</code></p>
<dd> Set the input query <i>LANGUAGE</i> to one of the supported languages which includes &#8216;sparql&#8217; (SPARQL Query Language for RDF, default), &#8216;sparql11&#8217; and &#8216;laqrs&#8217;. The full list of supported languages and subsets is given in the help summary with the <code>-h</code> / <code>&#8211;help</code> option.</p>
<dt><code>-p, &#8211;protocol SERVICE-URI</code></p>
<dd> Call the SPARQL HTTP protocol <i>SERVICE-URI</i> to execute the query instead of executing it inside the Rasqal query engine locally.</p>
<dt><code>-r, &#8211;results FORMAT</code></p>
<dd> Set the query results format.</p>
<dt>
<dd> For variable bindings, the values of <i>FORMAT</i> vary upon what Rasqal supports but include &#8216;simple&#8217; for a simple text format (default), &#8216;xml&#8217; for the SPARQL Query Results XML format, &#8216;rdfxml&#8217; and &#8216;turtle&#8217; for RDF syntax formats, and &#8216;json&#8217; for a JSON version of the results.</p>
<dt>
<dd> For RDF graph results, the values of <i>FORMAT</i> are &#8216;ntriples&#8217; (N-Triples, default), &#8216;rdfxml-abbrev&#8217; (RDF/XML Abbreviated), &#8216;rdfxml&#8217; (RDF/XML), &#8216;turtle&#8217; (Turtle), &#8216;json&#8217; (RDF/JSON resource centric), &#8216;json-triples&#8217; (RDF/JSON triples) or &#8216;rss-1.0&#8217; (RSS 1.0, also an RDF/XML syntax).</p>
<dt>
<dd> The exact list of formats depends on what <a href="/docs/linux/man/3-libraptor2/">libraptor2</a>(3) was built with but is given correct in the usage message with -h.</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-c, &#8211;count</code></p>
<dd> Only count the triples and produce no other output.</p>
<dt><code>-d, &#8211;dump-query FORMAT</code></p>
<dd> Print the parsed query out in a given <i>FORMAT</i> one of &#8216;none&#8217; (default), &#8216;debug&#8217;, &#8216;structure&#8217; or &#8216;sparql&#8217;</p>
<dt><code>-D, &#8211;data URI</code></p>
<dd> Add RDF data source URI (not a named graph). If no data sources are given, the query itself must point to the data such as via SPARQL FROM <i>uri</i> statements.</p>
<dt><code>-E, &#8211;ignore-errors</code></p>
<dd> Do not print error messages and do not exit with a non-0 status.</p>
<dt><code>-f, &#8211;feature NAME(=VALUE)</code></p>
<dd> Set query feature <i>NAME</i> to the <i>VALUE</i> or integer 1 if omitted. The known features can be shown with <code>-f help</code> or <code>&#8211;feature help</code>.</p>
<dt><code>-F, &#8211;format NAME</code></p>
<dd> Set the data source format <i>name</i> for subsequent data graphs called with <code>-D</code> / <code>&#8211;data</code> or <code>-G</code> / <code>&#8211;named</code>. The default if this is not specified is for the query engine to guess. The <i>name</i> is a Raptor parser name.</p>
<dt><code>-G, &#8211;named URI</code></p>
<dd> Add RDF data source URI (named graph)</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a summary of the options.</p>
<dt><code>-n, &#8211;dryrun</code></p>
<dd> Prepare the query but do not execute it.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> No extra information messages.</p>
<dt><code>-s, &#8211;source URI</code></p>
<dd> Add RDF data source URI (named graph) <i>URI</i> by adding it to the list of query data source URIs. <i>FORMAT</i> to &#8216;simple&#8217; (default) or &#8216;xml&#8217; (an experimental XML format)</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the rasqal library version and exit.</p>
<dt><code>-W, &#8211;warnings LEVEL</code></p>
<dd> Set the warning <i>LEVEL</i> in the range 0 (do not warn about anything) to 100 (show every warning). The Rasqal default is in the middle (50).</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> <code>roqet sparql-query-file.rq</code></dl>
<p> Run a SPARQL query contained in the local file sparql-query-file.rq. The data used would be described in FROM statements in the query file.</p>
<dl>
<dt>
<dd> <code>roqet -q -i sparql <a rel="nofollow" href="http://example.org/sparql-query.rq">http://example.org/sparql-query.rq</a></code></dl>
<p> Run a SPARQL query that is in the web at URI <a rel="nofollow" href="http://example.org/sparql-query.rq">http://example.org/sparql-query.rq</a> without an extra messages (quiet, -q).</p>
<dl>
<dt>
<dd> <code>roqet -q query-file.rq <a rel="nofollow" href="http://example.org/base/">http://example.org/base/</a></code></dl>
<p> Run an query (default languge SPARQL) from a local file query-file.rq but using base URI <a rel="nofollow" href="http://example.org/base/">http://example.org/base/</a> to resolve any relative URIs.</p>
<dl>
<dt>
<dd> <code>roqet -q -i sparql -r xml <a rel="nofollow" href="http://example.org/sparql-query.rq">http://example.org/sparql-query.rq</a></code></dl>
<p> Run a SPARQL query that is in the web at URI <a rel="nofollow" href="http://example.org/sparql-query.rq">http://example.org/sparql-query.rq</a> and format the results in the SPARQL Query Results XML format with no extra messages.</p>
<dl>
<dt>
<dd> <code>roqet -i sparql -e &#8216;SELECT * WHERE { ?s ?p ?o }&#8217; -D stuff.rdf</code></dl>
<p> Run a SPARQL query given on the command line against data in the file stuff.rdf. The type of the file will be guessed and likely is of format RDF/XML.</p>
<h2>CONFORMING TO</h2>
<p> <i>SPARQL Query Language for RDF</i>, Eric Prud&#8217;hommeaux and Andy Seaborne (eds), W3C Recommendation, 15 January 2008. <a rel="nofollow" href="http://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/">http://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/</a> </p>
<p> <i>SPARQL Query Results XML Format</i>, Jeen Broekstra and Dave Beckett (eds), W3C Recommendation, 15 January 2008. <a rel="nofollow" href="http://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115/">http://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-librasqal/">librasqal</a>(3),</code><a href="/docs/linux/man/3-libraptor/">libraptor</a>(3)</p>
<h2>CHANGES</h2>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
<h2>Index</h2>

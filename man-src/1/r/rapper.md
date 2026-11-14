---
title: "rapper(1)"
name: "rapper"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rapper/"
description: "rapper – Raptor RDF parsing and serializing utility"
---

<h2 class="name">NAME</h2>
<p> rapper &#8211; Raptor RDF parsing and serializing utility </p>
<h2>SYNOPSIS</h2>
<p> <code>rapper</code> [<code>OPTIONS</code>] <i>INPUT-URI</i> <i>[INPUT-BASE-URI]</i></p>
<h2>EXAMPLE</h2>
<pre>
<code>rapper -o ntriples <a rel="nofollow" href="http://planetrdf.com/guide/rss.rdf">http://planetrdf.com/guide/rss.rdf</a></code>
<br>
<code>rapper -i rss-tag-soup -o rss-1.0 pile-of-rss.xml <a rel="nofollow" href="http://example.org/base/">http://example.org/base/</a></code>
<br>
<code>rapper --count <a rel="nofollow" href="http://example.org/index.rdf">http://example.org/index.rdf</a></code>
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>rapper</code> utility allows parsing of RDF content by the <code>Raptor</code> RDF parser toolkit emitting the results as RDF triples in a choice of syntaxes. The <i>INPUT-URI</i> can be a file name, &#8216;-&#8216; for standard input or if Raptor is built with a WWW retrieval library, a general URI. The optional <i>INPUT-BASE-URI</i> is used as the document parser base URI if present otherwise defaults to the <i>INPUT-URI</i>. A value of &#8216;-&#8216; means no base URI.</p>
<h2>OPTIONS</h2>
<p> rapper uses the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;) if supported by the getopt_long function. Otherwise the short options are only available.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a summary of the options.</p>
<dt><code>-i, &#8211;input FORMAT</code></p>
<dd> Set the input <i>FORMAT</i> to one of &#8216;rdfxml&#8217; (RDF/XML, default), &#8216;ntriples&#8217; (N-Triples, see below), &#8216;turtle&#8217; (Turtle, see below) or &#8216;rss-tag-soup&#8217; (RSS Tag Soup). The RSS Tag Soup parser can turn the many XML RSS formats and Atom 0.3 into RDF triples.</p>
<dt>
<dd> The list of parsers depends on how <a href="/docs/linux/man/3-libraptor/">libraptor</a>(3) was built. The list of supported parsers is given in the help summary given by -h.</p>
<dt><code>-I, &#8211;input-uri URI</code></p>
<dd> Set the input/parser base <i>URI</i> or use value &#8216;-&#8216; for no base. The default is the INPUT-URI argument value.</p>
<dt><code>-o, &#8211;output FORMAT</code></p>
<dd> Set the output <i>FORMAT</i> to &#8216;ntriples&#8217; (N-Triples, default), &#8216;rdfxml&#8217; (RDF/XML), &#8216;rdfxml-abbrev&#8217; (RDF/XML with abbreviations) or &#8216;rss-1.0&#8217; (RSS 1.0, also an RDF/XML syntax).</p>
<dt>
<dd> The list of serializers depends on how <a href="/docs/linux/man/3-libraptor/">libraptor</a>(3) was built. The list of supported serializers is given in the help summary given by -h.</p>
<dt><code>-O, &#8211;output-uri URI</code></p>
<dd> Set the output/serializer base <i>URI</i> or use value &#8216;-&#8216; for no base. The default is the input base uri, either set by the argument INPUT-BASE-URI or via options <code>-I, &#8211;input-uri URI</code></p>
<dt><code>-c, &#8211;count</code></p>
<dd> Only count the triples and produce no other output.</p>
<dt><code>-e, &#8211;ignore-errors</code></p>
<dd> Ignore errors, do not emit the messages and try to continue parsing.</p>
<dt><code>-f, &#8211;feature FEATURE[=VALUE]</code></p>
<dd> Set a parser or serializer feature <i>FEATURE</i> to a value, or to 1 if <i>VALUE</i> is omitted, Use -f help to get lists of valid parser and serializer features.</p>
<dt>
<dd> If the form -f &#8216;xmlns:<i>prefix</i>=&quot;<i>uri</i>&quot;&#8217; is used, the prefix and namespace uri given will be set for serializing. The syntax matches XML in that either or both of <i>prefix</i> or <i>uri</i> can be omitted.</p>
<dt><code>-g, &#8211;guess</code></p>
<dd> Guess the parser to use from the source-URI rather than use the -i FORMAT.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> No extra information messages.</p>
<dt><code>-r, &#8211;replace-newlines</code></p>
<dd> Replace newlines in multi-line literals with spaces.</p>
<dt><code>&#8211;show-graphs</code></p>
<dd> Print graph names (URIs) as they are seen in the input. This only has a meaning for parsers that support graph names such as the TRiG parser.</p>
<dt><code>&#8211;show-namespaces</code></p>
<dd> Print namespaces as they are seen in the input.</p>
<dt><code>-t, &#8211;trace</code></p>
<dd> Print URIs retrieved during parsing. Especially useful for monitoring what the guess and GRDDL parsers are doing.</p>
<dt><code>-w, &#8211;ignore-warnings</code></p>
<dd> Ignore warnings, do not emit the messages.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the raptor version and exit.</dl>
<h2>EXAMPLES</h2>
<p> <code>rapper -q -i ntriples -o rdfxml -f &#8216;xmlns:rss=<a rel="nofollow" href="http://purl.org/rss/1.0/'">http://purl.org/rss/1.0/&#8217;</a> -f &#8216;xmlns:ex=<a href="http://example.org/'">http://example.org/&#8217;</a> tests/test.nt</code><br />
 <code>rapper -q -o rdfxml -f &#8216;xmlns:rdfs=<a rel="nofollow" href="http://www.w3.org/2000/01/rdf-schema#'">http://www.w3.org/2000/01/rdf-schema#&#8217;</a> tests/rdf-schema.rdf &#8216;<a href="http://www.w3.org/2000/01/rdf-schema#'">http://www.w3.org/2000/01/rdf-schema#&#8217;</a></code></p>
<h2>CONFORMING TO</h2>
<p> <i>RDF/XML Syntax (Revised)</i>, W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-syntax-grammar/">http://www.w3.org/TR/rdf-syntax-grammar/</a> </p>
<p> <i>N-Triples</i>, in <i>RDF Test Cases</i>, Jan Grant and Dave Beckett (eds.), W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a> </p>
<p> <i>Turtle Terse RDF Triple Language</i>, Dave Beckett, <a rel="nofollow" href="http://www.dajobe.org/2004/01/turtle/">http://www.dajobe.org/2004/01/turtle/</a> </p>
<p> <i>RDFA in XHTML: Syntax and Processing</i>, Ben Adida, Mark Birbeck, Shane McCarron and Steven Pemberton (eds.), W3C Candidate Recommendation, 20 June 2008 <a rel="nofollow" href="http://www.w3.org/TR/2008/CR-rdfa-syntax-20080620/">http://www.w3.org/TR/2008/CR-rdfa-syntax-20080620/</a> </p>
<p> <i>RDF Site Summary (RSS) 1.0</i>, 2000-12-06 <a rel="nofollow" href="http://purl.org/rss/1.0/spec">http://purl.org/rss/1.0/spec</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libraptor/">libraptor</a>(3),</code><a href="/docs/linux/man/1-raptor-config/">raptor-config</a>(1)</p>
<h2>CHANGES</h2>
<h3>2.0.0</h3>
<p> Removed -a option that did nothing. </p>
<p> Removed -m option from rapper but it was never documented here. </p>
<p> Removed -n option that was long hidden. </p>
<p> Removed -s option that was equivalent to -f scanForRDF</p>
<h3>1.4.16</h3>
<p> Added -I/&#8211;input-uri and -O/&#8211;output-uri to set the input and output (parser and serializer) base URIs separately.</p>
<h3>1.4.15</h3>
<p> Added -t/&#8211;trace to do URI traces.</p>
<h3>1.4.5</h3>
<p> Updated to add serializer rdfxml-abbrev</p>
<h3>1.4.3</h3>
<p> Updated potential parser and serializers and described -f for defining namespaces.</p>
<h3>1.3.0</h3>
<p> Added -f for features.<br />
 Added -g for guessing the parser to use.</p>
<h3>1.1.0</h3>
<p> Removed -a, &#8211;assume since rdf:RDF is now always optional. </p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
<h2>Index</h2>

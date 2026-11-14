---
title: "libraptor2(3)"
name: "libraptor2"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libraptor2/"
description: "libraptor2 – Raptor RDF syntax library 2.0"
---

<h2 class="name">NAME</h2>
<p> libraptor2 &#8211; Raptor RDF syntax library 2.0 </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;raptor2.h&gt;

world = raptor_new_world();

raptor_parser *p = raptor_new_parser(world, rdfxml);

raptor_set_statement_handler(p, NULL, print_triples);

raptor_uri *file_uri=raptor_new_uri(world,http://example.org/);

raptor_parser_parse_file(p,file_uri,base_uri);

raptor_parser_parse_uri(p,uri,NULL);

raptor_free_parser(p);

raptor_free_uri(file_uri);

raptor_free_world(world);

cc prog.c -o prog `pkg-config raptor2 --cflags` `pkg-config raptor2 --libs`
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>Raptor</i> library provides a high-level interface to a set of parsers and serializers that generate Resource Description Framework (RDF) triples by parsing syntaxes or serialize the triples into syntaxes. </p>
<p> The supported parsing syntaxes include RDF/XML, N-Triples, Turtle, TRiG, RSS tag soup (including all RSS and Atoms), GRDDL, RDF/JSON, RDFa and the serializing syntaxes include RDF/XML (3 varieties), N-Quads, N-Triples, Turtle, RSS 1.0, Atom 1.0, GraphViz DOT and RDF/JSON. The RDF/XML parser can use either <i>expat</i> or <i>libxml</i> XML parsers for providing the SAX event stream. The library functions are arranged in an object-oriented style with constructors, destructors and method calls. The statements and error messages are delivered via callback functions. </p>
<p> Raptor also contains classes to support the RDF graph triples: a statement object containing term objects and support for RDF URI-References for both parsing them and resolving / retrieval of URIs. </p>
<p> It some utility classes such as an I/O Stream abstraction for supporting reading and writing to and from a variety of locations, AVL Trees, String buffers and Sequences. </p>
<p> Raptor uses Unicode strings for RDF literals and URIs and preserves them throughout the library. It uses the UTF-8 encoding of Unicode at the API for passing in or returning Unicode strings. It is intended that the preservation of Unicode for URIs supports Internationalized Resource Identifiers (IRIs).</p>
<h2>API REFERENCE</h2>
<p> See the HTML API docs that may be installed system wide at /usr/share/gtk-doc/html/raptor2/ or on the web at <a rel="nofollow" href="http://librdf.org/raptor/api/">http://librdf.org/raptor/api/</a></p>
<h2>API CHANGES</h2>
<p> See the Raptor API docs changes section at <a rel="nofollow" href="http://librdf.org/raptor/api/raptor-changes.html">http://librdf.org/raptor/api/raptor-changes.html</a> and the upgrading information when converting from <a href="/docs/linux/man/1-libraptor/">libraptor</a>(1) code at <a rel="nofollow" href="http://librdf.org/raptor/UPGRADING.html">http://librdf.org/raptor/UPGRADING.html</a> </p>
<h2>CONFORMING TO</h2>
<p> <i>RDF/XML Syntax (Revised)</i>, Dave Beckett (ed.) W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-syntax-grammar/">http://www.w3.org/TR/rdf-syntax-grammar/</a> </p>
<p> <i>N-Triples</i>, in <i>RDF Test Cases</i>, Jan Grant and Dave Beckett (eds.) W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a> </p>
<p> <i>Turtle &#8211; Terse RDF Triple Language</i>, Dave Beckett, <a rel="nofollow" href="http://www.dajobe.org/2004/01/turtle/">http://www.dajobe.org/2004/01/turtle/</a> </p>
<p> <i>RSS 0.91 spec revision 3</i>, Dan Libby, Netscape, <a rel="nofollow" href="http://my.netscape.com/publish/formats/rss-spec-0.91.html">http://my.netscape.com/publish/formats/rss-spec-0.91.html</a> </p>
<p> <i>RDF Site Summary (RSS) 1.0</i>, <a rel="nofollow" href="http://purl.org/rss/1.0/spec">http://purl.org/rss/1.0/spec</a> </p>
<p> <i>Atom 1.0 syndication format</i>, RFC 4287, <a rel="nofollow" href="http://www.ietf.org/rfc/rfc4287.txt">http://www.ietf.org/rfc/rfc4287.txt</a> </p>
<p> <i>Gleaning Resource Descriptions from Dialects of Languages (GRDDL)</i>, Dan Connolly (ed.), W3C Recommendation, 2007-09-11, <a rel="nofollow" href="http://www.w3.org/TR/2007/REC-grddl-20070911/">http://www.w3.org/TR/2007/REC-grddl-20070911/</a> </p>
<p> <i>RDFa in XHTML: Syntax and Processing</i>, Ben Adida, Mark Birbeck, Shane McCarron, Steven Pemberton (eds.)<br />
&nbsp;<wbr>W3C Recommendation, 2008-10-14, <a rel="nofollow" href="http://www.w3.org/TR/2008/REC-rdfa-syntax-20081014/">http://www.w3.org/TR/2008/REC-rdfa-syntax-20081014/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rapper/">rapper</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://www.dajobe.org/">http://www.dajobe.org/</a> </p>
<h2>Index</h2>

---
title: "librasqal(3)"
name: "librasqal"
section: "3"
letter: "l"
url: "/docs/linux/man/3-librasqal/"
description: "librasqal – Rasqal RDF query library"
---

<h2 class="name">NAME</h2>
<p> librasqal &#8211; Rasqal RDF query library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;rasqal.h&gt;

&amp;nbsp;

rasqal_world *world = rasqal_new_world();

rasqal_query_results *results;

raptor_uri *base_uri = raptor_new_uri("http://example.org/foo");

rasqal_query *rq = rasqal_new_query(world, "rdql", NULL);

const char *query_string = "select * from &lt;http://example.org/data.rdf&gt;";

&amp;nbsp;

rasqal_query_prepare(rq, query_string, base_uri);

results = rasqal_query_execute(rq);

while (!rasqal_query_results_finished(results))
    &amp;nbsp;
{

    &amp;nbsp;
    for (i = 0; i &lt; rasqal_query_results_get_bindings_count(results); i++) {

        &amp;nbsp;
        &amp;nbsp;
        const char *name = rasqal_query_results_get_binding_name(results, i);

        &amp;nbsp;
        &amp;nbsp;
        rasqal_literal *value = rasqal_query_results_get_binding_value(results, i);

        &amp;nbsp;
        &amp;nbsp; /* ... */

        &amp;nbsp;
    }

    &amp;nbsp;
    rasqal_query_results_next(results);
}

rasqal_free_query_results(results);

rasqal_free_query(rq);

raptor_free_uri(base_uri);

rasqal_free_world(world);

cc prog.c - o prog `pkg - config rasqal-- cflags` `pkg - config rasqal-- libs`
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>Rasqal</i> library provides a high-level interface to RDF query parsing, query construction, query execution over an RDF graph and query results manipulation and formatting. The library provides APIs to each of the steps in the process and provides support for handling multiple query language syntaxes. At present Rasqal supports most of the W3C SPARQL 1.0 Query language, some of SPARQL 1.1 draft and fully supports RDQL. </p>
<p> Rasqal uses the <a href="/docs/linux/man/3-libraptor/">libraptor</a>(3) library for providing URI handling, WWW content retrieval and other support functions.</p>
<h2>API REFERENCE</h2>
<p> See the HTML API docs that may be installed system wide at /usr/share/gtk-doc/html/rasqal/ or on the web at <a rel="nofollow" href="http://librdf.org/rasqal/docs/api/">http://librdf.org/rasqal/docs/api/</a></p>
<h2>API CHANGES</h2>
<p> See the Raptor API docs changes section at <a rel="nofollow" href="http://librdf.org/rasqal/docs/api/rasqal-changes.html">http://librdf.org/rasqal/docs/api/rasqal-changes.html</a></p>
<h2>CONFORMING TO</h2>
<p> <i>SPARQL Query Language for RDF</i>, Eric Prud&#8217;hommeaux and Andy Seaborne (eds), W3C Recommendation, 15 January 2008 <a rel="nofollow" href="http://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/">http://www.w3.org/TR/2008/REC-rdf-sparql-query-20080115/</a> </p>
<p> <i>SPARQL Query Results XML Format</i>, Jeen Broekstra and Dave Beckett (eds), W3C Recommendation, 15 January 2008. <a rel="nofollow" href="http://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115/">http://www.w3.org/TR/2008/REC-rdf-sparql-XMLres-20080115/</a> </p>
<p> <i>RDQL &#8211; A Query Language for RDF</i>, Andy Seaborne, W3C Member Submission 9 January 2004 <a rel="nofollow" href="http://www.w3.org/Submission/2004/SUBM-RDQL-20040109/">http://www.w3.org/Submission/2004/SUBM-RDQL-20040109/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-roqet/">roqet</a></code>(1),<code><a href="/docs/linux/man/3-libraptor/">libraptor</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> Dave Beckett &#8211; <a rel="nofollow" href="http://purl.org/net/dajobe/">http://purl.org/net/dajobe/</a> </p>
<h2>Index</h2>

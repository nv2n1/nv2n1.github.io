---
title: "tracker3-endpoint(1)"
name: "tracker3-endpoint"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-endpoint/"
description: "tracker3-endpoint – Create a SPARQL endpoint"
---

<h2 class="name">NAME</h2>
<p> tracker3-endpoint &#8211; Create a SPARQL endpoint </p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker3 endpoint[--dbus - service | -b]&lt;service_name&gt;[--database - path | -d]&lt;database_path&gt;[[--ontology | -o]&lt;ontology_name&gt; |
                                                                                              [--ontology - path | -p]&lt;ontology_path&gt;]
                                                                                             [--http - port]&lt;port&gt;[--loopback]
                                                                                                                  [[--system | --session]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command allows creating SPARQL endpoints. The endpoint will be able to handle SPARQL select and update queries, and notify about changes in it. </p>
<p> The endpoint is exported via DBus, accessible through the given <i>service_name</i>, either using it in a <code>SERVICE</code> clause, or by creating a dedicated bus-based SPARQL connection. </p>
<p> When creating a database, the <i>ontology_name</i> (or alternatively, a <i>ontology_path</i>) must be provided in order to generate the database. If <i>ontology_name</i> is used, the ontology must exist in <i>$datadir/tracker/ontologies</i> </p>
<p> The database itself will be stored according to <i>database_path</i>.</p>
<h2>OPTIONS</h2>
<p> <code>-b, &#8211;dbus-service=&lt;</code><i>service_name</i><code>&gt;</code></p>
<dl>
<dt>
<dd> Service name to use on the endpoint.</dl>
<p> <code>-d, &#8211;database-path=&lt;</code><i>database_path</i><code>&gt;</code></p>
<dl>
<dt>
<dd> The path where the database will be stored.</dl>
<p> <code>-o, &#8211;ontology</code></p>
<dl>
<dt>
<dd> The name of an ontology in <i>$datadir/tracker/ontologies</i> to use on the constructed database.</dl>
<p> <code>-p, &#8211;ontology-path</code></p>
<dl>
<dt>
<dd> Full path to an ontology to use on the constructed database.</dl>
<p> <code>&#8211;session</code></p>
<dl>
<dt>
<dd> Use the session bus. This is the default.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Use the system bus.</dl>
<p> <code>-l, &#8211;list</code></p>
<dl>
<dt>
<dd> List all SPARQL endpoints available in DBus</dl>
<p> <code>&#8211;http-port</code></p>
<dl>
<dt>
<dd> Creates a HTTP endpoint that listens in the specified port</dl>
<p> <code>&#8211;loopback</code></p>
<dl>
<dt>
<dd> Allows only HTTP connections in the loopback device. Only effective with HTTP endpoints.</dl>
<h2>EXAMPLES</h2>
<p> Export a Nepomuk endpoint with the <i>org.example.Example1</i> bus name. </p>
<dl>
<dt>
<dd>
<pre>
$ tracker3 endpoint -b org.example.Example1 -o nepomuk -d /tmp/example1
</pre>
</dl>
<p> Access this endpoint with the <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a>(1)</code> subcommand. </p>
<dl>
<dt>
<dd>
<pre>
$ tracker3 sparql --dbus-service org.example.Example1 -q &quot;
  SELECT ?s ?o
  WHERE {
    ?u a ?o
  }&quot;
</pre>
</dl>
<p> Export a Nepomuk endpoint via HTTP. </p>
<dl>
<dt>
<dd>
<pre>
$ tracker3 endpoint --http-port 8080 -o nepomuk --loopback
</pre>
</dl>
<p> Access this endpoint via HTTP. </p>
<dl>
<dt>
<dd>
<pre>
$ tracker3 sparql --remote-service <a rel="nofollow" href="http://127.0.0.1:8080/sparql">http://127.0.0.1:8080/sparql</a> -q &quot;
  SELECT ?u {
    ?u a rdfs:Resource
  }&quot;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1), </p>
<p> <a rel="nofollow" href="https://www.w3.org/TR/sparql11-query/">https://www.w3.org/TR/sparql11-query/</a> </p>
<h2>Index</h2>

---

title: "serdi(1)"
name: "serdi"
section: "1"
letter: "s"
url: "/docs/linux/man/1-serdi/"
description: "serdi – Read and write RDF syntax"
---

<p> <code>serdi &#8211; Read and write RDF syntax</code></p>
<h2>SYNOPSIS</h2>
<p> serdi [OPTION]&#8230; INPUT BASE_URI </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> Fast bulk output for large serialisations. </dd>
<dt><code>-c PREFIX</code></dt>
<dd> Chop PREFIX from matching blank node IDs. </dd>
<dt><code>-e</code></dt>
<dd> Eat input one character at a time, rather than a page at a time which is the default. This is useful when reading from a pipe since output will be generated immediately as input arrives, rather than waiting until an entire page of input has arrived. With this option serdi uses one page less memory, but will likely be significantly slower. </dd>
<dt><code>-f</code></dt>
<dd> Keep full URIs in input (don&#8217;t qualify). </dd>
<dt><code>-h</code></dt>
<dd> Print the command line options. </dd>
<dt><code>-i SYNTAX</code></dt>
<dd> Read input in SYNTAX (`turtle&#8217; or `ntriples&#8217;). </dd>
<dt><code>-o SYNTAX</code></dt>
<dd> Write output in SYNTAX (`turtle&#8217; or `ntriples&#8217;). </dd>
<dt><code>-p PREFIX</code></dt>
<dd> Add PREFIX to blank node IDs. </dd>
<dt><code>-r ROOT_URI</code></dt>
<dd> Keep relative URIs within ROOT_URI. </dd>
<dt><code>-s INPUT</code></dt>
<dd> Parse INPUT as a string (terminates options). </dd>
<dt><code>-v</code></dt>
<dd> Display version information and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Serdi was written by David Robillard &lt;d@drobilla.net&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2011-2012 David Robillard.<br />
 License: &lt;<a rel="nofollow" href="http://www.opensource.org/licenses/isc">http://www.opensource.org/licenses/isc</a>&gt;<br />
 This is free software; you are free to change and redistribute it.<br />
 There is NO WARRANTY, to the extent permitted by law. </p>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://drobilla.net/software/serd">http://drobilla.net/software/serd</a>&gt; </p>

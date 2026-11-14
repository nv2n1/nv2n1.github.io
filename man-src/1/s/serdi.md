---
title: "serdi(1)"
name: "serdi"
section: "1"
letter: "s"
url: "/docs/linux/man/1-serdi/"
description: "serdi – Read and write RDF syntax"
---

<h2 class="name">NAME</h2>
<p> <code>serdi &#8211; Read and write RDF syntax</code></p>
<h2>SYNOPSIS</h2>
<p> serdi [OPTION]&#8230; INPUT BASE_URI </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Fast bulk output for large serialisations. </p>
<dt><code>-c PREFIX</code></p>
<dd> Chop PREFIX from matching blank node IDs. </p>
<dt><code>-e</code></p>
<dd> Eat input one character at a time, rather than a page at a time which is the default. This is useful when reading from a pipe since output will be generated immediately as input arrives, rather than waiting until an entire page of input has arrived. With this option serdi uses one page less memory, but will likely be significantly slower. </p>
<dt><code>-f</code></p>
<dd> Keep full URIs in input (don&#8217;t qualify). </p>
<dt><code>-h</code></p>
<dd> Print the command line options. </p>
<dt><code>-i SYNTAX</code></p>
<dd> Read input in SYNTAX (`turtle&#8217; or `ntriples&#8217;). </p>
<dt><code>-o SYNTAX</code></p>
<dd> Write output in SYNTAX (`turtle&#8217; or `ntriples&#8217;). </p>
<dt><code>-p PREFIX</code></p>
<dd> Add PREFIX to blank node IDs. </p>
<dt><code>-r ROOT_URI</code></p>
<dd> Keep relative URIs within ROOT_URI. </p>
<dt><code>-s INPUT</code></p>
<dd> Parse INPUT as a string (terminates options). </p>
<dt><code>-v</code></p>
<dd> Display version information and exit. </p>
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
<h2>Index</h2>

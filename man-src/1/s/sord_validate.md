---
title: "sord_validate(1)"
name: "sord_validate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sord_validate/"
description: "sord_validate – Validate RDF data"
---

<h2 class="name">NAME</h2>
<p> <code>sord_validate &#8211; Validate RDF data</code></p>
<h2>SYNOPSIS</h2>
<p> sord_validate [OPTION]&#8230; INPUT&#8230; </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print the command line options. </p>
<dt><code>-l</code></p>
<dd> Print errors on a single line. </p>
<dt><code>-v</code></p>
<dd> Display version information and exit. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> This is a simple validator which checks that all used properties are actually defined, and that the domain and range of properties is explicitly correct. Note that an &quot;error&quot; from this program does not necessarily mean data is invalid, since it is not required to explicitly list types in RDF, however it is a good idea to do so. </p>
<p> This program never retrieves data from the web or magical places on the file system, it only processes files passed directly on the command line. This means you must pass all used vocabularies to get a useful result. </p>
<p> If an appropriate schema is available, literals are checked against datatype definitions (both the explicit datatype of the literal itself as well as any types implied by the corresponding property). Three XML Schema Datatypes (XSD) constraints are currently supported: regular expressions (xsd:pattern), and inclusive range (xsd:minimumInclusive and xsd:maximumInclusive). Given an appropriate schema, this is enough to validate against most of the standard XSD datatypes. </p>
<h2>EXAMPLES</h2>
<p> sord_validate `find ~/schemas/ -name &#8216;*.ttl&#8217;` data.ttl </p>
<h2>AUTHOR</h2>
<p> sord_validate was written by David Robillard &lt;d@drobilla.net&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012-2013 David Robillard.<br />
 License: &lt;<a rel="nofollow" href="http://www.opensource.org/licenses/isc-license">http://www.opensource.org/licenses/isc-license</a>&gt;<br />
 This is free software; you are free to change and redistribute it.<br />
 There is NO WARRANTY, to the extent permitted by law. </p>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://drobilla.net/software/sord">http://drobilla.net/software/sord</a>&gt; </p>
<h2>Index</h2>

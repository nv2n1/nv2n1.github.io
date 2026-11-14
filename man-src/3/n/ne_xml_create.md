---
title: "ne_xml_create(3)"
name: "ne_xml_create"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_xml_create/"
description: "ne_xml_create, ne_xml_destroy – create and destroy an XML parser"
---

<p>ne_xml_create, ne_xml_destroy &#8211; create and destroy an XML parser</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_xml.h&gt;

ne_xml_parser *ne_xml_create(void);

void ne_xml_destroy(ne_xml_parser *parser);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_xml_create</code> function creates an XML parser object, which can be used for parsing XML documents using stacked SAX handlers.</p>
<h2>Return Value</h2>
<p><code>ne_xml_create</code> returns a pointer to an XML parser object, and never NULL</p>
<h2>See Also</h2>
<p>XXX</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>

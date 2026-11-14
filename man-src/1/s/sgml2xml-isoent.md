---
title: "sgml2xml-isoent(1)"
name: "sgml2xml-isoent"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgml2xml-isoent/"
description: "sgml2xml-isoent – Convert SGML to XML with support for ISO entities"
---

<h2>NAME</h2>
<p> sgml2xml-isoent &#8211; Convert SGML to XML with support for ISO entities</p>
<h2>SYNOPSIS</h2>
<p> <code>sgml2xml-isoent</code> [<i>sgml-document</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>sgml2xml-isoent</code> converts an SGML document to XML, with support for the ISO entities. This is done by using <code><a href="/docs/linux/man/1-sgml2xml/">sgml2xml</a></code>(1) from the SP package (or <code><a href="/docs/linux/man/1-osx/">osx</a></code>(1) from the OpenSP package), and the declaration for the XML version of the ISO entities is added to the output. This means that the output of this conversion should work as-is with any XML tool. </p>
<p> This program is often used for processing SGML DocBook documents with XML-based tools. In particular, <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1) calls this program as part of its <code>&#8211;sgml</code> option. On the other hand, it is probably not helpful for migrating a source SGML text file to XML, since the conversion mangles the original formatting. </p>
<p> Since the XML version of the ISO entities are referred to directly, not via a DTD, this tool also works with document types other than DocBook.</p>
<h2>NOTES</h2>
<p> The ISO entities are referred using the public identifiers ISO 8879:1986//ENTITIES//<i>&#8230;</i>//EN//XML. The catalogs used when parsing the converted document should resolve these entities to the appropriate place (on the local filesystem). If the entities are not resolved in the catalog, then the fallback is to get the entity files from the <a rel="nofollow" href="http://www.docbook.org/">http://www.docbook.org/</a> Web site.</p>
<h2>AUTHOR</h2>
<p> Steve Cheng &lt;stevecheng [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sgml2xml/">sgml2xml</a></code>(1), <code><a href="/docs/linux/man/1-osx/">osx</a></code>(1) </p>
<h2>Index</h2>

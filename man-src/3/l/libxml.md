---
title: "libxml(3)"
name: "libxml"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libxml/"
description: "libxml – library used to parse XML files"
---

<h2 class="name">NAME</h2>
<p> libxml &#8211; library used to parse XML files </p>
<h2>DESCRIPTION</h2>
<p> The <i>libxml</i> library is used to parse XML files. Its internal document representation is as close as possible to the <i>DOM </i> (Document Object Model) interface, an API for accessing XML or HTML structured documents. </p>
<p> The <i>libxml</i> library also has a <i>SAX</i>-like interface, which is designed to be compatible with <i><a href="/docs/linux/man/1-expat/">expat</a></i>(1). NOTE: <i>SAX</i>, the Simple API for XML, is a standard interface for event-based XML parsing, developed collaboratively by the members of the XML-DEV mailing list, currently hosted by OASIS. The <i>expat</i> library is a XML 1.0 parser written in C, which aims to be fully conforming. It is currently not a validating XML processor. </p>
<p> The <i>libxml </i> library now includes a nearly complete <i>XPath </i> implementation. The <i>XPath</i> (XML Path Language) is a language for addressing parts of an XML document, designed to be used by both <i>XSLT </i> and <i>XPointer</i>. </p>
<p> The <i>libxml </i> library exports Push and Pull type parser interfaces for both XML and <i>html</i>.</p>
<h2>FILES</h2>
<dl>
<dt><code>/depot/lib/libxml_2.0.0/libxml.a</code></p>
<dd> static library</p>
<dt><code>/depot/lib/libxml_2.0.0/libxml.so</code></p>
<dd> shared library</p>
<dt><code>/depot/package/libxml_2.0.0/bin/xmllint</code></p>
<dd> binary application for parsing XML files</dl>
<h2>AUTHORS</h2>
<p> Daniel Veillard (daniel [at] veillard.com). Red Hat Inc. Manual page by Ziying Sherwin (sherwin [at] nlm.nih.gov), Lister Hill National Center for Biomedical Communications, U.S. National Library of Medicine.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-xmllint/">xmllint</a></i>(1), <i><a href="/docs/linux/man/3-libxslt/">libxslt</a></i>(3), <i><a href="/docs/linux/man/3-libexslt/">libexslt</a></i>(3), <i><a href="/docs/linux/man/1-xsltproc/">xsltproc</a></i>(1) </p>
<h2>Index</h2>

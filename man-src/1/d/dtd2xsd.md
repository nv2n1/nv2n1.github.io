---
title: "dtd2xsd(1)"
name: "dtd2xsd"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dtd2xsd/"
description: "dtd2xsd – XML Schema generator from XML document that contains DTD."
---

<h2>NAME</h2>
<p> dtd2xsd &#8211; XML Schema generator from XML document that contains DTD.</p>
<h2>SYNOPSIS</h2>
<p> <code>dtd2xsd</code> [options] <i>instance-xmlfile</i> <i>optional-xsdfile</i></p>
<h2>DESCRIPTION</h2>
<p> dtd2xsd generates an XML schema document from a document type definition (DTD). Right now you have to specify instance XML file that references or contains DTD. DTD itself is not readable with this tiny tool. </p>
<p> By default, it outputs resulting XML schema to console. If optional-xsdfile parameter is specified, it outputs the result to the specified file.</p>
<h2>AUTHOR</h2>
<p> Atsushi Enomoto &lt;atsushi [at] ximian.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mono/">mono</a>(1) </p>
<h2>Index</h2>

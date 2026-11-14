---
title: "xmltoman(1)"
name: "xmltoman"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmltoman/"
description: "xmltoman – xml to man converter"
---

<h2>NAME</h2>
<p> xmltoman &#8211; xml to man converter</p>
<h2>SYNOPSIS</h2>
<p> <code>xmltoman </code><i>file.1.xml</i><code> &gt; file.1 </code></p>
<h2>DESCRIPTION</h2>
<p> xmltoman is a small script to convert xml to a man page in groff format. It features the usual man page items such a description, options, see also etc. The xml format also supports converting to html pages. </p>
<p> You will find the dtd in <i>/usr/share/xmltoman/</i> on a debian system. There is also an xsl file to generate html using <code><a href="/docs/linux/man/1-xsltproc/">xsltproc</a>(1)</code>. See also <i>/usr/share/doc/xmltoman/examples</i> for examples.</p>
<h2>FILES</h2>
<p> <i>/usr/share/xmltoman/xmltoman.dtd</i> the DTD file. </p>
<p> <i>/usr/share/xmltoman/xmltoman.xsl</i> XSLT stylesheet to generate html. </p>
<p> <i>/usr/share/xmltoman/xmltoman.css</i> stylesheet to be used for HTML.</p>
<h2>AUTHOR</h2>
<p> xmltoman was written by Oliver Kurth &lt;oku [at] masqmail.cx&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xmlmantohtml/">xmlmantohtml</a>(1)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code><a href="/docs/linux/man/1-xmltoman/">xmltoman</a>(1)</code> by the same author. </p>
<h2>Index</h2>

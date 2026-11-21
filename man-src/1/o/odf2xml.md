---
title: "odf2xml(1)"
name: "odf2xml"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odf2xml/"
description: "odf2xml – Create OpenDocument XML file from OD? package"
---

<p>odf2xml &#8211; Create OpenDocument XML file from OD? package</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>odf2xml</code> [-e] [-o&nbsp;<wbr><i>outputfile</i>] [<i>inputfile</i>]</dt></dl>
<h2>Description</h2>
<dd>OpenDocument can be a complete office document in a single XML file. The script will take an OpenDocument and create an XML file This is mainly useful XML processors such as XSL transformation. </dd>
<p> &quot;Inputfile&quot; is assumed to be an OpenDocument file. If there is no inputfile, the program will read from standard input.</p>
<h2>Options</h2>
<p> -e</p>
<dl>
<dt>
</dt><dd> Normally, images that are stored in the archive in the Pictures folder are ignored. Using the -e flag will <i>embed</i> the images in the XML as base64.</dd></dl>
<p> -o <i>outputfile</i></p>
<dl>
<dt>
</dt><dd> If output file is not specified output will be to standard out.</dd></dl>
<h2>Example</h2>
<dl>
<dt>
</dt><dd> <font SIZE="-1"> </font></dd>
<pre>
odf2xml -o file.xml  testdocument.odt
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-xml2odf/">xml2odf</a></code>(1)</p>
<h2>Bugs</h2>
<p> Doesn&#8217;t handle external data &#8212; images and such.</p>
<h2>Author</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
</dt><dd> Original author</dd></dl>

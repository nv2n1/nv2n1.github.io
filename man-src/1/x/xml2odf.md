---
title: "xml2odf(1)"
name: "xml2odf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2odf/"
description: "xml2odf – Create ODF package from OpenDocument in XML form"
---

<p>xml2odf &#8211; Create ODF package from OpenDocument in XML form</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>xml2odf</code> [-o&nbsp;<wbr><i>outputfile</i>] [-s] [<i>inputfile</i>]</dl>
<h2>Description</h2>
<dd>OpenDocument can be a complete office document in a single XML file. The script will take such a document and create a package. This is mainly useful as a postprocesser of a program producing XML, such as a stylesheet. </p>
<p> &#8220;Inputfile&#8221; is assumed to be an OpenDocument file in XML form. If there is no inputfile, the program will read from standard input. The flag -s adds correct suffix to the filename according to what mime type is found in the XML file, in cause you don&#8217;t know already what document type you are packaging. </p>
<p> If output file is not specified output will be to standard out. </p>
<p> Section 2.1.1 of Open Document Format for Office Applications says that the [content.xml] file contains the document content, along with the <i>automatic styles</i> needed for the document content. The [styles.xml] file contains all the named styles of a document, along with the <i>automatic styles</i> needed for the named styles. The application doesn&#8217;t know which automatic style is needed for what, so it puts the same set of automatic styles into both files. </p>
<p> One could assume that the inverse operation would be easier, but OpenOffice.org is quite happy to use the same names for two different automatic styles. For instance, a style used inside &lt;style:footer&gt; can have the same name as one used inside &lt;office:text&gt; but be a different paragraph style. This is reported as bug #90494 (<a rel="nofollow" href="http://www.openoffice.org/issues/show_bug.cgi?id=90494)">http://www.openoffice.org/issues/show_bug.cgi?id=90494)</a></p>
<h2>Example</h2>
<dl>
<dt>
<dd> <font SIZE="-1"> </font></p>
<pre>
xml2odf -o testdocument -s xml-file
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-odftools/">odftools</a></code>(1), <code><a href="/docs/linux/man/1-odf2xml/">odf2xml</a></code>(1)</p>
<h2>Bugs</h2>
<p> Doesn&#8217;t handle external data &#8212; images and such. </p>
<p> The library used for the parsing of XML expands empty elements from &lt;element/&gt; to &lt;element&gt;&lt;/element&gt;. It should not have an effect on the document parsing.</p>
<h2>Author</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>

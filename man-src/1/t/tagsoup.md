---
title: "tagsoup(1)"
name: "tagsoup"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tagsoup/"
description: "tagsoup – convert nasty, ugly HTML to clean XHTML"
---

<h2>NAME</h2>
<p> tagsoup &#8211; convert nasty, ugly HTML to clean XHTML</p>
<h2>SYNOPSIS</h2>
<p> <code>java -jar tagsoup</code> [ <i>options</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Rectify arbitrary HTML into clean XHTML, using a tailored description of HTML. The output will be well-formed XML, but not necessarily <i>valid</i> XHTML. </p>
<dl>
<dt><code>&#8211;files</code></dt>
<dd> multiple input <i>files</i> should be processed into corresponding output files</dd>
<dt><code>&#8211;encoding=</code><i>encoding</i></dt>
<dd> specifies the encoding of input files</dd>
<dt><code>&#8211;output-encoding=</code><i>encoding</i></dt>
<dd> specifies the encoding of the output (if the encoding name begins with &#8220;utf&#8221;, the output will not contain character entities; otherwise, all non-ASCII characters are represented as entities)</dd>
<dt><code>&#8211;html</code></dt>
<dd> output rectified HTML rather than XML, omitting the XML declaration and any namespace declarations</dd>
<dt><code>&#8211;method=html</code></dt>
<dd> output rectified HTML rather than XML (end-tags are omitted for empty elements, and no character escaping is done in script and style elements)</dd>
<dt><code>&#8211;omit-xml-declaration</code></dt>
<dd> omit the XML declaration</dd>
<dt><code>&#8211;lexical</code></dt>
<dd> output lexical features (specifically comments and any DOCTYPE declaration)</dd>
<dt><code>&#8211;nons</code></dt>
<dd> suppress namespaces in output</dd>
<dt><code>&#8211;nobogons</code></dt>
<dd> suppress unknown non-HTML elements in output</dd>
<dt><code>&#8211;nodefaults</code></dt>
<dd> suppress default attribute values</dd>
<dt><code>&#8211;nocolons</code></dt>
<dd> change explicit colons in element and attribute names to underscores</dd>
<dt><code>&#8211;norestart</code></dt>
<dd> don&#8217;t restart any restartable elements</dd>
<dt><code>&#8211;ignorable</code></dt>
<dd> pass through ignorable whitespace (whitespace in element-only content) via SAX method handler ignorableWhitespace</dd>
<dt><code>&#8211;any</code></dt>
<dd> treat unknown non-HTML elements as allowing any content (default)</dd>
<dt><code>&#8211;emptybogons</code></dt>
<dd> treat unknown non-HTML elements as empty elements</dd>
<dt><code>&#8211;norootbogons</code></dt>
<dd> don&#8217;t allow unknown non-HTML elements to be root elements</dd>
<dt><code>&#8211;doctype-system=</code><i>system-id</i></dt>
<dd> force DOCTYPE declaration to be output with specified system identifier</dd>
<dt><code>&#8211;doctype-public=</code><i>public-id</i></dt>
<dd> force DOCTYPE declaration to be output with specified public identifier</dd>
<dt><code>&#8211;standalone=[yes|no]</code></dt>
<dd> specify standalone pseudo-attribute in output XML declaration</dd>
<dt><code>&#8211;version=</code><i>version</i></dt>
<dd> specify version pseudo-attribute in output XML declaration (does not affect actual version of XML output)</dd>
<dt><code>&#8211;nocdata</code></dt>
<dd> treat the CDATA-content elements <i>script</i> and <i>style</i> as ordinary elements (mostly for testing)</dd>
<dt><code>&#8211;pyx</code></dt>
<dd> output PYX format rather than XML (mostly for testing)</dd>
<dt><code>&#8211;pyxin</code></dt>
<dd> input is PYX-format HTML (mostly for testing)</dd>
<dt><code>&#8211;reuse</code></dt>
<dd> reuse the same Parser object internally (for testing only)</dd>
<dt><code>&#8211;help</code></dt>
<dd> output basic help</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version number</dd></dl>
<p> <code>TagSoup</code> is a parser and reformatter for nasty, ugly HTML. Its normal processing mode is to accept HTML files on the command line, or from the standard input if none are given, and output them as clean XML to the standard output. The encoding is assumed to be the platform-local encoding on input, and is always UTF-8 on output. </p>
<p> When the <code>&#8211;files</code> option is given, each input file is processed into an output file of the corresponding name, with the extension changed to <i>xhtml</i>. If the extension is already <i>xhtml</i>, it is changed to <i>xhtml_</i>. </p>
<p> TagSoup will repair, by whatever means necessary, violations of XML well-formedness. In particular, it will fix up malformed attribute names and supply missing attribute-value quotation marks. More significantly, it supplies end-tags where HTML allows them to be omitted, and sometimes where it doesn&#8217;t. It will even supply start-tags where necessary; for example, if a document begins with a &lt;li&gt; tag, TagSoup will automatically prefix it with &lt;html&gt;&lt;body&gt;&lt;ul&gt;. </p>
<h2>BUGS</h2>
<p> TagSoup can be fooled by missing close quotes after attribute values, and by incorrect character encodings (it does not contain an encoding guesser). </p>
<p> TagSoup doesn&#8217;t understand namespace declarations, which are not properly part of HTML. Instead, any element or attribute name beginning <i>foo</i>: will be put into the artificial namespace urn:x-prefix:<i>foo</i>. </p>
<p> For the same reasons, namespace-qualified attributes like xml:space can&#8217;t be returned as default values, though an explicit attribute in the xml namespace will be returned with the proper namespace URI.</p>
<h2>AUTHOR</h2>
<p> John Cowan &lt;cowan [at] ccil.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2008 John Cowan<br />
 TagSoup is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>

---
title: "db2x_xsltproc(1)"
name: "db2x_xsltproc"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db2x_xsltproc/"
description: "db2x_xsltproc – XSLT processor invocation wrapper"
---

<h2>NAME</h2>
<p> db2x_xsltproc &#8211; XSLT processor invocation wrapper</p>
<h2>SYNOPSIS</h2>
<p> <code>db2x_xsltproc</code> [<i>options</i>] <i>xml-document</i></p>
<h2>DESCRIPTION</h2>
<p> <code>db2x_xsltproc</code> invokes the XSLT 1.0 processor for docbook2X. </p>
<p> This command applies the XSLT stylesheet (usually given by the <code>&#8211;stylesheet</code> option) to the XML document in the file <i>xml-document</i>. The result is written to standard output (unless changed with <code>&#8211;output</code>). </p>
<p> To read the source XML document from standard input, specify &#8211; as the input document.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Display the docbook2X version.</dl>
<h3>TRANSFORMATION OUTPUT OPTIONS</h3>
<dl>
<dt><code>&#8211;output </code><i>file</i>, <code>-o </code><i>file</i></p>
<dd> Write output to the given file (or URI), instead of standard output.</dl>
<h3>SOURCE DOCUMENT OPTIONS</h3>
<dl>
<dt><code>&#8211;xinclude</code>, <code>-I</code></p>
<dd> Process XInclude directives in the source document.</p>
<dt><code>&#8211;sgml</code>, <code>-S</code></p>
<dd> Indicate that the input document is SGML instead of XML. You need this set this option if <i>xml-document</i> is actually a SGML file. </p>
<p> SGML parsing is implemented by conversion to XML via <code><a href="/docs/linux/man/1-sgml2xml/">sgml2xml</a></code>(1) from the SP package (or <code><a href="/docs/linux/man/1-osx/">osx</a></code>(1) from the OpenSP package). All tag names in the SGML file will be normalized to lowercase (i.e. the <code>-xlower</code> option of <code><a href="/docs/linux/man/1-sgml2xml/">sgml2xml</a></code>(1) is used). ID attributes are available for the stylesheet (i.e. option <code>-xid</code>). In addition, any ISO SDATA entities used in the SGML document are automatically converted to their XML Unicode equivalents. (This is done by a <code>sed</code> filter.) </p>
<p> The encoding of the SGML document, if it is not us-ascii, must be specified with the standard SP environment variables: <code>SP_CHARSET_FIXED=1 SP_ENCODING=</code><i>encoding</i>. (Note that XML files specify their encoding with the XML declaration <code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;</code><i>encoding&quot;</i><code> ?&gt;</code> at the top of the file.) </p>
<p> The above conversion options cannot be changed. If you desire different conversion options, you should invoke <code><a href="/docs/linux/man/1-sgml2xml/">sgml2xml</a></code>(1) manually, and then pass the results of that conversion to this program.</dl>
<h3>RETRIEVAL OPTIONS</h3>
<dl>
<dt><code>&#8211;catalogs </code><i>catalog-files</i>, <code>-C </code><i>catalog-files</i></p>
<dd> Specify additional XML catalogs to use for resolving Formal Public Identifiers or URIs. SGML catalogs are not supported. </p>
<p> These catalogs are <i>not</i> used for parsing an SGML document under the <code>&#8211;sgml</code> option. Use the environment variable <code>SGML_CATALOG_FILES</code> instead to specify the catalogs for parsing the SGML document.</p>
<dt><code>&#8211;network</code>, <code>-N</code></p>
<dd> <code>db2x_xsltproc</code> will normally refuse to load external resources from the network, for security reasons. If you do want to load from the network, set this option. </p>
<p> Usually you want to have installed locally the relevent DTDs and other files, and set up catalogs for them, rather than load them automatically from the network.</dl>
<h3>STYLESHEET OPTIONS</h3>
<dl>
<dt><code>&#8211;stylesheet </code><i>file</i>, <code>-s </code><i>file</i></p>
<dd> Specify the filename (or URI) of the stylesheet to use. The special values man and texi are accepted as abbreviations, to specify that <i>xml-document</i> is in DocBook and should be converted to man pages or Texinfo (respectively).</p>
<dt><code>&#8211;param </code><i>name</i><code>=</code><i>expr</i>, <code>-p </code><i>name</i><code>=</code><i>expr</i></p>
<dd> Add or modify a parameter to the stylesheet. <i>name</i> is a XSLT parameter name, and <i>expr</i> is an XPath expression that evaluates to the desired value for the parameter. (This means that strings must be quoted, <i>in addition</i> to the usual quoting of shell arguments; use <code>&#8211;string-param</code> to avoid this.)</p>
<dt><code>&#8211;string-param </code><i>name</i><code>=</code><i>string</i>, <code>-g </code><i>name</i><code>=</code><i>string</i></p>
<dd> Add or modify a string-valued parameter to the stylesheet. </p>
<p> The string must be encoded in UTF-8 (regardless of the locale character encoding).</dl>
<h3>DEBUGGING AND PROFILING</h3>
<dl>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd> Display, to standard error, logs of what is happening during the XSL transformation.</p>
<dt><code>&#8211;nesting-limit </code><i>n</i>, <code>-D </code><i>n</i></p>
<dd> Change the maximum number of nested calls to XSL templates, used to detect potential infinite loops. If not specified, the limit is 500 (libxslt&#8217;s default).</p>
<dt><code>&#8211;profile</code>, <code>-P</code></p>
<dd> Display profile information: the total number of calls to each template in the stylesheet and the time taken for each. This information is output to standard error.</p>
<dt><code>&#8211;xslt-processor </code><i>processor</i>, <code>-X </code><i>processor</i></p>
<dd> Select the underlying XSLT processor used. The possible choices for <i>processor</i> are: libxslt, saxon, xalan-j. </p>
<p> The default processor is whatever was set when docbook2X was built. libxslt is recommended (because it is lean and fast), but SAXON is much more robust and would be more helpful when debugging stylesheets. </p>
<p> All the processors have XML catalogs support enabled. (docbook2X requires it.) But note that not all the options above work with processors other than the libxslt one.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>XML_CATALOG_FILES</code></p>
<dd> Specify XML Catalogs. If not specified, the standard catalog (<i>/etc/xml/catalog</i>) is loaded, if available.</p>
<dt><code>DB2X_XSLT_PROCESSOR</code></p>
<dd> Specify the XSLT processor to use. The effect is the same as the <code>&#8211;xslt-processor</code> option. The primary use of this variable is to allow you to quickly test different XSLT processors without having to add <code>&#8211;xslt-processor</code> to every script or make file in your documentation build system.</dl>
<h2>CONFORMING TO</h2>
<p> XML Stylesheet Language &#8211; Transformations (XSLT), version 1.0 &lt;<a rel="nofollow" href="http://www.w3.org/TR/xslt">http://www.w3.org/TR/xslt</a>&gt; , a W3C Recommendation.</p>
<h2>NOTES</h2>
<p> In its earlier versions (&lt; 0.8.4), docbook2X required XSLT extensions to run, and <code>db2x_xsltproc</code> was a special libxslt-based processor that had these extensions compiled-in. When the requirement for XSLT extensions was dropped, <code>db2x_xsltproc</code> became a Perl script which translates the options to <code>db2x_xsltproc</code> to conform to the format accepted by the stock <code><a href="/docs/linux/man/1-xsltproc/">xsltproc</a></code>(1) which comes with libxslt. </p>
<p> The prime reason for the existence of this script is backward compatibility with any scripts or make files that invoke docbook2X. However, it also became easy to add in support for invoking other XSLT processors with a unified command-line interface. Indeed, there is nothing special in this script to docbook2X, or even to DocBook, and it may be used for running other sorts of stylesheets if you desire. Certainly the author prefers using this command, because its invocation format is sane and is easy to use. (e.g. no typing long class names for the Java-based processors!)</p>
<h2>AUTHOR</h2>
<p> Steve Cheng &lt;stevecheng [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> The docbook2X manual (in Texinfo or HTML format) fully describes how to convert DocBook to man pages and Texinfo. </p>
<p> Up-to-date information about this program can be found at the docbook2X Web site &lt;<a rel="nofollow" href="http://docbook2x.sourceforge.net/">http://docbook2x.sourceforge.net/</a>&gt; . </p>
<p> You may wish to consult the documentation that comes with libxslt, SAXON, or Xalan. The W3C XSLT 1.0 specification would be useful for writing stylesheets. </p>
<h2>Index</h2>

---
title: "xsltproc(1)"
name: "xsltproc"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsltproc/"
description: "xsltproc – command line XSLT processor"
---

<h2 class="name">NAME</h2>
<p> xsltproc &#8211; command line XSLT processor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xsltproc</code> [[<code>-V</code> | <code>&#8211;version</code>] [<code>-v</code> | <code>&#8211;verbose</code>] [{<code>-o</code> | <code>&#8211;output</code>} {<i>FILE</i> | <i>DIRECTORY</i>}] | <code>&#8211;timing</code> | <code>&#8211;repeat</code> | <code>&#8211;debug</code> | <code>&#8211;novalid</code> | <code>&#8211;noout</code> | <code>&#8211;maxdepth&nbsp;<wbr></code><i>VALUE</i> | <code>&#8211;html</code> | <code>&#8211;encoding&nbsp;<wbr></code><i>ENCODING</i><code>&nbsp;<wbr></code> | <code>&#8211;param&nbsp;<wbr></code><i>PARAMNAME</i><code>&nbsp;<wbr></code><i>PARAMVALUE</i><code>&nbsp;<wbr></code> | <code>&#8211;stringparam&nbsp;<wbr></code><i>PARAMNAME</i><code>&nbsp;<wbr></code><i>PARAMVALUE</i><code>&nbsp;<wbr></code> | <code>&#8211;nonet</code> | <code>&#8211;path&nbsp;<wbr>&quot;</code><i>PATH(S)</i><code>&quot;</code> | <code>&#8211;load-trace</code> | <code>&#8211;catalogs</code> | <code>&#8211;xinclude</code> | [<code>&#8211;profile</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;norman</code>] | <code>&#8211;dumpextensions</code> | <code>&#8211;nowrite</code> | <code>&#8211;nomkdir</code> | <code>&#8211;writesubtree&nbsp;<wbr></code><i>PATH</i> | <code>&#8211;nodtdattr</code>] [<i>STYLESHEET</i>] {<i>XML-FILE</i> | -}</dl>
<h2>DESCRIPTION</h2>
<p> <code>xsltproc</code></p>
<dd>is a command line tool for applying XSLT stylesheets to XML documents. It is part of <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3), the XSLT C library for GNOME. While it was developed as part of the GNOME project, it can operate independently of the GNOME desktop. </p>
<p> <code>xsltproc</code> is invoked from the command line with the name of the stylesheet to be used followed by the name of the file or files to which the stylesheet is to be applied. It will use the standard input if a filename provided is <code>&#8211;</code> . </p>
<p> If a stylesheet is included in an XML document with a Stylesheet Processing Instruction, no stylesheet need to be named at the command line. <code>xsltproc</code> will automatically detect the included stylesheet and use it. </p>
<p> By default, output is to <i>stdout</i>. You can specify a file for output using the <code>-o</code> or <code>&#8211;output</code> option.</p>
<h2>OPTIONS</h2>
<p> <code>xsltproc</code> accepts the following options (in alphabetical order): </p>
<p> <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> Use the SGML catalog specified in <code>SGML_CATALOG_FILES</code> to resolve the location of external entities. By default, <code>xsltproc</code> looks for the catalog specified in <code>XML_CATALOG_FILES</code>. If that is not specified, it uses <i>/etc/xml/catalog</i>.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Output an XML tree of the transformed document for debugging purposes.</dl>
<p> <code>&#8211;dumpextensions</code></p>
<dl>
<dt>
<dd> Dumps the list of all registered extensions on <i>stdout</i>.</dl>
<p> <code>&#8211;html</code></p>
<dl>
<dt>
<dd> The input document is an HTML file.</dl>
<p> <code>&#8211;load-trace</code></p>
<dl>
<dt>
<dd> Display all the documents loaded during the processing to <i>stderr</i>.</dl>
<p> <code>&#8211;maxdepth </code><i>VALUE</i></p>
<dl>
<dt>
<dd> Adjust the maximum depth of the template stack before <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3) concludes it is in an infinite loop. The default is 3000.</dl>
<p> <code>&#8211;nodtdattr</code></p>
<dl>
<dt>
<dd> Do not apply default attributes from the document&#8217;s DTD.</dl>
<p> <code>&#8211;nomkdir</code></p>
<dl>
<dt>
<dd> Refuses to create directories.</dl>
<p> <code>&#8211;nonet</code></p>
<dl>
<dt>
<dd> Do not use the Internet to fetch DTDs, entities or documents.</dl>
<p> <code>&#8211;noout</code></p>
<dl>
<dt>
<dd> Do not output the result.</dl>
<p> <code>&#8211;novalid</code></p>
<dl>
<dt>
<dd> Skip loading the document&#8217;s DTD.</dl>
<p> <code>&#8211;nowrite</code></p>
<dl>
<dt>
<dd> Refuses to write to any file or resource.</dl>
<p> <code>-o</code> or <code>&#8211;output</code> <i>FILE</i> | <i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Direct output to the given <i>FILE</i>. Using the option with a <i>DIRECTORY</i> directs the output files to the specified directory. This can be useful for multiple outputs (also known as &quot;chunking&quot;) or manpage processing. </p>
<p> Important The given directory <code>must</code> already exist. </p>
<p> Note Make sure that <i>FILE</i> and <i>DIRECTORY</i> follow the &#8220;URI reference computation&#8221; as described in RFC 2396 and laters. This means, that e.g. <code>-o directory</code> will maybe not work, but <code>-o directory/</code> will.</dl>
<p> <code>&#8211;encoding </code><i>ENCODING</i></p>
<dl>
<dt>
<dd> Allow to specify the encoding for the input.</dl>
<p> <code>&#8211;param </code><i>PARAMNAME</i><i>PARAMVALUE</i></p>
<dl>
<dt>
<dd> Pass a parameter of name <i>PARAMNAME</i> and value <i>PARAMVALUE</i> to the stylesheet. You may pass multiple name/value pairs up to a maximum of 32. If the value being passed is a string, you can use <code>&#8211;stringparam</code> instead, to avoid additional quote characters that appear in string expressions. Note: the XPath expression must be UTF-8 encoded.</dl>
<p> <code>&#8211;path &quot;</code><i>PATH(S)</i><code>&quot;</code></p>
<dl>
<dt>
<dd> Use the (space- or colon-separated) list of filesystem paths specified by <i>PATHS</i> to load DTDs, entities or documents. Enclose space-separated lists by quotation marks.</dl>
<p> <code>&#8211;profile</code> or <code>&#8211;norman</code></p>
<dl>
<dt>
<dd> Output profiling information detailing the amount of time spent in each part of the stylesheet. This is useful in optimizing stylesheet performance.</dl>
<p> <code>&#8211;repeat</code></p>
<dl>
<dt>
<dd> Run the transformation 20 times. Used for timing tests.</dl>
<p> <code>&#8211;stringparam </code><i>PARAMNAME</i><i>PARAMVALUE</i></p>
<dl>
<dt>
<dd> Pass a parameter of name <i>PARAMNAME</i> and value <i>PARAMVALUE</i> where <i>PARAMVALUE</i> is a string rather than a node identifier. <code>Note:</code> The string must be UTF-8 encoded.</dl>
<p> <code>&#8211;timing</code></p>
<dl>
<dt>
<dd> Display the time used for parsing the stylesheet, parsing the document and applying the stylesheet and saving the result. Displayed in milliseconds.</dl>
<p> <code>-v</code> or <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Output each step taken by <code>xsltproc</code> in processing the stylesheet and the document.</dl>
<p> <code>-V</code> or <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the version of <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) and <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3) used.</dl>
<p> <code>&#8211;writesubtree </code><i>PATH</i></p>
<dl>
<dt>
<dd> Allow file write only within the <i>PATH</i> subtree.</dl>
<p> <code>&#8211;xinclude</code></p>
<dl>
<dt>
<dd> Process the input document using the XInclude specification. More details on this can be found in the XInclude specification: <i><a rel="nofollow" href="http://www.w3.org/TR/xinclude/">http://www.w3.org/TR/xinclude/</a></i></dl>
<h2>ENVIRONMENT</h2>
<p> <code>SGML_CATALOG_FILES</code></p>
<dl>
<dt>
<dd> SGML catalog behavior can be changed by redirecting queries to the user&#8217;s own set of catalogs. This can be done by setting the <code>SGML_CATALOG_FILES</code> environment variable to a list of catalogs. An empty one should deactivate loading the default <i>/etc/sgml/catalog</i> catalog.</dl>
<p> <code>XML_CATALOG_FILES</code></p>
<dl>
<dt>
<dd> XML catalog behavior can be changed by redirecting queries to the user&#8217;s own set of catalogs. This can be done by setting the <code>XML_CATALOG_FILES</code> environment variable to a list of catalogs. An empty one should deactivate loading the default <i>/etc/xml/catalog</i> catalog.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>xsltproc</code> return codes provide information that can be used when calling it from scripts. </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> No error (normal operation)</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> No argument</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> Too many parameters</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> Unknown option</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> Failed to parse the stylesheet</dl>
<p> <code>5</code></p>
<dl>
<dt>
<dd> Error in the stylesheet</dl>
<p> <code>6</code></p>
<dl>
<dt>
<dd> Error in one of the documents</dl>
<p> <code>7</code></p>
<dl>
<dt>
<dd> Unsupported xsl:output method</dl>
<p> <code>8</code></p>
<dl>
<dt>
<dd> String parameter contains both quote and double-quotes</dl>
<p> <code>9</code></p>
<dl>
<dt>
<dd> Internal processing error</dl>
<p> <code>10</code></p>
<dl>
<dt>
<dd> Processing was stopped by a terminating message</dl>
<p> <code>11</code></p>
<dl>
<dt>
<dd> Could not write the result to the output file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3), <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3) </p>
<p> More information can be found at </p>
<dl>
<dt>
<dd> &bull;<code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) web page <i><a rel="nofollow" href="http://www.xmlsoft.org/">http://www.xmlsoft.org/</a></i></dl>
<dl>
<dt>
<dd> &bull;W3C XSLT page <i><a rel="nofollow" href="http://www.w3.org/TR/xslt">http://www.w3.org/TR/xslt</a></i></dl>
<h2>AUTHOR</h2>
<p> <code>John Fleck</code> &lt;jfleck [at] inkstain.net&gt; </p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001, 2002 </p>
<h2>Index</h2>

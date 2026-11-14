---
title: "xmllint(1)"
name: "xmllint"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmllint/"
description: "xmllint – command line XML tool"
---

<h2 class="name">NAME</h2>
<p> xmllint &#8211; command line XML tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xmllint</code> [<code>&#8211;version</code> | <code>&#8211;debug</code> | <code>&#8211;shell</code> | <code>&#8211;xpath&nbsp;&quot;</code><i>XPath_expression</i><code>&quot;</code> | <code>&#8211;debugent</code> | <code>&#8211;copy</code> | <code>&#8211;recover</code> | <code>&#8211;noent</code> | <code>&#8211;noout</code> | <code>&#8211;nonet</code> | <code>&#8211;path&nbsp;&quot;</code><i>PATH(S)</i><code>&quot;</code> | <code>&#8211;load-trace</code> | <code>&#8211;htmlout</code> | <code>&#8211;nowrap</code> | <code>&#8211;valid</code> | <code>&#8211;postvalid</code> | <code>&#8211;dtdvalid&nbsp;</code><i>URL</i> | <code>&#8211;dtdvalidfpi&nbsp;</code><i>FPI</i> | <code>&#8211;timing</code> | <code>&#8211;output&nbsp;</code><i>FILE</i> | <code>&#8211;repeat</code> | <code>&#8211;insert</code> | <code>&#8211;compress</code> | <code>&#8211;html</code> | <code>&#8211;xmlout</code> | <code>&#8211;push</code> | <code>&#8211;memory</code> | <code>&#8211;maxmem&nbsp;</code><i>NBBYTES</i> | <code>&#8211;nowarning</code> | <code>&#8211;noblanks</code> | <code>&#8211;nocdata</code> | <code>&#8211;format</code> | <code>&#8211;encode&nbsp;</code><i>ENCODING</i> | <code>&#8211;dropdtd</code> | <code>&#8211;nsclean</code> | <code>&#8211;testIO</code> | <code>&#8211;catalogs</code> | <code>&#8211;nocatalogs</code> | <code>&#8211;auto</code> | <code>&#8211;xinclude</code> | <code>&#8211;noxincludenode</code> | <code>&#8211;loaddtd</code> | <code>&#8211;dtdattr</code> | <code>&#8211;stream</code> | <code>&#8211;walker</code> | <code>&#8211;pattern&nbsp;</code><i>PATTERNVALUE</i> | <code>&#8211;chkregister</code> | <code>&#8211;relaxng&nbsp;</code><i>SCHEMA</i> | <code>&#8211;schema&nbsp;</code><i>SCHEMA</i> | <code>&#8211;c14n</code>] {<i>XML-FILE(S)</i>&#8230; | -}</p>
<dt> <code>xmllint</code> <code>&#8211;help</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>xmllint</code> program parses one or more XML files, specified on the command line as <i>XML-FILE</i> (or the standard input if the filename provided is <code>&#8211;</code> ). It prints various types of output, depending upon the options selected. It is useful for detecting errors both in XML code and in the XML parser itself. </p>
<p> <code>xmllint</code> is included in <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3).</p>
<h2>OPTIONS</h2>
<p> <code>xmllint</code> accepts the following options (in alphabetical order): </p>
<p> <code>&#8211;auto</code></p>
<dl>
<dt>
<dd> Generate a small document for testing purposes.</dl>
<p> <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> Use the SGML catalog(s) from <code>SGML_CATALOG_FILES</code>. Otherwise XML catalogs starting from /etc/xml/catalog are used by default.</dl>
<p> <code>&#8211;chkregister</code></p>
<dl>
<dt>
<dd> Turn on node registration. Useful for developers testing <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) node tracking code.</dl>
<p> <code>&#8211;compress</code></p>
<dl>
<dt>
<dd> Turn on <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) compression of output.</dl>
<p> <code>&#8211;copy</code></p>
<dl>
<dt>
<dd> Test the internal copy implementation.</dl>
<p> <code>&#8211;c14n</code></p>
<dl>
<dt>
<dd> Use the W3C XML Canonicalisation (C14N) to serialize the result of parsing to stdout. It keeps comments in the result.</dl>
<p> <code>&#8211;dtdvalid </code><i>URL</i></p>
<dl>
<dt>
<dd> Use the DTD specified by an <i>URL</i> for validation.</dl>
<p> <code>&#8211;dtdvalidfpi </code><i>FPI</i></p>
<dl>
<dt>
<dd> Use the DTD specified by a Formal Public Identifier <i>FPI</i> for validation, note that this will require a catalog exporting that Formal Public Identifier to work.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Parse a file and output an annotated tree of the in-memory version of the document.</dl>
<p> <code>&#8211;debugent</code></p>
<dl>
<dt>
<dd> Debug the entities defined in the document.</dl>
<p> <code>&#8211;dropdtd</code></p>
<dl>
<dt>
<dd> Remove DTD from output.</dl>
<p> <code>&#8211;dtdattr</code></p>
<dl>
<dt>
<dd> Fetch external DTD and populate the tree with inherited attributes.</dl>
<p> <code>&#8211;encode </code><i>ENCODING</i></p>
<dl>
<dt>
<dd> Output in the given encoding. Note that this works for full document not fragments or result from XPath queries.</dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
<dd> Reformat and reindent the output. The <code>XMLLINT_INDENT</code> environment variable controls the indentation. The default value is two spaces &quot; &quot;).</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print out a short usage summary for <code>xmllint</code>.</dl>
<p> <code>&#8211;html</code></p>
<dl>
<dt>
<dd> Use the HTML parser.</dl>
<p> <code>&#8211;htmlout</code></p>
<dl>
<dt>
<dd> Output results as an HTML file. This causes <code>xmllint</code> to output the necessary HTML tags surrounding the result tree output so the results can be displayed/viewed in a browser.</dl>
<p> <code>&#8211;insert</code></p>
<dl>
<dt>
<dd> Test for valid insertions.</dl>
<p> <code>&#8211;loaddtd</code></p>
<dl>
<dt>
<dd> Fetch an external DTD.</dl>
<p> <code>&#8211;load-trace</code></p>
<dl>
<dt>
<dd> Display all the documents loaded during the processing to stderr.</dl>
<p> <code>&#8211;maxmem </code><i>NNBYTES</i></p>
<dl>
<dt>
<dd> Test the parser memory support. <i>NNBYTES</i> is the maximum number of bytes the library is allowed to allocate. This can also be used to make sure batch processing of XML files will not exhaust the virtual memory of the server running them.</dl>
<p> <code>&#8211;memory</code></p>
<dl>
<dt>
<dd> Parse from memory.</dl>
<p> <code>&#8211;noblanks</code></p>
<dl>
<dt>
<dd> Drop ignorable blank spaces.</dl>
<p> <code>&#8211;nocatalogs</code></p>
<dl>
<dt>
<dd> Do not use any catalogs.</dl>
<p> <code>&#8211;nocdata</code></p>
<dl>
<dt>
<dd> Substitute CDATA section by equivalent text nodes.</dl>
<p> <code>&#8211;noent</code></p>
<dl>
<dt>
<dd> Substitute entity values for entity references. By default, <code>xmllint</code> leaves entity references in place.</dl>
<p> <code>&#8211;nonet</code></p>
<dl>
<dt>
<dd> Do not use the Internet to fetch DTDs or entities.</dl>
<p> <code>&#8211;noout</code></p>
<dl>
<dt>
<dd> Suppress output. By default, <code>xmllint</code> outputs the result tree.</dl>
<p> <code>&#8211;nowarning</code></p>
<dl>
<dt>
<dd> Do not emit warnings from the parser and/or validator.</dl>
<p> <code>&#8211;nowrap</code></p>
<dl>
<dt>
<dd> Do not output HTML doc wrapper.</dl>
<p> <code>&#8211;noxincludenode</code></p>
<dl>
<dt>
<dd> Do XInclude processing but do not generate XInclude start and end nodes.</dl>
<p> <code>&#8211;nsclean</code></p>
<dl>
<dt>
<dd> Remove redundant namespace declarations.</dl>
<p> <code>&#8211;output </code><i>FILE</i></p>
<dl>
<dt>
<dd> Define a file path where <code>xmllint</code> will save the result of parsing. Usually the programs build a tree and save it on stdout, with this option the result XML instance will be saved onto a file.</dl>
<p> <code>&#8211;path &quot;</code><i>PATH(S)</i><code>&quot;</code></p>
<dl>
<dt>
<dd> Use the (space- or colon-separated) list of filesystem paths specified by <i>PATHS</i> to load DTDs or entities. Enclose space-separated lists by quotation marks.</dl>
<p> <code>&#8211;pattern </code><i>PATTERNVALUE</i></p>
<dl>
<dt>
<dd> Used to exercise the pattern recognition engine, which can be used with the reader interface to the parser. It allows to select some nodes in the document based on an XPath (subset) expression. Used for debugging.</dl>
<p> <code>&#8211;postvalid</code></p>
<dl>
<dt>
<dd> Validate after parsing has completed.</dl>
<p> <code>&#8211;push</code></p>
<dl>
<dt>
<dd> Use the push mode of the parser.</dl>
<p> <code>&#8211;recover</code></p>
<dl>
<dt>
<dd> Output any parsable portions of an invalid document.</dl>
<p> <code>&#8211;relaxng </code><i>SCHEMA</i></p>
<dl>
<dt>
<dd> Use RelaxNG file named <i>SCHEMA</i> for validation.</dl>
<p> <code>&#8211;repeat</code></p>
<dl>
<dt>
<dd> Repeat 100 times, for timing or profiling.</dl>
<p> <code>&#8211;schema </code><i>SCHEMA</i></p>
<dl>
<dt>
<dd> Use a W3C XML Schema file named <i>SCHEMA</i> for validation.</dl>
<p> <code>&#8211;shell</code></p>
<dl>
<dt>
<dd> Run a navigating shell. Details on available commands in shell mode are below (see the section called &#8220;SHELL COMMANDS&#8221;).</dl>
<p> <code>&#8211;xpath &quot;</code><i>XPath_expression</i><code>&quot;</code></p>
<dl>
<dt>
<dd> Run an XPath expression given as argument and print the result. In case of a nodeset result, each node in the node set is serialized in full in the output. In case of an empty node set the &quot;XPath set is empty&quot; result will be shown and an error exit code will be returned.</dl>
<p> <code>&#8211;stream</code></p>
<dl>
<dt>
<dd> Use streaming API &#8211; useful when used in combination with <code>&#8211;relaxng</code> or <code>&#8211;valid</code> options for validation of files that are too large to be held in memory.</dl>
<p> <code>&#8211;testIO</code></p>
<dl>
<dt>
<dd> Test user input/output support.</dl>
<p> <code>&#8211;timing</code></p>
<dl>
<dt>
<dd> Output information about the time it takes <code>xmllint</code> to perform the various steps.</dl>
<p> <code>&#8211;valid</code></p>
<dl>
<dt>
<dd> Determine if the document is a valid instance of the included Document Type Definition (DTD). A DTD to be validated against also can be specified at the command line using the <code>&#8211;dtdvalid</code> option. By default, <code>xmllint</code> also checks to determine if the document is well-formed.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version of <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) used.</dl>
<p> <code>&#8211;walker</code></p>
<dl>
<dt>
<dd> Test the walker module, which is a reader interface but for a document tree, instead of using the reader API on an unparsed document it works on an existing in-memory tree. Used for debugging.</dl>
<p> <code>&#8211;xinclude</code></p>
<dl>
<dt>
<dd> Do XInclude processing.</dl>
<p> <code>&#8211;xmlout</code></p>
<dl>
<dt>
<dd> Used in conjunction with <code>&#8211;html</code>. Usually when HTML is parsed the document is saved with the HTML serializer. But with this option the resulting document is saved with the XML serializer. This is primarily used to generate XHTML from HTML input.</dl>
<h2>SHELL COMMANDS</h2>
<p> <code>xmllint</code> offers an interactive shell mode invoked with the <code>&#8211;shell</code> command. Available commands in shell mode include (in alphabetical order): </p>
<p> <code>base</code></p>
<dl>
<dt>
<dd> Display XML base of the node.</dl>
<p> <code>bye</code></p>
<dl>
<dt>
<dd> Leave the shell.</dl>
<p> <code>cat </code><i>NODE</i></p>
<dl>
<dt>
<dd> Display the given node or the current one.</dl>
<p> <code>cd </code><i>PATH</i></p>
<dl>
<dt>
<dd> Change the current node to the given path (if unique) or root if no argument is given.</dl>
<p> <code>dir </code><i>PATH</i></p>
<dl>
<dt>
<dd> Dumps information about the node (namespace, attributes, content).</dl>
<p> <code>du </code><i>PATH</i></p>
<dl>
<dt>
<dd> Show the structure of the subtree under the given path or the current node.</dl>
<p> <code>exit</code></p>
<dl>
<dt>
<dd> Leave the shell.</dl>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Show this help.</dl>
<p> <code>free</code></p>
<dl>
<dt>
<dd> Display memory usage.</dl>
<p> <code>load </code><i>FILENAME</i></p>
<dl>
<dt>
<dd> Load a new document with the given filename.</dl>
<p> <code>ls </code><i>PATH</i></p>
<dl>
<dt>
<dd> List contents of the given path or the current directory.</dl>
<p> <code>pwd</code></p>
<dl>
<dt>
<dd> Display the path to the current node.</dl>
<p> <code>quit</code></p>
<dl>
<dt>
<dd> Leave the shell.</dl>
<p> <code>save </code><i>FILENAME</i></p>
<dl>
<dt>
<dd> Save the current document to the given filename or to the original name.</dl>
<p> <code>validate</code></p>
<dl>
<dt>
<dd> Check the document for errors.</dl>
<p> <code>write </code><i>FILENAME</i></p>
<dl>
<dt>
<dd> Write the current node to the given filename.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>SGML_CATALOG_FILES</code></p>
<dl>
<dt>
<dd> SGML catalog behavior can be changed by redirecting queries to the user&#8217;s own set of catalogs. This can be done by setting the <code>SGML_CATALOG_FILES</code> environment variable to a list of catalogs. An empty one should deactivate loading the default /etc/sgml/catalog catalog.</dl>
<p> <code>XML_CATALOG_FILES</code></p>
<dl>
<dt>
<dd> XML catalog behavior can be changed by redirecting queries to the user&#8217;s own set of catalogs. This can be done by setting the <code>XML_CATALOG_FILES</code> environment variable to a list of catalogs. An empty one should deactivate loading the default /etc/xml/catalog catalog.</dl>
<p> <code>XML_DEBUG_CATALOG</code></p>
<dl>
<dt>
<dd> Setting the environment variable <code>XML_DEBUG_CATALOG</code> to <i>non-zero</i> using the <code>export</code> command outputs debugging information related to catalog operations.</dl>
<p> <code>XMLLINT_INDENT</code></p>
<dl>
<dt>
<dd> Setting the environment variable <code>XMLLINT_INDENT</code> controls the indentation. The default value is two spaces &quot; &quot;.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>xmllint</code> return codes provide information that can be used when calling it from scripts. </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> No error</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Unclassified</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> Error in DTD</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> Validation error</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> Validation error</dl>
<p> <code>5</code></p>
<dl>
<dt>
<dd> Error in schema compilation</dl>
<p> <code>6</code></p>
<dl>
<dt>
<dd> Error writing output</dl>
<p> <code>7</code></p>
<dl>
<dt>
<dd> Error in pattern (generated when <code>&#8211;pattern</code> option is used)</dl>
<p> <code>8</code></p>
<dl>
<dt>
<dd> Error in Reader registration (generated when <code>&#8211;chkregister</code> option is used)</dl>
<p> <code>9</code></p>
<dl>
<dt>
<dd> Out of memory error</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) </p>
<p> More information can be found at </p>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) web page m[blue]<code><a rel="nofollow" href="http://www.xmlsoft.org/">http://www.xmlsoft.org/</a></code>m[]</dl>
<dl>
<dt>
<dd> &bull; W3C XSLT page m[blue]<code><a rel="nofollow" href="http://www.w3.org/TR/xslt">http://www.w3.org/TR/xslt</a></code>m[]</dl>
<h2>AUTHORS</h2>
<p> <code>John Fleck</code> &lt;jfleck [at] inkstain.net&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Ziying Sherwin</code> &lt;sherwin [at] nlm.nih.gov&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Heiko Rupp</code> &lt;hwr [at] pilhuhn.de&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001, 2004 </p>
<h2>Index</h2>

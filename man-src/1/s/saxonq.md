---
title: "saxonq(1)"
name: "saxonq"
section: "1"
letter: "s"
url: "/docs/linux/man/1-saxonq/"
description: "saxon8q – manual page for saxon8q"
---

<h2>NAME</h2>
<p> saxon8q &#8211; manual page for saxon8q</p>
<h2>SYNOPSIS</h2>
<p> <code>saxon8q</code> [<i>options</i>] <i>query </i>[ <i>params</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> saxon8q runs a query contained in a file. </p>
<h2>OPTIONS</h2>
<p> The options must come first, then the file name containing the query, then the params.</p>
<dl>
<dt>The options are as follows (in any order):</p>
<dd>
<dt><code>-cr</code> classname</p>
<dd> Use the specified CollectionURIResolver to process collection URIs passed to the collection() function. The CollectionURIResolver is a user-defined class that implements the net.sf.saxon.CollectionURIResolver interface.</p>
<dt><code>-ds</code></p>
<dd> Use the linked tree model for source documents. See Choosing a Tree Model.</p>
<dt><code>-dt</code></p>
<dd> Use the tinytree tree model for source documents. This is the default tree model. See Choosing a Tree Model.</p>
<dt><code>-e</code></p>
<dd> Display a query execution plan. This is a representation of the expression tree after rewriting by the optimizer.</p>
<dt><code>-l</code></p>
<dd> Causes line numbers to be maintained for source documents. These are accessible using the extension function saxon:line-number(). Line numbers are useful when the purpose of the query is to find errors or anomalies in the source XML file. Without this option, line numbers are available while source documents are being parsed and validated, but they are not retained in the tree representation of the document.</p>
<dt><code>-mr</code> classname</p>
<dd> Use the specified ModuleURIResolver to process all query module URIs. The ModuleURIResolver is a user-defined class that implements the net.sf.saxon.query.ModuleURIResolver interface. It is invoked to process URIs used in the import module declaration in the query prolog, and (if <code>-u</code> is also specified, or if the file name begins with http: or file:) to process the URI of the query source file provided on the command line.</p>
<dt><code>-noext</code></p>
<dd> Prevents the query calling external Java functions. This is useful for safety if the query is untrusted.</p>
<dt><code>-o</code> filename</p>
<dd> Send output to named file. In the absence of this option, the results go to standard output. The output format depends on whether the <code>-wrap</code> option is present.</p>
<dt><code>-p</code></p>
<dd> Use the PTreeURIResolver. This option is available in Saxon-SA only. It cannot be used in conjunction with the <code>-r</code> option, and it automatically switches on the <code>-u</code> and <code>-sa</code> options. The effect is twofold. Firstly, Saxon-specific file extensions are recognized in URIs (including the URI of the source document on the command line). Currently the only Saxon-specific file extension is .ptree, which indicates that the source document is supplied in the form of a Saxon PTree. This is a binary representation of an XML document, designed for speed of loading. Secondly, Saxon-specific query parameters are recognized in a URI. Currently the only query parameter that is recognized is val. This may take the values strict, lax, or strip. For example, source.xml?validation=strict loads a document with strict schema validation.</p>
<dt><code>-pull</code></p>
<dd> Execute query in pull mode. This may give performance advantages for certain kinds of query, especially queries that construct intermediate trees in memory.</p>
<dt><code>-r</code> classname</p>
<dd> Use the specified URIResolver to process all URIs. The URIResolver is a user-defined class, that implements the URIResolver interface defined in JAXP, whose function is to take a URI supplied as a string, and return a SAX InputSource. It is invoked to process URIs used in the doc() function, and (if <code>-u</code> is also specified) to process the URI of the source file provided on the command line.</p>
<dt><code>-s</code> filename-or-URI</p>
<dd> Take input from the specified file. If the <code>-u</code> option is specified, or if the name begins with file: or http:, then the name is assumed to be a URI rather than a filename. This file must contain an XML document. The document node of the document is made available to the query as the context item. The source document can be specified as &#8211; to take the source from standard input.</p>
<dt><code>-sall</code></p>
<dd> Strips all whitespace text nodes from source documents before any further processing, regardless of any xml:space attributes in the source document.</p>
<dt><code>-signorable</code></p>
<dd> Strips all ignorable whitespace text nodes from source documents before any further processing, regardless of any xml:space attributes in the source document. Whitespace text nodes are ignorable if they appear in elements defined in the DTD or schema as having element-only content.</p>
<dt><code>-snone</code></p>
<dd> Strips no whitespace before further processing.</p>
<dt><code>-strip</code></p>
<dd> Equivalent to <code>-sall</code>: retained for compatibility.</p>
<dt><code>-t</code></p>
<dd> Display version and timing information to the standard error output. The output also traces the files that are read and written, and extension modules that are loaded.</p>
<dt><code>-T</code></p>
<dd> Enable execution tracing. This will cause a trace of the query execution to be output to the standard error output. The events that are traced are currently function calls (entry and exit) and element construction.</p>
<dt><code>-TJ</code></p>
<dd> Switches on tracing of the binding of calls to external Java methods. This is useful when analyzing why Saxon fails to find a Java method to match an extension function call in the stylesheet, or why it chooses one method over another when several are available.</p>
<dt><code>-u</code></p>
<dd> Indicates that the name of the source document is a URI; otherwise it is taken as a filename, unless it starts with http: or file:, in which case they it is taken as a URL.</p>
<dt><code>-v</code></p>
<dd> Indicates that source documents are to be parsed using a validating parser (this invokes DTD validation, not schema validation).</p>
<dt><code>-val</code></p>
<dd> This option is available only with Saxon-SA, and it automatically switches on the <code>-sa</code> option. It requests strict validation of source documents using an XML Schema.</p>
<dt><code>-vlax</code></p>
<dd> This option is available only with Saxon-SA, and it automatically switches on the <code>-sa</code> option. It requests lax validation of source documents using an XML Schema. That is, the document will be validated if a suitable schema is available, and will not be validated otherwise.</p>
<dt><code>-vw</code></p>
<dd> Indicates that validation errors found when validating the result tree should be treated as warnings only. This option is available only with the Saxon-SA version of the command, com.saxonica.Query.</p>
<dt><code>-wrap</code></p>
<dd> Wraps the result sequence in an XML element structure that indicates the type of each node or atomic value in the query result. This format can handle any type of query result. In the absence of this option, the command effectively wraps a document{} constructor around the supplied query, so that the result is a single XML document, which is then serialized. This will fail if the query result includes constructs that cannot be added to a document node in this way, notably free-standing attribute nodes.</p>
<dt><code>-1</code>.1</p>
<dd> Allow XML 1.1 and XML Namespaces 1.1 constructs. This option must be set if source documents using XML 1.1 are to be read, or if result documents are to be serialized as XML 1.1. This option also enables use of XML 1.1 constructs within the query itself.</p>
<dt>-?</p>
<dd> Display command syntax</p>
<dt>query Identifies the file containing the query. Mandatory. The argument can be specified as &#8211; to read the query from standard input. The query can also be specified inline by enclosing it in curly braces (if it contains spaces, you will also need quotes outside the curly braces to keep the command line processor happy). For example java net.sf.saxon.Query {doc(&#8216;a.xml&#8217;)//p[1]} selects elements within the file a.xml in the current directory.</p>
<dd>
<p> A param takes the form name=value, name being the name of the parameter, and value the value of the parameter. These parameters are accessible within the query as external variables, using the syntax, provided they are declared in the query prolog. If there is no such declaration, the supplied parameter value is silently ignored.</dl>
<p> A param preceded by a leading plus sign (+) is interpreted as a filename or directory. The content of the file is parsed as XML, and the resulting document node is passed to the stylesheet as the value of the parameter. If the parameter value is a directory, then all the immediately contained files are parsed as XML, and the resulting sequence of document nodes is passed as the value of the parameter. For example, +lookup=lookup.xml sets the value of the external variable lookup to the document node at the root of the tree representing the parsed contents of the file lookup.xml. </p>
<p> A param preceded by a leading exclamation mark is interpreted as a serialization parameter. For example, !indent=yes requests indented output, and !encoding=iso-8859-1 requests that the serialized output be in ISO 8859/1 encoding. This is equivalent to specifying the option declaration declare option saxon:output indent=yes; or declare option saxon:output encoding=iso-8859-1; in the query prolog. </p>
<p> Under Windows, and some other operating systems, it is possible to supply a value containing spaces by enclosing it in double quotes, for example name=John Smith. This is a feature of the operating system shell, not something Saxon does, so it may not work the same way under every operating system. </p>
<p> If the parameter name is in a non-null namespace, the parameter can be given a value using the syntax {uri}localname=value. Here uri is the namespace URI of the parameter&#8217;s name, and localname is the local part of the name. </p>
<p> This applies also to output parameters. For example, you can set the indentation level to 4 by using the parameter !{<a rel="nofollow" href="http://saxon.sf.net/}indent-spaces=4.">http://saxon.sf.net/}indent-spaces=4.</a> For the extended set of output parameters supported by Saxon, see Additional serialization parameters.</p>
<h2>AUTHOR</h2>
<p> Michael H. Kay &lt;mike [at] saxonica.com&gt; </p>
<h2>Index</h2>

---
title: "saxon(1)"
name: "saxon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-saxon/"
description: "saxon8 – manual page for saxon8"
---

<h2>NAME</h2>
<p> saxon8 &#8211; manual page for saxon8</p>
<h2>SYNOPSIS</h2>
<p> <code>saxon8</code> [<i>options</i>] <i>source-document stylesheet </i>[ <i>params</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> saxon8 applies a given stylesheet to a given source XML document. </p>
<h2>OPTIONS</h2>
<p> For a schema-aware transformation, specify the option <code>-sa</code>, or (on the Java platform only) use the alternate entry point com.saxonica.Transform. For more details see Schema-Aware Transformations.</p>
<dl>
<dt>The options must come first, then the two file names, then the params. The stylesheet is omitted if the <code>-a</code> option is present.</p>
<dd>
<dt>The options are as follows (in any order):</p>
<dd>
<dt><code>-a</code></p>
<dd> Use the xml-stylesheet processing instruction in the source document to identify the stylesheet to be used. The stylesheet argument should be omitted.</p>
<dt><code>-c</code></p>
<dd> Indicates that the stylesheet argument identifies a compiled stylesheet rather than an XML source stylesheet. The stylesheet must have been previously compiled as described in Compiling a Stylesheet.</p>
<dt><code>-cr</code> classname</p>
<dd> Use the specified CollectionURIResolver to process collection URIs passed to the collection() function. The CollectionURIResolver is a user-defined class that implements the net.sf.saxon.CollectionURIResolver interface.</p>
<dt><code>-ds</code> | <code>-dt</code></p>
<dd> Selects the implementation of the internal tree model. <code>-dt</code> selects the tiny tree model (the default). <code>-ds</code> selects the linked tree model. See Choosing a tree model.</p>
<dt><code>-im</code> modename</p>
<dd> Selects the initial mode for the transformation. If this is namespaced, it can be written as {uri}localname</p>
<dt><code>-it</code> template</p>
<dd> Selects the initial named template to be executed. If this is namespaced, it can be written as {uri}localname. When this option is used, the source file should be omitted.</p>
<dt><code>-l</code></p>
<dd> Switches line numbering on for the source document. Line numbers are accessible through the extension function saxon:line-number(), or from a trace listener.</p>
<dt><code>-m</code> classname</p>
<dd> Use the specified Emitter to process the output from xsl:message. The class must implement the net.sf.saxon.output.Emitter class. This interface is similar to a SAX ContentHandler, it takes a stream of events to generate output. In general the content of a message is an XML fragment. By default the standard XML emitter is used, configured to write to the standard error stream, and to include no XML declaration. Each message is output as a new document.</p>
<dt><code>-noext</code></p>
<dd> Suppress calls on extension functions, other than system-supplied Saxon and EXSLT extension functions. This option is useful when loading an untrusted stylesheet, perhaps from a remote site using an http:// URL; it ensures that the stylesheet cannot call Java methods and thereby gain privileged access to resources on your machine.</p>
<dt><code>-novw</code></p>
<dd> No version warnings. This suppresses the warning message that is normally issued (as required by the W3C specification) when running an XSLT 2.0 processor against a stylesheet that specifies version=1.0.</p>
<dt><code>-o</code> filename</p>
<dd> Send output to named file. In the absence of this option, the results go to standard output. If the source argument identifies a directory, this option is mandatory and must also identify a directory; on completion it will contain one output file for each file in the source directory. If the stylesheet writes secondary output files using the xsl:result-document instruction; this filename acts as the base URI for the href attribute of this instruction. In the absence of this option, secondary output files are written relative to the current working directory.</p>
<dt><code>-p</code></p>
<dd> Use the PTreeURIResolver. This option is available in Saxon-SA only. It cannot be used in conjunction with the <code>-r</code> option, and it automatically switches on the <code>-u</code> and <code>-sa</code> options. The effect is twofold. Firstly, Saxon-specific file extensions are recognized in URIs (including the URI of the source document on the command line). Currently the only Saxon-specific file extension is .ptree, which indicates that the source document is supplied in the form of a Saxon PTree. This is a binary representation of an XML document, designed for speed of loading. Secondly, Saxon-specific query parameters are recognized in a URI. Currently the only query parameter that is recognized is val. This may take the values strict, lax, or strip. For example, source.xml?val=strict loads a document with strict schema validation.</p>
<dt><code>-r</code> classname</p>
<dd> Use the specified URIResolver to process all URIs. The URIResolver is a user-defined class, that extends the net.sf.saxon.URIResolver class, whose function is to take a URI supplied as a string, and return a SAX InputSource. It is invoked to process URIs used in the document() function, in the xsl:include and xsl:import elements, and (if <code>-u</code> is also specified) to process the URIs of the source file and stylesheet file provided on the command line.</p>
<dt><code>-sa</code></p>
<dd> Invoke a schema-aware transformation. Requires Saxon-SA to be installed.</p>
<dt><code>-sall</code></p>
<dd> Strips all whitespace text nodes from source documents before any further processing, regardless of any xsl:strip-space declarations in the stylesheet, or any xml:space attributes in the source document.</p>
<dt><code>-signorable</code></p>
<dd> Strips all ignorable whitespace text nodes from source documents before any further processing, regardless of any xsl:strip-space declarations in the stylesheet, or any xml:space attributes in the source document. Whitespace text nodes are ignorable if they appear in elements defined in the DTD or schema as having element-only content.</p>
<dt><code>-snone</code></p>
<dd> Strips no whitespace before further processing. (However, whitespace will still be stripped if this is specified in the stylesheet using xsl:strip-space).</p>
<dt><code>-t</code></p>
<dd> Display version and timing information to the standard error output. The output also traces the files that are read and writing, and extension modules that are loaded.</p>
<dt><code>-T</code></p>
<dd> Display stylesheet tracing information to the standard error output. This traces execution of each instruction in the stylesheet, so the output can be quite voluminous. Also switches line numbering on for the source document.</p>
<dt><code>-TJ</code></p>
<dd> Switches on tracing of the binding of calls to external Java methods. This is useful when analyzing why Saxon fails to find a Java method to match an extension function call in the stylesheet, or why it chooses one method over another when several are available.</p>
<dt><code>-TL</code> classname</p>
<dd> Run the stylesheet using the specified TraceListener. The classname names a user-defined class, which must implement net.sf.saxon.trace.TraceListener</p>
<dt><code>-TP</code></p>
<dd> Run the stylesheet using the TraceListener TimedTraceListener. This creates an output file giving timings for each instruction executed. This output file can subsequently be analyzed to give an execution time profile for the stylesheet. See Performance Analysis.</p>
<dt><code>-u</code></p>
<dd> Indicates that the names of the source document and the style document are URLs; otherwise they are taken as filenames, unless they start with http: or file:, in which case they are taken as URLs</p>
<dt><code>-v</code></p>
<dd> Requests DTD-based validation of the source file and of any files read using the document() function. Requires an XML parser that supports validation.</p>
<dt><code>-val</code></p>
<dd> Requests schema-based validation of the source file and of any files read using the document() function. This option is available only with Saxon-SA, and it automatically switches on the <code>-sa</code> option.</p>
<dt><code>-vlax</code></p>
<dd> This option is available only with Saxon-SA, and it automatically switches on the <code>-sa</code> option. It requests lax validation of source documents using an XML Schema. That is, the document will be validated if a suitable schema is available, and will not be validated otherwise.</p>
<dt><code>-vw</code></p>
<dd> Indicates that validation errors found when validating the result tree should be treated as warnings only. This option is available only with the Saxon-SA version of the command, com.saxonica.Transform.</p>
<dt><code>-w0</code>, w1, or w2</p>
<dd> Indicates the policy for handling recoverable errors in the stylesheet: w0 means recover silently, w1 means recover after writing a warning message to the system error output, w2 means signal the error and do not attempt recovery. (Note, this does not currently apply to all errors that the XSLT recommendation describes as recoverable). The default is w1.</p>
<dt><code>-x</code> classname</p>
<dd> Use specified SAX parser for source file and any files loaded using the document() function. The parser must be the fully-qualified class name of a Java class that implements the org.xml.sax.Parser or org.xml.sax.XMLReader interface</p>
<dt><code>-y</code> classname</p>
<dd> Use specified SAX parser for stylesheet file, including any loaded using xsl:include or xsl:import. The parser must be the fully-qualified class name of a Java class that implements the org.xml.sax.Parser or org.xml.sax.XMLReader interface</p>
<dt><code>-1</code>.1</p>
<dd> Allow XML 1.1 and XML Namespaces 1.1 constructs. This option must be set if source documents using XML 1.1 are to be read, or if result documents are to be serialized as XML 1.1. This option also enables use of XML 1.1 constructs within the stylesheet itself.</p>
<dt>-?</p>
<dd> Display command syntax</p>
<dt>source-document</p>
<dd> Identifies the source file or directory. Mandatory. If this is a directory, all the files in the directory will be processed individually. In this case the <code>-o</code> option is mandatory, and must also identify a directory, to contain the corresponding output files. A directory must be specified as a filename, not as a URL. The source-document can be specified as &#8211; to take the source from standard input.</p>
<dt>stylesheet</p>
<dd> Identifies the stylesheet. Mandatory unless the <code>-a</code> option is used. If the <code>-c</code> option is used, this argument identifies a compiled stylesheet. The stylesheet argument can be specified as &#8211; to read the stylesheet from standard input. </p>
<p> A param takes the form name=value, name being the name of the parameter, and value the value of the parameter. These parameters are accessible within the stylesheet as normal variables, using the syntax, provided they are declared using a top-level xsl:param element. If there is no such declaration, the supplied parameter value is silently ignored. If the xsl:param element has an as attribute indicating the required type, then the string value supplied on the command line is cast to this type: this may result in an error, for example if an integer is required and the supplied value cannot be converted to an integer.</p>
<dt>A param preceded by a leading exclamation mark (!) is interpreted as an output parameter. For example, !indent=yes requests indented output. This is equivalent to specifying the attribute indent=yes on an xsl:output declaration in the stylesheet. An output parameter specified on the command line overrides one specified within the stylesheet.</p>
<dd>
<dt>A param preceded by a leading plus sign (+) is interpreted as a filename or directory. The content of the file is parsed as XML, and the resulting document node is passed to the stylesheet as the value of the parameter. If the parameter value is a directory, then all the immediately contained files are parsed as XML, and the resulting sequence of document nodes is passed as the value of the parameter. For example, +lookup=lookup.xml sets the value of the stylesheet parameter lookup to the document node at the root of the tree representing the parsed contents of the file lookup.xml.</p>
<dd>
<dt>Under Windows, and some other operating systems, it is possible to supply a value containing spaces by enclosing it in double quotes, for example name=John Smith. This is a feature of the operating system shell, not something Saxon does, so it may not work the same way under every operating system. (In the jEdit console plugin it has to be written as name=John Smith)</p>
<dd>
<dt>If the parameter name is in a non-null namespace, the parameter can be given a value using the syntax {uri}localname=value. Here uri is the namespace URI of the parameter&#8217;s name, and localname is the local part of the name.</p>
<dd>
<dt>This applies also to output parameters. For example, you can set the indentation level to 4 by using the parameter !{<a rel="nofollow" href="http://saxon.sf.net/}indent-spaces=4.">http://saxon.sf.net/}indent-spaces=4.</a> See also Additional attributes for xsl:output.</p>
<dd>
<dt>If the <code>-a</code> option is used, the name of the stylesheet is omitted. The source document must contain a &lt;?xml-stylesheet?&gt; processing instruction before the first element start tag; this processing instruction must have a pseudo-attribute href that identifies the relative or absolute URL of the stylsheet document, and a pseudo-attribute type whose value is text/xml, application/xml, or text/xsl. For example:</p>
<dd>
<dt>&lt;?xml-stylesheet type=text/xsl href=../style3.xsl ?&gt;</p>
<dd>
<dt>It is also possible to refer to a stylesheet embedded within the source document, provided it has an id attribute and the id attribute is declared in the DTD as being of type ID.</p>
<dd></dl>
<h2>FILES</h2>
<p> <code>/etc/java/resolver/CatalogManager.properties</code></p>
<dl>
<dt>
<dd> The central catalog manager configuration file used by <code>saxon</code> for resolving XML entities and URIs if xml-commons-resolver is available.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xsltproc/">xsltproc</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Michael H. Kay &lt;mike [at] saxonica.com&gt; </p>
<h2>Index</h2>

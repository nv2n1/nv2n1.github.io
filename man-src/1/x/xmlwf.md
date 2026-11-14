---
title: "xmlwf(1)"
name: "xmlwf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlwf/"
description: "xmlwf – Determines if an XML document is well-formed"
---

<h2>NAME</h2>
<p> xmlwf &#8211; Determines if an XML document is well-formed</p>
<h2>SYNOPSIS</h2>
<p> <code>xmlwf</code> [ <code>-s</code>] [ <code>-n</code>] [ <code>-p</code>] [ <code>-x</code>] [ <code>-e </code><i>encoding</i>] [ <code>-w</code>] [ <code>-d </code><i>output-dir</i>] [ <code>-c</code>] [ <code>-m</code>] [ <code>-r</code>] [ <code>-t</code>] [ <code>-v</code>] [ <code>file &#8230;</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>xmlwf</code> uses the Expat library to determine if an XML document is well-formed. It is non-validating. </p>
<p> If you do not specify any files on the command-line, and you have a recent version of <code>xmlwf</code>, the input file will be read from standard input.</p>
<h2>WELL-FORMED DOCUMENTS</h2>
<p> A well-formed document must adhere to the following rules:</p>
<dl>
<dt>&bull;</p>
<dd> The file begins with an XML declaration. For instance, &lt;?xml version=&quot;1.0&quot; standalone=&quot;yes&quot;?&gt;. <code>NOTE:</code> <code>xmlwf</code> does not currently check for a valid XML declaration.</p>
<dt>&bull;</p>
<dd> Every start tag is either empty (&lt;tag/&gt;) or has a corresponding end tag.</p>
<dt>&bull;</p>
<dd> There is exactly one root element. This element must contain all other elements in the document. Only comments, white space, and processing instructions may come after the close of the root element.</p>
<dt>&bull;</p>
<dd> All elements nest properly.</p>
<dt>&bull;</p>
<dd> All attribute values are enclosed in quotes (either single or double).</dl>
<p> If the document has a DTD, and it strictly complies with that DTD, then the document is also considered <code>valid</code>. <code>xmlwf</code> is a non-validating parser &#8212; it does not check the DTD. However, it does support external entities (see the <code>-x</code> option).</p>
<h2>OPTIONS</h2>
<p> When an option includes an argument, you may specify the argument either separately (&quot;<code>-d</code> output&quot;) or concatenated with the option (&quot;<code>-d</code>output&quot;). <code>xmlwf</code> supports both.</p>
<dl>
<dt><code>-c</code></p>
<dd> If the input file is well-formed and <code>xmlwf</code> doesn&#8217;t encounter any errors, the input file is simply copied to the output directory unchanged. This implies no namespaces (turns off <code>-n</code>) and requires <code>-d</code> to specify an output file.</p>
<dt><code>-d output-dir</code></p>
<dd> Specifies a directory to contain transformed representations of the input files. By default, <code>-d</code> outputs a canonical representation (described below). You can select different output formats using <code>-c</code> and <code>-m</code>. </p>
<p> The output filenames will be exactly the same as the input filenames or &quot;STDIN&quot; if the input is coming from standard input. Therefore, you must be careful that the output file does not go into the same directory as the input file. Otherwise, <code>xmlwf</code> will delete the input file before it generates the output file (just like running cat &lt; file &gt; file in most shells). </p>
<p> Two structurally equivalent XML documents have a byte-for-byte identical canonical XML representation. Note that ignorable white space is considered significant and is treated equivalently to data. More on canonical XML can be found at <a rel="nofollow" href="http://www.jclark.com/xml/canonxml.html">http://www.jclark.com/xml/canonxml.html</a> .</p>
<dt><code>-e encoding</code></p>
<dd> Specifies the character encoding for the document, overriding any document encoding declaration. <code>xmlwf</code> supports four built-in encodings: US-ASCII, UTF-8, UTF-16, and ISO-8859-1. Also see the <code>-w</code> option.</p>
<dt><code>-m</code></p>
<dd> Outputs some strange sort of XML file that completely describes the input file, including character positions. Requires <code>-d</code> to specify an output file.</p>
<dt><code>-n</code></p>
<dd> Turns on namespace processing. (describe namespaces) <code>-c</code> disables namespaces.</p>
<dt><code>-p</code></p>
<dd> Tells xmlwf to process external DTDs and parameter entities. </p>
<p> Normally <code>xmlwf</code> never parses parameter entities. <code>-p</code> tells it to always parse them. <code>-p</code> implies <code>-x</code>.</p>
<dt><code>-r</code></p>
<dd> Normally <code>xmlwf</code> memory-maps the XML file before parsing; this can result in faster parsing on many platforms. <code>-r</code> turns off memory-mapping and uses normal file IO calls instead. Of course, memory-mapping is automatically turned off when reading from standard input. </p>
<p> Use of memory-mapping can cause some platforms to report substantially higher memory usage for <code>xmlwf</code>, but this appears to be a matter of the operating system reporting memory in a strange way; there is not a leak in <code>xmlwf</code>.</p>
<dt><code>-s</code></p>
<dd> Prints an error if the document is not standalone. A document is standalone if it has no external subset and no references to parameter entities.</p>
<dt><code>-t</code></p>
<dd> Turns on timings. This tells Expat to parse the entire file, but not perform any processing. This gives a fairly accurate idea of the raw speed of Expat itself without client overhead. <code>-t</code> turns off most of the output options (<code>-d</code>, <code>-m</code>, <code>-c</code>, &#8230;).</p>
<dt><code>-v</code></p>
<dd> Prints the version of the Expat library being used, including some information on the compile-time configuration of the library, and then exits.</p>
<dt><code>-w</code></p>
<dd> Enables support for Windows code pages. Normally, <code>xmlwf</code> will throw an error if it runs across an encoding that it is not equipped to handle itself. With <code>-w</code>, xmlwf will try to use a Windows code page. See also <code>-e</code>.</p>
<dt><code>-x</code></p>
<dd> Turns on parsing external entities. </p>
<p> Non-validating parsers are not required to resolve external entities, or even expand entities at all. Expat always expands internal entities (?), but external entity parsing must be enabled explicitly. </p>
<p> External entities are simply entities that obtain their data from outside the XML file currently being parsed. </p>
<p> This is an example of an internal entity: </p>
<pre>
&lt;!ENTITY vers '1.0.2'&gt;
</pre>
<p> And here are some examples of external entities: </p>
<pre>
&lt;!ENTITY header SYSTEM &quot;header-&amp;vers;.xml&quot;&gt;  (parsed)
&lt;!ENTITY logo SYSTEM &quot;logo.png&quot; PNG&gt;         (unparsed)
</pre>
<dt><code>&#8212;</code></p>
<dd> (Two hyphens.) Terminates the list of options. This is only needed if a filename starts with a hyphen. For example: </p>
<pre>
xmlwf -- -myfile.xml
</pre>
<p> will run <code>xmlwf</code> on the file <i>-myfile.xml</i>.</dl>
<p> Older versions of <code>xmlwf</code> do not support reading from standard input.</p>
<h2>OUTPUT</h2>
<p> If an input file is not well-formed, <code>xmlwf</code> prints a single line describing the problem to standard output. If a file is well formed, <code>xmlwf</code> outputs nothing. Note that the result code is <code>not</code> set.</p>
<h2>BUGS</h2>
<p> According to the W3C standard, an XML file without a declaration at the beginning is not considered well-formed. However, <code>xmlwf</code> allows this to pass. </p>
<p> <code>xmlwf</code> returns a 0 &#8211; noerr result, even if the file is not well-formed. There is no good way for a program to use <code>xmlwf</code> to quickly check a file &#8212; it must parse <code>xmlwf</code>&#8216;s standard output. </p>
<p> The errors should go to standard error, not standard output. </p>
<p> There should be a way to get <code>-d</code> to send its output to standard output rather than forcing the user to send it to a file. </p>
<p> I have no idea why anyone would want to use the <code>-d</code>, <code>-c</code>, and <code>-m</code> options. If someone could explain it to me, I&#8217;d like to add this information to this manpage.</p>
<h2>ALTERNATIVES</h2>
<p> Here are some XML validators on the web: </p>
<pre>
<a rel="nofollow" href="http://www.hcrc.ed.ac.uk/~richard/xml-check.html">http://www.hcrc.ed.ac.uk/~richard/xml-check.html</a>
<a rel="nofollow" href="http://www.stg.brown.edu/service/xmlvalid/">http://www.stg.brown.edu/service/xmlvalid/</a>
<a rel="nofollow" href="http://www.scripting.com/frontier5/xml/code/xmlValidator.html">http://www.scripting.com/frontier5/xml/code/xmlValidator.html</a>
<a rel="nofollow" href="http://www.xml.com/pub/a/tools/ruwf/check.html">http://www.xml.com/pub/a/tools/ruwf/check.html</a>
</pre>
<h2>SEE ALSO</h2>
<pre>
The Expat home page:        <a rel="nofollow" href="http://www.libexpat.org/">http://www.libexpat.org/</a>
The W3 XML specification:   <a rel="nofollow" href="http://www.w3.org/TR/REC-xml">http://www.w3.org/TR/REC-xml</a>
</pre>
<h2>AUTHOR</h2>
<p> This manual page was written by Scott Bronson &lt;bronson [at] rinspin.com&gt; for the Debian GNU/Linux system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1. </p>
<h2>Index</h2>

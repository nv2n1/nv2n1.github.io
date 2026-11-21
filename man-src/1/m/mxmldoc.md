---

title: "mxmldoc(1)"
name: "mxmldoc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mxmldoc/"
description: "mxmldoc – mini-xml documentation generator"
---

<h2>NAME</h2>
<p> mxmldoc &#8211; mini-xml documentation generator</p>
<p> <code>mxmldoc</code> &#8211;no-output [ <i>filename.xml</i> ] <i>source file(s)</i> ]<br />
 <code>mxmldoc</code> [ &#8211;footer <i>footerfile</i> ] [ &#8211;header <i>headerfile</i> ] [ &#8211;intro <i>introfile</i> ] [ &#8211;section <i>section</i> ] [ &#8211;title <i>title</i> ] [ <i>filename.xml</i> ] [ <i>source file(s)</i> ] &gt; <i>filename.html</i><br />
 <code>mxmldoc</code> &#8211;docset <i>directory.docset</i> [ &#8211;docversion <i>version</i> ] [ &#8211;feedname <i>name</i> ] [ &#8211;feedurl <i>url</i> ] [ &#8211;footer <i>footerfile</i> ] [ &#8211;header <i>headerfile</i> ] [ &#8211;intro <i>introfile</i> ] [ &#8211;section <i>section</i> ] [ &#8211;title <i>title</i> ] [ <i>filename.xml</i> ] [ <i>source file(s)</i> ]<br />
 <code>mxmldoc</code> &#8211;tokens <i>path</i> [ <i>filename.xml</i> ] [ <i>source file(s)</i> ] &gt; tokens.xml<br />
 <code>mxmldoc</code> &#8211;framed <i>basename</i> [ &#8211;footer <i>footerfile</i> ] [ &#8211;header <i>headerfile</i> ] [ &#8211;intro <i>introfile</i> ] [ &#8211;section <i>section</i> ] [ &#8211;title <i>title</i> ] [ <i>filename.xml</i> ] [ <i>source file(s)</i> ]<br />
 <code>mxmldoc</code> [ &#8211;footer <i>footerfile</i> ] [ &#8211;header <i>headerfile</i> ] [ &#8211;intro <i>introfile</i> ] &#8211;man <i>manpage</i> [ &#8211;section <i>section</i> ] [ &#8211;title <i>title</i> ] [ <i>filename.xml</i> ] [ <i>source file(s)</i> ] &gt; <i>filename.man</i></p>
<p> <i>mxmldoc</i> scans the specified C and C++ source files to produce an XML representation of globally accessible classes, constants, enumerations, functions, structures, typedefs, unions, and variables &#8211; the XML file is updated as necessary. By default, a HTML representation of the XML file is written to the standard output. Use the <i>&#8211;no-output</i> option to disable the HTML output. </p>
<p> Man page source can be generated using the <i>&#8211;man</i> option. </p>
<p> If no source files are specified then the current XML file is converted to the standard output. </p>
<p> In general, any C or C++ source code is handled by <i>mxmldoc</i>, however it was specifically written to handle code with documentation that is formatted according to the CUPS Developer Guide which is available at &quot;<a rel="nofollow" href="http://www.cups.org/documentation.php">http://www.cups.org/documentation.php</a>&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;docset directory.docset</dt>
<dd>
 Creates an Xcode documentation set in the specified directory.</dd>
<dt>&#8211;docversion version</dt>
<dd>
 Specifies the version number for the Xcode documentation set.</dd>
<dt>&#8211;feedname name</dt>
<dd>
 Specifies the Xcode documentation set feed name, typically the project or company name.</dd>
<dt>&#8211;feedurl url</dt>
<dd>
 Specifies the Xcode documentation set feed URL which must point to an ATOM file linking to updates.</dd>
<dt>&#8211;footer footerfile</dt>
<dd>
 Inserts the specified file at the bottom of the output documentation.</dd>
<dt>&#8211;framed basename</dt>
<dd>
 Creates HTML documentation using frames &#8211; one for the table-of-contents and one for the body.</dd>
<dt>&#8211;header headerfile</dt>
<dd>
 Inserts the specified file at the top of the output documentation.</dd>
<dt>&#8211;intro introfile</dt>
<dd>
 Inserts the specified file before the table of contents.</dd>
<dt>&#8211;man manpage</dt>
<dd>
 Generated a man page instead of HTML documentation.</dd>
<dt>&#8211;no-output</dt>
<dd>
 Disables generation of documentation on the standard output.</dd>
<dt>&#8211;section section</dt>
<dd>
 Sets the section/keywords in the output documentation.</dd>
<dt>&#8211;title title</dt>
<dd>
 Sets the title of the output documentation.</dd>
<dt>&#8211;tokens</dt>
<dd>
 Generates a Tokens.xml file for use with the Xcode documentation tools.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-mxml/">mxml</a>(3), Mini-XML Programmers Manual, <a rel="nofollow" href="http://www.minixml.org/">http://www.minixml.org/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2003-2009 by Michael Sweet. </p>

---
title: "djvuxml(1)"
name: "djvuxml"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvuxml/"
description: "djvutoxml, djvuxmlparser – DjVuLibre XML Tools."
---

<h2 class="name">NAME</h2>
<p> djvutoxml, djvuxmlparser &#8211; DjVuLibre XML Tools.</p>
<h2>SYNOPSIS</h2>
<p> <code>djvutoxml [</code><i>options</i><code>] </code><i>inputdjvufile</i><code> [</code><i>outputxmlfile</i><code>]</code><br />
 <code>djvuxmlparser [ -o </code><i>djvufile</i><code> ] </code><i>inputxmlfile</i> </p>
<h2>DESCRIPTION</h2>
<p> The DjVuLibre XML Tools provide for editing the metadata, hyperlinks and hidden text associated with DjVu files. Unlike <code><a href="/docs/linux/man/1-djvused/">djvused</a></code>(1) the DjVuLibre XML Tools rely on the XML technology and can take advantage of XML editors and verifiers. </p>
<h2>DJVUTOXML</h2>
<p> Program <code>djvutoxml</code> creates a XML file <i>outputxmlfile</i> containing a reference to the original DjVu document <i>inputdjvufile</i> as well as tags describing the metadata, hyperlinks, and hidden text associated with the DjVu file. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>&#8211;page </code><i>pagenum</i></p>
<dd> Select a page in a multi-page document. Without this option, <code>djvutoxml</code> outputs the XML corresponding to all pages of the document.</p>
<dt><code>&#8211;with-text</code></p>
<dd> Specifies the <code>HIDDENTEXT </code> element for each page should be included in the output. If specified without the <code>&#8211;with-anno</code> flag then the <code>&#8211;without-anno </code> is implied. If none of the <code>&#8211;with-text, </code> <code>&#8211;without-text, </code> <code>&#8211;with-anno, </code> or <code>&#8211;without-anno, </code> flags are specified, then the <code>&#8211;with-text </code> and <code>&#8211;with-anno </code> flags are implied.</p>
<dt><code>&#8211;without-text</code></p>
<dd> Specifies not to output the <code>HIDDENTEXT </code> element for each page. If specified without the <code>&#8211;without-anno </code> flag then the <code>&#8211;with-anno </code> flag is implied.</p>
<dt><code>&#8211;with-anno</code></p>
<dd> Specifies the area <code>MAP </code> element for each page should be included in the output. If specified without the <code>&#8211;with-text </code> flag then the <code>&#8211;without-text </code> flag is implied.</p>
<dt><code>&#8211;without-anno</code></p>
<dd> Specifies the area <code>MAP </code> element for each page should not be included in the output. If specified without the <code>&#8211;without-text </code> flag then the <code>&#8211;with-text </code> flag is implied. </p>
</dl>
<h2>DJVUXMLPARSER</h2>
<p> Files produced by <code>djvutoxml</code> can then be modified using either a text editor or a XML editor. Program <code>djvuxmlparser</code> parses the XML file <i>inputxmlfile</i> in order to modify the metadata of the corresponding DjVu file.</p>
<dl>
<dt><code>-o </code><i>djvufile</i></p>
<dd> In principle the target DjVu file is the file referenced by the <i>OBJECT </i> element of the XML file. This option provides the means to override the filename specified in the <i>OBJECT</i> element. </p>
</dl>
<h2>DJVUXML DOCUMENT TYPE DEFINITION</h2>
<p> The document type definition file (DTD)</p>
<dl>
<dt>
<dd> <code>/usr/share/djvu/pubtext/DjVuXML-s.dtd</code></dl>
<p> defines the input and output of the DjVu XML tools. </p>
<p> The DjVuXML-s DTD is a simplification of the HTML DTD:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.w3c.org/TR/1998/REC-html40-19980424/sgml/dtd.html">http://www.w3c.org/TR/1998/REC-html40-19980424/sgml/dtd.html</a></code></dl>
<p> with a few new attributes added specific to DjVu. Each of the specified pages of a DjVu document are represented as <code>OBJECT </code> elements within the <code>BODY </code> element of the XML file. Each <code>OBJECT</code> element may contain multiple <code>PARAM </code> elements to specify attributes like page name, resolution, and gamma factor. Each <code>OBJECT</code> element may also contain one <code>HIDDENTTEXT</code> element to specify the hidden text (usually generated with an OCR engine) within the DjVu page. In addition each <code>OBJECT</code> element may reference a single area <code>MAP</code> element which contains multiple <code>AREA</code> elements to represent all the hyperlink and highlight areas within the DjVu document. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PARAM Elements</h2>
<p> Legal <code>PARAM </code> elements of a DjVu <code>OBJECT </code> include but are not limited to <code>PAGE</code> for specifying the page-name, <code>GAMMA</code> for specifying the gamma correction factor (normally 2.2), and <code>DPI</code> for specifying the page resolution. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>HIDDENTEXT Elements</h2>
<p> The <code>HIDDENTEXT</code> elements consists of nested elements of <code>PAGECOLUMNS,</code> <code>REGION,</code> <code>PARAGRAPH,</code> <code>LINE,</code> and <code>WORD.</code> The most deeply nested element specified, should specify the bounding coordinates of the element in top-down orientation. The body of the most deeply nested element should contain the text. Most DjVu documents use either <code>LINE </code> or <code>WORD </code> as the lowest level element, but any element is legal as the lowest level element. A white space is always added between <code>WORD</code> elements and a line feed is always added between <code>LINE</code> elements. Since languages such as Japanese do not use spaces between words, it is quite common for Asian OCR engines to use <code>WORD</code> as characters instead. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MAP Elements</h2>
<p> The body of the <code>MAP</code> elements consist of <code>AREA</code> elements. In addition to the attributes listed in</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.w3.org/TR/1998/REC-html40-19980424/struct/objects.html#edef-AREA">http://www.w3.org/TR/1998/REC-html40-19980424/struct/objects.html#edef-AREA</a></code>,</dl>
<p> the attributes <code>bordertype</code>, <code>bordercolor</code>, <code>border</code>, and <code>highlight</code> have been added to specify border type, border color, border width, and highlight colors respectively. Legal values for each of these attributes are listed in the DjVuXML-s DTD. In addition, the shape <code>oval</code> has been added to the legal list of shapes. An oval uses a rectangular bounding box. </p>
<h2>BUGS</h2>
<p> Perhaps it would have been better to use CC2 style sheets with standard HTML elements instead of defining the <code>HIDDENTEXT </code> element. </p>
<h2>CREDITS</h2>
<p> The DjVu XML tools and DTD were written by Bill C. Riemers &lt;docbill [at] sourceforge.net&gt; and Fred Crary. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvused/">djvused</a></code>(1), and <code><a href="/docs/linux/man/7-utf8/">utf8</a></code>(7). </p>
<h2>Index</h2>

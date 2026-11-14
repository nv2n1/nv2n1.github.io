---
title: "slice2html(1)"
name: "slice2html"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slice2html/"
description: "slice2html – The Slice to HTML documentation tool."
---

<h2 class="name">NAME</h2>
<p> slice2html &#8211; The Slice to HTML documentation tool.</p>
<h2>SYNOPSIS</h2>
<p> slice2html [options] [files] </p>
<h2>DESCRIPTION</h2>
<p> slice2html generates HTML documentation from Slice files. </p>
<p> Full documentation for slice2html is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/Generating+Slice+Documentation">http://doc.zeroc.com/display/Ice/Generating+Slice+Documentation</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays help message. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays the compiler version. </p>
<dt><code>-DNAME</code></p>
<dd>
 Defines the preprocessor symbol NAME. </p>
<dt><code>-DNAME=DEF</code></p>
<dd>
 Defines the preprocessor symbol NAME with the value DEF. </p>
<dt><code>-UNAME</code></p>
<dd>
 Undefines the preprocessor symbol NAME. </p>
<dt><code>-IDIR</code></p>
<dd>
 Add the directory DIR to the search path for #include directives. </p>
<dt><code>-E</code></p>
<dd>
 Print the preprocessor output on stdout. </p>
<dt><code>&#8211;output-dir</code> <code>DIR</code></p>
<dd>
 Place the generated files into directory DIR. </p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>
 Print debug information showing the operation of the Slice parser. </p>
<dt><code>&#8211;ice</code></p>
<dd>
 Permit use of the normally reserved prefix Ice for identifiers. Use this option only when compiling the source code for the Ice run time. </p>
<dt><code>&#8211;hdr</code> <code>FILE</code></p>
<dd>
 Prepend FILE to each generated HTML file (except for _sindex.html). This allows you to replace the HTML header and other preamble information with a custom version, so you can connect style sheets to the generated pages. The specified file must include the &lt;body&gt; tag (but need not end with a &lt;body&gt; tag). FILE is expected to contain the string TITLE on a line by itself, starting in column one. slice2html replaces the TITLE string with the fully-scoped name of the Slice symbol that is documented on the corresponding page. </p>
<dt><code>&#8211;ftr</code> <code>FILE</code></p>
<dd>
 Append FILE to each generated HTML file (except for _sindex.html). This allows you to add, for example, a custom footer to each generated page. FILE must end with a &lt;/body&gt; tag. </p>
<dt><code>&#8211;indexhdr</code> <code>FILE</code></p>
<dd>
 slice2html generates a file _sindex.html that contains a table of contents of all Slice symbols that hyperlink to the corresponding page. This option allows you to replace the standard header with a custom header, for example, to attach a JavaScript. The specified file must include the &lt;body&gt; tag (but need not end with a &lt;body&gt; tag). The default value is the setting of &#8211;hdr (if any). </p>
<dt><code>&#8211;indexftr</code> <code>FILE</code></p>
<dd>
 Append FILE to the generated sindex.html page. This allows you to add, for example, a custom footer to the table of contents, or to invoke a JavaScript. FILE is must end with a &lt;/body&gt; tag. The default value is the setting of &#8211;ftr (if any). </p>
<dt><code>&#8211;image-dir</code> <code>DIR</code></p>
<dd>
 With this option, slice2html looks in the specified directory for images to use for the generated navigation hyperlinks. (Without this option, text links are used instead.) Please see the generated HTML for the names of the various image files. (They can easily be found by looking for img elements.) </p>
<dt><code>&#8211;logo-url</code> <code>URL</code></p>
<dd>
 Use the specified URL as a hyperlink for the company logo that is added to each page (if &#8211;image-dir is specified). The company logo is expected to be in &lt;image_dir&gt;/logo.gif. </p>
<dt><code>&#8211;search</code> <code>ACTION</code></p>
<dd>
 If this option is specified, the generated pages contain a search box that allows you to connect the generated pages to a search engine. On pressing the &quot;Search&quot; button, the specified ACTION is carried out. </p>
<dt><code>&#8211;index</code> <code>NUM</code></p>
<dd>
 slice2html generates sub-indexes for various Slice symbols. This option controls how many entries must be present before a sub-index is generated. For example, if NUM is set to 3, a sub-index will be generated only if there are three or more symbols that appear in that index. The default settings is 1, meaning that a sub-index is always generated. To disable sub-indexes entirely, set NUM to 0. </p>
<dt><code>&#8211;summary</code> <code>NUM</code></p>
<dd>
 If this option is set, summary sentences that exceed NUM characters generate a warning. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cpp/">slice2cpp</a></code>(1), <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freeze/">slice2freeze</a></code>(1), <code><a href="/docs/linux/man/1-slice2freezej/">slice2freezej</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2java/">slice2java</a></code>(1), <code><a href="/docs/linux/man/1-slice2php/">slice2php</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
<h2>Index</h2>

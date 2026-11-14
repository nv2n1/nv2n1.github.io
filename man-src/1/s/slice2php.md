---
title: "slice2php(1)"
name: "slice2php"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slice2php/"
description: "slice2php – The Slice to PHP compiler."
---

<h2 class="name">NAME</h2>
<p> slice2php &#8211; The Slice to PHP compiler.</p>
<h2>SYNOPSIS</h2>
<p> slice2php [options] [files] </p>
<h2>DESCRIPTION</h2>
<p> slice2php compiles Slice files to PHP. </p>
<p> Full documentation for slice2php is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/slice2php+Command-Line+Options">http://doc.zeroc.com/display/Ice/slice2php+Command-Line+Options</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays a help message. </p>
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
<dt><code>&#8211;underscore</code></p>
<dd>
 Permit use of underscores in Slice identifiers. </p>
<dt><code>&#8211;all</code></p>
<dd>
 Generate code for all Slice definitions, including those from included files. </p>
<dt><code>-n</code>, <code>&#8211;namespace</code></p>
<dd>
 Generate code using PHP namespaces. Note that namespaces are only supported in PHP 5.3 or later. Also note that the Ice extension for PHP must be built with namespace support enabled. </p>
<dt><code>&#8211;checksum</code> <code>CLASS</code></p>
<dd>
 Generate checksums for Slice definitions. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cpp/">slice2cpp</a></code>(1), <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freeze/">slice2freeze</a></code>(1), <code><a href="/docs/linux/man/1-slice2freezej/">slice2freezej</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2java/">slice2java</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
<h2>Index</h2>

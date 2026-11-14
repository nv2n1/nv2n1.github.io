---
title: "mate-doc-common(1)"
name: "mate-doc-common"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-doc-common/"
description: "mate-doc-common – include the standard user documentation build files"
---

<h2>NAME</h2>
<p> <code>mate-doc-common </code>&#8211; include the standard user documentation build files</p>
<h2>SYNOPSIS</h2>
<pre>
<code>mate-doc-common</code>
</pre>
<h2>DESCRIPTION</h2>
<p> This script is used by mate-autogen to include the standard user documentation build files in a MATE package. </p>
<p> To automatically include the standard user documentation build files (omf.make and xmldocs.make) in you package, set USE_COMMON_DOC_BUILD=yes in autogen.sh before calling the macros/autogen.sh script. </p>
<p> When porting applications across to use this feature, ensure that all of the references to xmldocs.make are to $(top_srcdir)/xmldocs.make in the appropriate Makefile.am files. Some modules assume that xmldocs.make is in another directory (like docs/ or something).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display the help of the script.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the script version.</p>
<dt><code>&#8211;copy</code></p>
<dd> Copy files instead of make symlinks.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mate-autogen/">mate-autogen</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Perberos &lt;perberos [at] gmail.com&gt; </p>
<h2>Index</h2>

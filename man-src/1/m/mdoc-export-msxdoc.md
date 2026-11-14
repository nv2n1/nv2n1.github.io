---
title: "mdoc-export-msxdoc(1)"
name: "mdoc-export-msxdoc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdoc-export-msxdoc/"
description: "mdoc export-msxdoc – Convert mdoc(5) XML to Microsoft XML Documentation"
---

<h2>NAME</h2>
<p> mdoc export-msxdoc &#8211; Convert <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) XML to Microsoft XML Documentation</p>
<h2>SYNOPSIS</h2>
<p> <code>mdoc export-msxdoc</code> [OPTION]* DIRECTORIES</p>
<h2>DESCRIPTION</h2>
<p> <code>mdoc export-msxdoc</code> creates <i>Microsoft XML Documentation</i> (as produced by <i>csc /doc</i>) from the <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5)-formatted documentation XML files within <i>DIRECTORIES</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code>, <code>&#8211;out</code>=<i>FILE</i></p>
<dd> The XML file to generate. </p>
<p> If not specified, a set of files matching the <i>//AssemblyInfo/AssemblyName</i> values within the documentation will be used. </p>
<p> Use <code>&#8211;</code> to write to standard output.</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Display a help message and exit.</dl>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/mdoc/">http://www.mono-project.com/docs/tools+libraries/tools/mdoc/</a> for details </p>
<h2>Index</h2>

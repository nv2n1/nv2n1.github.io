---
title: "gtk4-builder-tool(1)"
name: "gtk4-builder-tool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk4-builder-tool/"
description: "gtk4-builder-tool – GtkBuilder File Utility"
---

<h2 class="name">NAME</h2>
<p> gtk4-builder-tool &#8211; GtkBuilder File Utility </p>
<h2>SYNOPSIS</h2>
<pre><code>
gtk4 - builder - tool&lt;COMMAND&gt;[OPTIONS...]&lt;FILE&gt; gtk4 - builder - tool validate&lt;FILE&gt; gtk4 - builder - tool enumerate&lt;FILE&gt; gtk4 - builder - tool simplify[OPTIONS...]&lt;FILE&gt; gtk4 - builder - tool preview[OPTIONS...]&lt;FILE&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>gtk4-builder-tool</code> can perform various operations on GtkBuilder UI definition files.</p>
<h2>COMMANDS</h2>
<h3>Validation</h3>
<p> The <code>validate</code> command validates the given UI definition file and reports errors to <code>stderr</code>.</p>
<h3>Enumeration</h3>
<p> The <code>enumerate</code> command lists all the named objects that are present in the UI definition file.</p>
<h3>Preview</h3>
<p> The <code>preview</code> command displays the UI dfinition file. </p>
<p> This command accepts options to specify the ID of the toplevel object and a CSS file to use. </p>
<p> <code>&#8211;id=ID</code> The ID of the object to preview. If not specified, gtk4-builder-tool will choose a suitable object on its own. </p>
<p> <code>&#8211;css=FILE</code> Load style information from the given CSS file.</p>
<h3>Simplification</h3>
<p> The <code>simplify</code> command simplifies the UI definition file by removing properties that are set to their default values and writes the resulting XML to the standard output, or back to the input file. </p>
<p> When the <code>&#8211;3to4</code> option is specified, the <code>simplify</code> command interprets the input as a GTK 3 UI definuition file and attempts to convert it to GTK 4 equivalents. It performs various conversions, such as renaming properties, translating child properties to layout properties, rewriting the setup for GtkNotebook, GtkStack, GtkAssistant or changing toolbars into boxes. </p>
<p> You should always test the modified UI definition files produced by gtk4-builder-tool before using them in production. </p>
<p> Note in particular that the conversion done with <code>&#8211;3to4</code> is meant as a starting point for a port from GTK 3 to GTK 4. It is expected that you will have to do manual fixups after the initial conversion. </p>
<p> <code>&#8211;replace</code> Write the content back to the UI definition file instead of using the standard output. </p>
<p> <code>&#8211;3to4</code> Transform a GTK 3 UI definition file to the equivalent GTK 4 definitions. </p>
<h2>Index</h2>

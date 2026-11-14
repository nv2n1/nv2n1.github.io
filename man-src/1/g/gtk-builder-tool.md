---
title: "gtk-builder-tool(1)"
name: "gtk-builder-tool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-builder-tool/"
description: "gtk-builder-tool – GtkBuilder file utility"
---

<h2 class="name">NAME</h2>
<p> gtk-builder-tool &#8211; GtkBuilder file utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtk-builder-tool</code> [<i>COMMAND</i>] [<i>OPTION</i>&#8230;] <i>FILE</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>gtk-builder-tool</code></p>
<dd>can perform various operations on GtkBuilder .ui files. </p>
<p> You should always test the modified .ui files produced by gtk-builder-tool before using them in production.</p>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>validate</code></p>
<dl>
<dt>
<dd> Validates the .ui file and report errors to stderr.</dl>
<p> <code>simplify</code></p>
<dl>
<dt>
<dd> Simplifies the .ui file by removing properties that are set to their default values and write the resulting XML to stdout, or back to the input file.</dl>
<p> <code>enumerate</code></p>
<dl>
<dt>
<dd> Lists all the named objects that are created in the .ui file.</dl>
<p> <code>preview</code></p>
<dl>
<dt>
<dd> Preview the .ui file. This command accepts options to specify the ID of an object and a .css file to use.</dl>
<h2>SIMPLIFY OPTIONS</h2>
<p> The <code>simplify</code> command accepts the following options: </p>
<p> <code>&#8211;replace</code></p>
<dl>
<dt>
<dd> Write the content back to the .ui file instead of stdout.</dl>
<h2>PREVIEW OPTIONS</h2>
<p> The <code>preview</code> command accepts the following options: </p>
<p> <code>&#8211;id=</code><code>ID</code></p>
<dl>
<dt>
<dd> The ID of the object to preview. If not specified, gtk-builder-tool will choose a suitable object on its own.</dl>
<p> <code>&#8211;css=</code><code>FILE</code></p>
<dl>
<dt>
<dd> Load style information from the given .css file.</dl>
<h2>Index</h2>

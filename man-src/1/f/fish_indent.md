---
title: "fish_indent(1)"
name: "fish_indent"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fish_indent/"
description: "fish_indent — indenter and prettifier"
---

<h2 class="name">NAME</h2>
<p> <code>fish_indent</code> &#8212; indenter and prettifier </p>
<h3>Synopsis</h3>
<pre>
<code>fish_indent</code> [OPTIONS]
</pre>
<h3>Description</h3>
<p> fish_indent is used to indent a piece of fish code. fish_indent reads commands from standard input and outputs them to standard output. </p>
<p> The following options are available: </p>
<dl>
<dt>&bull;</dt>
<dd> -d or &#8211;dump dumps information about the parsed fish commands to stderr</dd>
<dt>&bull;</dt>
<dd> -i or &#8211;no-indent do not indent commands; only reformat to one job per line</dd>
<dt>&bull;</dt>
<dd> -v or &#8211;version displays the current fish version and then exits</dd>
<dt>&bull;</dt>
<dd> &#8211;ansi colorizes the output using ANSI escape sequences, appropriate for the current $TERM, using the colors defined in the environment (such as $fish_color_command).</dd>
<dt>&bull;</dt>
<dd> &#8211;html outputs HTML, which supports syntax highlighting if the appropriate CSS is defined. The CSS class names are the same as the variable names, such as fish_color_command</dd></dl>

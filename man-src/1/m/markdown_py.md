---
title: "markdown_py(1)"
name: "markdown_py"
section: "1"
letter: "m"
url: "/docs/linux/man/1-markdown_py/"
description: "markdown_py – a Python implementation of John Gruber’s Markdown."
---

<h2 class="name">NAME</h2>
<p> markdown_py &#8211; a Python implementation of John Gruber&#8217;s Markdown.</p>
<h2>SYNOPSIS</h2>
<p> <code>markdown_py [</code><i>options</i>] [<i>INPUT_FILE</i>]</p>
<dl>
<dt>
<dd> (STDIN is assumed if no INPUT_FILE is given) </p>
</dl>
<h2>DESCRIPTION</h2>
<p> Command-line Markdown compiler based on python-markdown module, with extensions support. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the help message and exit.</p>
<dt><code>-f </code><i>OUTPUT_FILE</i>, <code>&#8211;file=</code><i>OUTPUT_FILE</i></p>
<dd> Write output to OUTPUT_FILE. Defaults to STDOUT.</p>
<dt><code>-e </code><i>ENCODING</i>, <code>&#8211;encoding=</code><i>ENCODING</i></p>
<dd> Encoding for input and output files.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress all warnings.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print all warnings.</p>
<dt><code>-s </code><i>SAFE_MODE</i>, <code>&#8211;safe=</code><i>SAFE_MODE</i></p>
<dd> &#8216;replace&#8217;, &#8216;remove&#8217; or &#8216;escape&#8217; HTML tags in input.</p>
<dt><code>-o </code><i>OUTPUT_FORMAT</i>, <code>&#8211;output_format=</code><i>OUTPUT_FORMAT</i></p>
<dd> &#8216;xhtml1&#8217; (default), &#8216;html4&#8217; or &#8216;html5&#8217;.</p>
<dt><code>&#8211;noisy</code></p>
<dd> Print debug messages.</p>
<dt><code>-x </code><i>EXTENSION</i>, <code>&#8211;extension=</code><i>EXTENSION</i></p>
<dd> Load extension EXTENSION.</p>
<dt><code>-n</code>, <code>&#8211;no_lazy_ol</code></p>
<dd> Observe number of first item of ordered lists. </p>
</dl>
<h2>Index</h2>

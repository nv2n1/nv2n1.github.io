---
title: "cpttext(1)"
name: "cpttext"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpttext/"
description: "cpttext – print text coloured by a GMT colour palette table (cpt) file."
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cpttext</code> [-h] [-H] [-t&nbsp;<wbr><i>text</i>] [-v] [-V] [<i>file</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cpttext</code> program prints text in the colours specified by the <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1) colour palette table (cpt) file. Currently only HTML output is supported. </dd>
<p> The program will read the cpt file from stdin if a <i>file</i> is not specified as the final argument, and writes to stdout.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Brief help.</dd></dl>
<p> <code>-H</code>, <code>&#8211;html</code></p>
<dl>
<dt>
</dt><dd> Output in HTML format (the default, so this switch is redundant).</dd></dl>
<p> <code>-t</code>, <code>&#8211;text</code> <i>string</i></p>
<dl>
<dt>
</dt><dd> The text to print, which should be quoted if containing whitespace.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Verbose operation.</dd></dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Version information.</dd></dl>
<h2>EXAMPLE</h2>
<p> Colour some Lorem ipsum text in HTML: </p>
<dl>
<dt>
</dt><dd>
<pre>
  cpttext -H -t &quot;Lorem ipsum dolor sit amet&quot; test.cpt
</pre>
</dd></dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1). </p>

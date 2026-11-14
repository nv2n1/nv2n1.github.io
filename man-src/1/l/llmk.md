---
title: "llmk(1)"
name: "llmk"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llmk/"
description: "llmk – Light LaTeX Make"
---

<h2 class="name">NAME</h2>
<p> <code>llmk</code> &#8211; Light LaTeX Make </p>
<h2>SYNOPSIS</h2>
<p> <code>llmk</code> [OPTION]&#8230; [FILE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>llmk</code> is yet another LaTeX-specific build tool. Its aim is to provide a simple way to write down workflows for processing LaTeX documents. The only requirement is the <code><a href="/docs/linux/man/1-texlua/">texlua</a></code>(1) program. </p>
<p> If one or more FILE(s) are specified, <code>llmk</code> reads the TOML fields or other supported magic comments in the files. Otherwise, it will read the special configuration file <i>llmk.toml</i> in the working directory. Then, <code>llmk</code> will execute the specified workflow to typeset the LaTeX documents.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> Remove the temporary files such as <code>*.aux</code> and <code>*.log</code>.</p>
<dt><code>-C</code>, <code>&#8211;clobber</code></p>
<dd> Remove all generated files including final PDFs.</p>
<dt><code>-d</code>CAT, <code>&#8211;debug</code>=CAT</p>
<dd> Activate debug output restricted to CAT.</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Activate all debug output (equal to &quot;&#8211;debug=all&quot;).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print this help message.</p>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd> Show what would have been executed.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress warnings and most error messages.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Silence messages from called programs.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print additional information (e.g., running commands).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>0</p>
<dd> Success.</p>
<dt>1</p>
<dd> General error.</p>
<dt>2</p>
<dd> Failure executing the workflow. The exit status of the external program is reported in an error message.</p>
<dt>3</p>
<dd> Parser error.</p>
<dt>4</p>
<dd> Type error.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <i><a rel="nofollow" href="https://github.com/wtsnjp/llmk/issues">https://github.com/wtsnjp/llmk/issues</a></i>.<br />
 Source: <i><a rel="nofollow" href="https://github.com/wtsnjp/llmk">https://github.com/wtsnjp/llmk</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2018-2021 Takuto ASAKURA (wtsnjp).<br />
 License: The MIT License <i><a rel="nofollow" href="https://opensource.org/licenses/mit-license">https://opensource.org/licenses/mit-license</a></i>.<br />
 This is free software: you are free to change and redistribute it.</p>
<h2>SEE ALSO</h2>
<p> The full documentation is maintained as a PDF manual. The command</p>
<dl>
<dt>
<dd>
<pre>
texdoc llmk
</pre>
<dt>
<dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>

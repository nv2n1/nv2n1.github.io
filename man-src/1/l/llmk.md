---

title: "llmk(1)"
name: "llmk"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llmk/"
description: "llmk – Light LaTeX Make"
---

<p> <code>llmk</code> &#8211; Light LaTeX Make </p>
<p> <code>llmk</code> [OPTION]&#8230; [FILE]&#8230;</p>
<p> <code>llmk</code> is yet another LaTeX-specific build tool. Its aim is to provide a simple way to write down workflows for processing LaTeX documents. The only requirement is the <code><a href="/docs/linux/man/1-texlua/">texlua</a></code>(1) program. </p>
<p> If one or more FILE(s) are specified, <code>llmk</code> reads the TOML fields or other supported magic comments in the files. Otherwise, it will read the special configuration file <i>llmk.toml</i> in the working directory. Then, <code>llmk</code> will execute the specified workflow to typeset the LaTeX documents.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;clean</code></dt>
<dd> Remove the temporary files such as <code>*.aux</code> and <code>*.log</code>.</dd>
<dt><code>-C</code>, <code>&#8211;clobber</code></dt>
<dd> Remove all generated files including final PDFs.</dd>
<dt><code>-d</code>CAT, <code>&#8211;debug</code>=CAT</dt>
<dd> Activate debug output restricted to CAT.</dd>
<dt><code>-D</code>, <code>&#8211;debug</code></dt>
<dd> Activate all debug output (equal to &quot;&#8211;debug=all&quot;).</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print this help message.</dd>
<dt><code>-n</code>, <code>&#8211;dry-run</code></dt>
<dd> Show what would have been executed.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Suppress warnings and most error messages.</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd> Silence messages from called programs.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print additional information (e.g., running commands).</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version number.</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>0</dt>
<dd> Success.</dd>
<dt>1</dt>
<dd> General error.</dd>
<dt>2</dt>
<dd> Failure executing the workflow. The exit status of the external program is reported in an error message.</dd>
<dt>3</dt>
<dd> Parser error.</dd>
<dt>4</dt>
<dd> Type error.</dd></dl>
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
</dt><dd>
<pre>
texdoc llmk
</pre>
</dd></dl>
<p> should give you access to the complete manual. </p>

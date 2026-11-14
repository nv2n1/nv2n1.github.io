---
title: "spix(1)"
name: "spix"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spix/"
description: "spix – Compile a .tex file, executing commands that are set inside the file itself."
---

<h2 class="name">NAME</h2>
<p> spix &#8211; Compile a .tex file, executing commands that are set inside the file itself. </p>
<h2>SYNOPSIS</h2>
<p> <code>spix</code> [<code>&#8211;version</code>] [<code>-h</code>] [<code>-n</code>] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>spix</code> parses a .tex file to find lines starting with <i>%$</i> (before the preambule). Those lines are shell commands that are executed by <code>spix</code>. </p>
<p> Commands are executed as-is, excepted that:</p>
<dl>
<dt>
<dd>
<p> &#8211; command are run from the directory of the file given in argument; </p>
<p> &#8211; shell variables <i>$texname</i> and <i>$basename</i> are set to the name of the tex file (respectively with and without the .tex extension).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd> Print the commands that would be executed, but do not execute them.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help, and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version, and exit.</dl>
<h2>EXAMPLES</h2>
<p> Let <i>foo.tex</i> be the following file. </p>
<pre><code>
% Compile this file twice with lualatex.% $ lualatex foo.tex % $ lualatex foo.tex
\documentclass
{
    article
}
egin{document} Hello, world !
nd
{
    document
}
</code></pre>
<p> When running <code>spix</code> on this file, it is compiled twice using <code><a href="/docs/linux/man/1-lualatex/">lualatex</a>(1)</code> (as written in lines 2 and 3 of the file). </p>
<h2>Index</h2>

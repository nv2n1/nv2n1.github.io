---
title: "roff2ps(1)"
name: "roff2ps"
section: "1"
letter: "r"
url: "/docs/linux/man/1-roff2ps/"
description: "roff2ps – transform roff code into ps mode"
---

<h2 class="name">NAME</h2>
<p> roff2ps &#8211; transform roff code into ps mode </p>
<h2>SYNOPSIS</h2>
<p> [<i>groffer-option</i> &#8230; ] [ <code>&#8212;</code> ] [<i>filespec</i> &#8230; ] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code> </p>
<p> The options <code>-v</code> and <code>&#8211;version</code> print the version information of the program to standard output and exit. The options <code>-h</code> and <code>&#8211;help</code> print a usage information of the program to standard output and stop the program instantly. </p>
<p> All other options are assumed to be <code>groffer</code> options. They are internally passed to <code>groffer</code>. They override the behavior of the program. The options are optional, they can be omitted. </p>
<p> The <i>filespec</i> arguments correspond to the <i>filespec</i> arguments of <code>groffer</code>. So they are either the names of existing, readable files or <code>&#8211;</code> for standard input, or the name of a man page or a <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) man page search pattern. If no <i>filespec</i> is specified standard input is assumed automatically.</p>
<h2>DESCRIPTION</h2>
<p> <code>roff2ps</code> transforms <i>roff</i> code into <i>ps</i> mode. Print the result to standard output. </p>
<p> There are more of these programs for generating other formats of <i>roff</i> input.</p>
<dl>
<dt><code><a href="/docs/linux/man/1-roff2dvi/">roff2dvi</a></code>(1)</p>
<dd> is for <i>dvi</i> mode.</p>
<dt><code><a href="/docs/linux/man/1-roff2html/">roff2html</a></code>(1)</p>
<dd> generates <i>HTML</i> output.</p>
<dt><code><a href="/docs/linux/man/1-roff2pdf/">roff2pdf</a></code>(1)</p>
<dd> outputs <i>pdf</i> mode.</p>
<dt><code><a href="/docs/linux/man/1-roff2text/">roff2text</a></code>(1)</p>
<dd> generates text output in the <code>groff</code> device <i>latin1</i>.</p>
<dt><code><a href="/docs/linux/man/1-roff2x/">roff2x</a></code>(1)</p>
<dd> prints the output in the <code>groff</code> device <code>X</code> that is suitable for programs like <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) or <code><a href="/docs/linux/man/1-xditview/">xditview</a></code>(1).</dl>
<h2>AUTHORS</h2>
<p> <code>roff2ps</code> was written by Bernd Warken</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1), <code><a href="/docs/linux/man/1-roff2dvi/">roff2dvi</a></code>(1), <code><a href="/docs/linux/man/1-roff2html/">roff2html</a></code>(1), <code><a href="/docs/linux/man/1-roff2pdf/">roff2pdf</a></code>(1), <code><a href="/docs/linux/man/1-roff2text/">roff2text</a></code>(1), <code><a href="/docs/linux/man/1-roff2x/">roff2x</a></code>(1), <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1). </p>
<h2>Index</h2>

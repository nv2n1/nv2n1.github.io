---
title: "paperconf(1)"
name: "paperconf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-paperconf/"
description: "paperconf – print paper configuration information"
---

<h2 class="name">NAME</h2>
<p> <code>paperconf</code> &#8211; print paper configuration information </p>
<h2>SYNOPSIS</h2>
<p> <code>paperconf</code> [ [ <code>-p</code> ] <i>paper</i> | <code>-d</code> | <code>-a</code> ] [ <code>-z</code> ] [ <code>-n</code> | <code>-N</code> ] [ <code>-s</code> | <code>-w</code> | <code>-h</code> ] [ <code>-c</code> | <code>-m</code> | <code>-i</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>paperconf</code> prints information about a given paper. The information that can be obtained is the name of the paper, its size and its width or height. When called without arguments, <code>paperconf</code> prints the name of the system- or user-specified paper, obtained by looking in order at the <code>PAPERSIZE</code> environment variable, at the contents of the file specified by the <code>PAPERCONF</code> environment variable, at the contents of <code>/etc/papersize</code> or by using <code>letter</code> as a fall-back value if none of the other alternatives are successful. By default, width and height of the paper are printed in PostScript points.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code><i> paper</i></p>
<dd> Specify the name of the <i>paper</i> about which information is asked.</p>
<dt><code>-d</code></p>
<dd> Use the default builtin paper name.</p>
<dt><code>-a</code></p>
<dd> Consider all known paper names.</p>
<dt><code>-z</code></p>
<dd> If the paper name is unknown, print it but issue a message on the standard error and exit with a non-zero code.</p>
<dt><code>-n</code></p>
<dd> Print the name of the paper.</p>
<dt><code>-N</code></p>
<dd> Print the name of the paper with the first letter capitalized.</p>
<dt><code>-s</code></p>
<dd> Print the size (width followed by height) of the paper.</p>
<dt><code>-w</code></p>
<dd> Print the width of the paper.</p>
<dt><code>-h</code></p>
<dd> Print the height of the paper.</p>
<dt><code>-c</code></p>
<dd> Use centimetres as unit for paper size.</p>
<dt><code>-m</code></p>
<dd> Use millimetres as unit for paper size.</p>
<dt><code>-i</code></p>
<dd> Use inches as unit for paper size. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>PAPERSIZE</code></p>
<dd> Paper size to use regardless of what the papersize file contains.</p>
<dt><code>PAPERCONF</code></p>
<dd> Full path to a file containing the paper size to use.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/papersize</code></p>
<dd> Contains the name of the system-wide default paper size to be used if the <code>PAPERSIZE</code> and <code>PAPERCONF</code> variables are not set.</dl>
<h2>AUTHOR</h2>
<p> Yves Arrouye &lt;arrouye [at] debian.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-papersize/">papersize</a></code>(5) </p>
<h2>Index</h2>

---
title: "bookman(1)"
name: "bookman"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bookman/"
description: "bookman – Generate a book from man pages"
---

<h2>NAME</h2>
<p> <code>bookman </code>&#8211; Generate a book from man pages</p>
<h2>SYNOPSIS</h2>
<pre><code>
bookman[-pPxn][-o outfile][-a author][-d date][-r release]
       [-t title][-v volume][-c coverfile][manfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>bookman</code> compiles a set of man pages files specified by <i>manfile</i> arguments, or if no <i>manfile</i> is given, filenames are read from standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code></dt>
<dd> PDF output format.</dd>
<dt><code>-P</code></dt>
<dd> Postscript output format.</dd>
<dt><code>-x</code></dt>
<dd> X11 previewing, using <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1).</dd>
<dt><code>-n</code></dt>
<dd> no format, output is direct gtroff intermediate format.</dd>
<dt><code>-o</code> <i>outfile</i></dt>
<dd> Output in file <i>outfile</i>. Default is standard output.</dd>
<dt><code>-a</code> <i>author</i></dt>
<dd> Set the <i>author</i>, on the cover page.</dd>
<dt><code>-d</code> <i>date</i></dt>
<dd> Set the <i>date</i> on the cover page.</dd>
<dt><code>-r</code> <i>release</i></dt>
<dd> Set the book name and <i>release</i> on the cover page.</dd>
<dt><code>-t</code> <i>title</i></dt>
<dd> Set the <i>title</i> on the cover page.</dd>
<dt><code>-v</code> <i>volume</i></dt>
<dd> Specify the name of the <i>volume</i>.</dd>
<dt><code>-c</code> <i>coverfile</i></dt>
<dd> Uses the file <i>coverfile</i> to generate the cover page, i.e. all pages preceding the table of content. <i>coverfile</i> must be in <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7) format.</dd></dl>
<h2>EXAMPLE</h2>
<p> To build a reference manual from section 2 man, do: </p>
<pre>
    $ cd /usr/man/man2
    $ bookman -p -t 'Unix Reference Manual' * &gt;book.pdf
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code>mandoc</code>(7), <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-grops/">grops</a></code>(1), <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1), <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Marc Vertes &lt;mvertes [at] free.fr&gt; </p>

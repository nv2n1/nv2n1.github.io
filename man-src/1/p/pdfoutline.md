---
title: "pdfoutline(1)"
name: "pdfoutline"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfoutline/"
description: "pdfoutline – add outlines (aka bookmarks) to PDF files"
---

<h2>NAME</h2>
<p> pdfoutline &#8211; add outlines (aka bookmarks) to PDF files</p>
<h2>SYNOPSIS</h2>
<p> <code>pdfoutline</code> <i>input.pdf outlines.txt output.pdf</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pdfoutline</code> reads input file given as first argument, adds outlines from text file given as second argument, and saves result to file with name given as third argument. </p>
<p> File with outlines information should consist of lines in the following format: </p>
<dl>
<dt>
<dd>
<pre>
<i>&lt;level&gt;</i> <i>&lt;page&gt;</i> Outline text
</pre>
</dl>
<p> <i>&lt;level&gt;</i> and <i>&lt;page&gt;</i> should be integers. Each field should be separated by exactly one space symbol. All values for <i>&lt;level&gt;</i> should be greater or equal than that of the first line. Page numeration starts with 1. </p>
<p> Outlines file can contain comments that start with # in first column. Comments and empty lines are ignored.</p>
<h2>OPTIONS</h2>
<p> <code>pdfoutline</code> accepts no options.</p>
<h2>EXAMPLES</h2>
<p> Here is example of outlines data file: </p>
<dl>
<dt>
<dd>
<pre>
0 1 Document title
1 1 Chapter 1
2 1 Chapter 1.1
2 2 Chapter 1.2
1 3 Chapter 2
</pre>
</dl>
<p> Using this file will result in outlines like the following: </p>
<dl>
<dt>
<dd>
<pre>
Document title
+-Chapter 1
| +-Chapter 1.1
| +-Chapter 1.2
+-Chapter 2
</pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>pdfoutline</code> author is Eugeniy Meshcheryakov &lt;eugen [at] debian.org&gt;<br />
 <code>pdfoutline</code> is part of <code>fntsample</code> and can be downoaded from &lt;<a rel="nofollow" href="http://fntsample.sourceforge.net/">http://fntsample.sourceforge.net/</a>&gt;. </p>
<h2>Index</h2>

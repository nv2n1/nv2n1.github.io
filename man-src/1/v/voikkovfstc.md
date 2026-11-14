---
title: "voikkovfstc(1)"
name: "voikkovfstc"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voikkovfstc/"
description: "voikkovfstc – compiler for Varissuo finite state transducers"
---

<h2 class="name">NAME</h2>
<p> voikkovfstc &#8211; compiler for Varissuo finite state transducers </p>
<h2>SYNOPSIS</h2>
<p> <code>voikkovfstc</code> -o filename [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>voikkovfstc</code> is a compiler for Varissuo finite state transducers that are used as dictionaries for libvoikko, a library of language tools for Finnish and other languages. The compiler reads the transducer from stdin in unweighted AT&amp;T format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o filename</code></p>
<dd> Specify name for output file.</p>
<dt><code>-f format</code></p>
<dd> Specify format for output file. Possible formats are &#8216;be&#8217; (big endian), &#8216;le&#8217; (little endian) or &#8216;native&#8217; (use the endianess of the host). Default is &#8216;le&#8217;.</dl>
<h2>AUTHOR</h2>
<p> voikkovfstc and this manual page were written by Harri Pitk&auml;nen (hatapitk [at] iki.fi). </p>
<h2>Index</h2>

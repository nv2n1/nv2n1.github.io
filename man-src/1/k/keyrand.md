---
title: "keyrand(1)"
name: "keyrand"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keyrand/"
description: "keyrand – utility for collecting random data"
---

<h2 class="name">NAME</h2>
<p> keyrand &#8211; utility for collecting random data </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>keyrand</code> {<i>bits</i>} {<i>outfile</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>keyrand</code></p>
<dd>is a tool which collects a given number of random bits from the kernel random number generator, presenting a text-based user interface showing progress. </p>
<p> The random data is read from /dev/random and appended to the output file <i>outfile</i>, which must already exist.</p>
<h2>EXAMPLES</h2>
<p> The following example will collect 1024 bits of random data and append them to the file data: </p>
<dl>
<dt>
<dd>
<pre>
# keyrand 1024 data
      
</pre>
</dl>
<h2>FILES</h2>
<p> /dev/random</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-genkey/">genkey</a>(1) </p>
<h2>Index</h2>

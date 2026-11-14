---
title: "generate_randfile(1)"
name: "generate_randfile"
section: "1"
letter: "g"
url: "/docs/linux/man/1-generate_randfile/"
description: "generate_randfile – a program to generate a file of random data"
---

<h2>NAME</h2>
<p> <code>generate_randfile</code> &#8211; a program to generate a file of random data </p>
<h2>SYNOPSIS</h2>
<p> <code>generate_randfile</code> [ <code>-s</code> seed] [ <code>-f</code> file] <code>count</code> </p>
<h2>DESCRIPTION</h2>
<p> Produces a file comprised of random integers in network-byte-order from the <a href="/docs/linux/man/3-rand/">rand</a>(3) library call. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> the seed to use to create the random numbers.</p>
<dt><code>-f</code></p>
<dd> the file to create for writing the output (default is to use standard output).</p>
<dt><code>count</code></p>
<dd> the number of integers to write. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-rand/">rand</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> These programs were written by Russell Coker &lt;russell [at] coker.com.au&gt;. May be freely used and distributed without restriction. </p>
<h2>AVAILABILITY</h2>
<p> The source is available from <a rel="nofollow" href="http://www.coker.com.au/bonnie++">http://www.coker.com.au/bonnie++</a> . </p>
<p> See <a rel="nofollow" href="http://etbe.coker.com.au/category/benchmark">http://etbe.coker.com.au/category/benchmark</a> for further information. </p>
<h2>Index</h2>

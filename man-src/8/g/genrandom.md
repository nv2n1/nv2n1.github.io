---
title: "genrandom(8)"
name: "genrandom"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genrandom/"
description: "genrandom – generate a file containing random data"
---

<p>genrandom &#8211; generate a file containing random data</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>genrandom</code> [<code>-n&nbsp;<wbr></code><i>number</i>] {<i>size</i>} {<i>filename</i>}</dl>
<h2>Description</h2>
<p><code>genrandom</code></p>
<dd>generates a file or a set of files containing a specified quantity of pseudo-random data, which can be used as a source of entropy for other commands on systems with no random device.</p>
<h2>Arguments</h2>
<p>-n <i>number</i></p>
<dl>
<dd>In place of generating one file, generates <code>number</code> (from 2 to 9) files, appending <code>number</code> to the name.</dl>
<p> size</p>
<dl>
<dd>The size of the file, in kilobytes, to generate.</dl>
<p> filename</p>
<dl>
<dd>The file name into which random data should be written.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rand/">rand</a></code>(3), <code><a href="/docs/linux/man/3-arc4random/">arc4random</a></code>(3)</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2011 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>

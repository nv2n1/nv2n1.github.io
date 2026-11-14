---
title: "zsoelim(1)"
name: "zsoelim"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zsoelim/"
description: "zsoelim – satisfy .so requests in roff input"
---

<h2 class="name">NAME</h2>
<p> zsoelim &#8211; satisfy .so requests in roff input </p>
<h2>SYNOPSIS</h2>
<p> <code>zsoelim</code> [<code>-CVh</code>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>zsoelim</code> parses <i>file</i> arguments, or if none are specified, its standard input for lines of the form: </p>
<p> <code>.so</code> &lt;<i>filename</i>&gt; </p>
<p> These requests are replaced by the contents of the <i>filename</i> specified. If the request cannot be met, <code>zsoelim</code> looks for <i>filename.ext</i> where <i>.ext</i> can be one of <code>.gz</code>, <code>.Z</code> or <code>.z</code>. Other extension types may be supported depending upon compile time options. If the request can be met by a compressed file, this file is decompressed using an appropriate decompressor and its output is used to satisfy the request. </p>
<p> Traditionally, <code>soelim</code> programs were used to allow roff preprocessors to be able to preprocess the files referred to by the requests. This particular version was written to circumvent problems created by support for compressed manual pages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code>, <code>&#8211;compatible</code></p>
<dd> This flag is available for compatibility with other <code>soelim</code> programs. Its use is to enable .so requests followed by something other than whitespace. As this is already the default behaviour, it is ignored.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1)</p>
<h2>AUTHOR</h2>
<pre><code>
Wilf.(G.Wilford[at] ee.surrey.ac.uk).Fabrizio Polacco(fpolacco[at] debian.org).Colin Watson(cjwatson[at] debian.org).
</code></pre>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
<h2>Index</h2>

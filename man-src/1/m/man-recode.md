---
title: "man-recode(1)"
name: "man-recode"
section: "1"
letter: "m"
url: "/docs/linux/man/1-man-recode/"
description: "man-recode – convert manual pages to another encoding"
---

<h2 class="name">NAME</h2>
<p> man-recode &#8211; convert manual pages to another encoding </p>
<h2>SYNOPSIS</h2>
<p> <code>man-recode</code> <code>-t</code> <i>to-code</i> {<code>&#8211;suffix=</code><i>suffix/</i>|<code>&#8211;in-place</code>} [<code>-dqhV</code>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>man-recode</code> converts multiple manual pages from one encoding to another, guessing the appropriate input encoding for each one. It is useful when permanently recoding pages written in legacy character sets, or in build systems that need to recode a set of pages to a single common encoding (usually UTF-8) for installation. When converting many manual pages, this program is much faster than running <code>man &#8211;recode</code> or <code>manconv</code> on each page. </p>
<p> If an encoding declaration is found on the first line of a manual page, then that declaration is used as the input encoding for that page. Failing that, the input encoding is guessed based on the file name. </p>
<p> Encoding declarations have the following form: </p>
<dl>
<dt>
<dd>
<pre>
'\&quot; -*- coding: UTF-8 -*-
</pre>
</dl>
<p> or (if manual page preprocessors are also to be declared): </p>
<dl>
<dt>
<dd>
<pre>
'\&quot; t -*- coding: ISO-8859-1 -*-
</pre>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code> <i>encoding/</i>, <code>&#8211;to-code=</code><i>encoding</i></p>
<dd> Convert manual pages to <i>encoding</i>.</p>
<dt><code>&#8211;suffix=</code><i>suffix</i></p>
<dd> Form each output file name by appending <i>suffix</i> to the input file name, after removing any compression extension.</p>
<dt><code>&#8211;in-place</code></p>
<dd> Overwrite each input file with the output, after removing any compression extension.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not issue error messages when the page cannot be converted.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-iconv/">iconv</a></i>(1), <i><a href="/docs/linux/man/1-man/">man</a></i>(1), <i><a href="/docs/linux/man/1-manconv/">manconv</a></i>(1)</p>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a></p>
<h2>AUTHOR</h2>
<pre>
Colin Watson (cjwatson [at] debian.org).
</pre>
<h2>Index</h2>

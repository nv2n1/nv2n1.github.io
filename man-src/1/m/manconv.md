---
title: "manconv(1)"
name: "manconv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-manconv/"
description: "manconv – convert manual page from one encoding to another"
---

<h2 class="name">NAME</h2>
<p> manconv &#8211; convert manual page from one encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>manconv</code> <code>-f</code> [<i>from-code</i>[:<i>from-code</i>&#8230;]] <code>-t</code> <i>to-code</i> [<code>-dqhV</code>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>manconv</code> converts a manual page from one encoding to another, like <code>iconv</code>. Unlike <code>iconv</code>, it can try multiple possible input encodings in sequence. This is useful for manual pages installed in directories without an explicit encoding declaration, since they may be in UTF-8 or in a legacy character set. </p>
<p> If an encoding declaration is found on the first line of the manual page, that declaration overrides any input encodings specified on <code>manconv</code>&#8216;s command line. Encoding declarations have the following form: </p>
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
<dt><code>-f</code> <i>encodings</i>, <code>&#8211;from-code</code> <i>encodings</i></p>
<dd> Try each of <i>encodings</i> (a colon-separated list) in sequence as the input encoding. The default is to guess likely input encodings based on the file name.</p>
<dt><code>-t</code> <i>encoding</i>, <code>&#8211;to-code</code> <i>encoding</i></p>
<dd> Convert the manual page to <i>encoding</i>.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not issue error messages when the page cannot be converted.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-iconv/">iconv</a></i>(1), <i><a href="/docs/linux/man/1-man/">man</a></i>(1), <i><a href="/docs/linux/man/1-man-recode/">man-recode</a></i>(1)</p>
<h2>AUTHOR</h2>
<pre>
Colin Watson (cjwatson [at] debian.org).
</pre>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
<h2>Index</h2>

---
title: "discount-makepage(1)"
name: "discount-makepage"
section: "1"
letter: "d"
url: "/docs/linux/man/1-discount-makepage/"
description: "makepage – convert markdown input to a fully-formed xhtml page"
---

<h2 class="name">NAME</h2>
<p> <code>makepage</code> &#8211; convert markdown input to a fully-formed xhtml page </p>
<h2>SYNOPSIS</h2>
<p> [-<code>V</code> ] [-<code>F bitmap </code> ] [-<code>f </code><i>flags</i> ] [file ]</p>
<h2>DESCRIPTION</h2>
<p> The utility parses a <a href="/docs/linux/man/7-markdown/">markdown</a>(7)Ns-formatted textfile (or stdin if not specified,) compiles it, then prints a fully-formed xhtml page to stdout. </p>
<p> The &#8211;<code>F</code> &#8211;<code>f , </code> and &#8211;<code>V</code> flags are identical to the same options in <a href="/docs/linux/man/1-markdown/">markdown</a>(1). </p>
<p> is part of discount.</p>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-markdown/">markdown</a>(1), <a href="/docs/linux/man/3-markdown/">markdown</a>(3), <a href="/docs/linux/man/7-markdown/">markdown</a>(7), mkd-extensions7.</p>
<h2>AUTHOR</h2>
<p> An David Parsons (<code>orc [at] pell.portland.or.us</code> ) </p>
<h2>Index</h2>

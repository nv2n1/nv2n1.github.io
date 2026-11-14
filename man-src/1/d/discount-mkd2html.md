---
title: "discount-mkd2html(1)"
name: "discount-mkd2html"
section: "1"
letter: "d"
url: "/docs/linux/man/1-discount-mkd2html/"
description: "mkd2html – markdown to html converter"
---

<h2 class="name">NAME</h2>
<p> <code>mkd2html</code> &#8211; markdown to html converter </p>
<h2>SYNOPSIS</h2>
<p> [-<code>css file </code> ] [-<code>header string </code> ] [-<code>footer string </code> ] [file ]</p>
<h2>DESCRIPTION</h2>
<p> utility parses a <a href="/docs/linux/man/7-markdown/">markdown</a>(7)Ns-formatted textfile (or stdin if not specified,) and generates a web page. It reads <i>file</i> or <i>file.text</i><br />
&nbsp;<wbr>and writes the result in <i>file.html</i> (where file is the passed argument.) </p>
<p> is part of discount.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-css </code><i>file</i></p>
<dd> Specifies a CSS file.</p>
<dt><code>-header </code><i>string</i></p>
<dd> Specifies a line to add to the &lt;header&gt; tag.</p>
<dt><code>-footer </code><i>string</i></p>
<dd> Specifies a line to add before the &lt;/body&gt; tag.</dl>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-markdown/">markdown</a>(1), <a href="/docs/linux/man/3-markdown/">markdown</a>(3), <a href="/docs/linux/man/7-markdown/">markdown</a>(7), mkd-extensions7.</p>
<h2>AUTHOR</h2>
<p> An David Parsons (<code>orc [at] pell.portland.or.us</code> ) </p>
<h2>Index</h2>

---
title: "ifne(1)"
name: "ifne"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifne/"
description: "ifne – Run command if the standard input is not empty"
---

<h2 class="name">NAME</h2>
<p> ifne &#8211; Run command if the standard input is not empty </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ifne [-n] command</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>ifne</code></p>
<dd>runs the following command if and only if the standard input is not empty.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Reverse operation. Run the command if the standard input is empty. </p>
<p> Note that if the standard input is not empty, it is passed through ifne in this case.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt> <code>find . -name core | ifne mail -s &quot;Core files found&quot; root</code></dl>
<h2>AUTHOR</h2>
<dd>Copyright 2008 by Javier Merino &lt;cibervicho [at] gmail.com&gt; </p>
<p> Licensed under the GNU GPL </p>
<h2>Index</h2>

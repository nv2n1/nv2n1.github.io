---
title: "typefortune(1)"
name: "typefortune"
section: "1"
letter: "t"
url: "/docs/linux/man/1-typefortune/"
description: "typefortune – manual page for typefortune (part of gtypist)"
---

<h2>NAME</h2>
<p> typefortune &#8211; manual page for typefortune (part of gtypist)</p>
<h2>SYNOPSIS</h2>
<p> <code>typefortune</code> [ <i>Options</i>&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> typefortune creates a gtypist lesson-file from `fortune&#8217; and runs `gtypist&#8217; on it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> use D: (instead of S:)</p>
<dd>
<dt><code>-s</code> use `fortune -s&#8217;</p>
<dd>
<dt><code>-l</code> use `fortune -l&#8217;</p>
<dd>
<dt><code>-n</code> &lt;count&gt; practice &lt;count&gt; fortunes (default=1)</p>
<dd>
<dt><code>-o</code> &lt;gtypist_options&gt; pass options to gtypist</p>
<dd></dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd> To practice 3 fortunes and run gtypist as &#8211;silent -e 5 &#8211;word-processor:</p>
<dt>
<dd> `typefortune -n 3 -o &#8216;silent e,5 word-processor&#8217;</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gtypist (and typefortune)</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gtypist</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gtypist</code></dl>
<p> (section &quot;Using typefortune&quot;) should give you access to the complete manual. </p>
<h2>Index</h2>

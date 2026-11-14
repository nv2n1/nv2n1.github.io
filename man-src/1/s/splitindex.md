---
title: "splitindex(1)"
name: "splitindex"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splitindex/"
description: "splitindex – manual page for splitindex 0.2a"
---

<h2 class="name">NAME</h2>
<p> splitindex &#8211; manual page for splitindex 0.2a </p>
<h2>SYNOPSIS</h2>
<p> <code>splitindex.pl</code> [<i>OPTION</i>] &#8230; <i>INTERMEDIATE-INDEX-FILE </i>[<i>MAKEINDEX-OPTION</i>] &#8230; </p>
<p> <code>splitindex</code> [<i>OPTION</i>] &#8230; <i>INTERMEDIATE-INDEX-FILE </i>[<i>MAKEINDEX-OPTION</i>] &#8230; </p>
<p> <code>java splitindex</code> [<i>OPTION</i>] &#8230; <i>INTERMEDIATE-INDEX-FILE </i>[<i>MAKEINDEX-OPTION</i>] &#8230; </p>
<p> <code>tex splitindex</code></p>
<h2>DESCRIPTION</h2>
<p> splitindex 0.2a Copyright (c) 2002 Markus Kohm &lt;kohm [at] gmx.de&gt; </p>
<p> Split a single intermediate index file into multiple raw index files. </p>
<p> Example: splitindex.pl foo.idx.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and terminate</p>
<dt><code>-m</code>, <code>&#8211;makeindex</code> PROGNAME</p>
<dd> call PROGNAME instead of default `makeindex&#8217;.</p>
<dt><code>-i</code>, <code>&#8211;identify</code> EXPRESSION</p>
<dd> use regular EXPRESSION to match entries (see also option <code>&#8211;resultis</code> and <code>&#8211;suffixis</code>). Default is `^(\indexentry)\[([^]]*)\](.*)$&#8217;.</p>
<dt><code>-r</code>, <code>&#8211;resultis</code> PATTERN</p>
<dd> create line to be written from PATTERN after matching lines (see also option <code>&#8211;identify</code>). Default is `$1$3&#8242;.</p>
<dt><code>-s</code>, <code>&#8211;suffixis</code> PATTERN</p>
<dd> create suffix to be used from PATTERN after matching lines (see also option <code>&#8211;identify</code>). Default is `-$2&#8242;.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be more verbose (can be used multiple to increase verbosity)</p>
<dt><code>&#8211;version</code></p>
<dd> show version and terminate</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Markus Kohm &lt;kohm [at] gmx.de&gt;</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>splitindex</code> is maintained as a LaTeX manual. If the <code>texdoc</code> and <code>splitindex</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>texdoc splitidx</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>

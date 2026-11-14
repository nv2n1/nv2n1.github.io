---
title: "bbl2bib(1)"
name: "bbl2bib"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bbl2bib/"
description: "bbl2bib.pl – convert thebibliography environment to a bib file"
---

<h2 class="name">NAME</h2>
<p> bbl2bib.pl &#8211; convert thebibliography environment to a bib file </p>
<h2>SYNOPSIS</h2>
<p> bbl2bib.pl [-d] [-u] [<code>-o</code> <i>output</i>] <i>file</i></p>
<h2>OPTIONS</h2>
<dl>
<dt>[-d]</p>
<dd> Send debugging output to stdout</p>
<dt><code>-o</code> <i>output</i></p>
<dd> Output file. If this option is not used, the name for the output file is formed by changing the extension to <tt>&quot;.bib&quot;</tt></p>
<dt><code>-u</code></p>
<dd> Do not clean <font SIZE="-1">URL</font> fields. </p>
<p> Normally <tt>&quot;bbl2bib&quot;</tt> recognizes <font SIZE="-1">URL</font> fields of the kind <tt>&quot;<a rel="nofollow" href="http://dx.doi.org">http://dx.doi.org</a>&quot;</tt> and their variants and converts them to <font SIZE="-1">DOI</font> fields (see also <code><a href="/docs/linux/man/1-biburl2doi/">biburl2doi</a></code>(1) script). The switch <code>-u</code> suppresses this cleanup.</dl>
<h2>DESCRIPTION</h2>
<p> The script tries to reconstruct a <tt>&quot;bib&quot;</tt> file from the corresponding <tt>&quot;thebibliography&quot;</tt> environment. One can argue that this operation is akin to reconstructing a cow from the steak. The way the script does it is searching for the entry in the <font SIZE="-1">MR</font> database, and creating the corresponding BibTeX fields. </p>
<p> The script reads a TeX or Bbl file and extracts from it the <tt>&quot;thebibliography&quot;</tt> environment. For each bibitem it creates a plain text bibliography entry, and then tries to match it in the database.</p>
<h2>INPUT FILE</h2>
<p> We assume some structure of the input file:</p>
<dl>
<dt>1.</p>
<dd> The bibliography is contained between the lines </p>
<pre>
   egin{thebibliography}...
</pre>
<p> and </p>
<pre>
   nd{thebibliography}
</pre>
<dt>2.</p>
<dd> Each bibliography item starts from the line </p>
<pre><code>
ibitem[...]
{
    ....
}
</code></pre>
</dl>
<h2>EXAMPLES</h2>
<pre>
   bbl2bib  -o - file.tex &gt; result.bib
   bbl2bib  -o result.bib file.bbl
   bbl2bib  file.tex
</pre>
<h2>AUTHOR</h2>
<p> Boris Veytsman</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2014-2021 Boris Veytsman </p>
<p> This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law. </p>
<h2>Index</h2>

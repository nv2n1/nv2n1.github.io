---

title: "biburl2doi(1)"
name: "biburl2doi"
section: "1"
letter: "b"
url: "/docs/linux/man/1-biburl2doi/"
description: "biburl2doi.pl – convert URLs pointing to doi.org to DOIs"
---

<p> biburl2doi [<code>-D</code>] [<code>-o</code> <i>output</i>] <i>bib_file</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D</code></dt>
<dd> Do not delete URLs converted to DOIs</dd>
<dt><code>-o</code> <i>output</i></dt>
<dd> Output file. If this option is not used, the name for the output file is formed by adding <tt>&quot;_cleaned&quot;</tt> to the input file</dd></dl>
<p> The script recognizes <font SIZE="-1">URL</font> fields of the kind <tt>&quot;<a rel="nofollow" href="http://dx.doi.org">http://dx.doi.org</a>&quot;</tt> and their variants and converts them to <font SIZE="-1">DOI</font> fields.</p>
<h2>AUTHOR</h2>
<p> Boris Veytsman</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2021 Boris Veytsman </p>
<p> This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law. </p>

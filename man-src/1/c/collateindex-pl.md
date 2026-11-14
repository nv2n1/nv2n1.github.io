---
title: "collateindex-pl(1)"
name: "collateindex-pl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collateindex-pl/"
description: "collateindex.pl – generate DocBook index files"
---

<p>collateindex.pl &#8211; generate DocBook index files</p>
<h2>Synopsis</h2>
<p><code>collateindex.pl</code> [<code>-f</code>] [<code>-g</code>] [<code>-i</code> <i>id</i>] [<code>-I</code> <i>scope</i>] [<code>-N</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-p</code>]&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-q</code>]&nbsp;<wbr>[<code>-s</code>&nbsp;<wbr><i>name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>&nbsp;<wbr><i>scope</i>]&nbsp;<wbr>[<code>-t</code>&nbsp;<wbr><i>name</i>]&nbsp;<wbr>[<code>-x</code>]&nbsp;<wbr><i>file</i></p>
<h2>Description</h2>
<p><code>collateindex.pl</code> creates index data for DocBook <font SIZE="-1">XML</font> or <font SIZE="-1">SGML</font> files.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Force the output file to be written, even if it appears to have been edited by hand.</p>
<dt><code>-g</code></p>
<dd>Group terms with IndexDiv based on the first letter of the term (or its SortAs attribute). (This might not handle all language environments.)</p>
<dt><code>-i</code> <i>id</i></p>
<dd>The <font SIZE="-1">ID</font> to use for the &lt;index&gt; tag.</p>
<dt><code>-I</code> <i>scope</i></p>
<dd>The implied scope, must be <tt>&quot;all&quot;</tt>, <tt>&quot;local&quot;</tt>, or <tt>&quot;global&quot;</tt>. IndexTerms which do not specify a scope will have the implied scope. If unspecified, <tt>&quot;all&quot;</tt> is assumed.</p>
<dt><code>-N</code></p>
<dd>New index (generates an empty index file).</p>
<dt><code>-o</code> <i>file</i></p>
<dd>Output to <i>file</i>. Defaults to <i>stdout</i>.</p>
<dt><code>-p</code></p>
<dd>Link to points in the document. The default is to link to the closest containing section.</p>
<dt><code>-P</code> <i>file</i></p>
<dd>Read a preamble from <i>file</i>. The contents of <i>file</i> will be inserted before the &lt;index&gt; tag.</p>
<dt><code>-q</code></p>
<dd>Run quietly.</p>
<dt><code>-s</code> <i>name</i></p>
<dd>Name the IndexDiv that contains symbols. The default is <tt>&quot;Symbols&quot;</tt>. Meaningless if <code>-g</code> is not used.</p>
<dt><code>-S</code> <i>scope</i></p>
<dd>Scope of the index, must be <tt>&quot;all&quot;</tt>, <tt>&quot;local&quot;</tt>, or <tt>&quot;global&quot;</tt>. If unspecified, <tt>&quot;all&quot;</tt> is assumed.</p>
<dt><code>-t</code> <i>name</i></p>
<dd>Title for the index.</p>
<dt><code>-x</code></p>
<dd>Make a SetIndex.</p>
<dt><code>-V</code></p>
<dd>Print version number and exit.</p>
<dt><i>file</i></p>
<dd>The file containing index data generated with the DocBook <font SIZE="-1">DSSSL</font> <font SIZE="-1">HTML</font> stylesheet (usually called <i></i><font SIZE="-1"><i>HTML</i></font><i>.index</i>).</dl>
<h2>Example</h2>
<p><code>collateindex.pl</code> <code>-o</code> <i>index.sgml</i> <i></i><font SIZE="-1"><i>HTML</i></font><i>.index</i></p>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></p>
<dd>Success</p>
<dt><code>1</code></p>
<dd>Failure</dl>
<h2>Author</h2>
<p>Norm Walsh &lt;ndw [at] nwalsh.com&gt; </p>
<p> Minor updates by Adam Di Carlo &lt;adam [at] onshore.com&gt; and Peter Eisentraut &lt;peter_e [at] gmx.net&gt;</p>

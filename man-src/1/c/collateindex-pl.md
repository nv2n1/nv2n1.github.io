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
<p><code>collateindex.pl</code> [<code>-f</code>] [<code>-g</code>] [<code>-i</code> <i>id</i>] [<code>-I</code> <i>scope</i>] [<code>-N</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-p</code>]&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-q</code>]&nbsp;<wbr>[<code>-s</code>&nbsp;<wbr><i>name</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>&nbsp;<wbr><i>scope</i>]&nbsp;<wbr>[<code>-t</code>&nbsp;<wbr><i>name</i>]&nbsp;<wbr>[<code>-x</code>]&nbsp;<wbr><i>file</i></p>
<h2>Description</h2>
<p><code>collateindex.pl</code> creates index data for DocBook XML or SGML files.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></dt>
<dd>Force the output file to be written, even if it appears to have been edited by hand.</dd>
<dt><code>-g</code></dt>
<dd>Group terms with IndexDiv based on the first letter of the term (or its SortAs attribute). (This might not handle all language environments.)</dd>
<dt><code>-i</code> <i>id</i></dt>
<dd>The ID to use for the &lt;index&gt; tag.</dd>
<dt><code>-I</code> <i>scope</i></dt>
<dd>The implied scope, must be <tt>&quot;all&quot;</tt>, <tt>&quot;local&quot;</tt>, or <tt>&quot;global&quot;</tt>. IndexTerms which do not specify a scope will have the implied scope. If unspecified, <tt>&quot;all&quot;</tt> is assumed.</dd>
<dt><code>-N</code></dt>
<dd>New index (generates an empty index file).</dd>
<dt><code>-o</code> <i>file</i></dt>
<dd>Output to <i>file</i>. Defaults to <i>stdout</i>.</dd>
<dt><code>-p</code></dt>
<dd>Link to points in the document. The default is to link to the closest containing section.</dd>
<dt><code>-P</code> <i>file</i></dt>
<dd>Read a preamble from <i>file</i>. The contents of <i>file</i> will be inserted before the &lt;index&gt; tag.</dd>
<dt><code>-q</code></dt>
<dd>Run quietly.</dd>
<dt><code>-s</code> <i>name</i></dt>
<dd>Name the IndexDiv that contains symbols. The default is <tt>&quot;Symbols&quot;</tt>. Meaningless if <code>-g</code> is not used.</dd>
<dt><code>-S</code> <i>scope</i></dt>
<dd>Scope of the index, must be <tt>&quot;all&quot;</tt>, <tt>&quot;local&quot;</tt>, or <tt>&quot;global&quot;</tt>. If unspecified, <tt>&quot;all&quot;</tt> is assumed.</dd>
<dt><code>-t</code> <i>name</i></dt>
<dd>Title for the index.</dd>
<dt><code>-x</code></dt>
<dd>Make a SetIndex.</dd>
<dt><code>-V</code></dt>
<dd>Print version number and exit.</dd>
<dt><i>file</i></dt>
<dd>The file containing index data generated with the DocBook DSSSL HTML stylesheet (usually called <i></i><i>HTML</i><i>.index</i>).</dd></dl>
<h2>Example</h2>
<p><code>collateindex.pl</code> <code>-o</code> <i>index.sgml</i> <i></i><i>HTML</i><i>.index</i></p>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></dt>
<dd>Success</dd>
<dt><code>1</code></dt>
<dd>Failure</dd></dl>
<h2>Author</h2>
<p>Norm Walsh &lt;ndw [at] nwalsh.com&gt; </p>
<p> Minor updates by Adam Di Carlo &lt;adam [at] onshore.com&gt; and Peter Eisentraut &lt;peter_e [at] gmx.net&gt;</p>

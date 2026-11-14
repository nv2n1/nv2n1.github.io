---
title: "convertgls2bib(1)"
name: "convertgls2bib"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convertgls2bib/"
---

<h2>SYNOPSIS</h2>
<p> <code>convertgls2bib</code> [<i>option</i>]+ <i>auxfile</i></p>
<h2>DESCRIPTION</h2>
<p> Converts a <code>.tex</code> file containing glossary definitions using commands like <tt>&quot;
ewglossaryentry&quot;</tt> and <tt>&quot;
ewacronym&quot;</tt> to a <code>.bib</code> file in the format required for <code>bib2gls</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code> or <code>-h</code></p>
<dd> Display help message and exit.</p>
<dt><code>&#8211;version</code> or <code>-v</code></p>
<dd> Display version information and exit.</p>
<dt><code>&#8211;silent</code></p>
<dd> Suppress all messages except for errors.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Display messages.</p>
<dt><code>&#8211;debug</code></p>
<dd> Display debugging messages.</p>
<dt><code>&#8211;texenc</code> <i>name</i></p>
<dd> Set the character encoding to <i>name</i> for the input <code>.tex</code> files.</p>
<dt><code>&#8211;bibenc</code> <i>name</i></p>
<dd> Set the character encoding to <i>name</i> for the output <code>.bib</code> files.</p>
<dt><code>&#8211;ignore-sort</code></p>
<dd> Ignore the <code>sort</code> field (default).</p>
<dt><code>&#8211;no-ignore-sort</code></p>
<dd> Don&#8217;t ignore the <code>sort</code> field.</p>
<dt><code>&#8211;ignore-type</code></p>
<dd> Omit the <code>type</code> field. Default if <code>&#8211;split-on-type</code>.</p>
<dt><code>&#8211;no-ignore-type</code></p>
<dd> Don&#8217;t omit the <code>type</code> field. Default unless <code>&#8211;split-on-type</code>.</p>
<dt><code>&#8211;split-on-type</code> or <code>-t</code></p>
<dd> Split the entries into separate files according to the <code>type</code> field. This option automatically implements <code>&#8211;ignore-type</code> and <code>&#8211;no-overwrite</code>.</p>
<dt><code>&#8211;no-split-on-type</code></p>
<dd> Don&#8217;t split the entries into separate files according to the <code>type</code> field (default).</p>
<dt><code>&#8211;ignore-category</code></p>
<dd> Omit the <code>category</code> field. Default if <code>&#8211;split-on-category</code>.</p>
<dt><code>&#8211;no-ignore-category</code></p>
<dd> Don&#8217;t omit the <code>category</code> field. Default unless <code>&#8211;split-on-category</code>.</p>
<dt><code>&#8211;split-on-category</code> or <code>-t</code></p>
<dd> Split the entries into separate files according to the <code>category</code> field. This option automatically implements <code>&#8211;ignore-category</code> and <code>&#8211;no-overwrite</code>.</p>
<dt><code>&#8211;no-split-on-category</code></p>
<dd> Don&#8217;t split the entries into separate files according to the <code>category</code> field (default).</p>
<dt><code>&#8211;ignore-fields</code> <i>list</i> or <code>-f</code> <i>list</i></p>
<dd> Ignore all the fields in the comma-separated <i>list</i>. If the list includes <code>sort</code>, <code>type</code> or <code>category</code> it will automatically implement the corresponding <code>&#8211;ignore-sort</code>, <code>&#8211;ignore-type</code> or <code>&#8211;ignore&#8212;category</code> option. </p>
<p> This option isn&#8217;t cumulative. An empty list will clear a previously set list but won&#8217;t undo the sort, type or category ignore options.</p>
<dt><code>&#8211;overwrite</code></p>
<dd> Overwrite existing .bib files. Default unless <code>&#8211;split-on-type</code> used.</p>
<dt><code>&#8211;no-overwrite</code></p>
<dd> Don&#8217;t overwrite existing .bib files. Default if <code>&#8211;split-on-type</code> used.</p>
<dt><code>&#8211;index-conversion</code> or <code>-i</code></p>
<dd> Any entries that would normally be converted to <tt>@entry</tt> that don&#8217;t have a description or just have the description set to <tt>&quot;
opostdesc&quot;</tt> or <tt>&quot;\glsxtrnopostpunc&quot;</tt> will be converted to <tt>@index</tt> and the <code>description</code> field will be omitted.</p>
<dt><code>&#8211;no-index-conversion</code></p>
<dd> Don&#8217;t use <tt>@index</tt> instead of <tt>@entry</tt> if the description is empty or just <tt>&quot;
opostdesc&quot;</tt> or <tt>&quot;\glsxtrnopostpunc&quot;</tt> (default).</p>
<dt><code>&#8211;absorb-see</code></p>
<dd> Absorb <tt>&quot;\glssee&quot;</tt> and <tt>&quot;\glsxtrindexseealso&quot;</tt> into the data (default).</p>
<dt><code>&#8211;no-absorb-see</code></p>
<dd> Don&#8217;t absorb <tt>&quot;\glssee&quot;</tt> and <tt>&quot;\glsxtrindexseealso&quot;</tt> into the data.</p>
<dt><code>&#8211;preamble-only</code> or <code>-p</code></p>
<dd> Only parse the document preamble.</p>
<dt><code>&#8211;no-preamble-only</code></p>
<dd> Parse the entire document (default).</p>
<dt><code>&#8211;space-sub</code> <i>value</i> or <code>-s</code> <i>value</i></p>
<dd> Substitute spaces in labels with <i>value</i>.</p>
<dt><code>&#8211;locale</code> <i>lang tag</i></p>
<dd> Use the language resource files associated with the given language tag <i>lang tag</i>. If there isn&#8217;t an appropriate file, the <code>en</code> (English) file will be used.</dl>
<h2>REQUIRES</h2>
<p> Java 8 and a TeX distribution.</p>
<h2>LICENSE</h2>
<p> License GPLv3+: <font SIZE="-1">GNU GPL</font> version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt; This is free software: you are free to change and redistribute it. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>RECOMMENDED READING</h2>
<p> The bib2gls manual: </p>
<pre>
        texdoc bib2gls
</pre>
<p> The glossaries-extra manual: </p>
<pre>
        texdoc glossaries-extra
</pre>
<p> The glossaries manual: </p>
<pre>
        texdoc glossaries
</pre>
<h2>AUTHOR</h2>
<p> Nicola L. C. Talbot, &lt;<a rel="nofollow" href="http://www.dickimaw-books.com/">http://www.dickimaw-books.com/</a>&gt; </p>
<h2>Index</h2>

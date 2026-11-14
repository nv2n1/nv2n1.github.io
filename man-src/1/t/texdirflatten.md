---
title: "texdirflatten(1)"
name: "texdirflatten"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texdirflatten/"
description: "texdirflatten – Collects all components of a (La)TeX file in a single output directory — i.e., flattens its hierarchy."
---

<h2 class="name">NAME</h2>
<p> texdirflatten &#8211; Collects all components of a (La)TeX file in a single output directory &#8212; i.e., flattens its hierarchy. </p>
<h2>SYNOPSIS</h2>
<p> texdirflatten [-1|&#8211;onetex] [-f|&#8211;file input.tex] [-o outputdir]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;imgexts .ext1,.ext2,&#8230;]&nbsp;[&#8211;debug]&nbsp;[-V|&#8211;version]&nbsp;[-?|&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> This Perl script parses a LaTeX file recursively, scanning all child files, and collects details of any included and other data files, such as graphics and BiBTeX bibliography files. These component files, are then all put into a single directory (thus &#8220;flattening&#8221; the document&#8217;s directory tree). This is useful in distributing manuscripts to collaborators or in submitting to journals.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;file</code>, <code>-f</code> <i>input.tex</i></p>
<dd> Specifies input (La)TeX file.</p>
<dt><code>&#8211;onetex</code>, <code>-1</code></p>
<dd> If specified, produces a single TeX file by expanding all \input and \include commands in place.</p>
<dt><code>&#8211;output</code>, <code>-o</code> <i>outputdir</i></p>
<dd> Directory to collect all files. <code>texdirflatten</code> will copy each source file, graphics and bibliography file to this directory. It will be created if it is unexistent. If unspecified, it defaults to <tt>&quot;flat/&quot;</tt>.</p>
<dt><code>&#8211;imgexts</code> <i>.ext1,.ext2[,&#8230;]</i></p>
<dd> Prepends to the prioritized list of image extensions to search when trying to find the image to copy to output folder. The first file with the extension found will be copied and search stopped. Default order is <tt>&quot;&quot;, &quot;.eps&quot;, &quot;.pdf&quot;, &quot;.pstex&quot;</tt> (note that it includes files with no extension). If using pdflatex, one may want to add <font SIZE="-1">PDF</font> before <font SIZE="-1">EPS</font> with <tt>&quot;--imgexts .pdf&quot;</tt>. Don&#8217;t forget the dot before the extension!</p>
<dt><code>&#8211;debug</code></p>
<dd> Enables copious amounts of debugging output &#8211; useful if something is going wrong.</p>
<dt><code>&#8211;version</code>, <code>-V</code></p>
<dd> Displays the current version number and the usage and exits.</p>
<dt><code>&#8211;help</code>, <code>-?</code></p>
<dd> Show this manual page.</dl>
<h2>EXAMPLES</h2>
<p> The following example scans <tt>&quot;manuscript.tex&quot;</tt> in the current directory and gathers it and all its components in the <tt>&quot;submit_01/&quot;</tt> directory: </p>
<pre>
 $ texdirflatten -f manuscript.tex -o submit_01
</pre>
<h2>CAVEATS</h2>
<p> Please take backups before running this command. No warranties whatsoever provided. </p>
<p> You may need to run <tt>&quot;epstopdf&quot;</tt> on <font SIZE="-1">EPS</font> files if you are using <tt>&quot;pdflatex&quot;</tt>: </p>
<pre>
 $ for i in *.eps; do epstopdf $i; done
</pre>
<h2>BUGS</h2>
<p> Bug reports and patches are welcome.</p>
<h2>AUTHOR</h2>
<p> Cengiz Gunay &lt;cengique&lt;<font SIZE="-1">AT</font>&gt;users.sf.net&gt;</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyleft 2003-2017, Cengiz Gunay </p>
<p> This library is free software; you may redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>

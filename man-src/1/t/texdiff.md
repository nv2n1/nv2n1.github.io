---
title: "texdiff(1)"
name: "texdiff"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texdiff/"
description: "texdiff – Compares two (La)TeX documents to create a merged version showing changes, similar to that of ‘Change Tracking’ in some word processors."
---

<h2 class="name">NAME</h2>
<p> <code>texdiff</code> &#8211; Compares two (La)TeX documents to create a merged version showing changes, similar to that of &#8216;Change Tracking&#8217; in some word processors. </p>
<h2>SYNOPSIS</h2>
<p> texdiff [&#8211;nofloats|-n] old.tex new.tex [diff.tex]</p>
<h2>DESCRIPTION</h2>
<p> The first two files are compared and a new TeX file is output. When the output file is processed with (La)TeX it marks new changes with blue and old text with red with a strike-through line. Furthermore, passages with changes are marked at the margin with grey bars by the LaTeX <tt>&quot;changebar&quot;</tt> package (although only after running <tt>&quot;dvips&quot;</tt>, in <tt>&quot;xdvi&quot;</tt> the bars are one inch too far left to compensate the one inch offset inserted by TeX printer drivers). </p>
<p> <tt>&quot;texdiff&quot;</tt> uses and therefore requires the <tt>&quot;wdiff&quot;</tt> command to insert these marks. If LaTeX macros are included in those striked out or underlined passages, the latex run will most likely fail. The source of most problems lies in <tt>&quot;wdiff&quot;</tt> tearing apart pairs of braces. Therefore <tt>&quot;texdiff&quot;</tt> is a perl script that calls <tt>&quot;wdiff&quot;</tt> internally and fixes <tt>&quot;wdiff&quot;</tt>&#8216;s output by re-pairing braces again and handling some commonly used LaTeX macros. </p>
<p> For texdiff to work, the following LaTeX code must be inserted in the preamble of the LaTeX document: </p>
<pre><code></code>
<pre><code> \usepackage{xcolor} \usepackage{ulem} \usepackage{changebar}
 \newcommand\TLSins[1]{\cbstart{}\textcolor{ins}{\uline{#1}}\cbend{}}
 \newcommand\TLSdel[1]{\cbdelete{}\textcolor{del}{\sout{#1}}}
</code></pre>
<p> Define editing colors <code>&quot;ins&quot;</code> and <code>&quot;del&quot;</code> with existing <code>&quot;xcolor&quot;</code> color names: <br />
&nbsp;\colorlet{ins}{blue}&nbsp;\colorlet{del}{red} </p>
<p> Or from scratch: <br />
&nbsp;\definecolor{ins}{rgb}{0, 0.5, 0} </p>
<p> These macros are <font SIZE="-1">NOT</font> automatically interted at \begin{document} like the original scripts did (see the <font SIZE="-1"><code>ACKNOWLEDGMENTS</code></font> section below), because this will not work on files of a multi-file document (those included by \include or \input). Furthermore, if you insert the macros manually, you can tune them as you like, i. e. change text color or position of changebars. Have a look at the documentation of the ulem and changebar packages on how to do this!  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--nofloats</code>, <code>-n</code></dt>
<dd> <p> If given, skips contents of figure environments, but does show insertions and deletions in the caption commands. This is done to avoid complex messups in subfloat or complex figure environments. </p>
 </dd>
<dt><code>--debug</code>, <code>-d</code></dt>
<dd> <p> Turns on debugging. Temporary files that contain numbered braces are kept and a raw difference file is written as output file name appended with &#8216;-wdiff.tex&#8217;. In addition, several regular expression diagnostics are printed. <code>Warning: produces a lot of output.</code> </p>
 </dd></dl>
<h2>AUTHOR</h2>
<p> Mark Doll &lt;markdoll&lt;<font SIZE="-1">AT</font>&gt;gmx.net&gt;, Cengiz Gunay &lt;cengique&lt;<font SIZE="-1">AT</font>&gt;users.sf.net&gt;.  </p>
<h2>ACKNOWLEDGMENTS</h2>
<dl>
<dt><code>*</code></dt>
<dd> <p> Version 0.4, by <font SIZE="-1">CG</font>, 2009/09/15. Added use of GetOpt to take an optional parameter to skip float (e.g., figure or table) contents. Added an optional debug mode. Embedded <font SIZE="-1">POD</font> documentation. Fixed problem with insertion and deletions appearing in the middle of sectioning commands by throwing off LaTeX. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Version 0.3, modified by Cengiz Gunay &lt;cengique [at] users.sf.net&gt;, 2009/06/30. Added some Latex commands that should be excluded and fixed handling of &#8216;\%&#8216; characters. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Version 0.2, is a perl implementation of TeXdiff by Mark Doll &lt;markdoll [at] gmx.net&gt;, 2006/08/09. It was derived from the original bash and perl scripts created by Robert Maron &lt;robmar [at] mimuw.edu.pl&gt;, available at <a rel="nofollow" href="http://www.robmar.net/TexDiff/.">http://www.robmar.net/TexDiff/.</a> This version of texdiff is available at <a rel="nofollow" href="http://mark.doll.name/texdiff/.">http://mark.doll.name/texdiff/.</a> </p>
 </dd></dl>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyleft 2006-2009, Mark Doll and Cengiz Gunay </p>
<p> This library is free software; you may redistribute it and/or modify it under the same terms as Perl itself. </p>

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
<pre><code>


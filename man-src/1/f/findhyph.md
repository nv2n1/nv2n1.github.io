---
title: "findhyph(1)"
name: "findhyph"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findhyph/"
description: "findhyph – find words hyphenated by TeX in a document"
---
<h2 class="name">NAME</h2>
<p> findhyph – find words hyphenated by TeX in a document </p>
<h2>INSTALLATION</h2>
<p> Copy <code>findhyph</code> or <code>findhyph.bat</code> (depending on <font SIZE="-1">OS</font> used) to a directory included in system <font SIZE="-1">PATH.</font> Perl interpreter is required to be in <code>&quot;/usr/bin/&quot;</code> for Unix-like systems or in <font SIZE="-1">PATH</font> when using <code>findhyph.bat</code>.  </p>
<h2>SYNOPSIS</h2>
<p> <code>findhyph [options]</code> <i>foo.log</i>  </p>
<h2>DESCRIPTION</h2>
<p> To use this program: </p>
<dl>
<dt>1)</dt>
<dd> <p> set <code>&quot;\tracingparagraphs=1&quot;</code> in a TeX document <i>foo.tex</i> and run: </p>
 </dd>
<dt>2)</dt>
<dd> <p> <code>tex</code> <i>foo.tex</i> </p>
 </dd>
<dt>3)</dt>
<dd> <p> <code>findhyph [options]</code> <i>foo.log</i> </p>
 </dd></dl>
<p> If you are setting <code>&quot;\looseness=&lt;N&gt;&quot;</code> to optimize paragraphs, you need to pass that information to the file <i>foo.log</i> in a form <code>&quot;@looseness=&lt;N&gt;&quot;</code> (on a separate line). You can use a macro like <code>&quot;\def\setlooseness#1{\looseness=#1 \immediate\write-1{@looseness=#1}}&quot;</code> for this purpose. If the paragraph contains material in display math mode, you need to use the macro in all split parts of the paragraph.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd> <p> display hyphenated words in context </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> display font selectors and other strings starting with a backslash character </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> display program version </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> generate file containing information about one-letter prepositions and conjunctions left at the end of line </p>
 </dd>
<dt><code>-l=STRING</code></dt>
<dd> <p> use prepositions/conjunctions listed in <font SIZE="-1">STRING</font> instead of default list of prepositions and conjunctions <code>&quot;kKsSvVzZoOuUiIA&quot;</code> used for Slovak and Czech language </p>
 </dd></dl>
<h2>OUTPUT FILES</h2>
<dl>
<dt><i>foo.hyph</i></dt>
<dd> <p> List of hyphenated words. All punctuation characters, parentheses and other character immediately preceding or following displayed words are included in this list. TeX constructs which are too difficult to display (<code>&quot;\hbox{}&quot;</code>, <code>&quot;\mark{}&quot;</code> etc.) are shown as <code>&quot;[]&quot;</code>. Math mode is indicated by <code>&quot;$&quot;</code> sign. </p>
<p> Page numbers in square brackets refer to <font SIZE="-1">LOG</font> file and may occasionally differ from the typeset document. The reason is that TeX may need to break more paragraphs than it would eventually fit on the page in order to find a page break. </p>
<p> Words hyphenated in footnotes are listed before the words hyphenated in the paragraph in which the footnote is referenced. </p>
 </dd>
<dt><i>foo.prep</i></dt>
<dd> <p> List of prepositions if option <code>-p</code> is used. </p>
 </dd></dl>
<h2>HISTORY</h2>
<p> 1.0 (2001-04-08) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> public release </p>
 </dd></dl>
<p> 2.0 (2009-08-10) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> fixes in line breaks detection algorithm; support for the third pass of line breaking algorithm in TeX (positive <code>&quot;\emergencystretch&quot;</code>); support for discretionary breaks in the first pass </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> page number detection improved (recognized negative page numbers, compound page numbers when <code>&quot;\count1&quot;</code> to <code>&quot;\count9&quot;</code> registers are non-zero and <code>&quot;[nn{mapfile}]&quot;</code>, <code>&quot;[nn&lt;picture&gt;]&quot;</code> and <code>&quot;[nn&lt;newline&gt;&quot;</code> formats used by pdfTeX; false page number detection should be much more rare) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> configurable list of prepositions and conjunctions </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> hyphenated words can be displayed in context </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> suggestions and testing by Pavel Stříž </p>
 </dd></dl>
<p> 3.0 (2012-02-01) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> fixed a bug when total paragraph demerits are negative </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\looseness&quot;</code> setting is now taken into account (thanks to Karel Horák for identifying the issue) </p>
 </dd></dl>
<p> 3.1 (2012-11-03) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> fixed displaying of hyphenated ligatures (bug reported by Karel Horák) </p>
 </dd></dl>
<p> 3.2 (2012-11-21) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> improved example definition of the <code>&quot;\setlooseness&quot;</code> macro (thanks to Karl Berry) </p>
 </dd></dl>
<p> 3.3 (2013-06-18) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> fixed the manual page as suggested by Eric S. Raymond </p>
 </dd></dl>
<p> 3.4 (2015-10-18) </p>
<dl>
<dt>&bull;</dt>
<dd> <p> fixed processing of logs produced using ε-TeX&#8217;s <code>&quot;\lastlinefit&quot;</code> option (bug reported by Karel Horák) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> fixed cross-platform handling of linebreaks in the input file </p>
 </dd></dl>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or any later version.  </p>
<h2>AUTHOR</h2>
<p> Copyright (c) Martin Budaj &lt;m.b [at] speleo.sk&gt; 2000, 2001, 2009, 2012, 2015 </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">INSTALLATION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">OUTPUT FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">HISTORY</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">LICENSE</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">AUTHOR</a></dt>
<dd>  </dd></dl>

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
<p> Copy <code>findhyph</code> or <code>findhyph.bat</code> (depending on <font SIZE="-1">OS</font> used) to a directory included in system <font SIZE="-1">PATH.</font> Perl interpreter is required to be in <tt>&quot;/usr/bin/&quot;</tt> for Unix-like systems or in <font SIZE="-1">PATH</font> when using <code>findhyph.bat</code>.</p>
<h2>SYNOPSIS</h2>
<p> <code>findhyph [options]</code> <i>foo.log</i></p>
<h2>DESCRIPTION</h2>
<p> To use this program:</p>
<dl>
<dt>1)</p>
<dd> set <tt>&quot;	racingparagraphs=1&quot;</tt> in a TeX document <i>foo.tex</i> and run:</p>
<dt>2)</p>
<dd> <code>tex</code> <i>foo.tex</i></p>
<dt>3)</p>
<dd> <code>findhyph [options]</code> <i>foo.log</i></dl>
<p> If you are setting <tt>&quot;\looseness=&lt;N&gt;&quot;</tt> to optimize paragraphs, you need to pass that information to the file <i>foo.log</i> in a form <tt>&quot;@looseness=&lt;N&gt;&quot;</tt> (on a separate line). You can use a macro like <tt>&quot;\def\setlooseness#1{\looseness=#1 \immediate\write-1{@looseness=#1}}&quot;</tt> for this purpose. If the paragraph contains material in display math mode, you need to use the macro in all split parts of the paragraph.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> display hyphenated words in context</p>
<dt><code>-f</code></p>
<dd> display font selectors and other strings starting with a backslash character</p>
<dt><code>-v</code></p>
<dd> display program version</p>
<dt><code>-p</code></p>
<dd> generate file containing information about one-letter prepositions and conjunctions left at the end of line</p>
<dt><code>-l=STRING</code></p>
<dd> use prepositions/conjunctions listed in <font SIZE="-1">STRING</font> instead of default list of prepositions and conjunctions <tt>&quot;kKsSvVzZoOuUiIA&quot;</tt> used for Slovak and Czech language</dl>
<h2>OUTPUT FILES</h2>
<dl>
<dt><i>foo.hyph</i></p>
<dd> List of hyphenated words. All punctuation characters, parentheses and other character immediately preceding or following displayed words are included in this list. TeX constructs which are too difficult to display (<tt>&quot;\hbox{}&quot;</tt>, <tt>&quot;\mark{}&quot;</tt> etc.) are shown as <tt>&quot;[]&quot;</tt>. Math mode is indicated by <tt>&quot;$&quot;</tt> sign. </p>
<p> Page numbers in square brackets refer to <font SIZE="-1">LOG</font> file and may occasionally differ from the typeset document. The reason is that TeX may need to break more paragraphs than it would eventually fit on the page in order to find a page break. </p>
<p> Words hyphenated in footnotes are listed before the words hyphenated in the paragraph in which the footnote is referenced.</p>
<dt><i>foo.prep</i></p>
<dd> List of prepositions if option <code>-p</code> is used.</dl>
<h2>HISTORY</h2>
<p> 1.0 (2001-04-08)</p>
<dl>
<dt>&bull;</p>
<dd> public release</dl>
<p> 2.0 (2009-08-10)</p>
<dl>
<dt>&bull;</p>
<dd> fixes in line breaks detection algorithm; support for the third pass of line breaking algorithm in TeX (positive <tt>&quot;mergencystretch&quot;</tt>); support for discretionary breaks in the first pass</p>
<dt>&bull;</p>
<dd> page number detection improved (recognized negative page numbers, compound page numbers when <tt>&quot;

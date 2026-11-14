---
title: "latexdiff-fast(1)"
name: "latexdiff-fast"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latexdiff-fast/"
description: "latexdiff – determine and markup differences between two latex files"
---

<h2 class="name">NAME</h2>
<p> latexdiff &#8211; determine and markup differences between two latex files </p>
<h2>SYNOPSIS</h2>
<p> <code>latexdiff</code> [ <font SIZE="-1"><code>OPTIONS</code></font> ] <i>old.tex</i> <i>new.tex</i> &gt; <i>diff.tex</i></p>
<h2>DESCRIPTION</h2>
<p> Briefly, <i>latexdiff</i> is a utility program to aid in the management of revisions of latex documents. It compares two valid latex files, here called <tt>&quot;old.tex&quot;</tt> and <tt>&quot;new.tex&quot;</tt>, finds significant differences between them (i.e., ignoring the number of white spaces and position of line breaks), and adds special commands to highlight the differences. Where visual highlighting is not possible, e.g. for changes in the formatting, the differences are nevertheless marked up in the source. Note that old.tex and new.tex need to be real files (not pipes or similar) as they are opened twice (unless <tt>&quot;--encoding&quot;</tt> option is used) </p>
<p> The program treats the preamble differently from the main document. Differences between the preambles are found using line-based differencing (similarly to the Unix diff command, but ignoring white spaces). A comment, &quot;<tt>&quot;%DIF&nbsp;&gt;&quot;</tt>&quot; is appended to each added line, i.e. a line present in <tt>&quot;new.tex&quot;</tt> but not in <tt>&quot;old.tex&quot;</tt>. Discarded lines<br />
&nbsp;are deactivated by prepending&nbsp;&quot;<tt>&quot;%DIF&nbsp;&lt;&quot;</tt>&quot;. Changed blocks are preceded&nbsp;<wbr>&nbsp;by comment lines giving information about line numbers in the original files. Where there are insignificant differences, the resulting file <tt>&quot;diff.tex&quot;</tt> will be similar to <tt>&quot;new.tex&quot;</tt>. At the end of the preamble, the definitions for <i>latexdiff</i> markup commands are inserted. In differencing the main body of the text, <i>latexdiff</i> attempts to satisfy the following guidelines (in order of priority):</p>
<dl>
<dt>1.</p>
<dd> If both <tt>&quot;old.tex&quot;</tt> and <tt>&quot;new.tex&quot;</tt> are valid LaTeX, then the resulting <tt>&quot;diff.tex&quot;</tt> should also be valid LateX. (<font SIZE="-1">NB</font> If a few plain TeX commands are used within <tt>&quot;old.tex&quot;</tt> or <tt>&quot;new.tex&quot;</tt> then <tt>&quot;diff.tex&quot;</tt> is not guaranteed to work but usually will).</p>
<dt>2.</p>
<dd> Significant differences are determined on the level of individual words. All significant differences, including differences between comments should be clearly marked in the resulting source code <tt>&quot;diff.tex&quot;</tt>.</p>
<dt>3.</p>
<dd> If a changed passage contains text or text-producing commands, then running <tt>&quot;diff.tex&quot;</tt> through LateX should produce output where added and discarded passages are highlighted.</p>
<dt>4.</p>
<dd> Where there are insignificant differences, e.g. in the positioning of line breaks, <tt>&quot;diff.tex&quot;</tt> should follow the formatting of <tt>&quot;new.tex&quot;</tt></dl>
<p> For differencing the same algorithm as <i>diff</i> is used but words instead of lines are compared. An attempt is made to recognize blocks which are completely changed such that they can be marked up as a unit. Comments are differenced line by line but the number of spaces within comments is ignored. Commands including all their arguments are generally compared as one unit, i.e., no mark-up is inserted into the arguments of commands. However, for a selected number of commands (for example, <tt>&quot;

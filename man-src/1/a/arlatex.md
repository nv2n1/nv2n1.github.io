---
title: "arlatex(1)"
name: "arlatex"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arlatex/"
description: "arlatex – archive a number of ancillary LaTeX files into a master .tex file"
---

<h2 class="name">NAME</h2>
<p> arlatex &#8211; archive a number of ancillary LaTeX files into a master .tex file </p>
<h2>SYNOPSIS</h2>
<p> arlatex [<code>&#8211;outfile</code>=<i>filename</i><i>.tex</i>] <code>&#8211;document</code>=<i>filename</i><i>.tex</i> <i>filename</i> &#8230; </p>
<p> arlatex <code>&#8211;version</code> </p>
<p> arlatex <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arlatex</code> is an archiving program like <code>shar</code>, <code>tar</code>, <code>zip</code>, etc. Unlike those other archivers, however, <code>arlatex</code> is designed specifically for use with LaTeX. <code>arlatex</code> takes the name of a master <i>.tex</i> file and a number of ancillary files used by that master file (e.g., <i>.tex</i>, <i>.sty</i>, <i>.cls</i>, and <i>.eps</i> files). From these, <code>arlatex</code> outputs a single file that, when it&#8217;s run through <code>latex</code>, both regenerates the ancillary files and compiles the document into a <i>.dvi</i> file. </p>
<p> <code>arlatex</code> has a few advantages over other archiving programs:</p>
<dl>
<dt>&bull;</p>
<dd> The <i>.tex</i> files produced by <code>arlatex</code> are in a plain-text format. They are therefore perfectly portable and trivial to e-mail to colleagues.</p>
<dt>&bull;</p>
<dd> <code>arlatex</code> needs only LaTeX to run. There is no dependence on any external tools.</p>
<dt>&bull;</p>
<dd> There is no explicit extraction step. As the generated document is run through <code>latex</code>, it extracts the ancillary files and builds the document in the same step. The user running <code>latex</code> may not even notice that additional files are being produced.</dl>
<p> <code>arlatex</code> works by writing a number of <tt>&quot;egin{filecontents*}&quot;</tt>&nbsp;&#8230; <tt>&quot;nd{filecontents*}&quot;</tt> blocks to the output file, followed by the contents of the master file. (In fact, any LaTeX comments at the beginning of the master file are hoisted to the top of the generated file. This enables the author to draw attention, if so desired, to the fact that ancillary files will be generated.) The <tt>&quot;filecontents*&quot;</tt> environment, part of standard LaTeX2e, writes its contents verbatim to a specified file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Output the <code>arlatex</code> script&#8217;s version number.</p>
<dt><code>&#8211;help</code></p>
<dd> Output brief <code>arlatex</code> usage information.</p>
<dt><code>&#8211;document</code>=<i>.tex file</i></p>
<dd> Specify the master document. The output from <code>arlatex</code> is this file with all of the other files named on the command line prepended to it. Note that <tt>&quot;--document&quot;</tt> is a <i>mandatory</i> parameter; <code>arlatex</code> will abort with an error message if <tt>&quot;--document&quot;</tt> is not specified.</p>
<dt><code>&#8211;outfile</code>=<i>.tex file</i></p>
<dd> Specify the output file. The output file looks just like the master document, but with a number of <tt>&quot;filecontents*&quot;</tt> environments preceding the <tt>&quot;\documentclass&quot;</tt> line. If <tt>&quot;--outfile&quot;</tt> is not specified, output will be written to the standard output device.</dl>
<h2>EXAMPLES</h2>
<p> Suppose you have a paper called <i>paper.tex</i> that loads a custom package with <tt>&quot;

---
title: "fragmaster(1)"
name: "fragmaster"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fragmaster/"
description: "fragmaster – Using psfrag constructs with pdflatex"
---

<h2 class="name">NAME</h2>
<p> fragmaster &#8211; Using psfrag constructs with pdflatex </p>
<h2>SYNOPSIS</h2>
<pre><code>
fragmaster[options] Create EPS and PDF files with embedded psfrag substitutions.Options : -h, --help Brief usage guide.- m, --man Show full man page(needs perldoc)-- clean Clean auto - generated $basename.{eps, pdf} files.--debug Show more info and leave temporary files behind.--force Rebuild everything ignoring modification times.--dirfm = file Use given file as optional per - directory fragmaster fm control file instead of default "fragmaster.dfm".
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>fragmaster</code> is a perl script that helps using psfrag constructs with <code>pdflatex</code>. </p>
<p> <code>psfrag</code> is a LaTeX package which allows one to replace text elements in included <font SIZE="-1">EPS</font> graphics by arbitrary LaTeX output. Because <code>psfrag</code> uses PostScript for making the replacements, in principle you can&#8217;t use <code>psfrag</code> with <code>pdflatex</code> which doesn&#8217;t have any interfaces to PostScript. </p>
<p> <code>fragmaster</code> produces a new <font SIZE="-1">EPS</font> from your original <font SIZE="-1">EPS</font> which already contains all those <code>psfrag</code> replacements. This new <font SIZE="-1">EPS</font> graphic actually can be converted to <font SIZE="-1">PDF</font> including all replacements. The resulting &#8220;encapsulated&#8221; <font SIZE="-1">PDF</font> can then be used with pdflatex. </p>
<p> <code>fragmaster</code> will scan the current directory for files which end in <i>_fm</i> and have a <i>_fm.eps</i> counterpart. Looking at the modification dates, the script checks if the output files have to be rebuilt and does so if necessary (a little like &#8220;make&#8221; would do it). </p>
<p> In your LaTeX document you can include the produced graphics using </p>
<pre>
 \includegraphics{&lt;graphics&gt;}
</pre>
<p> conveniently omitting file extension. <code>latex</code> will choose the <font SIZE="-1">EPS,</font> <code>pdflatex</code> will choose the <font SIZE="-1">PDF.</font></p>
<h3><code>fragmaster</code> control file and other related files.</h3>
<p> To use the script you have to create two files per graphic: </p>
<pre>
    * &lt;graphics&gt;_fm.eps: the EPS file itself,
    * &lt;graphics&gt;_fm: a fragmaster control file.
</pre>
<p> From these files the psfragged graphics will be created: </p>
<pre>
    * &lt;graphics&gt;.eps,
    * &lt;graphics&gt;.pdf
</pre>
<p> The <i>_fm</i> control file is basically a LaTeX file (with optionally special comments) and can look like this: </p>
<pre><code>
% Just an ordinary comment %
    % Some special comments : % fmclass : book % fmclassopt : 11pt % fmopt : width = 6cm %
                                                                                     % Another special comment : % head : % 

---
title: "latexdiff-vc(1)"
name: "latexdiff-vc"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latexdiff-vc/"
description: "latexdiff-vc – wrapper script that calls latexdiff for different versions of a file under version management (CVS, RCS or SVN)"
---

<h2 class="name">NAME</h2>
<p> latexdiff-vc &#8211; wrapper script that calls latexdiff for different versions of a file under version management (CVS, RCS or SVN) </p>
<h2>SYNOPSIS</h2>
<p> <code>latexdiff-vc</code> [ <i>latexdiff-options</i> ] [ <i>latexdiff-vc-options</i> ] <code>-r</code> [<i>rev1</i>] [<code>-r</code> <i>rev2</i>] <i>file1.tex</i> [ <i>file2.tex</i> &#8230;] </p>
<pre>
 or
</pre>
<p> <code>latexdiff-vc</code> [ <i>latexdiff-options</i> ] [ <i>latexdiff-vc-options</i> ][ <code>&#8211;postscript</code> | <code>&#8211;pdf</code> ] <i>old.tex</i> <i>new.tex</i></p>
<h2>DESCRIPTION</h2>
<p> <i>latexdiff-vc</i> is a wrapper script that applies <i>latexdiff</i> to a file, or multiple files under version control (git, subversion (<font SIZE="-1">SVN</font>), mercurial (hg), <font SIZE="-1">CVS, RCS</font>), and optionally runs the sequence of <tt>&quot;latex&quot;</tt> and <tt>&quot;dvips&quot;</tt> or <tt>&quot;pdflatex&quot;</tt> commands necessary to produce pdf or postscript output of the difference tex file(s). It can also be applied to a pair of files to automatise the generation of difference file in postscript or pdf format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;rcs</code>, <code>&#8211;svn</code>, <code>&#8211;cvs</code>, <code>&#8211;git</code> or <code>&#8211;hg</code></p>
<dd> Set the version control system used. If no version system is specified, latexdiff-vc will venture a guess. </p>
<p> latexdiff-cvs, latexdiff-rcs etc are variants of latexdiff-vc which default to the respective versioning system. However, this default can still be overridden using the options above. </p>
<p> Note that hg needs to support the <tt>&quot;--root&quot;</tt> option (version &gt;= 2.9)</p>
<dt><code>-r</code>, <code>-r</code> <i>rev</i> or <code>&#8211;revision</code>, <code>&#8211;revision=</code><i>rev</i></p>
<dd> Choose revision (under <font SIZE="-1">RCS, CVS, SVN, GIT</font> or <font SIZE="-1">HG</font>). One or two <code>-r</code> options can be specified, and they result in different behaviour:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>latexdiff-vc</code> -r <i>file.tex</i> &#8230;</p>
<dd> compares <i>file.tex</i> with the most recently checked-in version checked.</p>
<dt><code>latexdiff-vc</code> -r <i>rev1</i> <i>file.tex</i> &#8230;</p>
<dd> compares <i>file.tex</i> with revision <i>rev1</i>.</p>
<dt><code>latexdiff-vc</code> -r <i>rev1</i> -r <i>rev2</i> <i>file.tex</i> &#8230;</p>
<dd> compares revisions <i>rev1</i> and <i>rev2</i> of <i>file.tex</i>. </p>
<p> Multiple files can be specified for all of the above options. All files must have the extensions <tt>&quot;.tex&quot;</tt>, <tt>&quot;.bbl&quot;</tt>, or <tt>&quot;.flt&quot;</tt>, though.</p>
<dt><code>latexdiff-vc</code> <i>old.tex</i> <i>new.tex</i></p>
<dd> compares two files.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The name of the difference file is generated automatically and reported to stdout.</dl>
<dt><code>-d</code> or <code>&#8211;dir</code> <code>-d</code> <i>path</i> or <code>&#8211;dir=</code><i>path</i></p>
<dd> Rather than appending the string <tt>&quot;diff&quot;</tt> and optionally the version numbers given to the output-file, this will prepend a directory name <tt>&quot;diff&quot;</tt> to the original filename, creating the directory and sub-directories should they not exist already. This is particularly useful in order to clone a complete directory hierarchy. Optionally, a pathname <i>path</i> can be specified, which is prepended instead of <tt>&quot;diff&quot;</tt>.</p>
<dt><code>&#8211;flatten,&#8211;flatten=keep-intermediate</code></p>
<dd> If combined with <tt>&quot;--git&quot;</tt>, <tt>&quot;--svn&quot;</tt> or <tt>&quot;--hg&quot;</tt> option or the corresponding modes, check out the revisions to compare in a separate temporary directory, and then pass on option <tt>&quot;--flatten&quot;</tt> to latexdiff. The directory in which <tt>&quot;latexdiff-vc&quot;</tt> is invoked defines the subtree which will be checked out. Note that if additional files are needed which are not included in the flatten procedure (package files, included graphics), they need to be accessible in the current directory. If you use bibtex, it is recommended to include the <tt>&quot;.bbl&quot;</tt> file in the version management. </p>
<p> The generic usage of this function is : <tt>&quot;latexdiff-vc --flatten -r rev1 [-r rev2] master.tex&quot;</tt> where master.tex is the project file containing the highest level of includes etc. </p>
<p> With <tt>&quot;--flatten=keep-intermediate&quot;</tt>, the intermediate revision snapshots are kept in the current directory (Default is to store them in a temporary directory and delete them after generating the diff file.)</p>
<dt><code>&#8211;only-changes</code></p>
<dd> Post-process the output such that only pages with changes on them are displayed. This requires the use of subtype <font SIZE="-1">ZLABEL</font> in latexdiff, which will be set automatically, but any manually set -s option will be overruled (also requires zref package to be installed). (note that this option must be combined with &#8211;ps or &#8211;pdf to make sense)</p>
<dt><code>&#8211;force</code></p>
<dd> Overwrite existing diff files without asking for confirmation. Default behaviour is to ask for confirmation before overwriting an existing difference file.</p>
<dt><code>&#8211;run</code></p>
<dd> run latex command on diff file after generation of diff file.</p>
<dt><code>&#8211;dvi</code></p>
<dd> run latex and dvixxx commands after generation of diff file.</p>
<dt><code>-c configfile</code> =item <code>&#8211;config var1=val1,var2=val2,&#8230;</code> or <code>-c var1=val1,..</code></p>
<dd> Set configuration variables for latexdiff and latexdiff-vc. The option can be repeated to set different variables (as an alternative to the comma-separated list). Available variables for latexdiff-vc:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;LATEXDIFF&quot; latexdiff command (e.g. latexdiff-fast, latexdiff-so). This command should support the option &quot;&#8211;interaction=batchmode&quot;</p>
<dd>
<dt>&quot;LATEX&quot; latex command (e.g. pdflatex, lualatex)</p>
<dd>
<dt>&quot;DVI2&quot; Command for conversion of dvi file (e.g. dvips, dvipdf)</p>
<dd>
<dt>&quot;BIBTEX&quot; Command replacing bibtex</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> All other config variables are passed to latexdiff. Explicitly set configuration changes always override implicit changes by the following shortcut options <code>&#8211;fast</code>, <code>&#8211;so</code>, <code>&#8211;ps</code> and <code>&#8211;pdf</code>.</dl>
<dt><code>&#8211;fast</code> or <code>&#8211;so</code></p>
<dd> Use <tt>&quot;latexdiff-fast&quot;</tt> or <tt>&quot;latexdiff-so&quot;</tt>, respectively (instead of <tt>&quot;latexdiff&quot;</tt>).</p>
<dt><code>&#8211;ps</code> or <code>&#8211;postscript</code></p>
<dd> Generate postscript output from difference file. This will run the sequence <tt>&quot;latex; latex; dvips&quot;</tt> on the difference file (do not use this option in the rare cases, where three <tt>&quot;latex&quot;</tt> commands are required if you care about correct referencing). If the difference file contains a <tt>&quot;ibliography&quot;</tt> tag, run the sequence <tt>&quot;latex; bibtex; latex; latex; dvips&quot;</tt>.</p>
<dt><code>&#8211;pdf</code></p>
<dd> Generate pdf output from difference file using <tt>&quot;pdflatex&quot;</tt>. This will run the sequence <tt>&quot;pdflatex; pdflatex&quot;</tt> on the difference file, or <tt>&quot;pdflatex; bibtex; pdflatex; pdflatex&quot;</tt> for files requiring bibtex. Note that this is not just a shortcut for setting configuration variable but also triggers some special behaviour.</p>
<dt><code>&#8211;show-config</code></p>
<dd> Show values of configuration variables.</p>
<dt><code>&#8211;help</code> or <code>-h</code></p>
<dd> Show help text</p>
<dt><code>&#8211;version</code></p>
<dd> Show version number</dl>
<p> All other options are passed on to <tt>&quot;latexdiff&quot;</tt>.</p>
<h2>SEE ALSO</h2>
<p> latexdiff</p>
<h2>PORTABILITY</h2>
<p> <i>latexdiff-vc</i> uses external commands and is therefore dependent on the system architecture; it has been tested mainly on Unix-like systems. It also requires a version control system and latex to be installed on the system to make use of all features. Modules from Perl 5.8 or higher are required.</p>
<h2>BUG REPORTING</h2>
<p> Please submit bug reports using the issue tracker of the github repository page <i><a rel="nofollow" href="https://github.com/ftilmann/latexdiff.git">https://github.com/ftilmann/latexdiff.git</a></i>, or send them to <i>tilmann &#8212; </i><font SIZE="-1"><i>AT</i></font><i> &#8212; gfz-potsdam.de</i>. Include the version number of <i>latexdiff-vc</i> (option <tt>&quot;--version&quot;</tt>).</p>
<h2>AUTHOR</h2>
<p> Version 1.2.1 Copyright (C) 2005-2017 Frederik Tilmann </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License Version 3 Contributors: S Utcke, H Bruyninckx; some ideas have been inspired by git-latexdiff bash script. C. Junghans: Mercurial Support. </p>
<h2>Index</h2>

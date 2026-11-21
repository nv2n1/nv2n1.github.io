---
title: "texsis(1)"
name: "texsis"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texsis/"
description: "TeXsis – TeX macros for Physicists"
---

<h2 class="name">NAME</h2>
<p> TeXsis &#8211; TeX macros for Physicists</p>
<h2>SYNOPSIS</h2>
<p> <code>texsis </code> [ filename ] </p>
<h2>DESCRIPTION</h2>
<p> <code>TeXsis </code> is a collection of <code>TeX</code> macros for typesetting physics documents such as papers and preprints, conference proceedings, books, theses, referee reports, letters, and memos. <code>TeXsis</code> macros provide automatic numbering of equations, automatic numbering and formatting of references, double column formatting, macros for making tables and figures, with or without captions, including tables with horizontal and vertical rules. <code>TeXsis</code> supports a wide variety of type sizes and a number of specialized document formats, and it even includes macros for making form letters for job applications or letters of recommendation. </p>
<p> TeXsis is an extension of &quot;plain&quot; TeX, so anything you know how to do in plain TeX you can do in TeXsis. TeXsis macro instructions are simply abbreviations for often used combinations of control sequences used to typeset physics documents. For more information about plain TeX see the man pages for <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), and/or <i>The TeXbook, </i> by D.E. Knuth. </p>
<p> TeXsis is stored as a pre-loaded format so that it loads quickly (see the man pages for <code><a href="/docs/linux/man/1-initex/">initex</a></code>(1), and/or &quot;preloaded formats&quot; in <i>The TeXbook</i> ). To run TeXsis simply give the command <code>texsis</code> in place of the <code>tex</code> command, i.e. </p>
<p> <code>texsis </code> [ filename ] </p>
<p> where <i>filename.tex </i> is the name of a file containing TeX and/or TeXsis \controlsequences. </p>
<p> TeXsis is initally in plain TeX mode, i.e. 10pt type and singlespaced, but the control sequence \texsis selects 12pt type, doublespacing, and enables other useful features. Alternatively, \paper turns on these features and sets things up to typeset a paper, \thesis does the same for typesetting a thesis, \letter is used to produce a letter using macros similar to those listed in the back of <i>The TeXbook,</i> \memo gives a setup for producing memoranda, and so on. </p>
<p> A manual which describes all of the TeXsis macro instructions is available. It is written in TeXsis, so it serves as its own example of how to write a document with TeXsis. The source code is also heavily commented, so it is possible to extract useful macros from the source code and modify them to suit your own purposes. Provisions are made for local customization of TeXsis. In particular, the file <i>TXSmods.tex, </i> if it exists, is read from the current directory or from the path <code>TEXINPUTS </code> whenever TeXsis is started. You can therefore put your own custom macros for a given project in a directory and they will automatically be loaded when TeXsis is run from that directory. </p>
<h2>INSTALLATION</h2>
<p> There is an appendix to the printed manual containing detailed installation instructions, but they are also provided in a form which can be processed by plain TeX, in the file <i>Install.tex.</i> </p>
<h2>DIAGNOSTICS</h2>
<p> TeXsis informational messages are written to the terminal and the log file begining with `% &#8216;. Warning and error messages begin with `&gt; &#8216;. </p>
<h2>FILES</h2>
<p> The source files for TeXsis and the TeXsis manual are usually installed in the same place the rest of TeX is kept. Although this may vary from intallation to installation, it will generally include a root directory named <i>texmf. </i> Common examples are <i>/usr/share/texmf/,</i> <i>/usr/lib/teTeX/texmf,</i> or <i>/usr/local/lib/texmf.</i> Filenames here are relative to this <i>texmf</i> root directory. <br />
 </p>
<dl>
<dt><i>web2c/texsis.fmt</i></dt>
<dd> <p> TeXsis pre-loaded format. </p>
 </dd>
<dt><i>tex/texsis/TXS*.tex</i></dt>
<dd> <p> TeXsis source code. </p>
 </dd>
<dt><i>tex/texsis/*.txs</i></dt>
<dd> <p> &quot;Style&quot; files which can be read in at run time for special document formats. </p>
 </dd>
<dt><i>doc/texsis/TXS*.doc</i></dt>
<dd> <p> Source for the printed TeXsis manual (written in TeXsis). </p>
 </dd>
<dt><i>tex/texsis/TXSsite.tex</i></dt>
<dd> <p> Local site customization instructions (this is read only once, when the format file is created). </p>
 </dd>
<dt><i>tex/texsis/TXSpatch.tex</i></dt>
<dd> <p> Run time patch file (like a system TeXsis.rc file, it is read every time TeXsis is run). </p>
 </dd>
<dt><i>TXSmods.tex</i></dt>
<dd> <p> Run time init file (this is read every time TeXsis is run from the current directory, or from the search path in <code>TEXINPUTS</code> ). </p>
 </dd></dl>
<h2>RESTRICTIONS</h2>
<p> Please note that TeXsis is designed to be completely compatible with plain TeX. As a result it cannot be compatible with LaTeX. </p>
<p> Having the full manual written in TeXsis can cause a problem if you don&#8217;t have a version of TeXsis already running. To get around this you can run <i>Manual.tex </i> through plain TeX and it will load the TeXsis files before processing the manual. This takes longer, but not by much. </p>
<h2>BUGS</h2>
<p> Please report bugs (or suggestions for improvements) to texsis [at] feynman.physics.lsa.umich.edu. </p>
<p> Patchs to correct small problems or make small improvements are available at </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="ftp://feynman.physics.lsa.umich.edu/texsis/">ftp://feynman.physics.lsa.umich.edu/texsis/</a> </p>
<p> in the file <i>TXSpatch.tex</i> (If that file doesn&#8217;t exist then there are no current patches.) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-initex/">initex</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-virtex/">virtex</a></code>(1) <br />
 Donald E. Knuth, <i>The TeXbook;</i> <br />
 Michael Doob, <i>A Gentle Introduction to TeX.</i> </p>
<h2>AUTHORS</h2>
<p> Eric Myers &lt;myers [at] umich.edu&gt; <br />
 Department of Physics <br />
 University of Michigan <br />
 Ann Arbor, Michigan USA </p>
<p> and </p>
<p> Frank E. Paige &lt;paige [at] bnl.gov&gt; <br />
 Physics Department <br />
 Brookhaven National Laboratory <br />
 Upton, New York 11973 USA </p>
<h2>VERSION</h2>
<p> Revision Number: 2.18/beta3 <br />
 Release Date: 16 May 2000 </p>

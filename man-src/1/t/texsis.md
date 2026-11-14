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
<p> where <i>filename.tex </i> is the name of a file containing TeX and/or TeXsis 

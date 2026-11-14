---
title: "pdfjadetex(1)"
name: "pdfjadetex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfjadetex/"
description: "pdfjadetex – PDF output from JadeTeX"
---

<h2 class="name">NAME</h2>
<p> pdfjadetex &#8211; PDF output from JadeTeX </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfjadetex</code> [<i>options</i>] [<i>commands</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page was derived from the manual page for pdfTeX and is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> pdfjadeTeX is a version of TeX that can create <i>PDF</i> files as well as <i>DVI</i> files. </p>
<p> The typical use of pdfjadeTeX is with a pregenerated formats for which PDF output has been enabled. The <code>pdfjadetex</code> command uses the equivalent of the plain JadeTeX format. </p>
<p> pdfjadeTeX&#8217;s handling of its command-line arguments is similar to that of LaTeX.</p>
<h2>OPTIONS</h2>
<p> This version of pdfjadeTeX understands the following command line options.</p>
<dl>
<dt><code>&#8211;fmt</code><i>&nbsp;format</i></p>
<dd> Use <i>format</i> as the name of the format to be used, instead of the name by which pdfjadeTeX was called or a <i>%&amp;</i> line.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;ini</code></p>
<dd> Be <code>pdfinitex</code>, for dumping formats; this is implicitly true if the program is called as <code>pdfinitex</code>.</p>
<dt><code>&#8211;interaction</code><i>&nbsp;mode</i></p>
<dd> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding 

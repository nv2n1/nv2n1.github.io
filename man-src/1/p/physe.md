---
title: "physe(1)"
name: "physe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-physe/"
description: "pdftex – PDF output from TeX"
---

<h2 class="name">NAME</h2>
<p> pdftex &#8211; PDF output from TeX </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftex</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]</p>
<h2>DESCRIPTION</h2>
<p> Run the pdfTeX typesetter on <i>file</i>, usually creating <i>file.pdf</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of pdfTeX commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument pdfTeX uses a different set of precompiled commands, contained in <i>format</i><code>.fmt</code>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> pdfTeX is a version of TeX, with the e-TeX extensions, that can create PDF files as well as DVI files. </p>
<p> In DVI mode, pdfTeX can be used as a complete replacement for the TeX engine. </p>
<p> The typical use of pdfTeX is with a pregenerated formats for which PDF output has been enabled. The <code>pdftex</code> command uses the equivalent of the plain TeX format, and the <code>pdflatex</code> command uses the equivalent of the LaTeX format. To generate formats, use the <code>-ini</code> switch. </p>
<p> The <code>pdfinitex</code> and <code>pdfvirtex</code> commands are pdfTeX&#8217;s analogues to the <code>initex</code> and <code>virtex</code> commands. In this installation, if the links exist, they are symbolic links to the <code>pdftex</code> executable. </p>
<p> In PDF mode, pdfTeX can natively handle the <i>PDF</i>, <i>JPG</i>, <i>JBIG2</i>, and <i>PNG</i> graphics formats. pdfTeX cannot include PostScript or Encapsulated PostScript (EPS) graphics files; first convert them to PDF using <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1). pdfTeX&#8217;s handling of its command-line arguments is similar to that of of the other TeX programs in the <i>web2c</i> implementation. </p>
<p> Starting with version 1.40, pdfTeX incorporates the e-TeX extensions, and pdfeTeX is just a copy of pdfTeX. See <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> This version of pdfTeX understands the following command line options.</p>
<dl>
<dt><code>-cnf-line</code><i>&nbsp;string</i></p>
<dd> Parse <i>string</i> as a <i>texmf.cnf</i> configuration line. See the Kpathsea manual.</p>
<dt><code>-draftmode</code></p>
<dd> Sets \pdfdraftmode so pdfTeX doesn&#8217;t write a PDF and doesn&#8217;t read any included images, thus speeding up execution.</p>
<dt><code>-enc</code></p>
<dd> Enable the encTeX extensions. This option is only effective in combination with <code>-ini</code>. For documentation of the encTeX extensions see <a rel="nofollow" href="http://www.olsak.net/enctex.html.">http://www.olsak.net/enctex.html.</a></p>
<dt><code>-etex</code></p>
<dd> Enable the e-TeX extensions. This option is only effective in combination with <code>-ini</code>. See <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1).</p>
<dt><code>-file-line-error</code></p>
<dd> Print error messages in the form <i>file:line:error</i> which is similar to the way many compilers format them.</p>
<dt><code>-no-file-line-error</code></p>
<dd> Disable printing error messages in the <i>file:line:error</i> style.</p>
<dt><code>-file-line-error-style</code></p>
<dd> This is the old name of the <code>-file-line-error</code> option.</p>
<dt><code>-fmt</code><i>&nbsp;format</i></p>
<dd> Use <i>format</i> as the name of the format to be used, instead of the name by which pdfTeX was called or a <i>%&amp;</i> line.</p>
<dt><code>-halt-on-error</code></p>
<dd> Exit with an error code when an error is encountered during processing.</p>
<dt><code>-help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-ini</code></p>
<dd> Start in <i>INI</i> mode, which is used to dump formats. The <i>INI</i> mode can be used for typesetting, but no format is preloaded, and basic initializations like setting catcodes may be required.</p>
<dt><code>-interaction</code><i>&nbsp;mode</i></p>
<dd> Sets the interaction mode. The mode can be either <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding 

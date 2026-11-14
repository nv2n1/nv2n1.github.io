---
title: "dvitype(1)"
name: "dvitype"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvitype/"
description: "dvitype, odvitype – translate a dvi file for humans"
---

<h2 class="name">NAME</h2>
<p> dvitype, odvitype &#8211; translate a dvi file for humans </p>
<h2>SYNOPSIS</h2>
<p> <code>dvitype</code> <i>dvi_name</i>[<i></i><code>.dvi</code>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>dvitype</code> program translates a DVI (DeVice Independent) file output by (for example) <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) or <code><a href="/docs/linux/man/1-gftodvi/">gftodvi</a></code>(1), to a file that humans can read. It also serves as a DVI file-validating program (i.e., if <code>dvitype</code> can read it, it&#8217;s correct) and as an example of a DVI-reading program for future device drivers. </p>
<p> The output file can include all commands, just the important ones, or none at all (in which case only errors are reported). A subinterval of pages may be selected for transliteration; the magnification and resolution of the &#8220;output device&#8221; may be changed; and so on. All options are specified with an on-line dialog. </p>
<p> The <code>.dvi</code> extension is supplied if omitted from <i>dvi_name</i>. The output goes to <i>stdout</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dpi=</code><i>REAL</i></p>
<dd> Set resolution to <i>REAL</i> pixels per inch; default 300.0.</dl>
<dl>
<dt><code>-magnification=</code><i>NUMBER</i></p>
<dd> Override existing magnification with <i>NUMBER</i>.</dl>
<dl>
<dt><code>-max-pages=</code><i>NUMBER</i></p>
<dd> Process <i>NUMBER</i> pages; default one million.</dl>
<dl>
<dt><code>-output-level=</code><i>NUMBER</i></p>
<dd> Verbosity level, from 0 to 4; default 4.</dl>
<dl>
<dt><code>-page-start=</code><i>PAGE-SPEC</i></p>
<dd> Start at <i>PAGE-SPEC</i>, for example `2&#8242; or `5.*.-2&#8242;.</dl>
<dl>
<dt><code>-show-opcodes</code></p>
<dd> Show numeric opcodes (in decimal).</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable TEXFONTS is used to search for the TFM files used in the DVI file. See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching. If TEXFONTS is not set, it uses the system default.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gftype/">gftype</a></code>(1), <code><a href="/docs/linux/man/1-pktype/">pktype</a></code>(1).<br />
 Donald E. Knuth, <i>TeXware</i>.</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote the program. It was published as part of the <i>TeXware</i> technical report, available from the TeX Users Group. Howard Trickey and Pavel Curtis originally ported it to Unix. </p>
<h2>Index</h2>

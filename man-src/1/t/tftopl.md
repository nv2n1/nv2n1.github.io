---
title: "tftopl(1)"
name: "tftopl"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tftopl/"
description: "tftopl – convert TeX font metric (tfm) files to property lists"
---

<h2 class="name">NAME</h2>
<p> tftopl &#8211; convert TeX font metric (tfm) files to property lists </p>
<h2>SYNOPSIS</h2>
<p> <code>tftopl</code> [<i>OPTIONS</i>] <i>tfm_name</i>[<i></i><code>.tfm</code>] [<i>pl_name</i>[<i></i><code>.pl</code>]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>tftopl</code> program translates a (program-oriented) font metric file to a (human-oriented) property list file. Thus, you can edit the contents of the TFM files, if the font designer has not done his or her job properly, or if you&#8217;re encountering strange difficulties, or if you&#8217;re just curious. It also serves as a TFM-file validating program, i.e., if no error messages are given, the input file is correct. </p>
<p> The <i>pl_name</i> is extended with <code>.pl</code> if it lacks a suffix. If <i>pl_name</i> is not given, standard output is used. Likewise, <i>tfm_name</i> is extended with <code>.tfm</code> if it lacks a suffix. Also, path searching is done for the TFM file using the environment variable TEXFONTS. If that is not set, <code>tftopl</code> uses the system default. </p>
<p> See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-charcode-format=</code><i>format</i></p>
<dd> The argument <i>format</i> specifies how character codes are output in the PL file. By default, only letters and digits are output using the <code>C</code> integer code (i.e., in ASCII); the others are output in octal. (Unless the font&#8217;s coding scheme starts with <code>TeX math sy</code> or <code>TeX math ex</code>, in which case all character codes are output in octal.) If <i>format</i> is <code>ascii</code>, all character codes that correspond to graphic characters, besides the left and right parentheses, are output in ASCII. Finally, if <i>format</i> is <code>octal</code>, all character codes are output in octal.</dl>
<dl>
<dt><code>-verbose</code></p>
<dd> Without this option, <code>tftopl</code> operates silently. With it, a banner and progress report are printed on <i>stdout</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1),<br />
 Donald E. Knuth, <i>TeXware</i>.<br />
 Donald E. Knuth, <i>The Metafontbook</i> (Volume C of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13445-4.</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote the program. It was published as part of the <i>TeXware</i> technical report, available from the TeX Users Group. Howard Trickey and Pavel Curtis originally ported it to Unix. </p>
<h2>Index</h2>

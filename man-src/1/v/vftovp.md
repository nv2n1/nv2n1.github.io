---
title: "vftovp(1)"
name: "vftovp"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vftovp/"
description: "vftovp – convert virtual font (vf) files to virtual property lists (vpl)"
---

<h2 class="name">NAME</h2>
<p> vftovp &#8211; convert virtual font (vf) files to virtual property lists (vpl) </p>
<h2>SYNOPSIS</h2>
<p> <code>vftovp</code> [<i>OPTIONS</i>] <i>vf_name</i>[<i></i><code>.vf</code>] [<i>tfm_name</i>[<i></i><code>.tfm</code>] [<i>vpl_name</i>[<i></i><code>.vpl</code>]]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>vftovp</code> program translates a (program-oriented) virtual font file and its accompanying TeX font metric file to a (human-oriented) property list file. Thus, the virtual font can be edited, and its exact contents can be displayed mnemonically. It also serves as a VF-file validating program; if no error messages are given, the input files are correct. </p>
<p> The filenames are extended with the appropriate extension if necessary.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-charcode-format=</code><i>format</i></p>
<dd> The argument <i>format</i> specifies how character codes are output in the VPL file. By default, only letters and digits are output using the <code>C</code> integer code (i.e., in ASCII); the others are output in octal. (Unless the font&#8217;s coding scheme starts with <code>TeX math sy</code> or <code>TeX math ex</code>, when all are output in octal.) If <i>format</i> is <code>ascii</code>, all character codes that correspond to graphic characters, besides the left and right parentheses, are output in ASCII. On the other hand, if <i>format</i> is <code>octal</code>, all character codes are output in octal.</dl>
<dl>
<dt><code>-verbose</code></p>
<dd> Without this option, <code>vftovp</code> operates silently. With it, a banner and progress report are printed on <i>stdout</i>.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>vftovp</code> looks for <i>vf_name</i> using the environment variable VFFONTS. If that is not set, it uses the variable TEXFONTS. If that is not set, it uses the system default. </p>
<p> See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1), <code><a href="/docs/linux/man/1-vptovf/">vptovf</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote the program, based in part on an idea of David Fuchs, starting with the code for <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1). Karl Berry adapted it for compilation with <code>web2c</code>. </p>
<h2>Index</h2>

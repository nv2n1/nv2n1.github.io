---
title: "vptovf(1)"
name: "vptovf"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vptovf/"
description: "vptovf – convert virtual property lists to virtual font metrics"
---

<h2 class="name">NAME</h2>
<p> vptovf &#8211; convert virtual property lists to virtual font metrics </p>
<h2>SYNOPSIS</h2>
<p> <code>vptovf</code> [<code>-verbose</code>] <i>vpl_name</i>[<i></i><code>.vpl</code>] [<i>vfm_name</i>[<i></i><code>.vf</code>] [<i>tfm_name</i>[<i></i><code>.tfm</code>]]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>vptovf</code> program translates a (human-oriented) property list file to a pair of (program-oriented) files in the VF (virtual font) and TFM (TeX font metric) formats. Thus, a virtual font file can be edited and its exact contents can be displayed mnemonically. New virtual fonts, which map characters as seen by TeX into an arbitrary sequence of low-level typesetting operations, can also be created in this way. </p>
<p> All three filenames, <i>vpl_name</i>, <i>vf_name</i>, and <i>tfm_name</i>, are extended with the appropriate suffix, if they lack one.</p>
<h2>OPTIONS</h2>
<p> Without the <code>-verbose</code> option, <code>vptovf</code> operates silently. With it, a banner and progress report are printed on <i>stdout</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1), <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1), <code><a href="/docs/linux/man/1-vftovp/">vftovp</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote the program, based in part on an idea of David Fuchs, starting with the code for <code><a href="/docs/linux/man/1-pltotf/">pltotf</a></code>(1). Karl Berry adapted it for compilation with <code>web2c</code>. </p>
<h2>Index</h2>

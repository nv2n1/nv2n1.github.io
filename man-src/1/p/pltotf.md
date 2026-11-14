---
title: "pltotf(1)"
name: "pltotf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pltotf/"
description: "pltotf – convert property list files to TeX font metric (tfm) format"
---

<h2 class="name">NAME</h2>
<p> pltotf &#8211; convert property list files to TeX font metric (tfm) format </p>
<h2>SYNOPSIS</h2>
<p> <code>pltotf</code> [<code>-verbose</code>] <i>pl_file_name</i>[<i></i><code>.pl</code>] [<i>tfm_file_name</i>[<i></i><code>.tfm</code>]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>pltotf</code> program translates a (human-oriented) property list file to a (program-oriented) TeX font metric file. Thus, after editing the property list file, a TFM file can be generated for use with, for example, <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1). </p>
<p> The <i>pl_file_name</i> is extended with <code>.pl</code> if it lacks a suffix. No path searching is done. </p>
<p> If no <i>tfm_file_name</i> is given, the basename of <i>pl_file_name</i> with suffix <code>.tfm</code> is used; otherwise <i>tfm_file_name</i> is extended with <code>.tfm</code> if it lacks a suffix.</p>
<h2>OPTIONS</h2>
<p> Without the <code>-verbose</code> option, <code>pltotf</code> operates silently. With it, a banner and progress report are printed on <i>stdout</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tftopl/">tftopl</a></code>(1).<br />
 Donald E. Knuth, <i>TeXware</i>.<br />
 Donald E. Knuth, <i>The Metafontbook</i>, (Volume C of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13445-4.</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote the program. It was published as part of the <i>TeXware</i> technical report, available from the TeX Users Group. Howard Trickey, Pavel Curtis, and Richard Furuta originally ported it to Unix. </p>
<h2>Index</h2>

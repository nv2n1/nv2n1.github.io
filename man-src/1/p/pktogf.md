---
title: "pktogf(1)"
name: "pktogf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pktogf/"
description: "pktogf – convert packed font files to generic font files"
---

<h2 class="name">NAME</h2>
<p> pktogf &#8211; convert packed font files to generic font files </p>
<h2>SYNOPSIS</h2>
<p> <code>pktogf</code> [<code>-v</code>] <i>pk_file_name</i> [<i>gf_file_name</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>pktogf</code> program converts a packed font file (<i>pk</i>) to a generic font file (<i>gf</i>). Packed font files are much smaller than the corresponding <i>gf</i> files, but some DVI readers only understand <i>gf</i> files. </p>
<p> The <i>pk_file_name</i> on the command line must be complete. Because the resolution is part of the extension, it would not make sense to append a default extension as is done with TeX or DVI-reading software. The <i>gf_file_name</i> defaults to the same (stripped) name as <i>pk_file_name</i>, and it is placed in the current working directory with the <code>gf</code> suffix replacing <code>pk</code>. For example, the input file <i>io.300pk</i> would become <i>io.300gf</i>.</p>
<h2>OPTIONS</h2>
<p> Unless the <code>-v</code> switch is given, <code>pktogf</code> operates silently. With <code>-v</code>, the version number of the program and statistics about the unpacking are output to <i>stdout</i>.</p>
<h2>ENVIRONMENT</h2>
<p> <code>pktogf</code> looks for <i>pk_file_name</i> using the environment variable PKFONTS. If that is not set, it uses the variable TEXPKS. If that is not set, it uses TEXFONTS. If that is not set, it uses the system default. </p>
<p> See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gftopk/">gftopk</a></code>(1), <code><a href="/docs/linux/man/1-gftype/">gftype</a></code>(1), <code><a href="/docs/linux/man/1-pktype/">pktype</a></code>(1).<br />
 Donald E. Knuth et al., <i>Metafontware</i>.</p>
<h2>AUTHORS</h2>
<p> Tomas Rokicki wrote the program. Pierre MacKay adapted it for compilation with <code>web2c</code>. </p>
<h2>Index</h2>

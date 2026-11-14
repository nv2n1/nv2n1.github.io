---
title: "gftopk(1)"
name: "gftopk"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gftopk/"
description: "gftopk – convert generic font files to packed font files"
---

<h2 class="name">NAME</h2>
<p> gftopk &#8211; convert generic font files to packed font files </p>
<h2>SYNOPSIS</h2>
<p> <code>gftopk</code> [<code>-v</code>] <i>gf_file_name</i> [<i>pk_file_name</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>gftopk</code> program converts a generic font file output by, for example, <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), to a packed font file for use by DVI-reading programs. Packed font files (<i>pk</i> files) are much smaller than the corresponding <i>gf</i> files, so they are generally the font format of choice. </p>
<p> The <i>gf_file_name</i> on the command line must be complete. Because the resolution is part of the extension, it would not make sense to append a default extension as is done with TeX or DVI-reading software. The <i>pk_file_name</i> defaults to the same (stripped) name as <i>gf_file_name</i>, and it is placed in the current working directory with the <code>pk</code> suffix replacing <code>gf</code>. For example, the input file <i>cmr10.300gf</i> would become <i>cmr10.300pk</i>.</p>
<h2>OPTIONS</h2>
<p> Unless the <code>-v</code> switch is given, <code>gftopk</code> operates silently. With <code>-v</code>, the version number of the program and statistics about the packing are output to <i>stdout</i>.</p>
<h2>ENVIRONMENT</h2>
<p> <code>gftopk</code> looks for <i>gf_file_name</i> first in the current directory. If it is not present there, it uses the environment variable GFFONTS. If that is not set, it uses the variable TEXFONTS. If that is not set, it uses the system default. </p>
<p> See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gftype/">gftype</a></code>(1), <code><a href="/docs/linux/man/1-pktogf/">pktogf</a></code>(1), <code><a href="/docs/linux/man/1-pktype/">pktype</a></code>(1).<br />
 Donald E. Knuth et al., <i>Metafontware</i>.</p>
<h2>AUTHORS</h2>
<p> Tomas Rokicki wrote the program. It was published as part of the <i>Metafontware</i> technical report, available from the TeX Users Group. Paul Richards originally ported it to Unix. </p>
<h2>Index</h2>

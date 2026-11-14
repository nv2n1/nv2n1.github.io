---
title: "gftype(1)"
name: "gftype"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gftype/"
description: "gftype – translate a generic font file for humans to read"
---

<h2 class="name">NAME</h2>
<p> gftype &#8211; translate a generic font file for humans to read </p>
<h2>SYNOPSIS</h2>
<p> <code>gftype</code> [<code>-i</code>] [<code>-m</code>] <i>gf_file_name</i> [<i>output_file_name</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>gftype</code> program translates a <i>gf</i> (generic font) file output by, for example, <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), to a file that humans can read. It also serves as a <i>gf</i> file-validating program (i.e., if <code>gftype</code> can read it, it&#8217;s correct) and as an example of a <i>gf</i>-reading program for other software that wants to read <i>gf</i> files. </p>
<p> The <i>gf_file_name</i> on the command line must be complete. Because the resolution is part of the extension, it would not make sense to append a default extension as is done with TeX or DVI-reading software. If no <i>output_file_name</i> is specified, the output goes to <i>stdout</i>.</p>
<h2>OPTIONS</h2>
<p> The output file includes bitmap images of the characters, if <code>-i</code> is given on the command line, and a symbolic listing of the <i>gf</i> commands, if <code>-m</code> is specified.</p>
<h2>ENVIRONMENT</h2>
<p> <code>gftype</code> looks for <i>gf_file_name</i> using the environment variable GFFONTS. If that is not set, it uses the variable TEXFONTS. If that is not set, it uses the system default.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1), <code><a href="/docs/linux/man/1-pktype/">pktype</a></code>(1).<br />
 Donald E. Knuth et al., <i>Metafontware</i>.</p>
<h2>AUTHORS</h2>
<p> David Fuchs and Don Knuth wrote the program. It was published as part of the <i>Metafontware</i> technical report, available from the TeX Users Group. Paul Richards originally ported it to Unix. </p>
<h2>Index</h2>

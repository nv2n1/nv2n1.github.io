---
title: "pktype(1)"
name: "pktype"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pktype/"
description: "pktype – verify and translate a packed font bitmap file to plain text"
---

<h2 class="name">NAME</h2>
<p> pktype &#8211; verify and translate a packed font bitmap file to plain text </p>
<h2>SYNOPSIS</h2>
<p> <code>pktype</code> <i>pk_file</i>[pk]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>pktype</code> program translates a packed font file (<i>pk</i>) (output by, for example, <code><a href="/docs/linux/man/1-gftopk/">gftopk</a></code>(1) to a file that humans can read. It also serves as a <i>pk</i> file-validating program (i.e., if <code>pktype</code> can read it, it&#8217;s correct) and as an example of a <i>pk</i>-reading program for other software that wants to read <i>pk</i> files. </p>
<p> The input <i>pk_file</i> on the command line may omit the suffix `pk. The plain text translation is always written to standard output. </p>
<p> The output file gives a compact encoding of the packed encoding, using conventions described in the source code. Run lengths of black pixels alternate with parenthesized run lengths of white pixels, and brackets are used to indicate when a row should be repeated.</p>
<h2>ENVIRONMENT</h2>
<p> <code>pktype</code> looks for <i>pk_file</i> in the usual places according to Kpathsea. </p>
<p> See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1), <code><a href="/docs/linux/man/1-gftopk/">gftopk</a></code>(1), <code><a href="/docs/linux/man/1-gftype/">gftype</a></code>(1).<br />
 Donald E. Knuth et al., <i>Metafontware</i>.</p>
<h2>AUTHORS</h2>
<p> Tomas Rokicki wrote the program, Donald E. Knuth originally ported it to Unix, Pierre MacKay originally adapted it for compilation with Web2c. </p>
<h2>Index</h2>

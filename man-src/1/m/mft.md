---
title: "mft(1)"
name: "mft"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mft/"
description: "mft – translate Metafont or MetaPost code to TeX code for prettyprinting"
---

<h2 class="name">NAME</h2>
<p> mft &#8211; translate Metafont or MetaPost code to TeX code for prettyprinting </p>
<h2>SYNOPSIS</h2>
<p> <code>mft</code> [<i>OPTIONS</i>] <i>mf_file_name</i>[<code>.mf</code>|<code>.mp</code>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>mft</code> program creates a TeX file from a Metafont or MetaPost program. It takes appropriate care of typographic details like page layout and the use of indentation, italics, boldface, etc., as illustrated in the book <i>Computer Modern Typefaces</i>. Special conventions in Metafont and MetaPost comments allow you to control things that would not otherwise come out right; section 1 of the MFT source program in the <i>Metafontware</i> report explains these rules. </p>
<p> The <code>mft</code> program uses an optional change file (which works just as the change files to <code><a href="/docs/linux/man/1-tangle/">tangle</a></code>(1) and <code><a href="/docs/linux/man/1-weave/">weave</a></code>(1) do) and one or several style files (which are prepended to everything). If no style file is specified, the style file <code>plain.mft</code> for Metafont (or <code>mplain.mft</code> for MetaPost) is automatically used. </p>
<p> The <i>mf_file_name</i>, optional <i>change_file_name</i>, and <i>style_file_name</i> files are searched for using the MFINPUTS (for Metafont) or MPINPUTS (for MetaPost) and MFTINPUTS environment variables if you have set them, or else the corresponding system defaults. </p>
<p> The output TeX file name is formed by using <code>.tex</code> in place of the extension of <i>mf_file_name</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-change=</code><i>change_file_name</i>[.ch]</p>
<dd> Apply the change file <i>change_file_name</i> to <i>mf_file_name</i>.</dl>
<dl>
<dt><code>-metapost</code></p>
<dd> Assume <i>mf_file_name</i> is a MetaPost source file (this is the default if <i>mf_file_name</i> has the extension <code>.mp</code>).</dl>
<dl>
<dt><code>-style=</code><i>style_file_name</i>[.mft]</p>
<dd> Use the style file <i>style_file_name</i> instead of <code>plain.mft</code> (or <code>mplain.mft</code>); this option can be given more than once.</dl>
<h2>FILES</h2>
<dl>
<dt><i>mftmac.tex</i></p>
<dd> TeX macros used by <code>mft</code> output.</p>
<dt><i>plain.mft</i>, <i>mplain.mft</i></p>
<dd> Default style files.</p>
<dt><i>cmbase.mft</i></p>
<dd> Style file for Computer Modern.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <code><a href="/docs/linux/man/1-weave/">weave</a></code>(1).<br />
 Donald E. Knuth, <i>Computer Modern Typefaces</i> (Volume E of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13446-2.<br />
 Donald E. Knuth et al., <i>Metafontware</i>.</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote the program, and he ported it to Unix with the help of Pierre MacKay and the Unix port of <code>weave</code> by Howard Trickey and Pavel Curtis. The program is published in the <i>Metafontware</i> technical report, available from the TeX Users Group. </p>
<h2>Index</h2>

---
title: "mktextfm(1)"
name: "mktextfm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mktextfm/"
description: "mktextfm – create a TFM file for a font"
---

<h2 class="name">NAME</h2>
<p> mktextfm &#8211; create a TFM file for a font </p>
<h2>SYNOPSIS</h2>
<p> <code>mktextfm</code> [<i>options</i>] <i>font</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mktextfm</code> is used to generate a tfm file from the Metafont source files for <i>font</i>, or <code><a href="/docs/linux/man/1-hbf2gf/">hbf2gf</a></code>(1), if possible. If <i>destdir</i> is given, the generated file will be installed there, otherwise a (rather complicated) heuristic is used. If the tfm file already exists in the destination location, this is reported and nothing is done. </p>
<p> If a GF (Generic Font) bitmap file is also generated, as is typical with &Mu;F, it is converted to PK (Packed Font) and installed similarly. </p>
<p> The full pathname of the generated file is printed on standard output. </p>
<p> If available, the <code><a href="/docs/linux/man/1-mf-nowin/">mf-nowin</a></code>(1) variant of Metafont is used to generate fonts to avoid the possibility of online display. </p>
<p> <code>mktextfm</code> is typically called by other programs, via Kpathsea, rather than from the command line.</p>
<h2>OPTIONS</h2>
<p> <code>mktextfm</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;destdir</code><i>&nbsp;dir</i></p>
<dd> A directory name. If the directory is absolute, it is used as-is. Otherwise, it is appended to the root destination directory set in the script.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit successfully.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit successfully.</dl>
<h2>ENVIRONMENT</h2>
<p> One environment variable is specific to <code>mktextfm</code>: <code>MF_MODE_EXTRA_INFO</code>. If this is set to a non-empty value, a Metafont macro <code>mode_include_extra_info</code> will be invoked when the font is made. The standard <code>modes.mf</code> file defines this, as of modes.mf version 4.0, released in 2020. This causes the so-called Xerox-world information, notably including the <code>CODINGSCHEME</code> for the font, to be included in the tfm file. (This is not done by default since it is too intrusive to redefine the necessary primitives, per Don Knuth.) The <code><a href="/docs/linux/man/1-mftrace/">mftrace</a></code>(1) program, for example, can use this to get a clue about the font encoding, although the information is not always perfectly definitive or unambiguous. </p>
<p> For more about the encodings of Metafont fonts, see the section &#8220;Bitmap font encodings&#8221; in the Dvips manual (e.g., <a rel="nofollow" href="https://tug.org/texinfohtml/dvips.html">https://tug.org/texinfohtml/dvips.html</a>). </p>
<p> The many other environment variables and various configuration files that control a TeX system also affect the behavior of <code>mktextfm</code>, as usual.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <code><a href="/docs/linux/man/1-mktexmf/">mktexmf</a></code>(1), <code><a href="/docs/linux/man/1-mktexpk/">mktexpk</a></code>(1).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: tex-k [at] tug.org (<a rel="nofollow" href="https://lists.tug.org/tex-k)">https://lists.tug.org/tex-k)</a><br />
 TeX Live home page: <a rel="nofollow" href="https://tug.org/texlive/">https://tug.org/texlive/</a> </p>
<h2>Index</h2>

---
title: "mktexpk(1)"
name: "mktexpk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mktexpk/"
description: "mktexpk – create a PK file for a font"
---

<h2 class="name">NAME</h2>
<p> mktexpk &#8211; create a PK file for a font </p>
<h2>SYNOPSIS</h2>
<p> <code>mktexpk</code> [<i>options</i>] <i>font</i> [<i>redirect</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Kpathsea: A library for path searching</i>. </p>
<p> <code>mktexpk</code> is used to generate a <i>pk</i> file from the Metafont source files or type1 sources for <i>font</i>, if possible. </p>
<p> If <i>redirect</i> is given, it must be string of the form <code>&gt;&amp;</code><i>n</i> where <i>n</i> is the number of the file descriptor which is to receive, instead of standard output, the name of the generated file. </p>
<p> <code>mktexpk</code> is typically called by other programs, rather than from the command line.</p>
<h2>OPTIONS</h2>
<p> <code>mktexpk</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;bdpi</code><i>&nbsp;num</i></p>
<dd> Set the base device resolution.</p>
<dt><code>&#8211;dpi</code><i>&nbsp;num</i></p>
<dd> Generate the font at resolution <i>num</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;mag</code><i>&nbsp;mag</i></p>
<dd> The Metafont magnification that corresponds to the combination of <i>bdpi</i> and <i>dpi</i> that has been specified.</p>
<dt><code>&#8211;mfmode</code><i>&nbsp;mode</i></p>
<dd> The Metafont mode to use.</p>
<dt><code>&#8211;destdir</code><i>&nbsp;dir</i></p>
<dd> A directory name. If the directory is absolute, it is used as-is. Otherwise, it is appended to the root destination directory set in the script.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>BUGS</h2>
<p> If the <i>mode</i> is not specified, <code>mktexpk</code> tries to determine it from <i>bdpi</i>. The manner in which this is done is primitive. Since <i>bpdi</i> doesn&#8217;t provide sufficient information to uniquely determine a <i>mode</i> it is strongly recommended that it be specified explicitly. </p>
<p> If the <i>mode</i> and <i>bpdi</i> don&#8217;t match, the <i>mode</i> is discarded. </p>
<p> The <i>dpi</i> parameter is redundant, but is not checked for consistency. Worse, the program will fail if the wrong <i>dpi</i> is specified.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mktexmf/">mktexmf</a></code>(1), <code><a href="/docs/linux/man/1-mktextfm/">mktextfm</a></code>(1).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: tex-k [at] tug.org (<a rel="nofollow" href="https://lists.tug.org/tex-k)">https://lists.tug.org/tex-k)</a><br />
 TeX Live home page: <a rel="nofollow" href="https://tug.org/texlive/">https://tug.org/texlive/</a> </p>
<h2>Index</h2>

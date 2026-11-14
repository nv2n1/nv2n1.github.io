---
title: "weave(1)"
name: "weave"
section: "1"
letter: "w"
url: "/docs/linux/man/1-weave/"
description: "weave – translate WEB to TeX"
---

<h2 class="name">NAME</h2>
<p> weave &#8211; translate WEB to TeX </p>
<h2>SYNOPSIS</h2>
<p> <code>weave</code> [<code>-x</code>] <i>webfile</i>[<i></i><code>.web</code>] [<i>changefile</i>[<i></i><code>.ch</code>]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>weave</code> program is used to create a TeX file for viewing a Web program. It takes appropriate care of typographic details like page layout and the use of indentation, italics, boldface, etc., and it supplies extensive cross-index information that it gathers automatically. The command line arguments are the same as for <code>tangle</code> except for the option: <code>-x</code> says to omit the index, module name list, and table of contents pages. (A <i>CONTENTS.tex</i> file will still be written when the TeX file is processed, however, unless some macros in <i>webmac.tex</i> are redefined.) </p>
<p> The output TeX file name is formed by adding <code>.tex</code> to the root of the Web file name. </p>
<p> There are several macros that probably should be redefined by the programmer at the beginning of the Web file. It is a good idea to set 	itle to the name of the program. And, to cause output of only changed modules, one can say \let\maybe=\iffalse (usually as the first change in the change file).</p>
<h2>ENVIRONMENT</h2>
<p> The environment variable WEBINPUTS is used to search for the input files, or the system default if WEBINPUTS is not set. See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>FILES</h2>
<dl>
<dt><i>$TEXMFMAIN/tex/plain/base/webmac.tex</i></p>
<dd> TeX macros used by <code>weave</code> output.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tangle/">tangle</a></code>(1) for references, authors, and other information. </p>
<h2>Index</h2>

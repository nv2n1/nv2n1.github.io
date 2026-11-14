---
title: "dvibook(1)"
name: "dvibook"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvibook/"
description: "dvibook – rearrange pages in DVI file into signatures"
---

<h2 class="name">NAME</h2>
<p> dvibook &#8211; rearrange pages in DVI file into signatures </p>
<h2>SYNOPSIS</h2>
<p> <code>dvibook</code> [ <code>-q</code> ] [ <code>-s</code><i>&lt;num&gt;</i> ] [ <code>-r</code> ] [ <code>-i</code> <i>infile</i> ] [ <code>-o</code> <i>outfile</i> ] [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Dvibook</i> rearranges pages from a DVI file produced by TeX into &#8220;signatures&#8221; for printing books or booklets, creating a new DVI file usable by any of the TeX conversion programs. </p>
<p> The <i>-s</i> option selects the size of signature which will be used. The signature size is the number of sides which will be folded and bound together; the number given should be a multiple of four. The default is to use one signature for the whole file. Extra blank sides will be added if the file does not contain a multiple of four pages. </p>
<p> By default, dvibook rearranges the pages into left-hand side binding signatures; the <i>-r</i> option switches to right-hand side binding signatures. This might be useful for pTeX vertical writing (tate-kumi) documents. </p>
<p> Dvibook normally prints the page numbers of the pages rearranged; the <i>-q</i> option suppresses this.</p>
<h2>AUTHOR</h2>
<p> Angus Duggan, from <a href="/docs/linux/man/1-dviselect/">dviselect</a>(1), by Chris Torek, University of Maryland. Currently maintained as part of TeX Live (<a rel="nofollow" href="https://tug.org/texlive">https://tug.org/texlive</a>).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dvitodvi/">dvitodvi</a>(1), <a href="/docs/linux/man/1-dviconcat/">dviconcat</a>(1), <a href="/docs/linux/man/1-dviselect/">dviselect</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), <a href="/docs/linux/man/1-tex/">tex</a>(1)<br />
 <i>MC-TeX User&#8217;s Guide</i></p>
<h2>BUGS</h2>
<p> <i>Dvibook</i> does not adjust the parameters in the postamble; however, since these values are normally used only to size certain structures in the output conversion programs, and the parameters never need to be adjusted upward, this has not proven to be a problem. </p>
<h2>Index</h2>

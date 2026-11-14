---
title: "gftodvi(1)"
name: "gftodvi"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gftodvi/"
description: "gftodvi – make proof sheets from generic font files"
---

<h2 class="name">NAME</h2>
<p> gftodvi &#8211; make proof sheets from generic font files </p>
<h2>SYNOPSIS</h2>
<p> <code>gftodvi</code> [<code>-overflow-label-offset=</code><i>,real/</i>] [<code>-verbose</code>] <i>gf_file_name</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>gftodvi</code> program converts a generic font (<i>gf</i>) file output by, for example, <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), to a device independent (DVI) file (that can then be typeset using the same software that has already been written for TeX). The characters in the <i>gf</i> file will appear one per page, with labels, titles, and annotations as specified in Appendix H (Hardcopy Proofs) of <i>The Metafontbook</i>. </p>
<p> <code>gftodvi</code> uses other fonts in addition to the main <i>gf</i> file. A `gray&#8217; font is used to typeset the pixels that actually make up the character. (We wouldn&#8217;t want all the pixels to be simply black, since then labels, key points, and other information would be lost.) A `title&#8217; font is used for the information at the top of the page. A `label&#8217; font is used for the labels on key points of the figure. A `slant&#8217; font is used to typeset diagonal lines, which otherwise have to be simulated using horizontal and vertical rules. The default gray, title, and label fonts are <i>gray</i>, <i>cmr8</i>, and <i>cmtt10</i>, respectively; there is no default slant font. </p>
<p> To change the default fonts, you can give <code>special</code> commands in your Metafont source file, or you can change the fonts online. An online dialog ensues if you end the <i>gf_file_name</i> with a `/&#8217;. For example, </p>
<p> &nbsp;<wbr>&nbsp; gftodvi cmr10.300gf/ </p>
<p> &nbsp;<wbr>&nbsp; Special font substitution: grayfont black </p>
<p> &nbsp;<wbr>&nbsp; OK; any more? grayfontarea /home/art/don/ </p>
<p> &nbsp;<wbr>&nbsp; OK; any more? slantfont /home/fonts/slantimagen6 </p>
<p> &nbsp;<wbr>&nbsp; OK; any more? &lt;RET&gt;<br />
 will use <i>/home/art/don/black</i> as the `gray&#8217; font and <i>/home/fonts/slantimagen6</i> as the `slant&#8217; font (this name indicates a font for lines with slope 1/6 at the resolution of an Imagen printer). </p>
<p> The <i>gf_file_name</i> on the command line must be complete. Because the resolution is part of the extension, it would not make sense to append a default extension as is done with TeX or DVI-reading software. The output file name uses the same root as the <i>gf</i> file, with the <code>.dvi</code> extension added. For example, the input file <i>cmr10.2602gf</i> would become <i>cmr10.dvi</i>.</p>
<h2>OPTIONS</h2>
<p> The argument to <code>-overflow-label-offset</code> specifies the distance from the right edge of the character bounding box at which the overflow equations (if any) are typeset. The value is given in TeX points. The default is a little over two inches. </p>
<p> Without the <code>-verbose</code> option, <code>gftodvi</code> operates silently. With it, a banner and progress report are printed on <i>stdout</i>.</p>
<h2>ENVIRONMENT</h2>
<p> <code>gftodvi</code> looks for <i>gf_file_name</i> using the environment variable GFFONTS. If that is not set, it uses the variable TEXFONTS. If that is not set, it uses the system default. </p>
<p> See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>FILES</h2>
<dl>
<dt><i>{gray.tfm,&#8230;}</i></p>
<dd> The default fonts.</p>
<dt><i>{gray.mf,&#8230;}</i></p>
<dd> The Metafont sources.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1).<br />
 Donald E. Knuth, <i>The Metafontbook</i> (Volume C of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13445-4.<br />
 Donald E. Knuth et al., <i>Metafontware</i>.</p>
<h2>AUTHORS</h2>
<p> Donald E. Knuth wrote and still maintains the program. It was published as part of the <i>Metafontware</i> technical report. Paul Richards originally ported it to Unix. Bug reports should go to tex-k [at] tug.org (<a rel="nofollow" href="https://lists.tug.org/tex-k">https://lists.tug.org/tex-k</a>). </p>
<h2>Index</h2>

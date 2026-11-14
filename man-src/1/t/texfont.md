---
title: "texfont(1)"
name: "texfont"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texfont/"
description: "texfont – font installation tool for ConTeXt"
---

<h2 class="name">NAME</h2>
<p> texfont &#8211; font installation tool for ConTeXt</p>
<h2>SYNOPSIS</h2>
<p> <code>texfont</code> [ <i>OPTION</i> &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> TeXFont is a <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) script that helps to set up and install TeX fonts. It was designed for use with ConTeXt, but may also be helpful for users of other formats, like plain TeX or LaTeX. Its use is described in detail in the files <i>mtexfont.pdf</i> and <i>mfont.pdf</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;fontroot</code>=<i>path</i> : texmf font root (automatically determined)</p>
<dt> <code>&#8211;sourcepath</code>=<i>path</i> : when installing, copy from this path (default: .)</p>
<dt> <code>&#8211;sourcepath</code>=<i>auto</i> : locate and use vendor/collection</p>
<dt> <code>&#8211;vendor</code>=<i>name</i> : vendor name (first level directory)</p>
<dt> <code>&#8211;collection</code>=<i>name</i> : font collection (second level</p>
<dd>directory)</p>
<dt> <code>&#8211;encoding</code>=<i>name</i> : encoding vector (default: texnansi)</p>
<dt> <code>&#8211;slant</code>=<i>s</i> : slant glyphs in font by factor (0.0 &#8211; 1.5)</p>
<dt> <code>&#8211;extend</code>=<i>s</i> : extend glyphs in font by factor (0.0 &#8211; 1.5)</p>
<dt> <code>&#8211;caps</code>=<i>s</i> : capitalize lowercase chars by factor (0.5 &#8211; 1.0)</p>
<dt> <code>&#8211;noligs</code> : remove ligatures</p>
<dt> <code>&#8211;install</code> : copy files from source to font tree</p>
<dt> <code>&#8211;listing</code> : list files on auto sourcepath</p>
<dt> <code>&#8211;remove</code> : remove files on auto sourcepath</p>
<dt> <code>&#8211;makepath</code> : when needed, create the paths</p>
<dt> <code>&#8211;test</code> : use test paths for vendor/collection</p>
<dt> <code>&#8211;show</code> : run tex on texfont.tex</p>
<dt> <code>&#8211;batch</code> : process given batch file</p>
<dt> <code>&#8211;weight</code> : multiple master weight</p>
<dt> <code>&#8211;width</code> : multiple master width</p>
<dt> <code>&#8211;expert</code> : also handle expert fonts</p>
<dt> <code>&#8211;help</code> : show some more info</p>
<dt></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1), <code><a href="/docs/linux/man/1-fontinst/">fontinst</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/1-texshow/">texshow</a></code>(1).</p>
<dt>&bull;</p>
<dd>
<dd>The ConTeXt Font manual, <i>mfonts.pdf</i> available from PRAGMA ADE &lt;URL: <a rel="nofollow" href="http://www.pragma-ade.com/dir/general/manuals/">http://www.pragma-ade.com/dir/general/manuals/</a> &gt;.</p>
<dt>&bull;</p>
<dd> The TeXFont manual, <i>mtexfont.pdf</i></p>
<dt>&bull;</p>
<dd> The TeXExec manual, <i>mtexexec.pdf</i>.</p>
<dt>&bull;</p>
<dd> ConTeXt wiki &lt;URL: <a rel="nofollow" href="http://www.contextgarden.net">http://www.contextgarden.net</a> &gt;.</p>
<dt>&bull;</p>
<dd> Donald E. Knuth&#8217;s <i>The TeXbook</i>. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Frank K&uuml;ster &lt;frank [at] kuesterei.ch&gt;, for the Debian GNU/Linux system, and modified by Sanjoy Mahajan &lt;sanjoy [at] mit.edu&gt;. It may be used and modified by others without contacting the authors. </p>
<h2>Index</h2>

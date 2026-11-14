---
title: "textools(1)"
name: "textools"
section: "1"
letter: "t"
url: "/docs/linux/man/1-textools/"
description: "textools – generate TeX map files, afm files, fix texmf trees"
---

<h2 class="name">NAME</h2>
<p> textools &#8211; generate TeX map files, afm files, fix texmf trees</p>
<h2>SYNOPSIS</h2>
<p> <code>textools</code> [ <i>OPTIONS</i> &#8230; ] [ <i>pattern</i> or <i>name</i> or <i>fromroot toroot</i> ] [ <i>MODIFIER OPTIONS</i> &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>textools</code> processes map files, converts Mac files to DOS format, generates map files, fixes texmf trees, and performs a utility-belt worth of other tasks also useful in installing and maintaining the zillion auxilliary files that <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) and its friends require. </p>
<h2>OPTIONS</h2>
<p> The modifier options are listed after the options that they modify.</p>
<dl>
<dt><code>&#8211;downcasefilenames</code> [<code>&#8211;recurse</code>] [<code>&#8211;force</code>]</p>
<dd>
<dt><code>&#8211;encmake</code> <i>afmfile</i> <i>encodingname</i></p>
<dd>
<dt><code>&#8211;findfile</code> <i>filename</i> [<code>&#8211;recurse</code>]</p>
<dd>
<dt><code>&#8211;fixafmfiles</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd>
<dt><code>&#8211;fixtexmftrees</code> [<i>texmfroot</i>] [<code>&#8211;force</code>]</p>
<dd>
<dt><code>&#8211;hidemapnames</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd>
<dt><code>&#8211;mactodos</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd> Fixes newlines from Macintosh files so that the file is readable in DOS.</p>
<dt><code>&#8211;removemapnames</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd>
<dt><code>&#8211;replacefile</code> <i>filename</i> [<code>&#8211;force</code>]</p>
<dd>
<dt><code>&#8211;restoremapnames</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd>
<dt><code>&#8211;showfont</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;stripformfeeds</code> [<code>&#8211;recurse</code>] [<code>&#8211;force</code>]</p>
<dd>
<dt><code>&#8211;tpmmake</code> <i>tpmfile</i></p>
<dd> Package files into a <i>t-modulename.tpm</i> file. Imagine this file structure: </p>
<pre>
tex/context/third/modulename/t-modulename.vim
doc/context/third/modulename/modulename-doc.pdf
doc/context/third/modulename/modulename-demo.pdf
tpm/t-modulename.tpm
</pre>
<p> where <i>t-modulename.tpm</i> is a valid tpm file. When you run </p>
<pre>
textools --tpmmake t-modulename
</pre>
<p> the <code>textools</code> command will replace file sizes declared in the tpm file with proper values and create a ZIP archive <i>t-modulename.zip</i> with the files specified by the tpm file. This command needs to be run in the root of the TEXMF tree.</p>
<dt><code>&#8211;unzipfiles</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd>
<dt><code>&#8211;updatetree</code> <i>fromroot</i> <i>toroot</i> [<code>&#8211;force</code> <code>&#8211;nocheck</code> <code>&#8211;merge</code> <code>&#8211;delete</code>]</p>
<dd>
<dt><code>&#8211;videmapnames</code> [<i>pattern</i>] [<code>&#8211;recurse</code>]</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1), <code><a href="/docs/linux/man/1-texmfstart/">texmfstart</a></code>(1). </p>
<p> <a rel="nofollow" href="http://www.contextgarden.net">http://www.contextgarden.net</a> laURL: L raConTeXt wiki </p>
<h2>BUGS</h2>
<p> This manual page is incomplete because I have no clue what this program does. </p>
<h2>AUTHOR</h2>
<p> <code><a href="/docs/linux/man/1-textools/">textools</a></code>(1) is part of the <a rel="nofollow" href="http://www.contextgarden.net">http://www.contextgarden.net</a> laURL: L raConTeXt suite of typesetting programs based on the <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) family of typesetting programs. This manual page was written by Sanjoy Mahajan &lt;sanjoy [at] mit.edu&gt; based on running <code>textools &#8211;help</code> and with help from Mojca Miklavec. It is in the public domain. </p>
<h2>Index</h2>

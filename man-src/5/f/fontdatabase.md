---
title: "fontdatabase(5)"
name: "fontdatabase"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fontdatabase/"
description: "FontDataBase – database of fonts accessible to t1lib."
---

<p>FontDataBase &#8211; database of fonts accessible to t1lib.</p>
<h2>Description</h2>
<p>This manual page has been written for the Debian GNU/Linux distribution. It has been adapted from the documentation included in the upstream <code>t1lib</code> distribution. </p>
<p> <code>/etc/t1lib/FontDataBase</code> is a text file which contains, minimally, the basenames of Type 1 font files to be made accessible to the <code>t1lib</code> font rasterizer library. The format is intentionally similar to that of the <code>fonts.dir</code> and <code>fonts.scale</code> files used by X11. </p>
<p> Line 1 of this file contains a positive integer specifying the number of fonts declared in that file. This is as in the <code>fonts.dir</code> files of the X11 system. </p>
<p> All remaining lines contain declarations of one font each. The only thing taken from such a line is the last string (delimited by white space) in it. It is assumed to be a filename of the format <i>basename</i>.<i>someextension</i>. </p>
<p> The <i>basename</i> part is assumed to be the <code><a href="/docs/linux/man/1-basename/">basename</a></code>(1) of a fontfile. After the a string has been parsed, the <i>extension</i> is cut off and replaced in turn with <i>.pfa</i> and <i>.pfb.</i> The initialization routine tries to open a font file in its search path with one of the resulting filenames. </p>
<p> The remainder of the line, i.e., from beginning to the start of the filename string, is completely ignored and thus may contain information for other programs.</p>
<h2>Examples</h2>
<p>Here is a minimal font database file for 4 fonts: </p>
<pre>4
isvl.afm
isvli.afm
isvd.afm
isvdi.afm</pre>
<p>This file is <i>minimal</i>, because it contains just the information needed, and nothing not needed by the library. Here is a more realistic example, which allows an application to match a fully qualified X11 fontname to a FontID in <code>t1lib.</code> This is also a valid font database file: </p>
<pre>4
Souvenir Souvenir-Light --- -itc-souvenir-light-r-normal--#-0-0-0-p-0-iso8859-1 isvl.afm
Souvenir Souvenir-LightItalic -*- -itc-souvenir-light-i-normal--#-0-0-0-p-0-iso8859-1 isvli.afm
 Souvenir-Demi *-- -itc-souvenir-demi-r-normal--#-0-0-0-p-0-iso8859-1 isvd.afm
 Souvenir-DemiItalic **- -itc-souvenir-demi-i-normal--#-0-0-0-p-0-iso8859-1 isvdi.afm</pre>
<h2>Files</h2>
<p><i>/etc/t1lib/FontDataBase</i></p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/1x-mkfontdir/">mkfontdir</a></code>(1x) </p>

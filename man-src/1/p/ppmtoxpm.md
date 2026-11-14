---
title: "ppmtoxpm(1)"
name: "ppmtoxpm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoxpm/"
description: "ppmtoxpm – convert a portable pixmap into an X11 pixmap"
---

<h2 class="name">NAME</h2>
<p> ppmtoxpm &#8211; convert a portable pixmap into an X11 pixmap</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoxpm </code> [<code>-name=</code><i>xpmname</i>] [<code>-rgb=</code><i>rgb-textfile</i>] [<code>-alphamask=</code><i>pgmfile</i>] [<i>ppmfile</i>] </p>
<p> Minimum unique abbrevations are acceptable. </p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces X11 pixmap (version 3) as output which can be loaded directly by the XPM library. </p>
<p> For example, to convert the file &quot;dot&quot; (found in /usr/include/X11/bitmaps), from xbm to xpm one could specify</p>
<dl>
<dt>
<dd> xbmtopbm dot | ppmtoxpm -name dot</dl>
<p> or, with a rgb text file (in the local directory)</p>
<dl>
<dt>
<dd> xbmtopbm dot | ppmtoxpm -name dot -rgb rgb.txt </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-name=</code><i>xpmname</i></p>
<dd> The <code>-name </code> option allows you to specify the prefix string which is printed in the resulting XPM output. If not specified, will default to the filename (without extension) of the &lt;ppmfile&gt; argument. If you do not specify <code>-name </code> or <i>ppmfile</i>, (i.e. your input is from Standad Input), the prefix string defaults to the string <code>noname</code>.</p>
<dt><code>rgb=</code><i>rgb-textfile</i></p>
<dd> The <code>-rgb </code> option allows you to specify an X11 rgb text file for the lookup of color name mnemonics. This rgb text file is typically the /usr/lib/X11/rgb.txt of the MIT X11 distribution, but any file using the same format may be used. When specified and a RGB value from the ppm input matches a RGB value from the &lt;rgb-textfile&gt;, then the corresponding color name mnemonic is printed in the XPM&#8217;s colormap. If you don&#8217;t specify <code>-rgb or if the RGB values don&#8217;t</code> match, then <code>ppmtoxpm produces the color specifications in the #RGB, #RRGGBB,</code> #RRRGGGBBB, or #RRRRGGGGBBBB hexadecimal format. </p>
<dt><code>-alphamask=</code><i>pgmfile</i></p>
<dd> This option names a PGM file to use as an alpha (transparency) mask. The file must contain an image the same dimensions as the input image. <code>ppmtoxpm</code> marks as transparent any pixel whose position in the alpha mask image is at most half white. </p>
<p> If you don&#8217;t specify <code>-alphamask</code>, <code>ppmtoxpm</code> makes all pixels in the output opaque. </p>
<p> <code>ppmcolormask</code> is one way to generate an alpha mask file. You might also generate it by extracting transparency information from an XPM file with the <code>-alphaout</code> option to <code>xpmtoppm</code>. There are similar options on other Netpbm converters that convert from formats that include transparency information too. </p>
</dl>
<h2>LIMITATIONS</h2>
<p> An option to match the closest (rather than exact) color name mnemonic from the rgb text would be a desirable enhancement. </p>
<p> Truncation of the least significant bits of a RGB value may result in nonexact matches when performing color name mnemonic lookups. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmcolormask/">ppmcolormask</a></code>(1), <code><a href="/docs/linux/man/1-xpmtoppm/">xpmtoppm</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)<br />
 XPM Manual by Arnaud Le Hors lehors [at] mirsa.inria.fr</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Mark W. Snitily. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. This software is provided &quot;as is&quot; without express or implied warranty. </p>
<p> This tool was developed for Schlumberger Technologies, ATE Division, and with their permission is being made available to the public with the above copyright notice and permission notice. </p>
<p> Upgraded to XPM2 by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Paul Breslaw, Mecasoft SA, Zurich, Switzerland&nbsp;(paul [at] mecazh.uu.ch)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Thu Nov&nbsp;<wbr>&nbsp;8 16:01:17 1990 </p>
<p> Upgraded to XPM version 3 by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Arnaud Le Hors&nbsp;(lehors [at] mirsa.inria.fr)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Tue Apr 9 1991 </p>
<h2>Index</h2>

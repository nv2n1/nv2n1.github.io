---
title: "infotopam(1)"
name: "infotopam"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infotopam/"
description: "infotopam – convert Amiga .info icons to PAM"
---

<h2 class="name">NAME</h2>
<p> infotopam &#8211; convert Amiga .info icons to PAM</p>
<h2>SYNOPSIS</h2>
<p> <code>infotopam</code> [<code>-forcecolor</code>] [<code>-numcolors</code> <i>numcolors</i>] [<code>-selected</code>] [<i>index color</i> &#8230;] [<i>filename</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>EXAMPLES</h2>
<p> By default, <code>infotopam</code> converts the first icon in a .info file: </p>
<pre>
    infotopam amiga.info &gt; amiga.first.pam
</pre>
<p> Use the <i>-selected</i> option to convert the second icon in a .info file. Here <code>infotopam</code> reads from Standard Input: </p>
<pre>
    infotopam -selected &lt; amiga.info &gt; amiga.second.pam
</pre>
<p> Use the <i>-forcecolor</i> option to force color conversion for a 1 bit-plane .info file: </p>
<pre>
    infotopam -forcecolor bw.info &gt; bw.pam
</pre>
<p> Use <i>-numcolors</i> to override colors for indexes 0 and 3. Notice the two ways to specify the color: </p>
<pre>
    infotopam -numcolors 2 0 green 3 #FF0000 icon.info &gt; icon.pam
</pre>
<p> Since Amiga monitors do not use square pixels, some icons may appear squished. Filtering the output through <code>pamscale</code> can fix this: </p>
<pre>
     infotopam squish.info | pamtopnm | pamscale -yscale 1.7 &gt; normal.pnm
</pre>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>infotopam</code> converts an Amiga .info (icon) file to a PAM image. <code>infotopam</code> reads a .info file from <i>filename</i>, or from Standard Input if you do not specify a file name, and writes the converted PAM image to Standard Output. </p>
<p> <code>infotopam</code> currently handles 1 and 2 bit-plane icons. If the .info icon only has 1 bit-plane, <code>infotopam</code> generates a bitmap (black&amp;white) PAM image; otherwise it generates a color PAM image. You can force <code>infotopam</code> to convert 1 bit-plane images to color PAM images by using the <i>-forcecolor</i> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-forcecolor</code></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Forces <code>infotopam</code> to convert 1 bit-plane icons to color PAM<br />
&nbsp;<wbr>&nbsp;<wbr>images instead of bitmap PAM images.&nbsp;<wbr>&nbsp;<wbr><code>infotopam</code>&nbsp;<wbr>uses the index 2<br />
&nbsp;<wbr>&nbsp;<wbr>color for black and the index 1 color for white&nbsp;<wbr>(more on this<br />
&nbsp;<wbr>&nbsp;<wbr>below). </p>
<dt><code>-numcolors</code> <i>numcolors</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Tells <code>infotopam</code> how many colors to override. Pixels in the<br />
&nbsp;<wbr>&nbsp;<wbr>Amiga .info files are assigned an index value rather than a specific color.<br />
&nbsp;<wbr>&nbsp;<wbr>The standard colors for a 2 bit-plane icon are: </p>
<pre>
    Index 0:  Blue   (00, 55, AA)
    Index 1:  White  (FF, FF, FF)
    Index 2:  Black  (00, 00, 20)
    Index 3:  Orange (FF, 8A, 00)
</pre>
<p> To override the colors, first specify how many colors to override using<br />
&nbsp;<wbr>&nbsp;<wbr><i>-numcolors</i>, then specify an&nbsp;<wbr>(<i>index color</i>)&nbsp;<wbr>pair for each color<br />
&nbsp;<wbr>&nbsp;<wbr>you want to override, where&nbsp;<wbr><i>index</i>&nbsp;<wbr>is a value from 0 to 3 and<br />
&nbsp;<wbr>&nbsp;<wbr><i>color</i>&nbsp;<wbr>the new color for that index.&nbsp;<wbr>&nbsp;<wbr>Specify&nbsp;<wbr><i>color</i>&nbsp;<wbr>as<br />
&nbsp;<wbr>&nbsp;<wbr>described for the&nbsp;<wbr> <code>ppm_parsecolor()</code> argument . </p>
<dt><code>-selected</code></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> Tells <code>infotopam</code> to convert the selected (second) icon instead of<br />
&nbsp;<wbr>&nbsp;<wbr>the normal&nbsp;<wbr>(first)&nbsp;<wbr>icon.&nbsp;<wbr>&nbsp;<wbr>Each Amiga .info icon file contains two icon<br />
&nbsp;<wbr>&nbsp;<wbr>images.&nbsp;<wbr>&nbsp;<wbr>The first image is the normal, unselected icon, and the second<br />
&nbsp;<wbr>&nbsp;<wbr>image is the selected icon.&nbsp;<wbr>&nbsp;<wbr>By default&nbsp;<wbr><code>infotopam</code>&nbsp;<wbr>converts the first<br />
&nbsp;<wbr>&nbsp;<wbr>icon.&nbsp;<wbr>&nbsp;<wbr>You can tell&nbsp;<wbr><code>infotopam</code>&nbsp;<wbr>to convert the second icon by using the<br />
&nbsp;<wbr>&nbsp;<wbr><i>-selected</i>&nbsp;<wbr>option. </p>
</dl>
<p> All options can be abbreviated to their shortest unique prefix. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) </p>
<h2>NOTES</h2>
<p> Thanks to the following people on comp.sys.amiga.programmer for tips and pointers on decoding the info file format: </p>
<dl>
<dt>&bull;</p>
<dd> Ben Hutchings</p>
<dt>&bull;</p>
<dd> Thomas Richter</p>
<dt>&bull;</p>
<dd> Kjetil Svalastog Matheussen</p>
<dt>&bull;</p>
<dd> Anders Melchiorsen</p>
<dt>&bull;</p>
<dd> Dirk Stoecker</p>
<dt>&bull;</p>
<dd> Ronald V.D. </p>
</dl>
<p> The format of the Amiga .info file is as follows: </p>
<pre>
    DiskObject header            78 bytes
    Optional DrawerData header   56 bytes
    First icon header            20 bytes
    First icon data              Varies
    Second icon header           20 bytes
    Second icon data             Varies  
</pre>
<p> The DiskObject header contains, among other things, the magic number (0xE310), the object width and height (inside the embedded Gadget header), and the version. </p>
<p> Each icon header contains the icon width and height, which can be smaller than the object width and height, and the number of bit-planes. </p>
<p> The icon data has the following format: </p>
<dl>
<dt>
<dd>
&nbsp;<wbr> </p>
<p> <i>BIT-PLANE</i> planes, each with <i>HEIGHT</i> rows of (<i>WIDTH</i><br />
&nbsp;<wbr>+15)&nbsp;<wbr>/&nbsp;<wbr>16&nbsp;<wbr>*&nbsp;<wbr>2 bytes length.</dl>
<p> So if you have a 9x3x2 icon, the icon data will look like this: </p>
<pre>
    aaaa aaaa a000 0000
    aaaa aaaa a000 0000
    aaaa aaaa a000 0000
    bbbb bbbb b000 0000
    bbbb bbbb b000 0000
    bbbb bbbb b000 0000
</pre>
<p> where <i>a</i> is a bit for the first bit-plane, <i>b</i> is a bit for the second bit-plane, and <i>0</i> is padding. Thanks again to Ben Hutchings for his very helpful post! </p>
<h2>HISTORY</h2>
<p> <code>infotopam</code> was new in Netpbm 10.22 (April 2004). </p>
<h2>LIMITATIONS</h2>
<p> <code>infotopam</code> currently only handles 1 and 2 bit-plane icons. </p>
<p> There is no <code>pamtoinfo</code> command, since the .info files contain a lot more than just icon data, and mapping the colors would be difficult. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000, 2004 by Richard Griswold. </p>
<h2>Index</h2>

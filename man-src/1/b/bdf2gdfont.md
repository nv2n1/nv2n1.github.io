---
title: "bdf2gdfont(1)"
name: "bdf2gdfont"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bdf2gdfont/"
---

<h2 class="name">NAME</h2>
 

 bdf2gdfont.pl - Convert X11 &quot;BDF&quot; fonts into a loadable font format for GD. 

<h2>SYNOPSIS</h2>

 <pre>
  % bdf2gdfont.pl courR12.bdf &gt; courR12.fnt
</pre>

<h2>DESCRIPTION</h2>

 This script converts BDF-style X11 font files into a format that can be loaded by the <font SIZE="-1">GD</font> module using the GD::Font-&gt;<i>load()</i> method. There are a number of ways to obtain <font SIZE="-1">BDF</font> fonts.
<dl>
<dt>1. The font is already present on your system.
<dd> Some <font SIZE="-1">BDF</font> fonts can be found in the standard X11R6 distribution. This script will automatically uncompress gzipped font files if their extension ends with .gz (the gunzip program must be on your path).
<dt>2. From a font server.
<dd> The ``fstobdf'' utility, a standard X11 utility, will read a named font from the font server of your choice and return it in <font SIZE="-1">BDF</font> format. You can pipe it to bdf2gdfont.pl: 

 <pre>
  fstobdf -s fontserverhost:7100 -fn 8x16 | bdf2gdfont.pl &gt; newfont.fnt
</pre> 

 Use xlsfonts to find out what fonts are available. Most fonts will have long names like -B&amp;H-LucidaTypewriter-Bold-R-Normal-Sans-18-180-75-75-M-110-ISO8859-10.
<dt>3. Using the pcf2bdf utility.
<dd> Some fonts are only available in <font SIZE="-1">PCF</font> (compiled) format. To obtain these, you can either turn on a font server and follow recipe (2), or use <font SIZE="-1">TAGA</font> Nayuta's pcf2bdf utility. This utility is available from <a rel="nofollow" HREF="http://www.tsg.ne.jp/GANA/S/pcf2bdf/">http://www.tsg.ne.jp/GANA/S/pcf2bdf/</a> (page is in Japanese, but you can find the download link).</dl>

<h2>Limitations</h2>

 This font converter only works with fixed-width fonts. If used with a TrueType or proportional font it will die with an error message.

<h2>SEE ALSO</h2>

 <font SIZE="-1">GD</font>

<h2>AUTHOR</h2>

 Lincoln Stein &lt;lstein [at] cshl.org&gt;, heavily adapted from bdftogd from Jan Pazdziora &lt;adelton [at] fi.muni.cz&gt;. 

 Copyright (c) 2004 Cold Spring Harbor Laboratory 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>



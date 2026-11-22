---
title: "bdf2gdfont-pl(1)"
name: "bdf2gdfont-pl"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bdf2gdfont-pl/"
---

bdf2gdfont.pl - Convert X11 &quot;BDF&quot; fonts into a loadable font format for GD. 

<h2>Synopsis</h2><pre> % bdf2gdfont.pl courR12.bdf &gt; courR12.fnt</pre><h2>Description</h2>This script converts BDF-style X11 font files into a format that can be loaded by the GD module using the GD::Font-&gt;<i>load()</i> method. There are a number of ways to obtain BDF fonts.
<dl><dt>1. The font is already present on your system.
</dt><dd>Some BDF fonts can be found in the standard X11R6 distribution. This script will automatically uncompress gzipped font files if their extension ends with .gz (the gunzip program must be on your path).
</dd><dt>2. From a font server.
</dt><dd>The ``fstobdf'' utility, a standard X11 utility, will read a named font from the font server of your choice and return it in BDF format. You can pipe it to bdf2gdfont.pl: 
 <pre> fstobdf -s fontserverhost:7100 -fn 8x16 | bdf2gdfont.pl &gt; newfont.fnt</pre>Use xlsfonts to find out what fonts are available. Most fonts will have long names like -B&amp;H-LucidaTypewriter-Bold-R-Normal-Sans-18-180-75-75-M-110-ISO8859-10.
</dd><dt>3. Using the pcf2bdf utility.
</dt><dd>Some fonts are only available in PCF (compiled) format. To obtain these, you can either turn on a font server and follow recipe (2), or use TAGA Nayuta's pcf2bdf utility. This utility is available from <a rel="nofollow" HREF="http://www.tsg.ne.jp/GANA/S/pcf2bdf/">http://www.tsg.ne.jp/GANA/S/pcf2bdf/</a> (page is in Japanese, but you can find the download link).</dd></dl><h3>Limitations</h3>This font converter only works with fixed-width fonts. If used with a TrueType or proportional font it will die with an error message.
<h2>See Also</h2>GD
<h2>Author</h2>Lincoln Stein &lt;lstein [at] cshl.org&gt;, heavily adapted from bdftogd from Jan Pazdziora &lt;adelton [at] fi.muni.cz&gt;. 

 Copyright (c) 2004 Cold Spring Harbor Laboratory 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

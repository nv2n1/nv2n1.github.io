---
title: "conjure-im6-q16(1)"
name: "conjure-im6-q16"
section: "1"
letter: "c"
url: "/docs/linux/man/1-conjure-im6-q16/"
description: "conjure – interprets and executes scripts written in the Magick Scripting Language (MSL)."
---

<p>conjure &#8211; interprets and executes scripts written in the Magick Scripting Language (MSL). </p>
<h2>Synopsis</h2>
<dl>
<dt><code>conjure-im6.q16</code> [<i>options</i>] <i>script.msl</i></p>
<dd></dl>
<h2>Overview</h2>
<p>The <code>conjure-im6.q16</code> program is a member of the <a href="/docs/linux/man/1-imagemagick-ims6-q16/">ImageMagick-ims6.q16</a>(1) suite of tools. Use it to process a Magick Scripting Language (MSL) script. The Magick scripting language (MSL) will primarily benefit those that want to accomplish custom image processing tasks but do not wish to program, or those that do not have access to a Perl interpreter or a compiler. </p>
<p> For more information about the conjure command, point your browser to file:///usr/share/doc/imagemagick-6-common/html/www/conjure.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="https://www.imagemagick.org/script/conjure.php.">https://www.imagemagick.org/script/conjure.php.</a></p>
<h2>Description</h2>
<p>Image Settings:<br />
&nbsp;<wbr>&nbsp;-monitor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;monitor progress<br />
&nbsp;<wbr>&nbsp;-quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suppress all warning messages<br />
&nbsp;<wbr>&nbsp;-regard-warnings&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pay attention to warning messages<br />
&nbsp;<wbr>&nbsp;-seed value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seed a new sequence of pseudo-random numbers<br />
&nbsp;<wbr>&nbsp;-verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print detailed information about the image </p>
<p> Miscellaneous Options:<br />
&nbsp;<wbr>&nbsp;-debug events&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display copious debugging information<br />
&nbsp;<wbr>&nbsp;-help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print program options<br />
&nbsp;<wbr>&nbsp;-log format&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;format of debugging information<br />
&nbsp;<wbr>&nbsp;-list type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print a list of supported option arguments<br />
&nbsp;<wbr>&nbsp;-version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print version information </p>
<p> In additiion, define any key value pairs required by your script. For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;conjure -size 100&#215;100 -color blue -foo bar script.msl</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-imagemagick-im6-q16/">ImageMagick-im6.q16</a>(1) </p>
<h2>Copyright</h2>
<p><code>Copyright (C) 1999-2020 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/imagemagick-6-common/html/www/license.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="https://www.imagemagick.org/script/license.php">https://www.imagemagick.org/script/license.php</a></code></p>
